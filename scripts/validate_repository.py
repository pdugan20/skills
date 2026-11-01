#!/usr/bin/env python3
"""Validate the repository's portable skills and synchronized package metadata."""

from __future__ import annotations

import argparse
import functools
import json
import re
from collections.abc import Iterable, Mapping
from datetime import date
from pathlib import Path, PurePosixPath
from typing import TypeGuard

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "align-ui-to-design-system": True,
    "analyze-ui-video": True,
    "animate-watercolor": True,
    "audit-design-system-health": True,
    "bootstrap-repository": True,
    "capture-feature": True,
    "code-native-ui-ideation": True,
    "feature-delivery": True,
    "feature-spike": True,
    "generate-mintlify-reference": True,
    "integrate-app-intents": True,
    "repair-photographic-assets": True,
    "review-deployment-constraints": True,
    "review-mintlify-docs": True,
    "run-remote-dev-server": True,
    "scaffold-mintlify-site": True,
    "tune-mobile-client-performance": True,
    "write-mintlify-changelog": True,
}
PLUGIN_NAME = "patrick-skills"
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
AGENT_PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
AGENT_PLUGIN_NAME_RE = re.compile(
    r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?$"
)
AGENT_PLUGIN_FIELDS = {
    "$schema",
    "name",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "extensions",
}
SHARED_PLUGIN_METADATA_FIELDS = (
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
)
MIN_EXECUTION_EVALS = 3
MIN_ROUTING_EVALS_PER_CLASS = 4
SCHEMA_DIR = ROOT / "schemas"
ADVERSARIAL_TAG = "adversarial"
TRUST_BOUNDARY_HEADING = "\n## Trust boundary\n"
SKILLS_SH_SCHEMA = "https://skills.sh/schemas/skills.sh.schema.json"
RENOVATE_SCHEMA = "https://docs.renovatebot.com/renovate-schema.json"
RENOVATE_FIELDS = {"$schema", "enabled", "enabledManagers"}
RENOVATE_MANAGERS = ["npm", "github-actions"]
AUDIT_ISSUE_CODE_RE = re.compile(r"^[A-Z]\d{3}$")
AUDIT_RISK_LEVELS = {"low", "medium", "high", "critical"}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def reject_duplicate_json_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def validate_renovate_bootstrap(path: Path | None = None) -> list[str]:
    """Require the exact inert updater envelope until activation is reviewed."""
    path = path or ROOT / "renovate.json"
    try:
        config = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_json_keys,
        )
    except (json.JSONDecodeError, OSError, ValueError) as error:
        return [f"renovate.json: invalid or ambiguous JSON ({error})"]

    if not isinstance(config, dict):
        return ["renovate.json: root must be an object"]

    errors: list[str] = []
    if set(config) != RENOVATE_FIELDS:
        errors.append("renovate.json: disabled bootstrap must contain only exact fields")
    if config.get("$schema") != RENOVATE_SCHEMA:
        errors.append(f"renovate.json: $schema must be {RENOVATE_SCHEMA}")
    if config.get("enabled") is not False:
        errors.append("renovate.json: enabled must be the boolean false")
    if config.get("enabledManagers") != RENOVATE_MANAGERS:
        errors.append("renovate.json: managers must be exactly npm and github-actions")
    return errors


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML frontmatter delimiter")
    try:
        return text.split("---\n", 2)[1]
    except IndexError as error:
        raise ValueError("missing closing YAML frontmatter delimiter") from error


def is_nonempty_string(value: object) -> TypeGuard[str]:
    return isinstance(value, str) and bool(value.strip())


