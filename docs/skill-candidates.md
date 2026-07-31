# Skill Candidate Inventory

This file is the canonical inventory of Patrick's recurring design and development processes that may deserve a skill or another reusable mechanism. It records decisions, evidence, the selected mechanism, and the implementation state of that mechanism.

Use the [skill authoring standard](skill-authoring.md) to classify candidates. Create a brief from the [skill candidate template](skill-candidates/_template.md) only after a process has enough real evidence to evaluate.

Do not commit credentials, client-confidential material, personal data, or raw private artifacts. Summarize sensitive examples and keep their source material in an appropriate private location.

## Implementation state

The rows are skill candidates. The state describes our reusable response, such
as a skill or script.

| Status | Meaning |
| --- | --- |
| `captured` | The recurring flow and desired outcome are understood at a high level. |
| `needs-evidence` | More real examples, corrections, artifacts, or boundary cases are required. |
| `classified` | The correct mechanism and rationale have been recorded. |
| `pilot` | The flow was selected for implementation and evaluation. |
| `validated` | The implementation passed its structural, routing, and behavioral evidence bar. |
| `released` | The selected reusable mechanism is versioned, distributed, and installation-checked. |
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

| ID | Skill candidate | Evidence | Classification and rationale | Status | Priority | Brief |
| --- | --- | --- | --- | --- | --- | --- |
| `SC-001` | Cross-platform component variant exploration | Patrick's repeated SwiftUI preview, React Native Storybook, and web dev-lab loop | **Technique skill:** enhance `code-native-ui-ideation`; the decision loop is portable while the comparison surface remains project-native | `released` | High | [Brief](skill-candidates/cross-platform-component-variant-exploration.md) |
| `SC-002` | End-to-end feature development and staged rollout | Private iOS and backend histories for Catch Me Up, user-generated lists, and series-detail trailers, plus baseline and forward replays against `feature-delivery` | **Composite skill:** `feature-delivery` owns product discovery, cross-repository impact, specification, execution-mode selection, and staged rollout while delegating optional strict implementation mechanics to Superpowers or an available agent-team runtime | `validated` | High | [Brief](skill-candidates/end-to-end-feature-development.md) |
| `SC-003` | Explicit production hardening | The released `production-hardening` skill plus repeated separation of exploration, implementation, and release-readiness work in the shared working agreement | **Discipline skill:** retain it as explicit-only because automatic hardening would make lightweight work unnecessarily heavy | `released` | Medium | Existing skill |
| `SC-004` | Agent environment bootstrap and plugin reconciliation | `agent-tooling` setup, refresh, catalog, lockfile, drift, and machine-check scripts with documented source-of-truth boundaries | **Scripts + human documentation:** the operations are deterministic and stateful; a skill would be a less reliable wrapper around the existing tested commands | `classified` | Medium | No skill brief |
| `SC-005` | Skill and plugin versioning, marketplace sync, and release | Release automation, version-sync, packaging, installation, and marketplace-bump scripts across `skills` and the former `mintlify-docs` repository | **Scripts + CI + human documentation:** transactional release steps need reproducible checks and explicit external-write approval, not agent judgment | `classified` | Medium | No skill brief |
| `SC-006` | Scaffold a Mintlify documentation site | The released `scaffold-mintlify-site` skill, templates, generators, mirror sync, and drift CI in the former focused repository | **Composite skill with scripts and assets:** information architecture requires judgment while detection, reusable files, and drift checks are deterministic | `released` | Medium | [Skill](../skills/scaffold-mintlify-site/SKILL.md) |
| `SC-007` | Generate drift-checked CLI, MCP, and API reference docs | The released `document-reference` skill and source-backed generators in the former focused repository | **Composite skill with scripts:** the skill selects and explains the reference shape while generators enforce source fidelity | `released` | Medium | [Skill](../skills/generate-mintlify-reference/SKILL.md) |
| `SC-008` | Review documentation content and information architecture | The released `review-docs` skill, shared editorial playbook, and quality fixture in the former focused repository | **Discipline skill with references:** page-order review and editorial judgment benefit from a bounded method | `released` | Medium | [Skill](../skills/review-mintlify-docs/SKILL.md) |
| `SC-009` | Write reader-facing changelog entries | The released `changelog-writer` skill, routing cases, and quality fixture in the former focused repository | **Technique skill:** translating implementation changes into reader value needs judgment while repository release mechanics remain scripts | `released` | Low | [Skill](../skills/write-mintlify-changelog/SKILL.md) |
| `SC-010` | Feature spike for value or feasibility validation | Patrick's recurring need to build the smallest useful slice before deciding whether a feature deserves production investment | **Provisional experiment skill:** keep a hypothesis, bounded implementation, evidence, and continue-or-stop decision distinct from production feature delivery and UI-direction comparison; concrete completed examples are still required before authoring | `needs-evidence` | High | Brief deferred pending evidence |

