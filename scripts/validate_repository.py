#!/usr/bin/env python3
"""Validate the repository's portable skills and synchronized package metadata."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "code-native-ui-ideation": True,
    "feature-delivery": True,
    "production-hardening": False,
}
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML frontmatter delimiter")
    try:
        return text.split("---\n", 2)[1]
    except IndexError as error:
        raise ValueError("missing closing YAML frontmatter delimiter") from error


def validate_skill(skill_name: str, implicit: bool) -> list[str]:
    errors: list[str] = []
    skill_dir = ROOT / "skills" / skill_name
    skill_file = skill_dir / "SKILL.md"
    openai_file = skill_dir / "agents" / "openai.yaml"
    if not skill_file.is_file():
        return [f"missing {skill_file.relative_to(ROOT)}"]
    if not openai_file.is_file():
        return [f"missing {openai_file.relative_to(ROOT)}"]

    text = skill_file.read_text(encoding="utf-8")
    try:
        metadata = frontmatter(text)
    except ValueError as error:
        return [f"{skill_file.relative_to(ROOT)}: {error}"]
    if f"name: {skill_name}\n" not in metadata:
        errors.append(f"{skill_file.relative_to(ROOT)}: frontmatter name must match its directory")
    if "description:" not in metadata:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing description")
    if len(text.splitlines()) > 500:
        errors.append(f"{skill_file.relative_to(ROOT)}: exceeds 500 lines")

    openai = openai_file.read_text(encoding="utf-8")
    expected_policy = f"allow_implicit_invocation: {str(implicit).lower()}"
    if expected_policy not in openai:
        errors.append(f"{openai_file.relative_to(ROOT)}: expected {expected_policy}")
    if f"${skill_name}" not in openai:
        errors.append(f"{openai_file.relative_to(ROOT)}: default prompt must mention ${skill_name}")
    return errors


def validate(release_tag: str | None = None) -> list[str]:
    errors: list[str] = []
    package = load_json(ROOT / "package.json")
    claude = load_json(ROOT / ".claude-plugin" / "plugin.json")
    codex = load_json(ROOT / ".codex-plugin" / "plugin.json")
    version = package.get("version")

    if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
        errors.append("package.json: version must be semantic x.y.z")
    for path, manifest in ((".claude-plugin/plugin.json", claude), (".codex-plugin/plugin.json", codex)):
        if manifest.get("name") != "patrick-workflows":
            errors.append(f"{path}: name must be patrick-workflows")
        if manifest.get("version") != version:
            errors.append(f"{path}: version must match package.json")

    actual_skills = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    if actual_skills != set(EXPECTED_SKILLS):
        errors.append(f"skills/: expected {sorted(EXPECTED_SKILLS)}, found {sorted(actual_skills)}")
    for skill_name, implicit in EXPECTED_SKILLS.items():
        errors.extend(validate_skill(skill_name, implicit))

    groups = load_json(ROOT / "skills.sh.json").get("groups", [])
    grouped = [skill for group in groups for skill in group.get("skills", [])]
    if sorted(grouped) != sorted(EXPECTED_SKILLS):
        errors.append("skills.sh.json: groupings must include every skill exactly once")

    if release_tag is not None and release_tag != f"v{version}":
        errors.append(f"release tag {release_tag!r} must equal v{version}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-tag")
    args = parser.parse_args()
    errors = validate(args.release_tag)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
