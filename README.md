# Skills for Design and Development

[![CI](https://github.com/pdugan20/skills/actions/workflows/ci.yml/badge.svg)](https://github.com/pdugan20/skills/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/pdugan20/skills?logo=github)](https://github.com/pdugan20/skills/releases/latest)
[![skills.sh](https://skills.sh/b/pdugan20/skills)](https://skills.sh/pdugan20/skills)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D22.22.2-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

Portable skills for code-native design exploration and production software delivery. They work with Claude Code, Codex, Cursor, and other Agent Skills clients.

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

Claude Code and Codex users can also install the collection as the `patrick-skills` plugin from [Patrick's Plugins](https://github.com/pdugan20/plugins).

## Versioning

Releases version the collection as a whole. Install a release tag when reproducibility matters, and see the [changelog](CHANGELOG.md) for skill-specific history.

## Development

```bash
npm ci
npm run verify
```

See the [skill authoring standard](docs/skill-authoring.md) and [workflow inventory](docs/workflow-inventory.md) when adding or changing a workflow.
