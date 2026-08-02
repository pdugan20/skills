#!/usr/bin/env python3
"""Check skills.sh audit verdicts against the repository's reviewed policy."""

from __future__ import annotations

import argparse
import json
import re
import time
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request

from check_skills_sh import (
    DEFAULT_REQUEST_DELAY_SECONDS,
    REPOSITORY,
    expected_skills,
    read_request,
)

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "skills-sh-audits.json"
VALID_STATUSES = frozenset({"pass", "warn", "fail"})
ISSUE_CODE_RE = re.compile(r"\b[A-Z]\d{3}\b")
RISK_LEVEL_RE = re.compile(r"Risk Level:\s*(LOW|MEDIUM|HIGH|CRITICAL)\b", re.IGNORECASE)


class AuditCardParser(HTMLParser):
    """Extract provider verdict cards from one public skill page."""

    def __init__(self, skill_name: str, repository: str = REPOSITORY) -> None:
        super().__init__()
        self._prefix = f"/{repository}/{skill_name}/security/"
        self._provider: str | None = None
        self._depth = 0
        self._text: list[str] = []
        self.statuses: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self._provider is not None:
            self._depth += 1
            return
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if isinstance(href, str) and href.startswith(self._prefix):
            self._provider = href.removeprefix(self._prefix).strip("/")
            self._depth = 1
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._provider is not None:
            self._text.append(data)

    def handle_endtag(self, _tag: str) -> None:
        if self._provider is None:
            return
        self._depth -= 1
        if self._depth:
            return
        normalized = " ".join(" ".join(self._text).split()).lower()
        matches = [status for status in VALID_STATUSES if re.search(rf"\b{status}\b", normalized)]
        if len(matches) != 1:
            raise ValueError(f"{self._provider}: could not determine one audit status")
        self.statuses[self._provider] = matches[0]
        self._provider = None
        self._text = []


class VisibleTextParser(HTMLParser):
    """Collect visible page text while ignoring hydration and styling scripts."""

    def __init__(self) -> None:
        super().__init__()
        self._ignored_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, _attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self._ignored_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._ignored_depth:
            self.parts.append(data)


def audit_statuses(html: str, skill_name: str) -> dict[str, str]:
    parser = AuditCardParser(skill_name)
    parser.feed(html)
    if not parser.statuses:
        raise ValueError(f"{skill_name}: no skills.sh audit cards found")
    return parser.statuses


def audit_detail(html: str) -> tuple[set[str], str]:
    parser = VisibleTextParser()
    parser.feed(html)
    text = " ".join(" ".join(parser.parts).split())
    codes = set(ISSUE_CODE_RE.findall(text))
    risk_match = RISK_LEVEL_RE.search(text)
    if risk_match is None:
        raise ValueError("audit detail has no risk level")
    return codes, risk_match.group(1).lower()


def exception_index(policy: dict[str, object]) -> dict[tuple[str, str], dict[str, object]]:
    exceptions = policy.get("exceptions")
    if not isinstance(exceptions, list):
        raise ValueError("skills-sh-audits.json: exceptions must be an array")
    indexed: dict[tuple[str, str], dict[str, object]] = {}
    for exception in exceptions:
        if not isinstance(exception, dict):
            raise ValueError("skills-sh-audits.json: every exception must be an object")
        skill = exception.get("skill")
        provider = exception.get("provider")
        if not isinstance(skill, str) or not isinstance(provider, str):
            raise ValueError("skills-sh-audits.json: exception skill and provider must be strings")
        key = (skill, provider)
        if key in indexed:
            raise ValueError(f"skills-sh-audits.json: duplicate exception for {skill}/{provider}")
        indexed[key] = exception
    return indexed


