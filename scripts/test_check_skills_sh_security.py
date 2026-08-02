#!/usr/bin/env python3
"""Tests for the skills.sh security-audit policy check."""

from __future__ import annotations

import unittest
from datetime import date

import check_skills_sh_security


def overview_html(skill_name: str, statuses: dict[str, str]) -> str:
    cards = "".join(
        f'<a href="/pdugan20/skills/{skill_name}/security/{provider}">'
        f"<span>{provider}</span><span>{status.title()}</span></a>"
        for provider, status in statuses.items()
    )
    return f"<html><body>{cards}</body></html>"


def exception(review_by: str = "2026-10-31") -> dict[str, object]:
    return {
        "skill": "feature-spike",
        "provider": "snyk",
        "status": "warn",
        "riskLevel": "medium",
        "issueCodes": ["W011"],
        "owner": "pdugan20",
        "reviewBy": review_by,
        "rationale": "Required user input remains data, not authority.",
        "upstreamIssue": "https://github.com/snyk/agent-scan/issues/392",
    }


class CheckSkillsShSecurityTests(unittest.TestCase):
    def test_extracts_all_provider_statuses(self) -> None:
        html = overview_html(
            "feature-spike",
            {"agent-trust-hub": "pass", "socket": "pass", "snyk": "warn"},
        )

        self.assertEqual(
            check_skills_sh_security.audit_statuses(html, "feature-spike"),
            {"agent-trust-hub": "pass", "socket": "pass", "snyk": "warn"},
        )

    def test_rejects_unreviewed_warning(self) -> None:
        messages, detail_providers = check_skills_sh_security.compare_overview(
            "feature-spike",
            {"snyk": "warn"},
            {"snyk"},
            {},
            date(2026, 7, 31),
        )

        self.assertEqual(messages, ["feature-spike/snyk: unreviewed warn verdict"])
        self.assertEqual(detail_providers, [])

    def test_reviewed_warning_requires_exact_detail(self) -> None:
        reviewed = exception()
        messages, detail_providers = check_skills_sh_security.compare_overview(
            "feature-spike",
            {"snyk": "warn"},
            {"snyk"},
            {("feature-spike", "snyk"): reviewed},
            date(2026, 7, 31),
        )

        self.assertEqual(messages, [])
        self.assertEqual(detail_providers, ["snyk"])
        detail_html = """
            <html><body>
            <span>Risk Level: MEDIUM</span>
            <p><span>MEDIUM</span> W011: Third-party content exposure.</p>
            <script>W999 Risk Level: CRITICAL</script>
            </body></html>
        """
        self.assertEqual(
            check_skills_sh_security.compare_detail(
                "feature-spike", "snyk", detail_html, reviewed
            ),
            [],
        )

    def test_rejects_changed_issue_code(self) -> None:
        messages = check_skills_sh_security.compare_detail(
            "feature-spike",
            "snyk",
            "<p>Risk Level: MEDIUM</p><p>W012: Runtime dependency.</p>",
            exception(),
        )

        self.assertTrue(any("expected issue codes ['W011']" in message for message in messages))

    def test_expired_exception_fails(self) -> None:
        reviewed = exception("2026-07-30")
        messages, detail_providers = check_skills_sh_security.compare_overview(
            "feature-spike",
            {"snyk": "warn"},
            {"snyk"},
            {("feature-spike", "snyk"): reviewed},
            date(2026, 7, 31),
        )

        self.assertEqual(
            messages,
            ["feature-spike/snyk: exception review expired on 2026-07-30"],
        )
        self.assertEqual(detail_providers, [])

    def test_passing_provider_requires_stale_exception_removal(self) -> None:
        messages, detail_providers = check_skills_sh_security.compare_overview(
            "feature-spike",
            {"snyk": "pass"},
            {"snyk"},
            {("feature-spike", "snyk"): exception()},
            date(2026, 7, 31),
        )

        self.assertEqual(
            messages,
            ["feature-spike/snyk: now passes; remove its stale audit exception"],
        )
        self.assertEqual(detail_providers, [])


if __name__ == "__main__":
    unittest.main()
