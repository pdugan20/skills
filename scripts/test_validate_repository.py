#!/usr/bin/env python3
"""Tests for repository validation helpers."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import validate_repository


class ValidateRepositoryTests(unittest.TestCase):
    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate_repository.validate(), [])

    def test_package_and_plugin_identity_is_explicit(self) -> None:
        package = validate_repository.load_json(validate_repository.ROOT / "package.json")
        claude = validate_repository.load_json(
            validate_repository.ROOT / ".claude-plugin" / "plugin.json"
        )
        codex = validate_repository.load_json(
            validate_repository.ROOT / ".codex-plugin" / "plugin.json"
        )

        self.assertEqual(package["name"], validate_repository.PLUGIN_NAME)
        self.assertEqual(claude["name"], validate_repository.PLUGIN_NAME)
        self.assertEqual(codex["name"], validate_repository.PLUGIN_NAME)

    def test_release_tag_matches_version(self) -> None:
        package = validate_repository.load_json(validate_repository.ROOT / "package.json")
        self.assertIsInstance(package, dict)
        self.assertEqual(validate_repository.validate(f"v{package['version']}"), [])

    def test_release_tag_mismatch_is_rejected(self) -> None:
        package = validate_repository.load_json(validate_repository.ROOT / "package.json")
        self.assertIsInstance(package, dict)
        errors = validate_repository.validate("v9.9.9")
        self.assertTrue(any(f"must equal v{package['version']}" in error for error in errors))

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


if __name__ == "__main__":
    unittest.main()
