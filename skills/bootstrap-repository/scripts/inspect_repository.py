#!/usr/bin/env python3
"""Emit a read-only snapshot of local and optional GitHub repository configuration."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.11+ is expected.
    tomllib = None  # type: ignore[assignment]


REPOSITORY_RE = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})/[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)
QUALITY_SCRIPTS = {
    "build",
    "check",
    "doctor",
    "format:check",
    "lint",
    "test",
    "typecheck",
    "verify",
}
LOCKFILES = (
    "Package.resolved",
    "bun.lock",
    "bun.lockb",
    "package-lock.json",
    "pnpm-lock.yaml",
    "uv.lock",
    "yarn.lock",
)
RUNTIME_PIN_FILES = (
    ".nvmrc",
    ".node-version",
    ".python-version",
    ".tool-versions",
    "mise.toml",
)
DOCUMENTATION_FILES = (
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "LICENSE.md",
    "README.md",
    "SECURITY.md",
)
INSTRUCTION_FILES = ("AGENTS.md", "CLAUDE.md")


def existing(root: Path, candidates: tuple[str, ...]) -> list[str]:
    return sorted(candidate for candidate in candidates if (root / candidate).exists())


def load_json(path: Path, warnings: list[str]) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        warnings.append(f"Could not parse {path.name}: {error}")
        return {}
    if not isinstance(value, dict):
        warnings.append(f"Could not inspect {path.name}: root is not an object")
        return {}
    return value


def load_toml(path: Path, warnings: list[str]) -> dict[str, Any]:
    if not path.is_file():
        return {}
    if tomllib is None:
        warnings.append("Could not parse pyproject.toml: Python 3.11 or newer is required")
        return {}
    try:
        value = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        warnings.append(f"Could not parse {path.name}: {error}")
        return {}
    return value


def unquote_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def inspect_workflow(path: Path, root: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    workflow_name = path.stem
    jobs: list[dict[str, str]] = []
    current_job: dict[str, str] | None = None
    inside_jobs = False

    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith((" ", "\t")):
            inside_jobs = line.strip() == "jobs:"
            if line.startswith("name:"):
                workflow_name = unquote_yaml_scalar(line.split(":", 1)[1]) or path.stem
            continue
        if not inside_jobs:
            continue
        job_match = re.match(r"^  ([A-Za-z0-9_-]+):\s*(?:#.*)?$", line)
        if job_match:
            if current_job is not None:
                jobs.append(current_job)
            job_id = job_match.group(1)
            current_job = {"id": job_id, "name": job_id}
            continue
        name_match = re.match(r"^    name:\s*(.+?)\s*$", line)
        if name_match and current_job is not None:
            current_job["name"] = unquote_yaml_scalar(name_match.group(1))

    if current_job is not None:
        jobs.append(current_job)

    return {
        "path": path.relative_to(root).as_posix(),
        "workflow_name": workflow_name,
        "jobs": jobs,
    }


def inspect_python(pyproject: dict[str, Any]) -> dict[str, Any] | None:
    if not pyproject:
        return None
    project = pyproject.get("project")
    project = project if isinstance(project, dict) else {}
    scripts = project.get("scripts")
    scripts = scripts if isinstance(scripts, dict) else {}
    tools = pyproject.get("tool")
    tools = tools if isinstance(tools, dict) else {}
    return {
        "project_name": project.get("name"),
        "requires_python": project.get("requires-python"),
        "commands": sorted(str(name) for name in scripts),
        "tools": sorted(str(name) for name in tools),
    }


def detect_ecosystems(root: Path) -> list[str]:
    ecosystems: list[str] = []
    if (root / "package.json").is_file():
        ecosystems.append("node")
    if (root / "pyproject.toml").is_file() or any(root.glob("requirements*.txt")):
        ecosystems.append("python")
    swift_sources = (
        (root / "Package.swift").is_file()
        or (root / "project.yml").is_file()
        or any(root.glob("*.xcodeproj"))
        or any(root.rglob("*.swift"))
    )
    if swift_sources:
        ecosystems.append("swift")
    return ecosystems


def inspect_local(root: Path) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"Repository path is not a directory: {root}")

    warnings: list[str] = []
    package = load_json(root / "package.json", warnings)
    pyproject = load_toml(root / "pyproject.toml", warnings)

    project_sources = existing(root, ("Package.swift", "package.json", "project.yml", "pyproject.toml"))
    project_sources.extend(sorted(path.name for path in root.glob("*.xcodeproj") if path.is_dir()))
    project_sources = sorted(set(project_sources))

    runtime_pins = existing(root, RUNTIME_PIN_FILES)
    engines = package.get("engines")
    if isinstance(engines, dict) and isinstance(engines.get("node"), str):
        runtime_pins.append("package.json#engines.node")
    if isinstance(package.get("packageManager"), str):
        runtime_pins.append("package.json#packageManager")

    scripts = package.get("scripts")
    scripts = scripts if isinstance(scripts, dict) else {}
    verification_commands = [
        f"npm run {name}"
        for name in sorted(scripts)
        if name in QUALITY_SCRIPTS and isinstance(scripts[name], str)
    ]

    workflows = sorted(
        [*(root / ".github" / "workflows").glob("*.yml"), *(root / ".github" / "workflows").glob("*.yaml")]
    )
    ci = [inspect_workflow(path, root) for path in workflows]
    release_automation = sorted(
        path.relative_to(root).as_posix()
        for path in workflows
        if re.search(r"release|publish|deploy", path.name, re.IGNORECASE)
    )

    dependency_automation = existing(
        root,
        (
            ".github/dependabot.yaml",
            ".github/dependabot.yml",
            ".github/renovate.json",
            "renovate.json",
        ),
    )

    report: dict[str, Any] = {
        "root": str(root),
        "git": {"present": (root / ".git").exists()},
        "ecosystems": detect_ecosystems(root),
        "project_sources": project_sources,
        "runtime_pins": sorted(runtime_pins),
        "lockfiles": existing(root, LOCKFILES),
        "instructions": existing(root, INSTRUCTION_FILES),
        "documentation": existing(root, DOCUMENTATION_FILES),
        "verification_commands": verification_commands,
        "ci": ci,
        "dependency_automation": dependency_automation,
        "release_automation": release_automation,
        "warnings": warnings,
    }
    python = inspect_python(pyproject)
    if python is not None:
        report["python"] = python
    return report


def validate_repository_name(repository: str) -> str:
    if not REPOSITORY_RE.fullmatch(repository) or ".." in repository.split("/"):
        raise ValueError("GitHub target must be an exact OWNER/REPOSITORY name")
    return repository


Runner = Callable[..., subprocess.CompletedProcess[str]]


def gh_json(endpoint: str, runner: Runner) -> Any:
    result = runner(
        ["gh", "api", "--method", "GET", endpoint],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def inspect_github(
    repository: str,
    *,
    runner: Runner = subprocess.run,
) -> dict[str, Any]:
    repository = validate_repository_name(repository)
    metadata = gh_json(f"repos/{repository}", runner)
    rulesets = gh_json(f"repos/{repository}/rulesets?per_page=100", runner)
    if not isinstance(metadata, dict):
        raise ValueError("GitHub repository response was not an object")
    if not isinstance(rulesets, list):
        raise ValueError("GitHub ruleset response was not an array")

    security = metadata.get("security_and_analysis")
    security = security if isinstance(security, dict) else {}
    security_status = {
        str(name): value.get("status") if isinstance(value, dict) else value
        for name, value in sorted(security.items())
    }

    summarized_rulesets = []
    for ruleset_summary in rulesets:
        if not isinstance(ruleset_summary, dict):
            continue
        ruleset_id = ruleset_summary.get("id")
        if not isinstance(ruleset_id, int):
            continue
        ruleset = gh_json(f"repos/{repository}/rulesets/{ruleset_id}", runner)
        if not isinstance(ruleset, dict):
            raise ValueError(f"GitHub ruleset {ruleset_id} response was not an object")
        rules = ruleset.get("rules")
        rules = rules if isinstance(rules, list) else []
        summarized_rulesets.append(
            {
                "id": ruleset.get("id"),
                "name": ruleset.get("name"),
                "target": ruleset.get("target"),
                "enforcement": ruleset.get("enforcement"),
                "rule_types": sorted(
                    str(rule.get("type"))
                    for rule in rules
                    if isinstance(rule, dict) and rule.get("type") is not None
                ),
            }
        )

    return {
        "repository": repository,
        "visibility": metadata.get("visibility"),
        "description": metadata.get("description"),
        "homepage": metadata.get("homepage"),
        "topics": sorted(str(topic) for topic in metadata.get("topics", []) if isinstance(topic, str)),
        "default_branch": metadata.get("default_branch"),
        "merge_policy": {
            "allow_merge_commit": metadata.get("allow_merge_commit"),
            "allow_rebase_merge": metadata.get("allow_rebase_merge"),
            "allow_squash_merge": metadata.get("allow_squash_merge"),
            "delete_branch_on_merge": metadata.get("delete_branch_on_merge"),
        },
        "security_and_analysis": security_status,
        "rulesets": summarized_rulesets,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect repository files and optional GitHub settings without changing them."
    )
    parser.add_argument("path", nargs="?", default=".", help="Local repository path (default: current directory)")
    parser.add_argument("--github", metavar="OWNER/REPOSITORY", help="Exact GitHub repository to inspect with gh api")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        report: dict[str, Any] = {"local": inspect_local(Path(args.path))}
        if args.github:
            report["github"] = inspect_github(args.github)
    except (ValueError, OSError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f"inspect_repository: {error}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