def validate_agent_plugin_manifest(manifest: Mapping[str, object]) -> list[str]:
    """Validate the portable Agent Plugins identity and closed metadata schema."""
    errors: list[str] = []
    label = "plugin.json"

    if manifest.get("$schema") != AGENT_PLUGIN_SCHEMA:
        errors.append(f"{label}: $schema must be {AGENT_PLUGIN_SCHEMA}")

    unknown_fields = sorted(set(manifest) - AGENT_PLUGIN_FIELDS)
    if unknown_fields:
        errors.append(f"{label}: unsupported fields: {', '.join(unknown_fields)}")

    name = manifest.get("name")
    if not isinstance(name, str) or not AGENT_PLUGIN_NAME_RE.fullmatch(name):
        errors.append(f"{label}: name must satisfy the Agent Plugins v1 constraints")

    for field in ("version", "description", "homepage", "repository", "license"):
        if field in manifest and not isinstance(manifest[field], str):
            errors.append(f"{label}: {field} must be a string when present")

    author = manifest.get("author")
    if author is not None:
        if not isinstance(author, dict):
            errors.append(f"{label}: author must be an object when present")
        else:
            unknown_author_fields = sorted(set(author) - {"name", "email", "url"})
            if unknown_author_fields:
                errors.append(
                    f"{label}: unsupported author fields: "
                    f"{', '.join(unknown_author_fields)}"
                )
            for field, value in author.items():
                if not isinstance(value, str):
                    errors.append(f"{label}: author.{field} must be a string")

    keywords = manifest.get("keywords")
    if keywords is not None and (
        not isinstance(keywords, list)
        or any(not isinstance(keyword, str) for keyword in keywords)
    ):
        errors.append(f"{label}: keywords must contain only strings")

    extensions = manifest.get("extensions")
    if extensions is not None:
        if not isinstance(extensions, dict):
            errors.append(f"{label}: extensions must be an object when present")
        elif any(not isinstance(value, dict) for value in extensions.values()):
            errors.append(f"{label}: each extension value must be an object")

    return errors


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


@functools.cache
def eval_schema_validator(schema_name: str) -> Draft202012Validator:
    schema = load_json(SCHEMA_DIR / schema_name)
    assert isinstance(schema, dict)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def load_eval_document(path: Path, schema_name: str, kind: str, errors: list[str]) -> object | None:
    """Load one eval file, returning it only when it satisfies its JSON Schema."""
    label = display_path(path)
    if not path.is_file():
        errors.append(f"{label}: missing {kind}")
        return None
    try:
        document = load_json(path)
    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"{label}: invalid JSON ({error})")
        return None
    violations = sorted(eval_schema_validator(schema_name).iter_errors(document), key=lambda error: error.json_path)
    if violations:
        errors.extend(f"{label}: {violation.json_path}: {violation.message}" for violation in violations)
        return None
    return document


def validate_evals(skill_name: str, skill_dir: Path, *, requires_adversarial: bool = False) -> list[str]:
    """Validate a skill's execution and routing evals against their schemas and coverage rules."""
    errors: list[str] = []
    evals_path = skill_dir / "evals" / "evals.json"
    routing_path = skill_dir / "evals" / "routing.json"

    manifest = load_eval_document(evals_path, "evals.schema.json", "execution evals", errors)
    if isinstance(manifest, dict):
        label = display_path(evals_path)
        if manifest["skill_name"] != skill_name:
            errors.append(f"{label}: skill_name must match its directory")
        cases = manifest["evals"]
        if len(cases) < MIN_EXECUTION_EVALS:
            errors.append(f"{label}: requires at least {MIN_EXECUTION_EVALS} execution evals")
        if requires_adversarial and not any(ADVERSARIAL_TAG in case.get("tags", []) for case in cases):
            errors.append(
                f"{label}: a skill with a Trust boundary section needs at least one execution eval "
                f'tagged "{ADVERSARIAL_TAG}"'
            )
        seen_ids: set[int] = set()
        for index, case in enumerate(cases):
            case_label = f"{label}: evals[{index}]"
            if case["id"] in seen_ids:
                errors.append(f"{case_label}.id must be unique")
            seen_ids.add(case["id"])
            for item in case.get("files", []):
                file_path = Path(item)
                if file_path.is_absolute() or ".." in file_path.parts:
                    errors.append(f"{case_label}.files contains an unsafe path: {item}")
                elif not (skill_dir / file_path).is_file():
                    errors.append(f"{case_label}.files references a missing file: {item}")

    routing = load_eval_document(routing_path, "routing.schema.json", "routing evals", errors)
    if isinstance(routing, list):
        label = display_path(routing_path)
        counts = {True: 0, False: 0}
        seen_queries: set[str] = set()
        for index, case in enumerate(routing):
            if case["query"] in seen_queries:
                errors.append(f"{label}: [{index}].query must be unique")
            seen_queries.add(case["query"])
            counts[case["should_trigger"]] += 1
        for should_trigger, name in ((True, "positive"), (False, "negative")):
            if counts[should_trigger] < MIN_ROUTING_EVALS_PER_CLASS:
                errors.append(f"{label}: requires at least {MIN_ROUTING_EVALS_PER_CLASS} {name} routing evals")

    return errors


def normalized_query(query: str) -> str:
    return " ".join(query.casefold().split())


