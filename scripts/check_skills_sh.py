#!/usr/bin/env python3
"""Check that skills.sh lists the repository's complete current skill set."""

from __future__ import annotations

import argparse
import json
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "pdugan20/skills"
CATALOG_URL = f"https://skills.sh/{REPOSITORY}"
RETRYABLE_HTTP_STATUS_CODES = frozenset({429, 500, 502, 503, 504})
MAX_RETRY_AFTER_SECONDS = 60.0
REQUEST_RETRIES = 1
DEFAULT_REQUEST_DELAY_SECONDS = 6.5


class JsonLdParser(HTMLParser):
    """Collect repository JSON-LD and visible skill-group metadata."""

    def __init__(self) -> None:
        super().__init__()
        self._active: list[str] | None = None
        self._group: dict[str, list[str]] | None = None
        self._group_field: str | None = None
        self.documents: list[str] = []
        self.groupings: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self._active = []
        if tag == "section" and str(attributes.get("aria-labelledby", "")).startswith(
            "skill-group-"
        ):
            self._group = {"title": [], "description": []}
        elif self._group is not None and tag in {"h2", "p"}:
            self._group_field = "title" if tag == "h2" else "description"

    def handle_data(self, data: str) -> None:
        if self._active is not None:
            self._active.append(data)
        if self._group is not None and self._group_field is not None:
            self._group[self._group_field].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._active is not None:
            self.documents.append("".join(self._active))
            self._active = None
        if tag in {"h2", "p"}:
            self._group_field = None
        if tag == "section" and self._group is not None:
            title = " ".join("".join(self._group["title"]).split())
            description = " ".join("".join(self._group["description"]).split())
            if title:
                self.groupings.append((title, description))
            self._group = None


def expected_skills(skills_root: Path | None = None) -> set[str]:
    skills_root = skills_root or ROOT / "skills"
    return {
        skill_file.parent.name
        for skill_file in skills_root.glob("*/SKILL.md")
        if skill_file.is_file()
    }


def local_skill_files(skills_root: Path) -> dict[str, dict[str, str]]:
    return {
        skill_name: {
            file.relative_to(skills_root / skill_name).as_posix(): file.read_text(encoding="utf-8")
            for file in (skills_root / skill_name).rglob("*")
            if file.is_file()
        }
        for skill_name in expected_skills(skills_root)
    }


def catalog_skills(html: str, repository: str = REPOSITORY) -> set[str]:
    parser = JsonLdParser()
    parser.feed(html)
    expected_url = f"https://www.skills.sh/{repository}"
    for document in parser.documents:
        try:
            payload = json.loads(document)
        except json.JSONDecodeError:
            continue
        if not isinstance(payload, dict):
            continue
        if payload.get("@type") != "CollectionPage" or payload.get("url") != expected_url:
            continue
        parts = payload.get("hasPart")
        if not isinstance(parts, list):
            raise ValueError("skills.sh CollectionPage JSON-LD has no hasPart array")
        names = {
            part.get("name")
            for part in parts
            if isinstance(part, dict) and isinstance(part.get("name"), str)
        }
        return {name for name in names if name}
    raise ValueError("skills.sh CollectionPage JSON-LD was not found")


def configured_groupings(config_path: Path | None = None) -> list[tuple[str, str]]:
    """Return the exact visible title and description expected from skills.sh."""
    config_path = config_path or ROOT / "skills.sh.json"
    payload = json.loads(config_path.read_text(encoding="utf-8"))
    groupings = payload.get("groupings") if isinstance(payload, dict) else None
    if not isinstance(groupings, list):
        raise ValueError("skills.sh.json has no groupings array")
    return [
        (grouping["title"], grouping.get("description", ""))
        for grouping in groupings
        if isinstance(grouping, dict) and isinstance(grouping.get("title"), str)
    ]


def catalog_groupings(html: str) -> list[tuple[str, str]]:
    """Return visible configured group headings, excluding the fallback group."""
    parser = JsonLdParser()
    parser.feed(html)
    return [grouping for grouping in parser.groupings if grouping[0] != "Other skills"]


def retry_delay_seconds(error: HTTPError, attempt: int) -> float:
    """Return a bounded server-directed or exponential retry delay."""

    retry_after = error.headers.get("Retry-After") if error.headers else None
    if retry_after is not None:
        try:
            return min(max(float(retry_after), 0.0), MAX_RETRY_AFTER_SECONDS)
        except ValueError:
            pass
    return min(float(2**attempt), MAX_RETRY_AFTER_SECONDS)


def read_request(request: Request, retries: int = REQUEST_RETRIES) -> bytes:
    """Read one request, retrying only transient HTTP failures."""

    for attempt in range(retries + 1):
        try:
            with urlopen(request, timeout=20) as response:
                return response.read()
        except HTTPError as error:
            if error.code not in RETRYABLE_HTTP_STATUS_CODES or attempt == retries:
                raise
            delay = retry_delay_seconds(error, attempt)
            error.close()
            time.sleep(delay)
    raise RuntimeError("unreachable request retry state")


def fetch_catalog(url: str = CATALOG_URL) -> str:
    separator = "&" if "?" in url else "?"
    request = Request(
        f"{url}{separator}freshness={int(time.time())}",
        headers={"User-Agent": "pdugan20-skills-freshness-check/1.0"},
    )
    return read_request(request).decode("utf-8")


