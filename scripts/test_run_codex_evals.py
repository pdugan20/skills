#!/usr/bin/env python3
"""Tests for the Codex eval runner's parsing, isolation, and planning helpers."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import run_codex_evals as runner


def event(**fields: object) -> str:
    return json.dumps(fields)


class TraceTests(unittest.TestCase):
    def test_detects_implicit_skill_read_and_sums_usage(self) -> None:
        lines = [
            event(type="thread.started"),
            event(
                type="item.completed",
                item={"type": "command_execution", "command": "/bin/zsh -lc 'cat /tmp/w/.agents/skills/demo/SKILL.md'"},
            ),
            event(type="item.completed", item={"type": "agent_message", "text": "first"}),
            event(type="item.completed", item={"type": "agent_message", "text": "final answer"}),
            event(type="turn.completed", usage={"input_tokens": 10, "cached_input_tokens": 4, "output_tokens": 3}),
            event(type="turn.completed", usage={"input_tokens": 5, "output_tokens": 1}),
            "not json",
        ]
        trace = runner.parse_trace(lines, "demo")
        self.assertTrue(trace.skill_fired)
        self.assertEqual(trace.final_message, "final answer")
        self.assertEqual((trace.input_tokens, trace.cached_input_tokens, trace.output_tokens), (15, 4, 4))

    def test_ignores_sibling_skills_and_records_errors(self) -> None:
        lines = [
            event(type="item.completed", item={"type": "command_execution", "command": "cat demo-extra/SKILL.md"}),
            event(type="item.completed", item={"type": "command_execution", "command": "cat other/SKILL.md"}),
            event(type="turn.failed", error={"message": "model_not_found"}),
        ]
        trace = runner.parse_trace(lines, "demo")
        self.assertFalse(trace.skill_fired)
        self.assertEqual(runner.fatal(trace), "model_not_found")

    def test_judge_errors_also_stop_the_batch(self) -> None:
        agent = runner.Trace()
        judge = runner.parse_trace([event(type="error", message="You've hit your usage limit")], "demo")
        self.assertIsNone(runner.fatal(agent))
        self.assertEqual(runner.fatal(agent, judge), "You've hit your usage limit")
        self.assertIsNone(runner.fatal(agent, None))


class GradeTests(unittest.TestCase):
    def test_accepts_complete_grade_in_assertion_order(self) -> None:
        raw = json.dumps(
            {
                "assertions": [
                    {"index": 2, "passed": False, "reason": "missing"},
                    {"index": 1, "passed": True, "reason": "present"},
                ]
            }
        )
        grade = runner.parse_grade(raw, 2)
        self.assertIsNone(grade.error)
        self.assertEqual(grade.passed, [True, False])

    def test_rejects_incomplete_or_unreadable_grades(self) -> None:
        partial = json.dumps({"assertions": [{"index": 1, "passed": True, "reason": "ok"}]})
        self.assertIsNotNone(runner.parse_grade(partial, 2).error)
        self.assertIsNotNone(runner.parse_grade("", 1).error)
        duplicate = json.dumps(
            {"assertions": [{"index": 1, "passed": True, "reason": "a"}, {"index": 3, "passed": True, "reason": "b"}]}
        )
        self.assertIsNotNone(runner.parse_grade(duplicate, 2).error)


class WorkspaceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.skill_dir = root / "skills" / "demo"
        (self.skill_dir / "evals" / "fixtures").mkdir(parents=True)
        (self.skill_dir / "references").mkdir()
        (self.skill_dir / "SKILL.md").write_text("---\nname: demo\n---\n")
        (self.skill_dir / "references" / "guide.md").write_text("guide")
        (self.skill_dir / "evals" / "evals.json").write_text("{}")
        (self.skill_dir / "evals" / "fixtures" / "input.md").write_text("input")
        self.workspace = root / "workspace"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_skill_arm_gets_skill_without_its_evals(self) -> None:
        attached = runner.prepare_workspace(
            self.workspace, self.skill_dir, ["evals/fixtures/input.md"], with_skill=True
        )
        installed = self.workspace / ".agents" / "skills" / "demo"
        self.assertEqual(attached, ["input.md"])
        self.assertEqual((self.workspace / "input.md").read_text(), "input")
        self.assertTrue((installed / "SKILL.md").is_file())
        self.assertTrue((installed / "references" / "guide.md").is_file())
        self.assertFalse((installed / "evals").exists())
        self.assertTrue((self.workspace / ".git").is_dir())

    def test_baseline_arm_has_no_skill(self) -> None:
        runner.prepare_workspace(self.workspace, self.skill_dir, [], with_skill=False)
        self.assertFalse((self.workspace / ".agents").exists())

    def test_installed_copies_are_found_by_link_and_real_path(self) -> None:
        root = Path(self.temp.name) / "user-skills"
        root.mkdir()
        (root / "demo").symlink_to(self.skill_dir)
        paths = runner.installed_skill_files("demo", (root, Path(self.temp.name) / "missing"))
        self.assertEqual(len(paths), 2)
        self.assertTrue(all(path.endswith("demo/SKILL.md") for path in paths))


class CommandAndPlanTests(unittest.TestCase):
    def test_runs_ignore_user_config_in_read_only_sandbox(self) -> None:
        command = runner.codex_command(Path("/tmp/w"), "gpt-6-astra", "do it", ["/a/demo/SKILL.md"])
        self.assertIn("--ignore-user-config", command)
        self.assertEqual(command[command.index("-s") + 1], "read-only")
        self.assertEqual(command[command.index("-m") + 1], "gpt-6-astra")
        override = command[command.index("-c") + 1]
        self.assertEqual(override, 'skills.config=[{path = "/a/demo/SKILL.md", enabled = false}]')
        self.assertEqual(command[-1], "do it")

    def test_plan_counts_judge_calls_and_summary_scores_arms(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill_dir = Path(directory) / "demo"
            (skill_dir / "evals").mkdir(parents=True)
            (skill_dir / "evals" / "evals.json").write_text(
                json.dumps(
                    {
                        "skill_name": "demo",
                        "evals": [{"id": 1, "prompt": "p", "expected_output": "e", "assertions": ["a", "b"]}],
                    }
                )
            )
            (skill_dir / "evals" / "routing.json").write_text(
                json.dumps([{"query": "q1", "should_trigger": True}, {"query": "q2", "should_trigger": False}])
            )
            planned = runner.plan_runs(skill_dir, ("execution", "routing"), 2, ("with-skill", "without-skill"))
        self.assertEqual(len(planned), 8)
        self.assertEqual(runner.codex_calls(planned), 12)

        results = [
            {"case": "execution-01", "arm": "with-skill", "attempt": 1, "skill_fired": True,
             "assertions": [{"passed": True}, {"passed": True}], "grade_error": None, "tokens": {"input": 5}},
            {"case": "execution-01", "arm": "without-skill", "attempt": 1, "skill_fired": False,
             "assertions": [{"passed": True}, {"passed": False}], "grade_error": None, "tokens": {"input": 3}},
            {"case": "routing-01", "arm": "with-skill", "attempt": 1, "skill_fired": True,
             "should_trigger": True, "routing_pass": True},
            {"case": "routing-02", "arm": "with-skill", "attempt": 1, "skill_fired": True,
             "should_trigger": False, "routing_pass": False},
        ]
        summary = runner.summarize(results)
        self.assertEqual(summary["execution"]["with-skill"]["assertions_passed"], 2)
        self.assertEqual(summary["execution"]["without-skill"]["assertions_passed"], 1)
        self.assertEqual(summary["routing"]["positives_fired"], "1/1")
        self.assertEqual(summary["routing"]["negatives_quiet"], "0/1")
        self.assertEqual(summary["routing"]["misses"], ["routing-02"])
        self.assertEqual(summary["tokens"]["input"], 8)


if __name__ == "__main__":
    unittest.main()
