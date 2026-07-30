# Changelog

All notable changes to this project are documented in this file. The project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Documentation

- Recorded the completed release, client-installation evidence, and lessons for the first audited design workflow.

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

- A researched skill authoring standard covering workflow selection, portable structure, routing, evaluation, external tools, and review.
- A durable workflow inventory and evidence-based candidate brief template for auditing Patrick's real design and development processes.
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

[unreleased]: https://github.com/pdugan20/skills/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/pdugan20/skills/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/pdugan20/skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/pdugan20/skills/releases/tag/v1.0.0
