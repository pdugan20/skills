# Skills for Design and Development

[![CI](https://github.com/pdugan20/skills/actions/workflows/ci.yml/badge.svg)](https://github.com/pdugan20/skills/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/pdugan20/skills?logo=github)](https://github.com/pdugan20/skills/releases/latest)
[![skills.sh](https://skills.sh/b/pdugan20/skills)](https://skills.sh/pdugan20/skills)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D22.22.2-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

Portable skills for code-native design exploration, production software delivery, and technical documentation. They work with Claude Code, Codex, Cursor, and other Agent Skills clients.

## Install

```bash
npx skills@latest add pdugan20/skills
```

## Skills

| Skill | Use it for |
| --- | --- |
| [`code-native-ui-ideation`](skills/code-native-ui-ideation/SKILL.md) | Brainstorming and comparing runnable UI directions before choosing one. |
| [`feature-delivery`](skills/feature-delivery/SKILL.md) | Implementing substantial production features with proportional rigor. |
| [`production-hardening`](skills/production-hardening/SKILL.md) | Explicit release-readiness review of a selected implementation. |
| [`scaffold-mintlify-site`](skills/scaffold-mintlify-site/SKILL.md) | Creating a project-specific Mintlify documentation site. |
| [`review-mintlify-docs`](skills/review-mintlify-docs/SKILL.md) | Reviewing Mintlify content, navigation, and launch readiness. |
| [`generate-mintlify-reference`](skills/generate-mintlify-reference/SKILL.md) | Generating drift-checked CLI, MCP, and API reference pages. |
| [`write-mintlify-changelog`](skills/write-mintlify-changelog/SKILL.md) | Writing concise reader-facing Mintlify changelog entries. |

Claude Code and Codex users can also install the collection as the `patrick-skills` plugin from [Patrick's Plugins](https://github.com/pdugan20/plugins).

The Mintlify skills use the official Mintlify capability for current component and schema mechanics when it is available, while keeping Patrick's editorial workflows portable and self-contained.

## Versioning

Releases version the collection as a whole. Install a release tag when reproducibility matters, and see the [changelog](CHANGELOG.md) for skill-specific history. Previous `mintlify-docs` users can follow the [migration guide](docs/migrations/mintlify-docs.md).

## Development

```bash
npm ci
npm run verify
```

See the [skill authoring standard](docs/skill-authoring.md), [workflow inventory](docs/workflow-inventory.md), and [release guide](RELEASING.md) when maintaining the collection.