def compare_overview(
    skill_name: str,
    actual: dict[str, str],
    required_providers: set[str],
    exceptions: dict[tuple[str, str], dict[str, object]],
    today: date,
) -> tuple[list[str], list[str]]:
    messages: list[str] = []
    detail_providers: list[str] = []
    missing = sorted(required_providers - set(actual))
    unexpected = sorted(set(actual) - required_providers)
    if missing:
        messages.append(f"{skill_name}: missing audit providers: {', '.join(missing)}")
    if unexpected:
        messages.append(f"{skill_name}: unreviewed audit providers: {', '.join(unexpected)}")

    for provider in sorted(required_providers & set(actual)):
        status = actual[provider]
        exception = exceptions.get((skill_name, provider))
        if status == "pass":
            if exception is not None:
                messages.append(
                    f"{skill_name}/{provider}: now passes; remove its stale audit exception"
                )
            continue
        if exception is None:
            messages.append(f"{skill_name}/{provider}: unreviewed {status} verdict")
            continue
        expected_status = exception.get("status")
        if status != expected_status:
            messages.append(
                f"{skill_name}/{provider}: expected {expected_status}, found {status}"
            )
            continue
        review_by = exception.get("reviewBy")
        try:
            deadline = date.fromisoformat(review_by) if isinstance(review_by, str) else None
        except ValueError:
            deadline = None
        if deadline is None:
            messages.append(f"{skill_name}/{provider}: exception has an invalid reviewBy date")
            continue
        if today > deadline:
            messages.append(
                f"{skill_name}/{provider}: exception review expired on {deadline.isoformat()}"
            )
            continue
        detail_providers.append(provider)
    return messages, detail_providers


def compare_detail(
    skill_name: str,
    provider: str,
    html: str,
    exception: dict[str, object],
) -> list[str]:
    actual_codes, actual_risk = audit_detail(html)
    configured_codes = exception.get("issueCodes")
    expected_codes = set(configured_codes) if isinstance(configured_codes, list) else set()
    expected_risk = exception.get("riskLevel")
    messages: list[str] = []
    if actual_codes != expected_codes:
        messages.append(
            f"{skill_name}/{provider}: expected issue codes {sorted(expected_codes)}, "
            f"found {sorted(actual_codes)}"
        )
    if actual_risk != expected_risk:
        messages.append(
            f"{skill_name}/{provider}: expected {expected_risk} risk, found {actual_risk}"
        )
    return messages


def fetch_page(url: str) -> str:
    separator = "&" if "?" in url else "?"
    request = Request(
        f"{url}{separator}audit={int(time.time())}",
        headers={
            "Cache-Control": "no-cache",
            "User-Agent": "pdugan20-skills-security-check/1.0",
        },
    )
    return read_request(request).decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    parser.add_argument(
        "--request-delay-seconds",
        type=float,
        default=DEFAULT_REQUEST_DELAY_SECONDS,
        help="Minimum pause between separate skills.sh reads",
    )
    args = parser.parse_args()
    if args.request_delay_seconds < 0:
        parser.error("--request-delay-seconds cannot be negative")

    try:
        policy = json.loads(args.policy.read_text(encoding="utf-8"))
        if not isinstance(policy, dict):
            raise ValueError("skills-sh-audits.json: root must be an object")
        providers = policy.get("requiredProviders")
        if not isinstance(providers, list) or any(not isinstance(item, str) for item in providers):
            raise ValueError("skills-sh-audits.json: requiredProviders must contain strings")
        required_providers = set(providers)
        exceptions = exception_index(policy)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"skills.sh audit policy is invalid: {error}")
        return 1

    messages: list[str] = []
    made_request = False

    def pace_request() -> None:
        nonlocal made_request
        if made_request and args.request_delay_seconds:
            time.sleep(args.request_delay_seconds)
        made_request = True

    for skill_name in sorted(expected_skills()):
        try:
            pace_request()
            overview = fetch_page(f"https://www.skills.sh/{REPOSITORY}/{skill_name}")
            statuses = audit_statuses(overview, skill_name)
            overview_messages, detail_providers = compare_overview(
                skill_name,
                statuses,
                required_providers,
                exceptions,
                date.today(),
            )
            messages.extend(overview_messages)
            for provider in detail_providers:
                pace_request()
                detail = fetch_page(
                    f"https://www.skills.sh/{REPOSITORY}/{skill_name}/security/{provider}"
                )
                messages.extend(
                    compare_detail(
                        skill_name,
                        provider,
                        detail,
                        exceptions[(skill_name, provider)],
                    )
                )
        except HTTPError as error:
            messages.append(f"{skill_name}: skills.sh returned HTTP {error.code}")
        except (URLError, OSError, UnicodeError, ValueError) as error:
            messages.append(f"{skill_name}: could not inspect skills.sh audits: {error}")

    if messages:
        print("skills.sh security audits differ from reviewed policy:")
        for message in messages:
            print(f"- {message}")
        return 1

    print(
        f"skills.sh security audits match reviewed policy for "
        f"{len(expected_skills())} skills and {len(required_providers)} providers."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
