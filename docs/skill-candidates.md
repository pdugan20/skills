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
| `deprecated` | A released mechanism no longer justifies continued use and remains only for a documented compatibility window before removal. |
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
| `SC-002` | End-to-end feature development and staged rollout | Private iOS and backend histories for Catch Me Up, user-generated lists, and series-detail trailers, plus baseline and forward replays against `feature-delivery` | **Composite skill:** `feature-delivery` owns product discovery, cross-repository impact, specification, execution-mode selection, and staged rollout while delegating optional strict implementation mechanics to Superpowers or an available agent-team runtime | `released` | High | [Brief](skill-candidates/end-to-end-feature-development.md) |
| `SC-003` | Explicit production hardening | Three completed hardening histories plus fresh natural-prompt comparisons with and without the former released skill | **No standalone skill:** remove `production-hardening` because a direct hardening request already activates the needed behavior; keep repository instructions, `feature-delivery`, and optional release-operation skills in their narrower roles | `no-action` | Medium | [Brief](skill-candidates/production-hardening.md) |
| `SC-004` | Agent environment bootstrap and plugin reconciliation | `agent-tooling` setup, refresh, catalog, lockfile, drift, and machine-check scripts with documented source-of-truth boundaries | **Scripts + human documentation:** the operations are deterministic and stateful; a skill would be a less reliable wrapper around the existing tested commands | `classified` | Medium | No skill brief |
| `SC-005` | Skill and plugin versioning, marketplace sync, and release | Release automation, version-sync, packaging, installation, and marketplace-bump scripts across `skills` and the former `mintlify-docs` repository | **Scripts + CI + human documentation:** transactional release steps need reproducible checks and explicit external-write approval, not agent judgment | `classified` | Medium | No skill brief |
| `SC-006` | Scaffold a Mintlify documentation site | The released `scaffold-mintlify-site` skill, templates, generators, mirror sync, and drift CI in the former focused repository | **Composite skill with scripts and assets:** information architecture requires judgment while detection, reusable files, and drift checks are deterministic | `released` | Medium | [Skill](../skills/scaffold-mintlify-site/SKILL.md) |
| `SC-007` | Generate drift-checked CLI, MCP, and API reference docs | The released `document-reference` skill and source-backed generators in the former focused repository | **Composite skill with scripts:** the skill selects and explains the reference shape while generators enforce source fidelity | `released` | Medium | [Skill](../skills/generate-mintlify-reference/SKILL.md) |
| `SC-008` | Review documentation content and information architecture | The released `review-docs` skill, shared editorial playbook, and quality fixture in the former focused repository | **Discipline skill with references:** page-order review and editorial judgment benefit from a bounded method | `released` | Medium | [Skill](../skills/review-mintlify-docs/SKILL.md) |
| `SC-009` | Write reader-facing changelog entries | The released `changelog-writer` skill, routing cases, and quality fixture in the former focused repository | **Technique skill:** translating implementation changes into reader value needs judgment while repository release mechanics remain scripts | `released` | Low | [Skill](../skills/write-mintlify-changelog/SKILL.md) |
| `SC-010` | Feature spike for value or feasibility validation | A kill-or-continue third-party capability probe, a deferred native-package performance proof of concept, and a platform experiment that changed implementation medium, plus fresh no-skill and forward replays | **Pattern skill:** `feature-spike` preserves the decision uncertainty, validity conditions, accepted decision rule, non-binary outcome, and code disposition without inheriting production delivery or UI-comparison scope | `released` | High | [Brief](skill-candidates/feature-spike.md) |
| `SC-011` | Analyze a UI screen recording | Two frame-led diagnoses in `nextup-ios-app`, a 60 fps competitor transition reconstruction in `audiobook-ios`, a source-frame artifact diagnosis in `pat-portfolio`, and a fresh ambiguous-video replay | **Composite skill with a script:** `analyze-ui-video` shares one evidence-first temporal analysis method, then branches into reference reconstruction or visual-bug diagnosis and audits the target repository before proposing implementation steps | `released` | High | [Brief](skill-candidates/analyze-ui-video.md) |
| `SC-012` | Explore UI directions at deliberate design-system distances | Patrick sometimes wants component variants that strictly reuse an existing system, stretch its vocabulary, or deliberately diverge from it, plus baseline and forward NextUp section-header replays | **Enhancement to `code-native-ui-ideation`:** the trigger, comparison surface, and selection artifact are unchanged; design-system posture is an optional comparison axis instead of another ideation skill | `released` | High | [Brief](skill-candidates/design-system-distance-ui-ideation.md) |
| `SC-013` | Align a completed component with its design system | Patrick runs a focused conformance pass after building a component to find accidental token, primitive, state, interaction, or visual-language deviations, plus no-skill and forward NextUp component replays | **Targeted skill:** `align-ui-to-design-system` reviews one completed surface against repository evidence, distinguishes violations from intentional exceptions and system gaps, and applies only approved fixes without expanding into a repository-wide audit | `released` | High | [Brief](skill-candidates/align-ui-to-design-system.md) |
| `SC-014` | Audit design-system drift and consolidation opportunities | Patrick audits repositories for hardcoded values, inconsistent conventions, overlapping visual components, and candidates for consolidation or stronger enforcement, plus no-skill and forward `pat-portfolio` replays | **Composite skill with stack-specific tooling:** `audit-design-system-health` combines deterministic token and duplication signals with rendered and semantic review, then produces a prioritized read-only health, consolidation, and enforcement report rather than automatically refactoring the repository | `released` | High | [Brief](skill-candidates/audit-design-system-health.md) |
| `SC-015` | Bootstrap a repository to its intended maturity | A current audit of active Swift, Expo/React Native, Python, and TypeScript repositories plus four candidate-absent and four forward scaffold evaluations | **Composite skill with a read-only inspector and stack references:** `bootstrap-repository` selects an upstream project generator, applies an exploration, maintained, or shipping profile, prepares local quality gates and GitHub policy proportionally, then verifies the result; stack mechanics stay delegated to official generators and focused upstream skills | `validated` | High | [Brief](skill-candidates/bootstrap-repository.md) |
| `SC-016` | Tune user-visible mobile client performance | Private SwiftUI and Expo/React Native histories covering scroll jank, cold-start stalls, late paints, transition pauses, keyboard-motion conflicts, image decode, state fan-out, and instrumentation overhead, plus fresh read-only historical baseline and forward comparisons | **Validated composite skill:** `tune-mobile-client-performance` traces one concrete mobile smoothness symptom across presentation, rendering, state, media, network, and observability boundaries, then runs one discriminating experiment and verifies the smallest fix; framework mechanics stay in focused platform references | `validated` | High | [Brief](skill-candidates/tune-mobile-client-performance.md) |
| `SC-017` | Automate Apple builds, Simulator flows, and runtime debugging | Current project automation plus a live XcodeBuildMCP 2.7.0 semantic snapshot, runtime-log capture, and LLDB stack cycle against the Messenger Simulator | **External tool plus upstream skill:** pinned Codex-first XcodeBuildMCP pilot in `agent-tooling`, retaining computer use for visual surfaces and Instruments for performance attribution; do not write a competing skill or install `build-ios-apps` | `pilot` | High | [Brief](skill-candidates/ios-development-capabilities.md#sc-017-structured-apple-runtime-control) |
| `SC-018` | Investigate iOS memory lifetimes with memgraphs | Apple Memory Graph and `leaks` tooling, OpenAI's capture and summary helpers, and current public overlap, but no real local leak case yet | **Needs real-case evidence:** use Apple's tools on the next app-owned leak or retained-growth investigation, then decide whether repeated capture and analysis failures justify a script-backed first-party skill | `needs-evidence` | Medium | [Brief](skill-candidates/ios-development-capabilities.md#sc-018-memgraph-lifetime-investigation) |
| `SC-019` | Profile a focused iOS CPU path with ETTrace | Upstream ETTrace workflow, OpenAI's dSYM and flamegraph helpers, and local synthetic checks, but no current local CPU case that Instruments failed to answer | **Task-level fallback:** keep ETTrace outside the managed catalog until a bounded real case demonstrates actionable lift over Instruments or `xctrace` and tolerates temporary app linkage | `needs-evidence` | Low | [Brief](skill-candidates/ios-development-capabilities.md#sc-019-ettrace-cpu-profiling) |
| `SC-020` | Build App Intents system integrations | NextUp's shipped entities, intents, interactive snippets, Spotlight, routing, tests, post-launch corrections, device-verification debt, and planned App Schemas upgrade | **First-party skill pilot:** author a compact `integrate-app-intents` skill from current Apple APIs and NextUp evidence, using the App Schemas upgrade as its first forward evaluation; do not import the stale OpenAI templates or oversized Axiom reference | `pilot` | High | [Brief](skill-candidates/ios-development-capabilities.md#sc-020-app-intents-integration) |

## Current collection

These Patrick-owned skills are represented in the audit above so the inventory covers the complete recurring process instead of only net-new ideas:

| Skill | Classification | Primary boundary |
| --- | --- | --- |
| `code-native-ui-ideation` | Technique | Lightweight runnable design exploration, not production delivery. |
| `align-ui-to-design-system` | Discipline | Bounded post-build UI conformance and approved corrections, not repository-wide auditing. |
| `audit-design-system-health` | Composite | Read-only repository-wide drift, consolidation, system-gap, and enforcement analysis, not automatic remediation. |
| `analyze-ui-video` | Composite | Recording-led diagnosis or reference reconstruction, not code-only motion review or automatic implementation. |
| `feature-spike` | Pattern | Bounded runnable evidence for an investment decision, not UI comparison or production delivery. |
| `feature-delivery` | Composite | Released in v2.2.0; coordinates idea-to-spec, cross-repository delivery, explicit execution-mode selection, and staged rollout without imposing strict mechanics on bounded features. |
| `bootstrap-repository` | Composite | Published in v3.0.0 for new or empty repositories; selects proportional maturity, delegates to maintained generators, and keeps remote mutation separately authorized. Inventory promotion awaits a current skills.sh snapshot. |
| `tune-mobile-client-performance` | Composite | One concrete SwiftUI or React Native smoothness symptom across motion, rendering, state, media, network, and observability; not a whole-app audit or motion-ideation workflow. |
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
installed and verified. It can remain archived to preserve its history and
releases, but the sole user has migrated and does not need a user-facing
migration guide.

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
third-party validator pass. `SC-002` was released in v2.2.0 after the tagged
archive, curated notes, and exact-tag multi-client installation were verified.

The next discovery pass should start from another naturally described recurring design or development process, not from the presence of an interesting third-party skill. Non-Patrick skills installed through `agent-tooling` retain their upstream provenance and are external capabilities, not evidence that Patrick owns the corresponding process.

The mobile-performance pass captured `SC-016` from recurring SwiftUI and React
Native symptoms whose visible animation was often not the frame consumer.
Historical controls and forward replays showed that the reusable lift is
selecting the first causal boundary and one-variable experiment across motion,
state publication, rendering, media, network, and instrumentation—not adding
another framework optimization checklist. The separate capability brief records
why XcodeBuildMCP is an agent-tooling pilot, Memgraph and ETTrace remain
case-triggered, and App Intents proceeds as a focused first-party pilot.

The next pass supplied the missing `SC-010` evidence. A throwaway integration
probe removed backend scope while preserving an inconclusive commercial gate; a
native package proof of concept produced a large performance win but a `defer`
decision; and a platform experiment changed implementation medium without
rejecting the product objective. Fresh no-skill baselines already kept spikes
small, but they invented decision thresholds, collapsed results into binary
recommendations, and omitted invalid-test or code-disposition rules. The pilot
therefore targets those specific decision failures rather than teaching agents
that a spike should simply be quick.

Initial forward replays showed that the pilot still allowed arbitrary experiment
budgets and could aggregate several unknowns into one false gate. After
tightening those boundaries, fresh integration, architecture, and product-value
replays kept budgets provisional, classified independent gates, used accepted
decision rules, considered all five outcomes, and preserved a separate
production handoff. Repository validation, the pinned third-party validator,
official Claude validation, clean Claude Code, Codex, and Cursor layout
installation, and the optional GitHub publishing preview all pass. `SC-010` is
released in Patrick Skills v2.3.0 and pinned by Patrick Plugins v3.2.0 after
exact-tag archive, clean-install, and marketplace-install verification.

The next discovery pass captured `SC-011` after Patrick described the same
screen-recording analysis loop for competitor references and visual bugs. The
existing evidence shows that these are two branches of one skill rather than
separate mobile, web, animation, and debugging skills: both require the agent to
scope the relevant moment, inspect rendered frames before forming a theory,
separate observations from inferences, and inspect the target repository before
recommending an implementation. The existing `verify-motion` contact-sheet
script is a strong platform-neutral starting point, while its SwiftUI-specific
diagnostic advice should remain outside the portable core.

The pilot against a real NextUp recording exposed a concrete flaw in that
starting script: it treated a nominal 120 fps container rate as the observed
rate even though the clip contained 916 frames over 15.403 seconds. The new
portable helper distinguishes the 59.468 fps observed average, emits timestamped
overview and detail manifests, and is covered by focused tests. The no-skill
baseline already described the visible rail and repository well, while the
pilot added media-integrity checks, reproducible evidence, explicit uncertainty,
and one discriminating re-recording. Because Patrick described the actual bug
as unusually subtle, this clip validates ambiguity handling rather than hidden
defect discovery. Structural, routing, behavioral, external-validator, plugin,
and multi-client installation gates pass. Patrick Skills v2.4.0 now contains
`SC-011` through `SC-014`; its tagged archive and clean exact-tag installation
were verified byte-for-byte across the Claude Code, Codex, and Cursor layouts.

The following discovery pass captured three related design-system intents but
did not collapse them into one large skill. `SC-012` is another axis inside the
released `code-native-ui-ideation` loop: the user still chooses and compares
runnable directions, but the directions intentionally occupy faithful,
stretching, and divergent relationships to the existing system. `SC-013` is a
narrow post-build conformance pass on one component or surface. `SC-014` is a
repository-wide health and consolidation audit whose cost, artifact, and
default read-only boundary are materially different. The latter two therefore
remain separate skill candidates that can share evidence concepts without
sharing a trigger.

External tooling covers pieces rather than the complete intent. Google's
[DESIGN.md](https://github.com/google-labs-code/design.md) provides an alpha
design-system contract and linter, while its
[Stitch skills](https://github.com/google-labs-code/stitch-skills) can extract
that contract from frontend code. OpenAI's Figma skills reconcile code with
Figma libraries, but remain Figma-specific. Maintained tools such as
[Stylelint](https://stylelint.io/user-guide/rules/declaration-property-value-allowed-list/)
and [SwiftLint](https://github.com/realm/SwiftLint) can enforce approved token
rules in target repositories, and [jscpd](https://github.com/kucherenko/jscpd)
can identify duplicated source as one consolidation signal. None can decide
whether a visual deviation is intentional, whether two differently implemented
components are semantically redundant, or how far an exploratory direction
should push an existing system. Those judgment boundaries are the candidate
skills' reusable value; deterministic enforcement should remain stack-specific
and be added only after an audit establishes the repository's actual rules.

Fresh baselines showed that capable agents already perform all three tasks well,
so the implementations stayed narrow. The ideation enhancement adds an optional
protected-foundation and intentional-departure contract. The component skill
adds a stable evidence hierarchy and four-way finding classification. The
repository audit adds signal normalization, semantic consolidation tests,
uncertainty, and enforcement criteria without imposing an exhaustive surface
inventory or synthetic score. Forward replays on `nextup-ios-app` and
`pat-portfolio` retained the baseline strengths and made those boundaries more
explicit. Repeated skills.sh searches and source inspection found close Figma,
token, web consistency, normalization, drift-detection, and exhaustive UI/UX
planning skills, but no maintained public skill with the same proportional,
code-repository-first, native-and-web scope. The candidate briefs record the
specific upstream-use and retirement conditions so this conclusion can be
rechecked before later releases.

Patrick Plugins v3.3.0 pins Patrick Skills v2.4.0 in both runtime catalogs; its
Claude Code and Codex marketplace installation smoke test passed before and
after publication. Agent Tooling v0.7.0 locks all eleven Patrick-owned skill
snapshots to the same source tag and verified the complete Codex and Claude
setup on Patrick's current Mac. The Cursor claim remains installation-layout
compatibility only because no paid Cursor account was used for live behavior.

The next audit revisited `SC-003` instead of assuming that a released skill
should keep expanding. Three real hardening histories supplied the evidence:
quote-share variant graduation in `pat-portfolio`, actionable-notification
acceptance in `nextup-ios-app`, and the simulator-focused Messenger 1.0 pass.
An initial comparison was discarded because its prompts disclosed the desired
review checklist. Fresh natural-prompt controls and released-skill runs both
found concrete historical defects, preserved the selected behavior, stayed
proportional, and withheld release actions. The released skill did not produce
a reliable lift. Patrick rejected a compatibility-only deprecation window, so
`production-hardening` was removed from the current source collection rather
than expanded. The next release must therefore be a major release. Repository
production instructions remain useful; `feature-delivery` still owns
substantial feature completion, and maintained
release-readiness skills may be composed when the requested artifact is an
operational go/no-go and rollout plan.

The next discovery pass captured `SC-015` after Patrick described standing up
Swift, React Native, Python, and other repositories with the right local and
GitHub configuration. The active-repository audit found that intended maturity,
not programming language, is the primary rigor axis. Lightweight prototypes
need a fast quality floor; maintained applications need reproducible setup,
tests, dependency updates, and required CI; shipped apps, services, and packages
add release automation, security policy, and protected tags. Platform-specific
generators and focused Expo, Vercel, Swift, and Python tooling already own many
mechanics, so the candidate should coordinate and verify them instead of
maintaining competing framework boilerplate. GitHub description, topics,
merge policy, rulesets, Dependabot, security features, and release/tag policy
are part of the repository outcome rather than a separate skill.

Four fresh candidate-absent scaffolds confirmed a narrower pilot. Capable
agents produced runnable, verified local projects, but the maintained Expo and
React cases omitted CI, dependency automation, and a concrete GitHub settings
plan; the shipping Python case hand-authored its scaffold instead of starting
from `uv init`; and the React case reconstructed current generator output after
the generator could not write its preference state. The lightweight Swift case
was appropriately small but added no reusable quality command or promotion
triggers. The pilot therefore needs to coordinate maturity, generator
provenance, local verification, and remote policy. It starts with one read-only
inspector and focused references, not a universal template, copied framework
boilerplate, reusable CI assets, or a GitHub mutation helper.

Four forward scaffolds then showed the intended lift. The lightweight Swift
project gained a reusable local contract and promotion triggers without being
overbuilt. Maintained Expo and React projects kept their official generators
while adding clean-install checks, CI, dependency automation, runtime pins, and
concrete GitHub plans. The shipping Python package moved to `uv init` and added
verified distribution artifacts plus an inert release path. The replays also
exposed two necessary boundaries: generator recovery stops after one narrowly
redirected state retry and may not escalate into internal inspection, shims,
patches, or hand reconstruction; licenses and other publisher identities remain
deferred until the owner chooses them. Structural, routing, script, installation
layout, and focused follow-up behavioral checks pass, so `SC-015` is validated
but not yet released.

Patrick Skills v3.0.0 now publishes `bootstrap-repository` and removes the
former `production-hardening` skill. The curated release notes, archive, and
clean exact-tag Claude Code, Codex, and Cursor layout installations were
verified, and Patrick Plugins v3.4.0 plus Agent Tooling v0.8.0 carry the same
collection boundary. The skills.sh collection discovered the new skill but
still serves stale stored files for three older records and retains the removed
record under the upstream stale-snapshot defect. `SC-015` therefore remains
`validated` until that external catalog gate passes. Real-repository dogfood is
also tracked separately for the next genuinely new or empty repository;
established projects such as `audiobook-ios` are deliberately excluded from
that bootstrap test.

`SC-001` validated the general-purpose approach: the ideation and comparison loop belongs in one portable skill, while SwiftUI, React Native, and web guidance belongs in platform references loaded only when relevant. The pilot also established that behavior claims require trace-backed evaluation, distribution claims require clean installation from a published tag, and an unavailable authenticated client should be described as packaging-compatible rather than behavior-verified. Future candidates should reuse those evidence boundaries instead of splitting skills by framework or overstating client support.

## Working rules

- Capture flows from completed tasks, corrections, working artifacts, and real failure cases.
- Keep one row per coherent outcome, not one row per individual step.
- Use `AGENTS.md` for always-on constraints and scripts for deterministic operations.
- Do not create a candidate brief until at least two representative examples or one strong example plus repeated corrections exist.
- Update the row and its brief together when classification or status changes.
- Record rejected candidates as `no-action` with a short rationale so the decision is not repeatedly reopened.
