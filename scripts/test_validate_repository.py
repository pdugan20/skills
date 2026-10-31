#!/usr/bin/env python3
"""Tests for repository validation helpers."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

import validate_repository


def load_object(path: Path) -> dict[str, Any]:
    value = validate_repository.load_json(path)
    assert isinstance(value, dict)
    return value


class ValidateRepositoryTests(unittest.TestCase):
    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate_repository.validate(), [])

    def test_package_and_plugin_identity_is_explicit(self) -> None:
        package = load_object(validate_repository.ROOT / "package.json")
        portable = load_object(
            validate_repository.ROOT / "plugin.json"
        )
        claude = load_object(
            validate_repository.ROOT / ".claude-plugin" / "plugin.json"
        )
        codex = load_object(
            validate_repository.ROOT / ".codex-plugin" / "plugin.json"
        )

        self.assertEqual(package["name"], validate_repository.PLUGIN_NAME)
        self.assertEqual(portable["name"], validate_repository.PLUGIN_NAME)
        self.assertEqual(portable["$schema"], validate_repository.AGENT_PLUGIN_SCHEMA)
        self.assertEqual(claude["name"], validate_repository.PLUGIN_NAME)
        self.assertEqual(codex["name"], validate_repository.PLUGIN_NAME)

    def validate_renovate_text(self, contents: str) -> list[str]:
        with tempfile.TemporaryDirectory(dir=validate_repository.ROOT) as directory:
            path = Path(directory) / "renovate.json"
            path.write_text(contents, encoding="utf-8")
            return validate_repository.validate_renovate_bootstrap(path)

    def test_renovate_bootstrap_is_exact_disabled_and_bounded(self) -> None:
        self.assertEqual(validate_repository.validate_renovate_bootstrap(), [])

        for enabled in (True, 0, 1, None, "false"):
            with self.subTest(enabled=enabled):
                config = {
                    "$schema": validate_repository.RENOVATE_SCHEMA,
                    "enabled": enabled,
                    "enabledManagers": validate_repository.RENOVATE_MANAGERS,
                }
                self.assertTrue(self.validate_renovate_text(json.dumps(config)))

        expanded = {
            "$schema": validate_repository.RENOVATE_SCHEMA,
            "enabled": False,
            "enabledManagers": ["npm", "github-actions", "custom.regex"],
        }
        self.assertTrue(self.validate_renovate_text(json.dumps(expanded)))

        active_policy = {
            "$schema": validate_repository.RENOVATE_SCHEMA,
            "enabled": False,
            "enabledManagers": validate_repository.RENOVATE_MANAGERS,
            "automerge": True,
        }
        self.assertTrue(self.validate_renovate_text(json.dumps(active_policy)))

    def test_renovate_bootstrap_rejects_duplicate_keys(self) -> None:
        errors = self.validate_renovate_text(
            '{"$schema":"https://docs.renovatebot.com/renovate-schema.json",'
            '"enabled":true,"enabled":false,'
            '"enabledManagers":["npm"],'
            '"enabledManagers":["npm","github-actions"]}'
        )

        self.assertTrue(any("ambiguous JSON" in error for error in errors))

    def test_agent_plugin_manifest_rejects_unknown_fields(self) -> None:
        manifest = {
            "$schema": validate_repository.AGENT_PLUGIN_SCHEMA,
            "name": "patrick-skills",
            "skills": "./skills/",
        }

        errors = validate_repository.validate_agent_plugin_manifest(manifest)

        self.assertIn("plugin.json: unsupported fields: skills", errors)

    def test_agent_plugin_manifest_rejects_invalid_extensions(self) -> None:
        manifest = {
            "$schema": validate_repository.AGENT_PLUGIN_SCHEMA,
            "name": "patrick-skills",
            "extensions": {"com.example.client": "invalid"},
        }

        errors = validate_repository.validate_agent_plugin_manifest(manifest)

        self.assertIn("plugin.json: each extension value must be an object", errors)

    def test_release_tag_matches_version(self) -> None:
        package = load_object(validate_repository.ROOT / "package.json")
        self.assertIsInstance(package, dict)
        self.assertEqual(validate_repository.validate(f"v{package['version']}"), [])

    def test_release_tag_mismatch_is_rejected(self) -> None:
        package = load_object(validate_repository.ROOT / "package.json")
        self.assertIsInstance(package, dict)
        errors = validate_repository.validate("v9.9.9")
        self.assertTrue(any(f"must equal v{package['version']}" in error for error in errors))

    def test_codex_starter_prompt_limits_are_enforced(self) -> None:
        manifest = {
            "interface": {
                "defaultPrompt": [
                    "Prompt one.",
                    "Prompt two.",
                    "Prompt three.",
                    "Prompt four.",
                ]
            }
        }

        errors = validate_repository.validate_codex_interface(manifest)

        self.assertIn(
            ".codex-plugin/plugin.json: defaultPrompt supports at most 3 entries",
            errors,
        )

    def test_skills_sh_config_uses_current_schema(self) -> None:
        config = load_object(validate_repository.ROOT / "skills.sh.json")
        self.assertIsInstance(config, dict)
        self.assertEqual(validate_repository.validate_skills_sh_config(config), [])
        self.assertNotIn("groups", config)

    def test_skills_sh_config_rejects_duplicate_skills(self) -> None:
        config = {
            "$schema": validate_repository.SKILLS_SH_SCHEMA,
            "notGrouped": "bottom",
            "groupings": [
                {
                    "title": "Duplicate",
                    "skills": ["feature-spike", "feature-spike"],
                }
            ],
        }

        errors = validate_repository.validate_skills_sh_config(config)

        self.assertIn("skills.sh.json: each skill may appear in only one grouping", errors)

    def test_w011_audit_exception_requires_runtime_trust_boundary(self) -> None:
        policy = {
            "requiredProviders": ["snyk"],
            "exceptions": [
                {
                    "skill": "feature-spike",
                    "provider": "snyk",
                    "status": "warn",
                    "riskLevel": "medium",
                    "issueCodes": ["W011"],
                    "owner": "pdugan20",
                    "reviewBy": "2026-10-31",
                    "rationale": "The skill consumes required user input.",
                    "upstreamIssue": "https://github.com/snyk/agent-scan/issues/392",
                }
            ],
        }
        with tempfile.TemporaryDirectory(dir=validate_repository.ROOT) as directory:
            skills_root = Path(directory)
            skill_dir = skills_root / "feature-spike"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text("# Feature spike\n", encoding="utf-8")

            errors = validate_repository.validate_skills_sh_audit_policy(
                policy, skills_root
            )

        self.assertTrue(any("require a ## Trust boundary" in error for error in errors))

    def test_audit_policy_never_accepts_fail_verdicts(self) -> None:
        policy = {
            "requiredProviders": ["snyk"],
            "exceptions": [
                {
                    "skill": "feature-spike",
                    "provider": "snyk",
                    "status": "fail",
                    "riskLevel": "high",
                    "issueCodes": ["W999"],
                    "owner": "pdugan20",
                    "reviewBy": "2026-10-31",
                    "rationale": "This must still be rejected.",
                    "upstreamIssue": "https://example.com/issue",
                }
            ],
        }

        errors = validate_repository.validate_skills_sh_audit_policy(policy)

        self.assertTrue(any("fail verdicts cannot be accepted" in error for error in errors))

    def test_eval_manifest_requires_execution_coverage(self) -> None:
        with tempfile.TemporaryDirectory(dir=validate_repository.ROOT) as directory:
            skill_dir = Path(directory)
            evals_dir = skill_dir / "evals"
            evals_dir.mkdir()
            (evals_dir / "evals.json").write_text(
                json.dumps(
                    {
                        "skill_name": "example-skill",
                        "evals": [
                            {
                                "id": 1,
                                "prompt": "Run a realistic example.",
                                "expected_output": "A useful result.",
                                "files": [],
                                "assertions": ["The result is useful."],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (evals_dir / "routing.json").write_text(
                json.dumps(
                    [
                        {"query": f"Positive routing case {index}", "should_trigger": True}
                        for index in range(4)
                    ]
                    + [
                        {"query": f"Negative routing case {index}", "should_trigger": False}
                        for index in range(4)
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_repository.validate_evals("example-skill", skill_dir)

        self.assertTrue(any("at least 3 execution evals" in error for error in errors))

    def test_routing_manifest_requires_near_misses(self) -> None:
        with tempfile.TemporaryDirectory(dir=validate_repository.ROOT) as directory:
            skill_dir = Path(directory)
            evals_dir = skill_dir / "evals"
            evals_dir.mkdir()
            (evals_dir / "evals.json").write_text(
                json.dumps(
                    {
                        "skill_name": "example-skill",
                        "evals": [
                            {
                                "id": index,
                                "prompt": f"Run realistic example {index}.",
                                "expected_output": "A useful result.",
                                "files": [],
                                "assertions": ["The result is useful."],
                            }
                            for index in range(3)
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (evals_dir / "routing.json").write_text(
                json.dumps(
                    [
                        {"query": f"Positive routing case {index}", "should_trigger": True}
                        for index in range(8)
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_repository.validate_evals("example-skill", skill_dir)

        self.assertTrue(any("at least 4 negative routing evals" in error for error in errors))

    def test_eval_manifest_rejects_missing_fixture(self) -> None:
        with tempfile.TemporaryDirectory(dir=validate_repository.ROOT) as directory:
            skill_dir = Path(directory)
            evals_dir = skill_dir / "evals"
            evals_dir.mkdir()
            (evals_dir / "evals.json").write_text(
                json.dumps(
                    {
                        "skill_name": "example-skill",
                        "evals": [
                            {
                                "id": index,
                                "prompt": f"Run realistic example {index}.",
                                "expected_output": "A useful result.",
                                "files": ["evals/fixtures/missing.md"] if index == 1 else [],
                                "assertions": ["The result is useful."],
                            }
                            for index in range(1, 4)
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (evals_dir / "routing.json").write_text(
                json.dumps(
                    [
                        {"query": f"Positive routing case {index}", "should_trigger": True}
                        for index in range(4)
                    ]
                    + [
                        {"query": f"Negative routing case {index}", "should_trigger": False}
                        for index in range(4)
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_repository.validate_evals("example-skill", skill_dir)

        self.assertTrue(any("references a missing file" in error for error in errors))


def eval_case(case_id: int, **extra: object) -> dict[str, object]:
    return {
        "id": case_id,
        "prompt": f"Run realistic example {case_id}.",
        "expected_output": "A useful result.",
        "files": [],
        "assertions": ["The result is useful."],
        **extra,
    }


def routing_cases(prefix: str, **extra: object) -> list[dict[str, object]]:
    return [
        {"query": f"{prefix} positive {index}", "should_trigger": True, **extra} for index in range(4)
    ] + [{"query": f"{prefix} negative {index}", "should_trigger": False} for index in range(4)]


class EvalSchemaTests(unittest.TestCase):
    def write_skill(
        self,
        root: Path,
        name: str,
        cases: list[dict[str, object]],
        routing: list[dict[str, object]],
    ) -> Path:
        skill_dir = root / name
        (skill_dir / "evals").mkdir(parents=True)
        (skill_dir / "evals" / "evals.json").write_text(
            json.dumps({"skill_name": name, "evals": cases}), encoding="utf-8"
        )
        (skill_dir / "evals" / "routing.json").write_text(json.dumps(routing), encoding="utf-8")
        return skill_dir

    def test_schema_rejects_misspelled_eval_field(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            case = eval_case(1)
            case["assertion"] = case.pop("assertions")
            skill_dir = self.write_skill(
                Path(directory), "demo", [case, eval_case(2), eval_case(3)], routing_cases("demo")
            )
            errors = validate_repository.validate_evals("demo", skill_dir)
        self.assertTrue(any("'assertions' is a required property" in error for error in errors), errors)
        self.assertTrue(any("'assertion' was unexpected" in error for error in errors), errors)

    def test_schema_rejects_unknown_tag(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill_dir = self.write_skill(
                Path(directory),
                "demo",
                [eval_case(1, tags=["untrusted"]), eval_case(2), eval_case(3)],
                routing_cases("demo"),
            )
            errors = validate_repository.validate_evals("demo", skill_dir)
        self.assertTrue(any("$.evals[0].tags[0]" in error for error in errors), errors)

    def test_trust_boundary_skill_requires_adversarial_case(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            cases = [eval_case(1), eval_case(2), eval_case(3)]
            skill_dir = self.write_skill(Path(directory), "demo", cases, routing_cases("demo"))
            missing = validate_repository.validate_evals("demo", skill_dir, requires_adversarial=True)
            cases[0]["tags"] = ["adversarial"]
            (skill_dir / "evals" / "evals.json").write_text(
                json.dumps({"skill_name": "demo", "evals": cases}), encoding="utf-8"
            )
            present = validate_repository.validate_evals("demo", skill_dir, requires_adversarial=True)
        self.assertTrue(any('tagged "adversarial"' in error for error in missing), missing)
        self.assertEqual(present, [])

    def test_routing_accepts_held_out_flag(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill_dir = self.write_skill(
                Path(directory),
                "demo",
                [eval_case(1), eval_case(2), eval_case(3)],
                routing_cases("demo", held_out=True),
            )
            self.assertEqual(validate_repository.validate_evals("demo", skill_dir), [])

    def test_positive_query_claimed_by_two_skills_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases = [eval_case(1), eval_case(2), eval_case(3)]
            self.write_skill(root, "first", cases, routing_cases("shared"))
            self.write_skill(root, "second", cases, routing_cases("Shared "))
            self.write_skill(root, "third", cases, routing_cases("other"))
            errors = validate_repository.validate_routing_overlap(root, ["first", "second", "third"])
        self.assertEqual(len(errors), 4, errors)
        self.assertTrue(all("first, second" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