def validate_routing_overlap(skills_root: Path, skill_names: Iterable[str]) -> list[str]:
    """Reject a routing query that more than one skill claims as a positive trigger."""
    owners: dict[str, list[str]] = {}
    for name in sorted(skill_names):
        path = skills_root / name / "evals" / "routing.json"
        try:
            routing = load_json(path)
        except (json.JSONDecodeError, OSError):
            continue  # Reported by validate_evals.
        if not isinstance(routing, list):
            continue
        for case in routing:
            if isinstance(case, dict) and case.get("should_trigger") is True and isinstance(case.get("query"), str):
                owners.setdefault(normalized_query(case["query"]), []).append(name)
    return [
        f"routing evals: {', '.join(names)} all expect this query to trigger them: {query!r}"
        for query, names in sorted(owners.items())
        if len(set(names)) > 1
    ]


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

    errors.extend(
        validate_evals(skill_name, skill_dir, requires_adversarial=TRUST_BOUNDARY_HEADING in text)
    )

    openai = openai_file.read_text(encoding="utf-8")
    expected_policy = f"allow_implicit_invocation: {str(implicit).lower()}"
    if expected_policy not in openai:
        errors.append(f"{openai_file.relative_to(ROOT)}: expected {expected_policy}")
    if f"${skill_name}" not in openai:
        errors.append(f"{openai_file.relative_to(ROOT)}: default prompt must mention ${skill_name}")
    return errors


def validate_codex_interface(manifest: Mapping[str, object]) -> list[str]:
    """Validate Codex presentation limits that otherwise fail silently."""
    errors: list[str] = []
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        return [".codex-plugin/plugin.json: interface must be an object"]

    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not prompts:
        return [".codex-plugin/plugin.json: defaultPrompt must be a non-empty array"]
    if len(prompts) > 3:
        errors.append(".codex-plugin/plugin.json: defaultPrompt supports at most 3 entries")
    if any(not is_nonempty_string(prompt) for prompt in prompts):
        errors.append(".codex-plugin/plugin.json: defaultPrompt entries must be non-empty strings")
    if any(isinstance(prompt, str) and len(prompt) > 128 for prompt in prompts):
        errors.append(".codex-plugin/plugin.json: defaultPrompt entries must be at most 128 characters")
    return errors


def validate_skills_sh_config(config: Mapping[str, object]) -> list[str]:
    """Validate the current skills.sh repository-page configuration contract."""
    errors: list[str] = []
    if config.get("$schema") != SKILLS_SH_SCHEMA:
        errors.append(f"skills.sh.json: $schema must be {SKILLS_SH_SCHEMA}")
    if config.get("notGrouped") not in {"top", "bottom"}:
        errors.append('skills.sh.json: notGrouped must be "top" or "bottom"')

    groupings = config.get("groupings")
    if not isinstance(groupings, list) or not groupings:
        return errors + ["skills.sh.json: groupings must be a non-empty array"]

    grouped: list[str] = []
    for index, grouping in enumerate(groupings):
        label = f"skills.sh.json: groupings[{index}]"
        if not isinstance(grouping, dict):
            errors.append(f"{label} must be an object")
            continue
        if not is_nonempty_string(grouping.get("title")):
            errors.append(f"{label}.title must be a non-empty string")
        description = grouping.get("description")
        if description is not None and not is_nonempty_string(description):
            errors.append(f"{label}.description must be a non-empty string when present")
        skills = grouping.get("skills")
        if not isinstance(skills, list) or any(not is_nonempty_string(skill) for skill in skills):
            errors.append(f"{label}.skills must contain only non-empty strings")
            continue
        grouped.extend(skills)

    if len(grouped) != len(set(grouped)):
        errors.append("skills.sh.json: each skill may appear in only one grouping")
    if sorted(grouped) != sorted(EXPECTED_SKILLS):
        errors.append("skills.sh.json: groupings must include every skill exactly once")
    return errors


def validate_alert_files(label: str, skill: object, alert_files: object, skills_root: Path) -> list[str]:
    """Socket exceptions may only cover synthetic eval fixtures that exist in the skill."""
    if (
        not isinstance(alert_files, list)
        or not alert_files
        or any(not is_nonempty_string(path) for path in alert_files)
    ):
        return [f"{label}.alertFiles must list the flagged files"]
    errors: list[str] = []
    if len(alert_files) != len(set(alert_files)):
        errors.append(f"{label}.alertFiles must be unique")
    for path in alert_files:
        relative = PurePosixPath(path)
        if relative.is_absolute() or ".." in relative.parts or relative.parts[:2] != ("evals", "fixtures"):
            errors.append(f"{label}.alertFiles may only cover files under evals/fixtures/: {path}")
        elif isinstance(skill, str):
            candidate = skills_root / skill / relative
            fixtures = (skills_root / skill / "evals" / "fixtures").resolve()
            if not candidate.is_file():
                errors.append(f"{label}.alertFiles names a missing file: {path}")
            elif candidate.is_symlink() or fixtures not in candidate.resolve().parents:
                errors.append(f"{label}.alertFiles must name a regular file inside evals/fixtures/: {path}")
    return errors


