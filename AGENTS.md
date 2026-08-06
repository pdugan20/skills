# Repository Instructions

## Architecture

- `skills/` is the canonical portable skill tree. Keep one `SKILL.md` per skill and add only resources the skill actually needs.
- Root `plugin.json` gives the collection its portable Agent Plugins identity;
  `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` retain
  client-specific compatibility and presentation metadata for the same skill
  tree.
- `skills.sh.json` controls the groupings shown by Skills CLI-compatible indexes.
- `skills-sh-audits.json` records reviewed exceptions to the pass-by-default
  skills.sh security policy. Exceptions must be exact, owned, and temporary.
- `docs/skill-authoring.md` defines the authoring and review standard for this collection.
- `docs/skill-candidates.md` is the durable source of truth for skill candidates and classification decisions.
- `docs/skill-candidates/` contains evidence-backed briefs for candidates that are developed beyond initial capture.
- Every skill keeps execution evals in `evals/evals.json` and routing evals in `evals/routing.json`.
- Keep manifest and package versions synchronized. Release tags use `v<version>`.

## Changes

- Preserve Agent Skills portability in `SKILL.md`; place runtime-specific presentation metadata under `agents/`.
- Write descriptions as routing instructions that say what the skill does and when it should or should not run.
- Update execution and routing evals whenever behavior, scope, or the description changes.
- Add a narrow trust boundary and an adversarial execution eval when a skill
  consumes content that could contain instructions outside the user's request
  or applicable agent instruction files.
- Update the skill candidate inventory and candidate brief when a skill decision or status changes.
- Update `CHANGELOG.md` for user-facing changes.
- Run `npm run verify` before a release.
- CI must also pass the pinned external Agent Skills validator.

Do not publish a tag or release without explicit authorization.
