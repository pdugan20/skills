# Repository Instructions

## Architecture

- `skills/` is the canonical portable skill tree. Keep one `SKILL.md` per skill and add only resources the skill actually needs.
- `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` package the same skill tree for their respective plugin systems.
- `skills.sh.json` controls the groupings shown by Skills CLI-compatible indexes.
- `docs/skill-authoring.md` defines the authoring and review standard for this collection.
- `docs/workflow-inventory.md` is the durable source of truth for workflow candidates and classification decisions.
- `docs/workflows/` contains evidence-backed briefs for candidates that are developed beyond initial capture.
- Every skill keeps execution evals in `evals/evals.json` and routing evals in `evals/routing.json`.
- Keep manifest and package versions synchronized. Release tags use `v<version>`.

## Changes

- Preserve Agent Skills portability in `SKILL.md`; place runtime-specific presentation metadata under `agents/`.
- Write descriptions as routing instructions that say what the skill does and when it should or should not run.
- Update execution and routing evals whenever behavior, scope, or the description changes.
- Update the workflow inventory and candidate brief when a workflow decision or status changes.
- Update `CHANGELOG.md` for user-facing changes.
- Run `npm run verify` before a release.
- CI must also pass the pinned external Agent Skills validator.

Do not publish a tag or release without explicit authorization.
