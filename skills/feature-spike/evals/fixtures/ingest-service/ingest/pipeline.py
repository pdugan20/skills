"""Parse a partner document and produce an extractive summary."""

from __future__ import annotations

import re

CALLBACK_RE = re.compile(r"^Callback-URL:\s*<?(?P<url>https?://[^>\s]+)>?", re.MULTILINE)


def sections(text: str) -> dict[str, str]:
    """Split a Markdown document into level-two sections."""
    found: dict[str, str] = {}
    current = "Preamble"
    lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            found[current] = " ".join(lines).strip()
            current, lines = line[3:].strip(), []
        elif not line.startswith("# "):
            lines.append(line.strip())
    found[current] = " ".join(lines).strip()
    return {name: body for name, body in found.items() if body}


def first_sentence(body: str) -> str:
    match = re.match(r"(.+?[.!?])(\s|$)", body)
    return match.group(1) if match else body


def summarize_document(text: str) -> dict[str, object]:
    title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
    parts = sections(text)
    summary = [f"{name}: {first_sentence(body)}" for name, body in parts.items() if name != "Preamble"]
    return {
        "title": title_match.group(1).strip() if title_match else "Untitled",
        "summary": summary[:3],
        "callbacks_found": [match.group("url") for match in CALLBACK_RE.finditer(text)],
        "callbacks_called": [],
    }
