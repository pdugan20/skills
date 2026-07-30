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
MIN_EXECUTION_EVALS = 3
MIN_ROUTING_EVALS_PER_CLASS = 4


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML frontmatter delimiter")
    try:
        return text.split("---\n", 2)[1]
    except IndexError as error:
        raise ValueError("missing closing YAML frontmatter delimiter") from error


def is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_evals(skill_name: str, skill_dir: Path) -> list[str]:
    """Validate Agent Skills behavioral and routing evals."""
    errors: list[str] = []
    evals_path = skill_dir / "evals" / "evals.json"
    routing_path = skill_dir / "evals" / "routing.json"

    if not evals_path.is_file():
        errors.append(f"{evals_path.relative_to(ROOT)}: missing execution evals")
    else:
        try:
            manifest = load_json(evals_path)
        except (json.JSONDecodeError, OSError) as error:
            errors.append(f"{evals_path.relative_to(ROOT)}: invalid JSON ({error})")
        else:
            if not isinstance(manifest, dict):
                errors.append(f"{evals_path.relative_to(ROOT)}: root must be an object")
                manifest = {}
            if manifest.get("skill_name") != skill_name:
                errors.append(f"{evals_path.relative_to(ROOT)}: skill_name must match its directory")
            cases = manifest.get("evals")
            if not isinstance(cases, list):
                errors.append(f"{evals_path.relative_to(ROOT)}: evals must be an array")
            else:
                if len(cases) < MIN_EXECUTION_EVALS:
                    errors.append(
                        f"{evals_path.relative_to(ROOT)}: requires at least "
                        f"{MIN_EXECUTION_EVALS} execution evals"
                    )
                seen_ids: set[int] = set()
                for index, case in enumerate(cases):
                    label = f"{evals_path.relative_to(ROOT)}: evals[{index}]"
                    if not isinstance(case, dict):
                        errors.append(f"{label} must be an object")
                        continue
                    case_id = case.get("id")
                    if not isinstance(case_id, int) or isinstance(case_id, bool):
                        errors.append(f"{label}.id must be an integer")
                    elif case_id in seen_ids:
                        errors.append(f"{label}.id must be unique")
                    else:
                        seen_ids.add(case_id)
                    for field in ("prompt", "expected_output"):
                        if not is_nonempty_string(case.get(field)):
                            errors.append(f"{label}.{field} must be a non-empty string")
                    assertions = case.get("assertions")
                    if not isinstance(assertions, list) or not assertions:
                        errors.append(f"{label}.assertions must be a non-empty array")
                    elif any(not is_nonempty_string(item) for item in assertions):
                        errors.append(f"{label}.assertions must contain only non-empty strings")
                    files = case.get("files", [])
                    if not isinstance(files, list) or any(not is_nonempty_string(item) for item in files):
                        errors.append(f"{label}.files must contain only non-empty strings")
                    elif isinstance(files, list):
                        for item in files:
                            file_path = Path(item)
                            if file_path.is_absolute() or ".." in file_path.parts:
                                errors.append(f"{label}.files contains an unsafe path: {item}")
                            elif not (skill_dir / file_path).is_file():
                                errors.append(f"{label}.files references a missing file: {item}")

    if not routing_path.is_file():
        errors.append(f"{routing_path.relative_to(ROOT)}: missing routing evals")
    else:
        try:
            routing = load_json(routing_path)
        except (json.JSONDecodeError, OSError) as error:
            errors.append(f"{routing_path.relative_to(ROOT)}: invalid JSON ({error})")
        else:
            if not isinstance(routing, list):
                errors.append(f"{routing_path.relative_to(ROOT)}: root must be an array")
            else:
                counts = {True: 0, False: 0}
                seen_queries: set[str] = set()
                for index, case in enumerate(routing):
                    label = f"{routing_path.relative_to(ROOT)}: [{index}]"
                    if not isinstance(case, dict):
                        errors.append(f"{label} must be an object")
                        continue
                    query = case.get("query")
                    should_trigger = case.get("should_trigger")
                    if not is_nonempty_string(query):
                        errors.append(f"{label}.query must be a non-empty string")
                    elif query in seen_queries:
                        errors.append(f"{label}.query must be unique")
                    else:
                        seen_queries.add(query)
                    if not isinstance(should_trigger, bool):
                        errors.append(f"{label}.should_trigger must be a boolean")
                    else:
                        counts[should_trigger] += 1
                for should_trigger, name in ((True, "positive"), (False, "negative")):
                    if counts[should_trigger] < MIN_ROUTING_EVALS_PER_CLASS:
                        errors.append(
                            f"{routing_path.relative_to(ROOT)}: requires at least "
                            f"{MIN_ROUTING_EVALS_PER_CLASS} {name} routing evals"
                        )

    return errors


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

    errors.extend(validate_evals(skill_name, skill_dir))

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
    assert isinstance(package, dict)
    assert isinstance(claude, dict)
    assert isinstance(codex, dict)
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

    skills_config = load_json(ROOT / "skills.sh.json")
    assert isinstance(skills_config, dict)
    groups = skills_config.get("groups", [])
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
