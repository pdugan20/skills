"""Command line entry point: python3 -m ingest summarize <document> [--dry-run]."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ingest.pipeline import summarize_document


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ingest")
    commands = parser.add_subparsers(dest="command", required=True)
    summarize = commands.add_parser("summarize", help="summarize one partner document")
    summarize.add_argument("document", type=Path)
    summarize.add_argument("--dry-run", action="store_true", help="never call callbacks or read credentials")
    args = parser.parse_args(argv)

    if not args.dry_run:
        print("live mode needs staging credentials from the secret store; use --dry-run locally", file=sys.stderr)
        return 2
    result = summarize_document(args.document.read_text(encoding="utf-8"))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