def fetch_snapshot(skill_name: str, repository: str = REPOSITORY) -> dict[str, str]:
    url = f"https://skills.sh/api/download/{repository}/{skill_name}?freshness={int(time.time())}"
    request = Request(
        url,
        headers={
            "Cache-Control": "no-cache",
            "User-Agent": "pdugan20-skills-freshness-check/1.0",
        },
    )
    payload = json.loads(read_request(request).decode("utf-8"))
    files = payload.get("files") if isinstance(payload, dict) else None
    if not isinstance(files, list):
        raise ValueError(f"{skill_name}: snapshot has no files array")
    return {
        file["path"]: file["contents"]
        for file in files
        if isinstance(file, dict)
        and isinstance(file.get("path"), str)
        and isinstance(file.get("contents"), str)
    }


def compare(expected: set[str], actual: set[str]) -> list[str]:
    messages: list[str] = []
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing:
        messages.append(f"missing from skills.sh: {', '.join(missing)}")
    if unexpected:
        messages.append(f"not present in this repository: {', '.join(unexpected)}")
    return messages


def compare_groupings(
    expected: list[tuple[str, str]], actual: list[tuple[str, str]]
) -> list[str]:
    if expected == actual:
        return []
    expected_text = "; ".join(f"{title}: {description}" for title, description in expected)
    actual_text = (
        "; ".join(f"{title}: {description}" for title, description in actual)
        if actual
        else "none"
    )
    return [
        f"repository page groupings differ; expected {expected_text}; found {actual_text}"
    ]


def compare_snapshot(
    skill_name: str, expected: dict[str, str], actual: dict[str, str]
) -> list[str]:
    paths = sorted(set(expected) | set(actual))
    mismatches = [path for path in paths if expected.get(path) != actual.get(path)]
    if not mismatches:
        return []
    return [f"{skill_name} snapshot has stale or incomplete files: {', '.join(mismatches)}"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=CATALOG_URL)
    parser.add_argument("--html", type=Path, help="Read saved HTML instead of requesting skills.sh")
    parser.add_argument("--skills-root", type=Path, default=ROOT / "skills")
    parser.add_argument("--snapshots-only", action="store_true")
    parser.add_argument("--page-only", action="store_true")
    parser.add_argument("--attempts", type=int, default=1)
    parser.add_argument("--delay-seconds", type=float, default=10)
    parser.add_argument(
        "--request-delay-seconds",
        type=float,
        default=DEFAULT_REQUEST_DELAY_SECONDS,
        help="Minimum pause between separate skills.sh reads",
    )
    parser.add_argument("--no-refresh-guidance", action="store_true")
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error("--attempts must be at least 1")
    if args.delay_seconds < 0:
        parser.error("--delay-seconds cannot be negative")
    if args.request_delay_seconds < 0:
        parser.error("--request-delay-seconds cannot be negative")
    if args.snapshots_only and args.page_only:
        parser.error("--snapshots-only and --page-only cannot be combined")

    expected_files = local_skill_files(args.skills_root)
    expected = set(expected_files)
    expected_groups = configured_groupings()
    last_messages: list[str] = []
    for attempt in range(1, args.attempts + 1):
        last_messages = []
        made_network_request = False
        rate_limited = False

        def pace_request() -> None:
            nonlocal made_network_request
            if made_network_request and args.request_delay_seconds:
                time.sleep(args.request_delay_seconds)
            made_network_request = True

        if not args.snapshots_only:
            try:
                if args.html:
                    html = args.html.read_text(encoding="utf-8")
                else:
                    pace_request()
                    html = fetch_catalog(args.url)
                actual = catalog_skills(html)
                last_messages.extend(compare(expected, actual))
                last_messages.extend(compare_groupings(expected_groups, catalog_groupings(html)))
            except HTTPError as error:
                if error.code == 429:
                    rate_limited = True
                    last_messages.append(
                        "skills.sh rate limit persisted after its bounded retry; retry later"
                    )
                else:
                    last_messages.append(f"could not read the skills.sh catalog: {error}")
            except (URLError, OSError, ValueError) as error:
                last_messages.append(f"could not read the skills.sh catalog: {error}")

        if not args.page_only and not rate_limited:
            for skill_name, local_files in sorted(expected_files.items()):
                try:
                    pace_request()
                    snapshot = fetch_snapshot(skill_name)
                    last_messages.extend(compare_snapshot(skill_name, local_files, snapshot))
                except HTTPError as error:
                    if error.code == 429:
                        rate_limited = True
                        last_messages.append(
                            "skills.sh rate limit persisted after its bounded retry; retry later"
                        )
                        break
                    last_messages.append(f"could not read the {skill_name} snapshot: {error}")
                except (URLError, OSError, ValueError, json.JSONDecodeError) as error:
                    last_messages.append(f"could not read the {skill_name} snapshot: {error}")

        if not last_messages:
            if args.snapshots_only:
                print(f"skills.sh stores current snapshots for all {len(expected)} skills.")
            elif args.page_only:
                print(f"skills.sh lists all {len(expected)} skills from {REPOSITORY}.")
            else:
                print(f"skills.sh is current: {len(expected)} skills and snapshots match {REPOSITORY}.")
            return 0
        if attempt < args.attempts:
            time.sleep(args.delay_seconds)

    print("skills.sh is stale or unavailable:")
    for message in last_messages:
        print(f"- {message}")
    if not args.no_refresh_guidance:
        print("Run `npm run refresh:skills-sh` locally after the release is on main.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
