#!/usr/bin/env python3
"""Extract one version's curated notes from CHANGELOG.md."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"


class ReleaseNotesError(Exception):
    """Raised when a release has no usable changelog section."""


def extract_release_notes(version: str, changelog: str) -> str:
    escaped = re.escape(version)
    match = re.search(
        rf"(?ms)^## \[{escaped}\](?:\s+-\s+\d{{4}}-\d{{2}}-\d{{2}})?\s*$\n"
        rf"(?P<body>.*?)(?=^## \[|\Z)",
        changelog,
    )
    if not match:
        raise ReleaseNotesError(f"CHANGELOG.md has no [{version}] section")

    body = re.split(r"\n(?=\[[^\]]+\]:\s)", match.group("body"), maxsplit=1)[
        0
    ].strip()
    if not body:
        raise ReleaseNotesError(f"CHANGELOG.md [{version}] section is empty")
    return f"{body}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        notes = extract_release_notes(args.version, CHANGELOG.read_text(encoding="utf-8"))
        if args.output:
            args.output.write_text(notes, encoding="utf-8")
        else:
            print(notes, end="")
    except (OSError, ReleaseNotesError) as error:
        raise SystemExit(f"Release notes failed: {error}") from error


if __name__ == "__main__":
    main()