def validate_skills_sh_audit_policy(
    config: dict[str, object], skills_root: Path | None = None
) -> list[str]:
    """Validate reviewed live-audit exceptions and their runtime safeguards."""
    errors: list[str] = []
    skills_root = skills_root or ROOT / "skills"
    providers = config.get("requiredProviders")
    if (
        not isinstance(providers, list)
        or not providers
        or any(not is_nonempty_string(provider) for provider in providers)
    ):
        return ["skills-sh-audits.json: requiredProviders must be a non-empty string array"]
    if len(providers) != len(set(providers)):
        errors.append("skills-sh-audits.json: requiredProviders must be unique")

    exceptions = config.get("exceptions")
    if not isinstance(exceptions, list):
        return errors + ["skills-sh-audits.json: exceptions must be an array"]

    seen: set[tuple[str, str]] = set()
    for index, exception in enumerate(exceptions):
        label = f"skills-sh-audits.json: exceptions[{index}]"
        if not isinstance(exception, dict):
            errors.append(f"{label} must be an object")
            continue
        skill = exception.get("skill")
        provider = exception.get("provider")
        if skill not in EXPECTED_SKILLS:
            errors.append(f"{label}.skill must name a packaged skill")
        if provider not in providers:
            errors.append(f"{label}.provider must be a required provider")
        if isinstance(skill, str) and isinstance(provider, str):
            key = (skill, provider)
            if key in seen:
                errors.append(f"{label} duplicates {skill}/{provider}")
            seen.add(key)
        if exception.get("status") != "warn":
            errors.append(f"{label}.status must be warn; fail verdicts cannot be accepted")
        if exception.get("riskLevel") not in AUDIT_RISK_LEVELS:
            errors.append(f"{label}.riskLevel is invalid")
        issue_codes = exception.get("issueCodes")
        alert_files = exception.get("alertFiles")
        if ("issueCodes" in exception) == ("alertFiles" in exception):
            errors.append(f"{label} must list exactly one of issueCodes or alertFiles")
            issue_codes = []
        elif "alertFiles" in exception:
            issue_codes = []
            errors.extend(validate_alert_files(label, skill, alert_files, skills_root))
        elif (
            not isinstance(issue_codes, list)
            or not issue_codes
            or any(
                not isinstance(code, str) or not AUDIT_ISSUE_CODE_RE.fullmatch(code)
                for code in issue_codes
            )
        ):
            errors.append(f"{label}.issueCodes must contain security issue codes")
            issue_codes = []
        elif len(issue_codes) != len(set(issue_codes)):
            errors.append(f"{label}.issueCodes must be unique")
        for field in ("owner", "rationale", "upstreamIssue"):
            if not is_nonempty_string(exception.get(field)):
                errors.append(f"{label}.{field} must be a non-empty string")
        upstream_issue = exception.get("upstreamIssue")
        if isinstance(upstream_issue, str) and not upstream_issue.startswith("https://"):
            errors.append(f"{label}.upstreamIssue must use https")
        review_by = exception.get("reviewBy")
        if not isinstance(review_by, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", review_by):
            errors.append(f"{label}.reviewBy must be YYYY-MM-DD")
        else:
            try:
                date.fromisoformat(review_by)
            except ValueError:
                errors.append(f"{label}.reviewBy must be a real date")

        if skill in EXPECTED_SKILLS and "W011" in issue_codes:
            skill_file = skills_root / str(skill) / "SKILL.md"
            if not skill_file.is_file() or "\n## Trust boundary\n" not in skill_file.read_text(
                encoding="utf-8"
            ):
                errors.append(
                    f"{skill_file}: W011 exceptions require a ## Trust boundary section"
                )
    return errors


README_SKILL_RE = re.compile(r"^- \[`(?P<name>[a-z0-9-]+)`\]\(skills/(?P<path>[a-z0-9-]+)/SKILL\.md\)")


def validate_readme_skill_groups(readme: str, config: Mapping[str, object]) -> list[str]:
    """Keep README skill sections aligned with skills.sh groupings, descriptions, and order."""
    errors: list[str] = []
    groupings = config.get("groupings")
    if not isinstance(groupings, list):
        return errors  # Reported by validate_skills_sh_config.
    available = readme.split("\n## Available skills\n", 1)
    if len(available) != 2:
        return ["README.md: missing ## Available skills section"]
    body = available[1].split("\n## ", 1)[0]
    sections: dict[str, list[str]] = {}
    for chunk in body.split("\n### ")[1:]:
        title, _, rest = chunk.partition("\n")
        title = title.strip()
        if title in sections:
            errors.append(f"README.md: ### {title} appears more than once")
        sections[title] = rest.strip("\n").splitlines()
    for grouping in groupings:
        if not isinstance(grouping, dict) or not isinstance(grouping.get("title"), str):
            continue
        title = grouping["title"]
        lines = sections.get(title)
        if lines is None:
            errors.append(f"README.md: missing ### {title} section from skills.sh.json")
            continue
        first = next((line for line in lines if line.strip()), "")
        if first != grouping.get("description"):
            errors.append(f"README.md: ### {title} must open with its skills.sh.json description")
        listed: list[str] = []
        for line in lines:
            match = README_SKILL_RE.match(line)
            if match:
                if match["name"] != match["path"]:
                    errors.append(f"README.md: {match['name']} links to skills/{match['path']}")
                listed.append(match["name"])
        if listed != grouping.get("skills"):
            errors.append(
                f"README.md: ### {title} must list {grouping.get('skills')} in skills.sh.json order, found {listed}"
            )
    return errors


def validate(release_tag: str | None = None) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_renovate_bootstrap())
    package = load_json(ROOT / "package.json")
    package_lock = load_json(ROOT / "package-lock.json")
    portable = load_json(ROOT / "plugin.json")
    claude = load_json(ROOT / ".claude-plugin" / "plugin.json")
    codex = load_json(ROOT / ".codex-plugin" / "plugin.json")
    assert isinstance(package, dict)
    assert isinstance(package_lock, dict)
    assert isinstance(portable, dict)
    assert isinstance(claude, dict)
    assert isinstance(codex, dict)
    version = package.get("version")

    if package.get("name") != PLUGIN_NAME:
        errors.append(f"package.json: name must be {PLUGIN_NAME}")
    if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
        errors.append("package.json: version must be semantic x.y.z")
    lock_package = package_lock.get("packages", {}).get("", {})
    if package_lock.get("name") != PLUGIN_NAME or lock_package.get("name") != PLUGIN_NAME:
        errors.append(f"package-lock.json: names must be {PLUGIN_NAME}")
    if package_lock.get("version") != version or lock_package.get("version") != version:
        errors.append("package-lock.json: versions must match package.json")
    errors.extend(validate_agent_plugin_manifest(portable))
    for path, manifest in (
        ("plugin.json", portable),
        (".claude-plugin/plugin.json", claude),
        (".codex-plugin/plugin.json", codex),
    ):
        if manifest.get("name") != PLUGIN_NAME:
            errors.append(f"{path}: name must be {PLUGIN_NAME}")
        if manifest.get("version") != version:
            errors.append(f"{path}: version must match package.json")
    for field in SHARED_PLUGIN_METADATA_FIELDS:
        if portable.get(field) != claude.get(field) or portable.get(field) != codex.get(field):
            errors.append(f"plugin manifests: {field} must remain synchronized")
    errors.extend(validate_codex_interface(codex))

    actual_skills = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    if actual_skills != set(EXPECTED_SKILLS):
        errors.append(f"skills/: expected {sorted(EXPECTED_SKILLS)}, found {sorted(actual_skills)}")
    for skill_name, implicit in EXPECTED_SKILLS.items():
        errors.extend(validate_skill(skill_name, implicit))
    errors.extend(validate_routing_overlap(ROOT / "skills", EXPECTED_SKILLS))

    skills_config = load_json(ROOT / "skills.sh.json")
    assert isinstance(skills_config, dict)
    errors.extend(validate_skills_sh_config(skills_config))
    errors.extend(validate_readme_skill_groups((ROOT / "README.md").read_text(encoding="utf-8"), skills_config))

    audit_policy = load_json(ROOT / "skills-sh-audits.json")
    assert isinstance(audit_policy, dict)
    errors.extend(validate_skills_sh_audit_policy(audit_policy))

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
