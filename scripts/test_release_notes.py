#!/usr/bin/env python3
"""Tests for curated release-note extraction."""

from __future__ import annotations

import unittest

import release_notes


class ReleaseNotesTests(unittest.TestCase):
    def test_extracts_requested_version_only(self) -> None:
        changelog = """# Changelog

## [Unreleased]

Later work.

## [1.2.3] - 2026-07-28

### Added

- A useful thing.

## [1.2.2] - 2026-07-20

- Older work.

[1.2.3]: https://example.com/releases/1.2.3
"""

        notes = release_notes.extract_release_notes("1.2.3", changelog)
        older_notes = release_notes.extract_release_notes("1.2.2", changelog)

        self.assertIn("A useful thing", notes)
        self.assertNotIn("Later work", notes)
        self.assertNotIn("Older work", notes)
        self.assertNotIn("example.com", older_notes)

    def test_rejects_missing_version(self) -> None:
        with self.assertRaisesRegex(release_notes.ReleaseNotesError, r"no \[2.0.0\]"):
            release_notes.extract_release_notes("2.0.0", "# Changelog\n")

    def test_rejects_empty_section(self) -> None:
        changelog = """# Changelog

## [2.0.0] - 2026-07-30

## [1.0.0] - 2026-07-20

- Older work.
"""

        with self.assertRaisesRegex(release_notes.ReleaseNotesError, "section is empty"):
            release_notes.extract_release_notes("2.0.0", changelog)


if __name__ == "__main__":
    unittest.main()