## Current collection

These Patrick-owned skills are represented in the audit above so the inventory covers the complete recurring process instead of only net-new ideas:

| Skill | Classification | Primary boundary |
| --- | --- | --- |
| `code-native-ui-ideation` | Technique | Lightweight runnable design exploration, not production delivery. |
| `feature-delivery` | Composite | Validated expansion coordinates idea-to-spec, cross-repository delivery, explicit execution-mode selection, and staged rollout without imposing strict mechanics on bounded features; publication is pending. |
| `production-hardening` | Discipline | Explicit release-readiness work on a selected implementation. |
| `scaffold-mintlify-site` | Composite | New-site scaffolding, not review or external deployment. |
| `review-mintlify-docs` | Discipline | Mintlify editorial and information-architecture review, not generated output. |
| `generate-mintlify-reference` | Composite | Source-backed Mintlify reference generation and drift checks. |
| `write-mintlify-changelog` | Technique | Reader-facing Mintlify entries, not repository release logs. |

## Audit decision

The first pass contained nine skill candidates backed by working artifacts or recorded corrections. `SC-001` justified new authoring in this collection. `SC-002` and `SC-003` already had bounded skills. `SC-004` and `SC-005` remain scripts, CI, and human documentation because their value is deterministic execution and state safety.

The initial decision to keep `SC-006` through `SC-009` in a separate
`mintlify-docs` repository was revisited after the main collection established
stronger portable validation and one-command installation. These are
Patrick-owned skills without a necessary independent release cadence. Their
canonical source is moving into this collection, with explicit names,
self-contained resources, standard evals, and clean-install coverage. The old
repository should be deprecated and archived only after the combined release is
installed and verified; it should not be deleted because its history, releases,
and incoming links remain useful migration evidence.

The second discovery pass reopened `SC-002` after Patrick described a larger scope than the released thin skill covered: turning an idea into an approved design and specification, investigating effects across client and backend repositories, selecting an implementation engine, and planning gated delivery through development environments and TestFlight or equivalent release channels. It also captured `SC-010` as a distinct feature-spike outcome. A spike is complete when it produces enough evidence for a continue, change, or stop decision; it is not an abbreviated production release and should not inherit strict TDD or rollout ceremony by default.

Reviewing the private iOS and backend histories for Catch Me Up, user-generated lists, and series-detail trailers supplied the missing `SC-002` evidence. Across different implementation eras and orchestration methods, all three required an explicit client/backend contract, dependency-ordered phases, separate code and live-environment verification, and a rollout state that could not be inferred from either repository alone. Patrick approved the execution-mode and strict-TDD boundaries: `feature-delivery` is the portable outer coordinator, proportional tests remain the default, and strict Superpowers or agent-team mechanics are selected explicitly rather than implied.

Three baseline replays against the released thin skill preserved lightweight
behavior for a bounded web feature and inferred much of the required rollout
discipline from detailed prompts. They also exposed the value of the pilot:
ambiguous architecture could be prescribed before repository evidence, no case
recorded its execution mode, and the released skill did not guarantee a
canonical cross-repository handoff or multidimensional delivery state. The
pilot expansion and its evals now target those specific omissions.

Forward replays preserved the bounded path and improved the two historical
cross-repository patterns. An initial expanded-skill replay still recommended a
provisional architecture before repository inspection, and cross-repository
outputs could omit the execution-mode record. Tightening those two requirements
produced fresh replays that held architectures as hypotheses until discovery
and explicitly selected proportional inline execution. Repository verification,
clean installation across Claude Code, Codex, and Cursor layouts, and the pinned
third-party validator now pass. `SC-002` is validated but remains unreleased
until the collection receives an authorized versioned release.

The next discovery pass should start from another naturally described recurring design or development process, not from the presence of an interesting third-party skill. Non-Patrick skills installed through `agent-tooling` retain their upstream provenance and are external capabilities, not evidence that Patrick owns the corresponding process.

`SC-001` validated the general-purpose approach: the ideation and comparison loop belongs in one portable skill, while SwiftUI, React Native, and web guidance belongs in platform references loaded only when relevant. The pilot also established that behavior claims require trace-backed evaluation, distribution claims require clean installation from a published tag, and an unavailable authenticated client should be described as packaging-compatible rather than behavior-verified. Future candidates should reuse those evidence boundaries instead of splitting skills by framework or overstating client support.

## Working rules

- Capture flows from completed tasks, corrections, working artifacts, and real failure cases.
- Keep one row per coherent outcome, not one row per individual step.
- Use `AGENTS.md` for always-on constraints and scripts for deterministic operations.
- Do not create a candidate brief until at least two representative examples or one strong example plus repeated corrections exist.
- Update the row and its brief together when classification or status changes.
- Record rejected candidates as `no-action` with a short rationale so the decision is not repeatedly reopened.
