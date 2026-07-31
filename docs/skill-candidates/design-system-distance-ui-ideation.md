# Skill Candidate: Design-System-Distance UI Ideation

- **Inventory ID:** `SC-012`
- **Status:** `validated`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-31

## Intent

- **Outcome:** Compare runnable UI directions that intentionally sit at different distances from a repository's existing design system.
- **Trigger:** A user asks for faithful, boundary-pushing, and radically different directions for the same component or surface.
- **Artifact:** A small, comparable direction set with repository-backed foundations, named intentional departures, and the existing `code-native-ui-ideation` selection or build handoff.
- **Non-goals:** Post-build conformance review, repository-wide system auditing, static mockups, or forcing every UI exploration into three prescribed postures.

## Real evidence

Patrick described this as a recurring axis inside his existing component-variant process: sometimes every direction should adhere to the established system, while other explorations should compare strict adherence, a controlled extension, and deliberate divergence.

### Representative examples

1. A read-only replay against `nextup-ios-app` compared a quiet native rail header, an extension of an existing glass treatment, and an editorial departure while holding content, behavior, and states constant.
2. Patrick uses the same code-native comparison loop in SwiftUI, React Native Storybook, and web development surfaces, so design-system distance changes the comparison contract rather than the platform or outcome.

### Repeated corrections

- Agents should not treat a token or color swap as a meaningful difference in system posture.
- Stretching should preserve named foundations while adding one intelligible rule; divergence should identify both the conventions it changes and the product or accessibility constraints it protects.

### Sensitive material

The baseline records only safe design-system observations and file categories. It does not commit private source, user data, credentials, or model transcripts.

## Mechanism decision

- **Decision:** Enhance `code-native-ui-ideation`; do not create another skill.
- **Classification:** Optional comparison technique inside the existing code-native ideation skill.
- **Rationale:** The trigger still asks for multiple runnable UI directions, and the artifact still uses the same comparison surface, fixtures, selection gate, and graduation boundary. A second skill would create routing overlap without a distinct outcome.
- **Scope:** Broadly portable across native and web repositories with an observable design language.

## Reusable contents

- **Instructions:** Distinguish protected foundations from conventions that may vary; define faithful, stretch, and divergent relationships; keep the component's job comparable.
- **Scripts:** None. Design-system evidence and project-native rendering are repository-specific.
- **References:** Continue using the existing SwiftUI, React Native, and web adapters only after directions are selected or implementation is explicitly requested.
- **Assets:** None.
- **Dependencies:** A target repository with enough interface or source evidence to infer its current system.

## External overlap gate

The 2026-07-31 `skills@1.5.21 find` searches for `ui ideation design system` and `align ui to design system` returned general design-system, brand, and alignment skills, but no skill centered on runnable comparison at deliberate design-system distances. The closest alignment skill is a broad system inventory and token-architecture checklist, not an ideation-stage comparison method. Re-run these searches before release because the index changes independently of this repository.

## Safety and boundaries

- Do not invent a formal design system when repository evidence is weak; state uncertainty and ground the directions in the observable interface and code.
- Preserve representative content, behavior, interaction, accessibility, and platform constraints across postures.
- Do not advance from choosing directions to implementation without the user's selection or explicit request to build now.
- Route targeted post-build alignment and repository-wide design-system auditing to their own skills.

## Evaluation plan

### Execution

1. Ask for three section-header directions in a SwiftUI app at faithful, stretching, and divergent distances. Success requires repository evidence, comparable behavior, and named protected or changed rules.
2. Ask to build card variants at deliberate system distances in React Native Storybook. Success requires shared fixtures and a posture record for each runnable variant.
3. Ask for web navigation directions without prescribing postures. Success means the optional technique is not forced into an unrelated exploration.

### Routing

- **Should trigger:** “Show faithful, stretching, and divergent directions”; “Build variants at different distances from our design language”; “Explore how far this component can push our system”; “Compare a system-native version with a radical one.”
- **Should not trigger:** “Align this finished component with our system”; “Audit the repository for design drift”; “Implement this approved design exactly”; “Generate static visual concepts.”

### Baseline

Compare against the last released `code-native-ui-ideation`. A fresh NextUp replay already produced three strong, grounded directions and respected the selection gate. The enhancement is therefore justified only as a small repeatability improvement: it should explicitly preserve foundations, name intentional departures, reject superficial posture differences, and leave unrelated explorations unchanged.

### Behavioral evidence

The baseline and forward replay used the same read-only prompt and inspected the same `nextup-ios-app` design-system and rail-header sources. The baseline already produced three coherent, repository-grounded directions, held content and behavior constant, and stopped for selection. The forward replay retained those strengths while adding an explicit protected-foundation contract, separating established system idioms from changeable component conventions, naming the new rule introduced by the stretching direction, and listing the exact conventions intentionally rejected by the divergent direction.

OpenAI's quick validator, the pinned `agent-ecosystem/skill-validator` v1.5.6, repository tests, Claude plugin validation, and isolated Skills CLI installation checks for all eleven skills across Claude Code, Codex, and Cursor layouts pass. This is unreleased source behavior; no new tagged-install or live-client claim is made.

## Definition of done

- [x] Mechanism and scope are approved.
- [x] Reusable resources are implemented and referenced.
- [x] Structural and repository validation passes.
- [x] Execution and routing eval coverage is updated.
- [x] Representative with-skill and baseline results are reviewed.
- [x] Intended Claude, Codex, and other claimed installation layouts are checked.
- [ ] Version, changelog, distribution metadata, and installation are verified.
- [x] Inventory status and lessons are updated.
