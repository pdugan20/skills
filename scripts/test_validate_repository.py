#!/usr/bin/env python3
"""Tests for repository validation helpers."""

from __future__ import annotations

import unittest

import validate_repository


class ValidateRepositoryTests(unittest.TestCase):
    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate_repository.validate(), [])

    def test_release_tag_matches_version(self) -> None:
        self.assertEqual(validate_repository.validate("v1.0.0"), [])

    def test_release_tag_mismatch_is_rejected(self) -> None:
        errors = validate_repository.validate("v9.9.9")
        self.assertTrue(any("must equal v1.0.0" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
