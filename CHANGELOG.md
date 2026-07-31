# Changelog

All notable changes to this project are documented in this file. The project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Documentation

- Recorded v2.3.0 publication, exact-tag installation, archive integrity, and
  marketplace evidence and marked `feature-spike` as released.

## [2.3.0] - 2026-07-30

### Added

- Added the [`feature-spike`](skills/feature-spike/SKILL.md) skill for bounded
  product-value and technical-feasibility experiments that end in a
  `continue`, `change`, `stop`, `defer`, or `inconclusive` decision.
- Added focused evidence guidance, a reusable feature-spike brief, five
  execution evals, and twenty balanced routing cases grounded in three
  completed proofs of concept and fresh no-skill baselines.

### Documentation

- Recorded v2.2.0 publication and exact-tag installation evidence and marked
  the expanded `feature-delivery` skill as released.

## [2.2.0] - 2026-07-30

### Changed

- Expanded [`feature-delivery`](skills/feature-delivery/SKILL.md) from a thin
  implementation loop into an evidence-led coordinator for product and
  technical specification, cross-repository contracts, explicit execution-mode
  selection, integration, and staged user availability.
- Added a reusable feature-delivery template and focused references for
  specification, cross-repository compatibility, optional Superpowers or
  agent-team execution, and independently gated rollout and rollback.
- Expanded `feature-delivery` to six execution evals and twenty balanced routing
  cases, with baseline and fresh-context forward replays covering ambiguous
  architecture, mid-flight mobile/backend rollout, and proportional
  single-repository delivery.
- Replaced the old inventory naming and `WF-*` records with a skill candidate
  inventory and `SC-*` identifiers so the repository consistently describes
  the reusable artifacts as skills.

### Documentation

- Recorded exact-tag installation evidence for v2.1.0 and marked the four
  migrated Mintlify skills as released.

## [2.1.0] - 2026-07-30

### Added

- Consolidated and hardened the former `mintlify-docs` collection as [`scaffold-mintlify-site`](skills/scaffold-mintlify-site/SKILL.md), [`review-mintlify-docs`](skills/review-mintlify-docs/SKILL.md), [`generate-mintlify-reference`](skills/generate-mintlify-reference/SKILL.md), and [`write-mintlify-changelog`](skills/write-mintlify-changelog/SKILL.md).
- Added self-contained editorial references, standard assets, cross-runtime metadata, execution evals, routing evals, and clean-install coverage for the documentation skills.
- Added skill-local MIT metadata so licensing survives individual Skills CLI installations.
- Added a permanent migration guide from the retired `mintlify-docs` skill and plugin names.
- Added a security policy covering agent instructions, bundled scripts, and packaging risks.
- Added a release runbook for immutable tags, curated notes, exact-tag installation, and downstream marketplace sequencing.

### Changed

- Replaced the former generic Mintlify skill names `review-docs`, `document-reference`, and `changelog-writer` with explicit globally installable names.
- Made the official Mintlify capability an optional source of current syntax and schema mechanics instead of a runtime-specific requirement for loading Patrick's editorial skills.
- Replaced the historical mirror-repository default with Mintlify's current direct repository and subdirectory model, while keeping all publishing actions explicit and separately authorized.
- Added deterministic contrast checking and hardened the bundled reference generators, starter MDX, favicon, and local validation commands.

### Documentation

- Recorded the completed release, client-installation evidence, and lessons for the first audited design skill.
- Classified end-to-end feature development as a candidate expansion of `feature-delivery`, grounded in three private cross-repository feature histories and an explicit composition boundary with optional Superpowers and agent-team execution.
- Captured `feature-spike` as a separate evidence-seeking skill candidate whose outcome is a continue, change, or stop decision rather than production delivery.

## [2.0.0] - 2026-07-30

### Changed

- Renamed the repository from `pdugan20/patrick-workflows` to `pdugan20/skills` so the public name matches the artifacts it distributes.
- Renamed the Claude Code and Codex plugin package from `patrick-workflows` to `patrick-skills`.
- Simplified the README around one Skills CLI install command and canonical repository links for each skill.

### Migration

- Install directly with `npx skills@latest add pdugan20/skills`.
- Marketplace users should replace `patrick-workflows@patrick-tools` with `patrick-skills@patrick-plugins`.

## [1.1.0] - 2026-07-30

### Added

- A researched skill authoring standard covering skill selection, portable structure, routing, evaluation, external tools, and review.
- A durable skill candidate inventory and evidence-based brief template for auditing Patrick's real design and development processes.
- Versioned execution and routing evals for [`code-native-ui-ideation`](https://github.com/pdugan20/skills/tree/v1.1.0/skills/code-native-ui-ideation), [`feature-delivery`](https://github.com/pdugan20/skills/tree/v1.1.0/skills/feature-delivery), and [`production-hardening`](https://github.com/pdugan20/skills/tree/v1.1.0/skills/production-hardening), enforced by repository validation.
- An isolated Skills CLI installation smoke test for Claude Code, Codex, and Cursor, enforced in CI.
- A pinned external Agent Skills validation gate for structure, links, context size, orphaned resources, and content-quality heuristics.
- Platform-specific SwiftUI, React Native, and web guidance for [`code-native-ui-ideation`](https://github.com/pdugan20/skills/tree/v1.1.0/skills/code-native-ui-ideation), covering runnable variants with consistent fixtures and project-native development surfaces.
- Standard repository badges, direct skill source and skills.sh links, and installation paths organized by client and version behavior.
- Curated GitHub Release notes extracted from the matching changelog section.

### Changed

- Expanded [`code-native-ui-ideation`](https://github.com/pdugan20/skills/tree/v1.1.0/skills/code-native-ui-ideation) with an ideate-versus-build branch, a shared comparison contract, and an explicit graduation cleanup boundary.
- Replaced the `claude-code-lint` gate, dependency, and configuration with the exactly pinned official Claude Code plugin validator after a scope audit found duplicate, ineffective, and non-portable checks.
- Documented collection-level semantic versioning with per-skill history in this central changelog instead of non-portable skill-local versions and changelogs.

## [1.0.0] - 2026-07-30

### Added

- The `code-native-ui-ideation`, `feature-delivery`, and `production-hardening` skills.
- Claude Code and Codex plugin manifests backed by one canonical skill tree.
- Skills CLI metadata, repository validation, spelling checks, workflow-security analysis, scheduled link validation, and automated release checks.

[unreleased]: https://github.com/pdugan20/skills/compare/v2.3.0...HEAD
[2.3.0]: https://github.com/pdugan20/skills/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/pdugan20/skills/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/pdugan20/skills/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/pdugan20/skills/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/pdugan20/skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/pdugan20/skills/releases/tag/v1.0.0
