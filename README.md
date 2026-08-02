# Skills for Design and Development

[![CI](https://github.com/pdugan20/skills/actions/workflows/ci.yml/badge.svg)](https://github.com/pdugan20/skills/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/pdugan20/skills?logo=github)](https://github.com/pdugan20/skills/releases/latest)
[![skills.sh](https://skills.sh/b/pdugan20/skills)](https://skills.sh/pdugan20/skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

Portable skills for code-native design exploration, production software delivery, and technical documentation. They work with Claude Code, Codex, Cursor, and other Agent Skills clients.

## Who is this for?

These skills are for designers and engineers who build products directly in code and use agents across design, implementation, release, and documentation—not just code generation.

They help an agent recognize what kind of work it is doing and apply the right level of rigor:

- Explore runnable alternatives before choosing one.
- Analyze a finished interface or recording against repository evidence.
- Trace one mobile interaction from a visible hitch to its causal boundary.
- Distinguish a feature spike from production delivery.
- Stand up a new repository with rigor that matches its intended maturity.
- Produce documentation grounded in the actual product instead of generic filler.

The collection does not impose one visual style or stack. It encodes repeatable decision points, evidence standards, and approval boundaries so an agent can work more like a thoughtful collaborator.

## Install

```bash
npx skills@latest add pdugan20/skills
```

## Skills

### Design and development

- [`code-native-ui-ideation`](skills/code-native-ui-ideation/SKILL.md) — Brainstorm and compare runnable UI directions before choosing one.
- [`align-ui-to-design-system`](skills/align-ui-to-design-system/SKILL.md) — Review one completed UI surface against its repository's design system and apply only approved corrections.
- [`audit-design-system-health`](skills/audit-design-system-health/SKILL.md) — Audit repository-wide design drift, missing system capabilities, consolidation candidates, and enforceable rules.
- [`analyze-ui-video`](skills/analyze-ui-video/SKILL.md) — Dissect UI recordings against a target repository before diagnosing or reconstructing behavior.
- [`feature-spike`](skills/feature-spike/SKILL.md) — Test feature value or technical feasibility before production investment.
- [`tune-mobile-client-performance`](skills/tune-mobile-client-performance/SKILL.md) — Trace one jittery or late mobile interaction to its causal boundary and verify the smallest supported adjustment.
- [`feature-delivery`](skills/feature-delivery/SKILL.md) — Take substantial features from idea through coordinated implementation and staged rollout.
- [`bootstrap-repository`](skills/bootstrap-repository/SKILL.md) — Scaffold new repositories with proportional local tooling, CI, and GitHub policy.

### Mintlify and documentation

- [`scaffold-mintlify-site`](skills/scaffold-mintlify-site/SKILL.md) — Create a project-specific Mintlify documentation site.
- [`review-mintlify-docs`](skills/review-mintlify-docs/SKILL.md) — Review Mintlify content, navigation, and launch readiness.
- [`generate-mintlify-reference`](skills/generate-mintlify-reference/SKILL.md) — Generate drift-checked CLI, MCP, and API reference pages.
- [`write-mintlify-changelog`](skills/write-mintlify-changelog/SKILL.md) — Write concise reader-facing Mintlify changelog entries.

The Mintlify skills use the official Mintlify capability for current component and schema mechanics when it is available, while keeping Patrick's editorial guidance portable and self-contained.

## Versioning

Releases version the collection as a whole. Install a release tag when reproducibility matters, and see the [changelog](CHANGELOG.md) for skill-specific history.

## Development

```bash
npm ci
npm run verify
```

See the [skill authoring standard](docs/skill-authoring.md), [skill candidate inventory](docs/skill-candidates.md), and [release guide](RELEASING.md) when maintaining the collection.
