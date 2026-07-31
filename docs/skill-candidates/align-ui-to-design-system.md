# Skill Candidate: Align UI to a Design System

- **Inventory ID:** `SC-013`
- **Status:** `validated`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-31

## Intent

- **Outcome:** Decide whether one completed UI component or bounded surface conforms to the design system that actually exists in its repository, then optionally apply only the approved corrections.
- **Trigger:** A user finishes a component and asks to align, normalize, or review it against the repository's design language.
- **Artifact:** A source- and render-backed conformance review that classifies accidental deviations, intentional exceptions, system gaps, and uncertainty; when requested, a narrowly verified correction patch.
- **Non-goals:** Generating alternative directions, auditing an entire repository, inventing a new design system, exact translation from a supplied design, or a general production-readiness pass.

## Real evidence

Patrick described this as a recurring pass after building a component. It differs from ideation because the component's job and selected direction are already settled, and from a system audit because the scope is one surface and its direct dependencies.

### Representative examples

1. Review `ContinueWatchingCornerWordmarkBelowCard` in `nextup-ios-app` against the theme, peer media cards, platform interaction behavior, and accessibility expectations without auditing the rest of the repository.
2. Apply the same bounded review to a React Native Storybook component or a web component after its direction has been selected, preserving justified product-specific exceptions while removing accidental one-off styling.

### Repeated corrections

- “Make it match” must not flatten intentional hierarchy or product character merely because another component is more common.
- A repeated need that the system cannot express should be reported as a system gap, not silently hidden behind another one-off value or prematurely generalized into a global primitive.
- Review should remain read-only unless the user asked for fixes or approves a proposed correction set.

### Sensitive material

Use repository source and sanitized development renders. Do not commit private screenshots, production data, credentials, or raw user content as eval evidence.

## Mechanism decision

- **Decision:** Create `align-ui-to-design-system`.
- **Classification:** Discipline skill with an evidence and classification method.
- **Rationale:** General coding agents can compare styles, but the recurring judgment is whether a difference is accidental, intentional, or evidence of a missing primitive. That decision cannot be enforced reliably by token linters or exact-match tools and has a distinct trigger and artifact.
- **Scope:** Portable across native and web codebases; the repository supplies the design-system evidence and rendering tools.

## Reusable contents

- **Instructions:** Bound the surface; establish its job; infer the repository's system from an evidence hierarchy; compare tokens, composition, interaction, states, accessibility, responsive behavior, and motion; classify before recommending changes; preserve intentional exceptions.
- **Scripts:** None initially. Universal regex checks would confuse hardcoded values with contextual exceptions. Use repository linters or stack tools when present.
- **References:** A concise evidence and finding model may move to a reference only if the core skill would otherwise become bulky.
- **Assets:** None.
- **Dependencies:** Target repository source plus its normal preview, Storybook, simulator, or browser tooling when practical.

## External overlap gate

The 2026-07-31 Skills CLI searches for `align completed ui component design system`, `component design system conformance`, and `align ui to design system` found no same-named skill. The closest skills were:

- `aladicf/better-react-web-ui@normalize` (16 installs), which is frontend-specific, depends on a proprietary companion skill, assumes immediate execution, and aims for perfect conformity rather than a read-only classification of exceptions and system gaps.
- `owl-listener/designpowers@design-system-alignment` (15 installs), which combines system inventory, token architecture, component specifications, accessibility, and documentation into a broad design-system program rather than reviewing one finished surface.
- Figma synchronization and high-fidelity review skills, which should remain upstream choices when Figma is the source of truth.

The skills.sh index changes independently, so repeat the exact and semantic searches before validation and release. If a maintained portable skill gains the same bounded, classification-first behavior, prefer it or contribute upstream instead of retaining a duplicate.

## Safety and boundaries

- Default to review-only unless the request already authorizes edits; do not convert “review” into a rewrite.
- Read the nearest repository instructions and preserve unrelated user changes.
- Treat frequency as evidence, not proof: a common pattern may itself be drift, and a rare pattern may be intentional.
- Do not create a global token or shared primitive from one occurrence without evidence and approval.
- Do not expand a component review into a repository-wide audit or production hardening pass.

## Evaluation plan

### Execution

1. Review a completed SwiftUI media card against the repository theme and peer components. Success requires file-and-line evidence, classification, confidence, and no edits.
2. Align a selected React Native reaction component after the user authorizes fixes. Success preserves intentional interaction differences, uses existing primitives where justified, and verifies the story on-device.
3. Review a web portfolio module that intentionally uses bespoke display typography but accidentally hardcodes spacing and focus styles. Success preserves the intentional typography and proposes the smallest token and accessibility corrections.

### Routing

- **Should trigger:** “Align this finished card with our design system”; “Review this component for accidental design drift”; “Normalize this selected surface without redesigning it”; “Fix the conformance issues you find in this one component.”
- **Should not trigger:** “Show me three design directions”; “Audit the entire component library”; “Implement this Figma frame exactly”; “Harden this feature for production”; “Explain design systems generally.”

### Baseline

Use a no-skill, read-only replay on a real completed NextUp component. Retain the candidate only if the skill more reliably establishes repository authority, distinguishes accidental deviations from intentional exceptions and system gaps, scopes evidence to the component, and keeps corrections behind the user's edit boundary.

The no-skill replay was already strong: it found a likely VoiceOver labeling defect, preserved the component's intentional media and navigation choices, identified two plausible missing primitives from repeated sibling implementations, declined an over-broad caption abstraction, stayed read-only, and skipped a disproportionate build. The candidate therefore should not claim superior design judgment. Its justification is a portable, repeatable review contract and routing boundary; if the forward replay merely adds ceremony or weakens the baseline's judgment, retire the candidate.

### Behavioral evidence

The forward replay retained the baseline's bounded, read-only behavior and the same high-confidence VoiceOver finding. The explicit authority ladder led it to inspect the component's selected design specification and a role-equivalent full-row treatment, which exposed two additional evidence-backed issues: an undersized overflow target and missing Increased Contrast adaptation. It classified long-title behavior as uncertain pending a discriminating Dynamic Type render instead of guessing, preserved the optical wordmark values and split interaction as intentional, and proposed only one narrow shared primitive.

OpenAI's quick validator, the pinned `agent-ecosystem/skill-validator` v1.5.6, repository tests, Claude plugin validation, Skills CLI discovery, and isolated installation checks for all eleven skills across Claude Code, Codex, and Cursor layouts pass. This source is validated but unreleased; no tagged-install or live-client behavior claim is made.

## Definition of done

- [x] Mechanism and scope are approved.
- [x] Reusable resources are implemented and referenced.
- [x] Structural and repository validation passes.
- [x] Execution and routing eval coverage passes.
- [x] Representative with-skill and baseline results are reviewed.
- [x] Intended Claude, Codex, and other claimed installation layouts are checked.
- [ ] Version, changelog, distribution metadata, and installation are verified.
- [x] Inventory status and lessons are updated.
