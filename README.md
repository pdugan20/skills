# Patrick Workflows

Portable, versioned workflows for code-native design exploration and production software delivery. The skills use the open Agent Skills format and work with Claude Code, Codex, Cursor, and other compatible clients.

## Install

Install the complete collection with the Skills CLI:

```bash
npx skills add pdugan20/patrick-workflows
```

Pin a release for reproducible installation:

```bash
npx skills add https://github.com/pdugan20/patrick-workflows/tree/v1.0.0
```

After the collection is listed in [Patrick's Tools](https://github.com/pdugan20/patrick-tools), Claude Code and Codex users can also install the plugin as `patrick-workflows@patrick-tools`.

## Skills

| Skill | Use it for |
| --- | --- |
| `code-native-ui-ideation` | Comparing UI, interaction, layout, visual, or motion directions as runnable code. |
| `feature-delivery` | Implementing substantial production-ready features with proportional rigor. |
| `production-hardening` | Explicit release-readiness review of a selected implementation. |

Each skill is self-contained under `skills/<name>/`. Codex-specific interface metadata lives in `agents/openai.yaml`; clients that do not use it can still consume the portable `SKILL.md`.

## Versioning

Releases follow semantic versioning. Install a tag when stability matters, or install the repository default branch to receive the latest changes. See [CHANGELOG.md](CHANGELOG.md) for user-facing changes.

## Development

```bash
npm ci
npm run verify
```

The repository publishes both Claude Code and Codex plugin manifests while keeping one canonical copy of every skill.
