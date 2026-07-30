# Workflow Inventory

This file is the canonical inventory of Patrick's recurring design and development workflows that may deserve reusable agent support. It records decisions and evidence; [GitHub issue #2](https://github.com/pdugan20/patrick-workflows/issues/2) records changing execution status.

Use the [skill authoring standard](skill-authoring.md) to classify candidates. Create a brief from the [workflow template](workflows/_template.md) only after a flow has enough real evidence to evaluate.

Do not commit credentials, client-confidential material, personal data, or raw private artifacts. Summarize sensitive examples and keep their source material in an appropriate private location.

## Status model

| Status | Meaning |
| --- | --- |
| `captured` | The recurring flow and desired outcome are understood at a high level. |
| `needs-evidence` | More real examples, corrections, artifacts, or boundary cases are required. |
| `classified` | The correct mechanism and rationale have been recorded. |
| `pilot` | The flow was selected for implementation and evaluation. |
| `validated` | The implementation passed its structural, routing, and behavioral evidence bar. |
| `released` | The result is versioned, distributed, and installation-checked. |
| `no-action` | Existing agent behavior is sufficient or the flow should not become reusable tooling. |

## Prioritization signals

Rank with judgment rather than a synthetic total score:

- **Frequency:** How often does the flow recur?
- **Correction cost:** How often does Patrick need to redirect or repair agent work?
- **Distinctive expertise:** Does the flow contain knowledge or decisions a capable model would not reliably infer?
- **Reusable reach:** Would the guidance help across projects, runtimes, or users?
- **Observability:** Can we tell whether the resulting behavior or artifact is better?
- **Boundary clarity:** Can we say when the mechanism should and should not apply?

Prefer a pilot with strong evidence, recurring friction, and observable outcomes over the most ambitious candidate.

## Candidates

| ID | Workflow | Evidence | Classification and rationale | Status | Priority | Brief |
| --- | --- | --- | --- | --- | --- | --- |
| `WF-001` | Cross-platform component variant exploration | Patrick's repeated SwiftUI preview, React Native Storybook, and web dev-lab loop | **Skill (technique):** enhance `code-native-ui-ideation`; the decision loop is portable while the comparison surface remains project-native | `validated` | High | [Brief](workflows/cross-platform-component-variant-exploration.md) |
| `WF-002` | Substantial production feature delivery | The released `feature-delivery` workflow plus the production mode and proportional-testing corrections in the shared working agreement | **Skill (composite workflow):** retain the existing bounded skill; ordinary small changes stay under agent defaults and repository instructions | `released` | Medium | Existing skill |
| `WF-003` | Explicit production hardening | The released `production-hardening` workflow plus repeated separation of exploration, implementation, and release-readiness work in the shared working agreement | **Skill (discipline workflow):** retain it as explicit-only because automatic hardening would make lightweight work unnecessarily heavy | `released` | Medium | Existing skill |
| `WF-004` | Agent environment bootstrap and plugin reconciliation | `agent-tooling` setup, refresh, catalog, lockfile, drift, and machine-check scripts with documented source-of-truth boundaries | **Scripts + human documentation:** the operations are deterministic and stateful; a skill would be a less reliable wrapper around the existing tested commands | `classified` | Medium | No skill brief |
| `WF-005` | Skill and plugin versioning, marketplace sync, and release | Release workflows and version-sync, packaging, installation, and marketplace-bump scripts across `patrick-workflows` and `mintlify-docs` | **Scripts + CI + human documentation:** transactional release steps need reproducible checks and explicit external-write approval, not agent judgment | `classified` | Medium | No skill brief |
| `WF-006` | Scaffold a Mintlify documentation site | The released `scaffold-mintlify-site` skill, templates, generators, mirror sync, and drift CI in `mintlify-docs` | **Skill + scripts + assets:** information architecture requires judgment while tree generation and drift checks are deterministic; keep it in the focused docs plugin | `released` | Medium | Existing external collection |
| `WF-007` | Generate drift-checked CLI, MCP, and API reference docs | The released `document-reference` skill and source-backed generators in `mintlify-docs` | **Skill + scripts:** the skill selects and explains the reference shape while generators enforce source fidelity; keep it in the focused docs plugin | `released` | Medium | Existing external collection |
| `WF-008` | Review documentation content and information architecture | The released `review-docs` skill and shared editorial playbook in `mintlify-docs` | **Skill (discipline workflow) + reference:** page-order review and editorial judgment benefit from a bounded method; Mintlify mechanics remain in the official plugin | `released` | Medium | Existing external collection |
| `WF-009` | Write reader-facing changelog entries | The released `changelog-writer` skill and house-style corrections in `mintlify-docs` | **Skill (technique) + reference:** translating implementation changes into reader value needs judgment; repository release mechanics remain scripts | `released` | Low | Existing external collection |

## Existing collection

These released Patrick Workflows skills are also represented in the audit above so the inventory covers the complete recurring process instead of only net-new ideas:

| Skill | Classification | Primary boundary |
| --- | --- | --- |
| `code-native-ui-ideation` | Technique | Lightweight runnable design exploration, not production delivery. |
| `feature-delivery` | Composite workflow | Substantial production feature work, not small changes or visual exploration. |
| `production-hardening` | Discipline workflow | Explicit release-readiness work on a selected implementation. |

## Audit decision

The first pass contains nine workflows backed by working artifacts or recorded corrections. Only `WF-001` justified new authoring in this collection. `WF-002` and `WF-003` already had appropriately bounded skills. `WF-004` and `WF-005` remain scripts, CI, and human documentation because their value is deterministic execution and state safety. `WF-006` through `WF-009` already belong to the focused `mintlify-docs` collection and should not be duplicated here.

The next discovery pass should start from another naturally described recurring design or development loop, not from the presence of an interesting third-party skill. The seven non-Patrick skills installed through `agent-tooling` retain their upstream provenance and are external capabilities, not evidence that Patrick owns the corresponding workflow.

## Working rules

- Capture flows from completed tasks, corrections, working artifacts, and real failure cases.
- Keep one row per coherent outcome, not one row per individual step.
- Use `AGENTS.md` for always-on constraints and scripts for deterministic operations.
- Do not create a candidate brief until at least two representative examples or one strong example plus repeated corrections exist.
- Update the row and its brief together when classification or status changes.
- Record rejected candidates as `no-action` with a short rationale so the decision is not repeatedly reopened.
