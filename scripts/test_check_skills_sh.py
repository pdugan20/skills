#!/usr/bin/env python3
"""Tests for the skills.sh freshness check."""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch
from urllib.error import HTTPError
from urllib.request import Request

import check_skills_sh


def collection_html(skills: list[str]) -> str:
    parts = [
        {
            "@type": "SoftwareApplication",
            "name": name,
            "url": f"https://www.skills.sh/pdugan20/skills/{name}",
        }
        for name in skills
    ]
    return f"""
        <html><head>
        <script type="application/ld+json">
        {{
          "@context": "https://schema.org",
          "@type": "CollectionPage",
          "name": "pdugan20/skills — Agent skills",
          "url": "https://www.skills.sh/pdugan20/skills",
          "hasPart": {__import__('json').dumps(parts)}
        }}
        </script>
        </head></html>
    """


class CheckSkillsShTests(unittest.TestCase):
    @staticmethod
    def make_skills_root(root: Path, names: list[str]) -> Path:
        skills_root = root / "skills"
        for name in names:
            skill_dir = skills_root / name
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(f"# {name}\n", encoding="utf-8")
        return skills_root

    def test_retries_rate_limited_requests_after_server_delay(self) -> None:
        response = Mock()
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=None)
        response.read.return_value = b"current"
        error = HTTPError(
            "https://skills.sh/example",
            429,
            "Too Many Requests",
            {"Retry-After": "0"},
            None,
        )
        self.addCleanup(error.close)

        with (
            patch.object(check_skills_sh, "urlopen", side_effect=[error, response]) as opener,
            patch.object(check_skills_sh.time, "sleep") as sleep,
        ):
            body = check_skills_sh.read_request(Request("https://skills.sh/example"))

        self.assertEqual(body, b"current")
        self.assertEqual(opener.call_count, 2)
        sleep.assert_called_once_with(0.0)

    def test_does_not_retry_non_transient_http_errors(self) -> None:
        error = HTTPError(
            "https://skills.sh/missing",
            404,
            "Not Found",
            {},
            None,
        )
        self.addCleanup(error.close)

        with (
            patch.object(check_skills_sh, "urlopen", side_effect=error) as opener,
            patch.object(check_skills_sh.time, "sleep") as sleep,
            self.assertRaises(HTTPError),
        ):
            check_skills_sh.read_request(Request("https://skills.sh/missing"))

        self.assertEqual(opener.call_count, 1)
        sleep.assert_not_called()

    def test_caps_server_retry_delay(self) -> None:
        error = HTTPError(
            "https://skills.sh/example",
            429,
            "Too Many Requests",
            {"Retry-After": "600"},
            None,
        )
        self.addCleanup(error.close)

        self.assertEqual(check_skills_sh.retry_delay_seconds(error, 0), 60.0)

    def test_main_stops_after_persistent_rate_limit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            skills_root = self.make_skills_root(Path(temporary_directory), ["one", "two"])
            error = HTTPError(
                "https://skills.sh/example",
                429,
                "Too Many Requests",
                {"Retry-After": "60"},
                None,
            )
            self.addCleanup(error.close)
            output = io.StringIO()
            with (
                patch.object(
                    sys,
                    "argv",
                    [
                        "check_skills_sh.py",
                        "--skills-root",
                        str(skills_root),
                        "--request-delay-seconds",
                        "0",
                        "--no-refresh-guidance",
                    ],
                ),
                patch.object(
                    check_skills_sh,
                    "fetch_catalog",
                    return_value=collection_html(["one", "two"]),
                ),
                patch.object(check_skills_sh, "fetch_snapshot", side_effect=error) as fetch,
                redirect_stdout(output),
            ):
                result = check_skills_sh.main()

        self.assertEqual(result, 1)
        self.assertEqual(fetch.call_count, 1)
        self.assertEqual(output.getvalue().count("rate limit persisted"), 1)

    def test_main_paces_separate_network_reads(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            skills_root = self.make_skills_root(Path(temporary_directory), ["one", "two"])
            output = io.StringIO()
            with (
                patch.object(
                    sys,
                    "argv",
                    [
                        "check_skills_sh.py",
                        "--skills-root",
                        str(skills_root),
                        "--request-delay-seconds",
                        "3.25",
                    ],
                ),
                patch.object(
                    check_skills_sh,
                    "fetch_catalog",
                    return_value=collection_html(["one", "two"]),
                ),
                patch.object(
                    check_skills_sh,
                    "fetch_snapshot",
                    side_effect=lambda name: {"SKILL.md": f"# {name}\n"},
                ),
                patch.object(check_skills_sh.time, "sleep") as sleep,
                redirect_stdout(output),
            ):
                result = check_skills_sh.main()

        self.assertEqual(result, 0)
        self.assertEqual(sleep.call_count, 2)
        sleep.assert_called_with(3.25)

    def test_extracts_collection_skill_names(self) -> None:
        html = collection_html(["feature-spike", "feature-delivery"])

        self.assertEqual(
            check_skills_sh.catalog_skills(html),
            {"feature-spike", "feature-delivery"},
        )

    def test_reports_missing_and_unexpected_skills(self) -> None:
        messages = check_skills_sh.compare(
            {"feature-spike", "feature-delivery"},
            {"feature-spike", "obsolete-skill"},
        )

        self.assertEqual(
            messages,
            [
                "missing from skills.sh: feature-delivery",
                "not present in this repository: obsolete-skill",
            ],
        )

    def test_reports_stale_snapshot_files(self) -> None:
        messages = check_skills_sh.compare_snapshot(
            "feature-spike",
            {"SKILL.md": "current", "agents/openai.yaml": "same"},
            {"SKILL.md": "old", "agents/openai.yaml": "same", "old.txt": "obsolete"},
        )

        self.assertEqual(
            messages,
            ["feature-spike snapshot has stale or incomplete files: SKILL.md, old.txt"],
        )

    def test_rejects_pages_without_collection_json_ld(self) -> None:
        with self.assertRaisesRegex(ValueError, "CollectionPage JSON-LD was not found"):
            check_skills_sh.catalog_skills("<html></html>")


if __name__ == "__main__":
    unittest.main()
