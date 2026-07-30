# Repository Instructions

## Architecture

- `skills/` is the canonical portable skill tree. Keep one `SKILL.md` per skill and add only resources the skill actually needs.
- `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` package the same skill tree for their respective plugin systems.
- `skills.sh.json` controls the groupings shown by Skills CLI-compatible indexes.
- Keep manifest and package versions synchronized. Release tags use `v<version>`.

## Changes

- Preserve Agent Skills portability in `SKILL.md`; place runtime-specific presentation metadata under `agents/`.
- Write descriptions as routing instructions that say what the skill does and when it should or should not run.
- Update `CHANGELOG.md` for user-facing changes.
- Run `npm run verify` before a release.

Do not publish a tag or release without explicit authorization.
