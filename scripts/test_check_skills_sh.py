#!/usr/bin/env python3
"""Tests for the skills.sh freshness check."""

from __future__ import annotations

import unittest

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
