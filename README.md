# Patrick Workflows

[![CI](https://github.com/pdugan20/patrick-workflows/actions/workflows/ci.yml/badge.svg)](https://github.com/pdugan20/patrick-workflows/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/pdugan20/patrick-workflows?logo=github)](https://github.com/pdugan20/patrick-workflows/releases/latest)
[![skills.sh](https://skills.sh/b/pdugan20/patrick-workflows)](https://skills.sh/pdugan20/patrick-workflows)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D22.22.2-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

Portable, versioned workflows for code-native design exploration and production software delivery. They use the open Agent Skills format and work with Claude Code, Codex, Cursor, and other compatible clients.

## Skills

| Skill | Use it for | Catalog |
| --- | --- | --- |
| [`code-native-ui-ideation`](skills/code-native-ui-ideation/SKILL.md) | Comparing UI, interaction, layout, visual, or motion directions as runnable code. | [skills.sh](https://skills.sh/pdugan20/patrick-workflows/code-native-ui-ideation) |
| [`feature-delivery`](skills/feature-delivery/SKILL.md) | Implementing substantial production-ready features with proportional rigor. | [skills.sh](https://skills.sh/pdugan20/patrick-workflows/feature-delivery) |
| [`production-hardening`](skills/production-hardening/SKILL.md) | Explicit release-readiness review of a selected implementation. | [skills.sh](https://skills.sh/pdugan20/patrick-workflows/production-hardening) |

Each skill is self-contained under [`skills/`](skills/). Codex-specific interface metadata lives beside each skill in `agents/openai.yaml`; clients that do not use it can still consume the portable `SKILL.md`.

## Install

Choose the Skills CLI for a direct install in Claude Code, Codex, or Cursor. Choose the Patrick's Tools marketplace when you want the collection managed as a Claude or Codex plugin.

| Path | Best for | Version behavior |
| --- | --- | --- |
| Skills CLI | Any supported client; all or selected skills | Default branch, or an exact release when the URL contains a tag |
| Patrick's Tools | Claude Code or Codex plugin management | Version pinned by the marketplace |

### Skills CLI (recommended)

Run the interactive installer and choose the skills, clients, and scope:

```bash
npx skills add pdugan20/patrick-workflows
```

For a reproducible project install of every skill into Claude Code, Codex, and Cursor:

```bash
npx skills add https://github.com/pdugan20/patrick-workflows/tree/v1.1.0 \
  --skill '*' --agent claude-code codex cursor --yes
```

Install one skill by replacing `code-native-ui-ideation` and the client as needed:

```bash
npx skills add https://github.com/pdugan20/patrick-workflows/tree/v1.1.0 \
  --skill code-native-ui-ideation --agent cursor --yes
```

Add `--global` for a user-level install. Run `npx skills list --json` afterward to inspect project installations, or add `--global` to inspect user-level installations.

### Claude Code plugin

```text
/plugin marketplace add pdugan20/patrick-tools
/plugin install patrick-workflows@patrick-tools
```

### Codex plugin

```text
codex plugin marketplace add pdugan20/patrick-tools
codex plugin add patrick-workflows@patrick-tools
```

The marketplace always points at a tagged Patrick Workflows release. Use the direct Skills CLI path when you need to choose individual skills or pin a release independently of the marketplace.

## Versioning and releases

The collection has one semantic version shared by its package and Claude/Codex plugin manifests. Skills do not carry independent version numbers or local changelog files because clients install them from the same repository release. The central [changelog](CHANGELOG.md) names every affected skill and is the source for the matching GitHub Release notes.

This keeps one source of truth while preserving per-skill history. A skill should move to its own package and release stream only when it needs an independent compatibility boundary or publishing cadence.

## Development

```bash
npm ci
npm run verify
```

Read the [skill authoring standard](docs/skill-authoring.md) before adding or materially changing a skill. Use the [workflow inventory](docs/workflow-inventory.md) and its [candidate template](docs/workflows/_template.md) to capture real processes, classify the right mechanism, and preserve evaluation evidence.

The repository keeps one canonical copy of every skill and publishes synchronized Claude Code and Codex plugin manifests. Verification covers repository policy, eval structure, isolated Skills CLI installation into Claude Code/Codex/Cursor layouts, Claude's official strict plugin validation, Markdown, formatting, and the pinned third-party `agent-ecosystem/skill-validator` gate.
