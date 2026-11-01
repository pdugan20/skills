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


def alert(severity: str, path: str) -> str:
    return (
        f"<div><span>Security</span> <span>{path}</span> <span>{severity}</span> <span>Security</span> "
        f"<span>{severity}</span> <span>{path}</span> <p>Description of the alert.</p> "
        "<span>Confidence: 94 %</span> <span>Severity: 82 %</span></div>"
    )


def socket_page(*alerts: str, count: int | None = None) -> str:
    total = len(alerts) if count is None else count
    return f"<p>{total} alert found: Security</p>{''.join(alerts)}<h2>Audit Metadata</h2>"


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

    def test_socket_exceptions_match_the_exact_flagged_files(self) -> None:
        reviewed = {**exception(), "provider": "socket", "alertFiles": ["evals/fixtures/records.md"]}
        del reviewed["issueCodes"]
        detail_html = socket_page(alert("MEDIUM", "evals/fixtures/records.md"))
        self.assertEqual(
            check_skills_sh_security.compare_detail("feature-spike", "socket", detail_html, reviewed), []
        )
        moved = detail_html.replace("evals/fixtures/records.md", "SKILL.md")
        messages = check_skills_sh_security.compare_detail("feature-spike", "socket", moved, reviewed)
        self.assertTrue(any("expected alert files" in message for message in messages))
        escalated = detail_html.replace("<span>MEDIUM</span>", "<span>HIGH</span>")
        messages = check_skills_sh_security.compare_detail("feature-spike", "socket", escalated, reviewed)
        self.assertTrue(any("expected medium risk, found high" in message for message in messages))
        with self.assertRaises(ValueError):
            check_skills_sh_security.compare_detail("feature-spike", "socket", "<p>No alerts</p>", reviewed)

    def test_socket_parsing_fails_closed_on_unknown_or_extra_alerts(self) -> None:
        known = alert("MEDIUM", "evals/fixtures/records.md")
        with self.assertRaisesRegex(ValueError, "unknown severity"):
            check_skills_sh_security.socket_alerts(socket_page(known, alert("SEVERE", "SKILL.md"), count=2))
        with self.assertRaisesRegex(ValueError, "reports 1 alerts but 2"):
            check_skills_sh_security.socket_alerts(socket_page(known, alert("LOW", "SKILL.md"), count=1))
        decoy = "<p>Example: HIGH Security HIGH SKILL.md was flagged elsewhere.</p>"
        files, risk = check_skills_sh_security.socket_alerts(decoy + socket_page(known) + decoy)
        self.assertEqual((files, risk), ({"evals/fixtures/records.md"}, "medium"))

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
