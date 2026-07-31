#!/usr/bin/env python3
"""Tests for the bootstrap-repository read-only inspector."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "bootstrap-repository" / "scripts" / "inspect_repository.py"


def load_script(test: unittest.TestCase):
    test.assertTrue(SCRIPT.is_file(), f"missing portable helper: {SCRIPT}")
    spec = importlib.util.spec_from_file_location("bootstrap_repository_inspector", SCRIPT)
    test.assertIsNotNone(spec)
    test.assertIsNotNone(spec.loader)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(root: Path, relative: str, contents: str = "") -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents, encoding="utf-8")


class InspectRepositoryTests(unittest.TestCase):
    def test_reports_node_quality_contract_and_stable_ci_names(self) -> None:
        module = load_script(self)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(
                root,
                "package.json",
                json.dumps(
                    {
                        "name": "fieldnotes",
                        "packageManager": "npm@11.5.2",
                        "engines": {"node": ">=22 <23"},
                        "scripts": {
                            "check": "npm run typecheck && npm test",
                            "test": "jest",
                            "typecheck": "tsc --noEmit",
                            "dev": "expo start",
                        },
                    }
                ),
            )
            write(root, "package-lock.json")
            write(root, ".nvmrc", "22\n")
            write(root, "AGENTS.md", "# Repository instructions\n")
            write(root, "README.md", "# FieldNotes\n")
            write(root, ".github/dependabot.yml", "version: 2\n")
            write(
                root,
                ".github/workflows/ci.yml",
                """name: CI
on: [push]
jobs:
  verify:
    name: Verify
    runs-on: ubuntu-latest
    steps: []
  build:
    runs-on: ubuntu-latest
    steps: []
""",
            )

            report = module.inspect_local(root)

            self.assertEqual(report["ecosystems"], ["node"])
            self.assertEqual(report["lockfiles"], ["package-lock.json"])
            self.assertEqual(
                report["runtime_pins"],
                [".nvmrc", "package.json#engines.node", "package.json#packageManager"],
            )
            self.assertEqual(
                report["verification_commands"],
                ["npm run check", "npm run test", "npm run typecheck"],
            )
            self.assertEqual(report["dependency_automation"], [".github/dependabot.yml"])
            self.assertEqual(
                report["ci"],
                [
                    {
                        "path": ".github/workflows/ci.yml",
                        "workflow_name": "CI",
                        "jobs": [
                            {"id": "verify", "name": "Verify"},
                            {"id": "build", "name": "build"},
                        ],
                    }
                ],
            )

    def test_reports_python_packaging_release_and_tooling(self) -> None:
        module = load_script(self)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(
                root,
                "pyproject.toml",
                """[project]
name = "docweave-check"
requires-python = ">=3.11"

[project.scripts]
docweave-check = "docweave_check.cli:main"

[dependency-groups]
dev = ["pytest", "ruff", "mypy"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
target-version = "py311"

[tool.mypy]
strict = true
""",
            )
            write(root, "uv.lock")
            write(root, ".python-version", "3.11\n")
            for filename in (
                "README.md",
                "CHANGELOG.md",
                "CONTRIBUTING.md",
                "SECURITY.md",
                "LICENSE",
            ):
                write(root, filename)
            write(root, ".github/workflows/release.yml", "name: Release\njobs:\n  publish:\n    steps: []\n")

            report = module.inspect_local(root)

            self.assertEqual(report["ecosystems"], ["python"])
            self.assertEqual(report["lockfiles"], ["uv.lock"])
            self.assertEqual(report["runtime_pins"], [".python-version"])
            self.assertEqual(
                report["python"],
                {
                    "project_name": "docweave-check",
                    "requires_python": ">=3.11",
                    "commands": ["docweave-check"],
                    "tools": ["mypy", "pytest", "ruff"],
                },
            )
            self.assertEqual(report["release_automation"], [".github/workflows/release.yml"])
            self.assertEqual(
                report["documentation"],
                ["CHANGELOG.md", "CONTRIBUTING.md", "LICENSE", "README.md", "SECURITY.md"],
            )

    def test_reports_swift_project_sources_without_inventing_policy(self) -> None:
        module = load_script(self)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root, "project.yml", "name: PageTurnLab\n")
            write(root, "PageTurnLab.xcodeproj/project.pbxproj")
            write(root, "Sources/App.swift", "import SwiftUI\n")
            write(root, "README.md")

            report = module.inspect_local(root)

            self.assertEqual(report["ecosystems"], ["swift"])
            self.assertEqual(
                report["project_sources"],
                ["PageTurnLab.xcodeproj", "project.yml"],
            )
            self.assertEqual(report["ci"], [])
            self.assertEqual(report["dependency_automation"], [])
            self.assertNotIn("profile", report)
            self.assertNotIn("score", report)

    def test_github_inspection_uses_exact_read_only_api_targets(self) -> None:
        module = load_script(self)
        calls: list[list[str]] = []

        def runner(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
            calls.append(command)
            endpoint = command[-1]
            if endpoint.endswith("/rulesets/7"):
                payload = {
                    "id": 7,
                    "name": "Protect main",
                    "target": "branch",
                    "enforcement": "active",
                    "rules": [{"type": "required_status_checks"}],
                }
            elif endpoint.endswith("/rulesets?per_page=100"):
                payload = [
                    {
                        "id": 7,
                        "name": "Protect main",
                        "target": "branch",
                        "enforcement": "active",
                    }
                ]
            else:
                payload = {
                    "full_name": "pdugan20/fieldnotes",
                    "visibility": "private",
                    "default_branch": "main",
                    "description": "Field notes app",
                    "homepage": "",
                    "topics": ["expo", "react-native"],
                    "delete_branch_on_merge": True,
                    "allow_squash_merge": True,
                    "allow_merge_commit": False,
                    "allow_rebase_merge": False,
                    "security_and_analysis": {
                        "secret_scanning": {"status": "enabled"},
                    },
                }
            return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")

        report = module.inspect_github("pdugan20/fieldnotes", runner=runner)

        self.assertEqual(len(calls), 3)
        self.assertTrue(all(command[:4] == ["gh", "api", "--method", "GET"] for command in calls))
        self.assertEqual(
            [command[-1] for command in calls],
            [
                "repos/pdugan20/fieldnotes",
                "repos/pdugan20/fieldnotes/rulesets?per_page=100",
                "repos/pdugan20/fieldnotes/rulesets/7",
            ],
        )
        self.assertEqual(report["repository"], "pdugan20/fieldnotes")
        self.assertEqual(report["topics"], ["expo", "react-native"])
        self.assertEqual(
            report["rulesets"],
            [
                {
                    "id": 7,
                    "name": "Protect main",
                    "target": "branch",
                    "enforcement": "active",
                    "rule_types": ["required_status_checks"],
                }
            ],
        )

    def test_rejects_ambiguous_or_unsafe_github_targets(self) -> None:
        module = load_script(self)

        for value in (
            "fieldnotes",
            "https://github.com/pdugan20/fieldnotes",
            "pdugan20/../fieldnotes",
            "pdugan20/fieldnotes;gh repo delete",
        ):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "OWNER/REPOSITORY"):
                    module.validate_repository_name(value)


if __name__ == "__main__":
    unittest.main()
