# Workflow Candidate: Cross-Platform Component Variant Exploration

- **Inventory ID:** `WF-001`
- **Status:** `released`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-30

## Intent

- **Outcome:** Turn an initial component or UI idea into a small set of meaningful, runnable directions that can be compared on the actual target platform, then preserve the selected direction for production work.
- **Trigger:** Patrick asks to brainstorm, explore, compare, revise, or try multiple versions of a component or UI in a native-mobile or web repository.
- **Artifact:** Two to four working variants using comparable content and state, a project-native way to switch among or inspect them, and a clear cleanup path for the selected variant.
- **Non-goals:** Static image mockups, a separate browser-based option picker, a general product-design audit, production hardening before a direction is chosen, or separate skills whose only distinction is the target platform.

## Real evidence

Patrick described the same recurring decision loop across native-mobile and web projects: contribute directions, select a few worth building, compare them with live or fixture data, choose one, and graduate it to production.

### Representative examples

1. `nextup-ios-app` uses SwiftUI `#Preview` declarations, reusable Preview Content fixtures, and a `PreviewCatalogView` for rapid component review on the native platform.
2. `messenger-proto` uses React Native Storybook, screen stories, resettable story providers, and messenger fixtures to exercise multiple realistic UI states in isolation.
3. `pat-portfolio` uses dev-only comparison labs, a reusable `VariantPicker`, and persisted selection state to toggle UI treatments directly in the running Next.js site.

### Repeated preferences and corrections

- Work in real project code and render on the relevant platform rather than replacing the exploration with generated images or static mockups.
- Make alternatives easy to compare using the same representative content, state, and constraints so incidental data differences do not distort the decision.
- Reuse a repository's existing Storybook, preview catalog, route, dev panel, fixtures, tokens, and components before inventing new infrastructure.
- Keep exploration code reversible and give the chosen direction an explicit graduation and cleanup step.

### Sensitive material

Use synthetic or safely derived fixtures. Do not copy production user data, private messages, credentials, personal identifiers, or confidential client material into stories, previews, eval fixtures, or committed documentation.

## Mechanism decision

- **Decision:** Enhance the existing `code-native-ui-ideation` skill. Keep the common decision loop in `SKILL.md` and put SwiftUI, React Native, and web implementation guidance in directly linked references.
- **Classification:** Technique with a reusable comparison pattern.
- **Rationale:** The trigger, design decisions, comparison contract, and graduation outcome are the same across platforms. Separate mobile and web skills would duplicate the core method, overlap in routing for cross-platform repositories, and require the user to choose an implementation detail. Platform-specific workbenches are adaptations of the method, not independently useful outcomes.
- **Scope:** Broadly portable, with repository-native capability detection and no requirement that a project adopt a particular preview system.

The default interaction should be proportional:

1. Inspect the existing interface, repository instructions, design system, data sources, and available preview or development surfaces.
2. Combine Patrick's starting ideas with a few materially distinct directions of the agent's own.
3. When Patrick asked to explore rather than immediately build, present a concise direction set and let him select the two to four worth implementing.
4. Build the selected variants behind one project-native comparison surface using a shared data and state contract.
5. Render and exercise the variants on the real target platform, including relevant interaction and responsive or dynamic states.
6. Record the selection. When asked to graduate it, preserve the chosen implementation, remove abandoned variants and temporary controls, and hand substantial production work to the appropriate delivery workflow.

If Patrick explicitly asks the agent to build alternatives immediately, it should choose a small representative set and proceed without adding a redundant approval pause.

## Reusable contents

- **Instructions:** The shared ideate, select, build, compare, choose, and graduate loop; guidance for meaningful variation; a comparable-data contract; proportional verification; and cleanup boundaries.
- **Scripts:** None initially. Repository-specific build and launch commands should remain in repository documentation unless repeated evidence justifies a portable detector or launcher.
- **References:**
  - SwiftUI: prefer existing `#Preview` declarations and Preview Content fixtures; use an in-app debug gallery when navigation, environment, or multi-step interaction cannot be evaluated adequately in a preview; verify in previews or the simulator as appropriate.
  - React Native: prefer an existing on-device Storybook and its providers; preserve the repository's boundary between story code and production bundles; use the simulator or development client for platform behavior.
  - Web: prefer an existing Storybook when present; otherwise use a development route, local lab, dev panel, query parameter, or reversible variant picker in the running app; verify responsive and interaction states in the browser.
- **Assets:** None initially. The comparison surface should fit the host project's visual language and infrastructure.
- **Dependencies:** The target repository and its native build, preview, Storybook, simulator, or browser tooling. No external hosted service is required by the skill.

## Safety and boundaries

- Do not use ImageGen or static image mockups unless Patrick explicitly requests them.
- Do not create a detached option-picker application when the target project can host runnable variants directly.
- Do not expose Storybook, preview fixtures, dev routes, or temporary toggles in a production bundle unintentionally.
- Do not mutate production data or depend on sensitive data to make a design comparison realistic.
- Do not turn lightweight exploration into architecture, release, or hardening work without an explicit request.
- Do not trigger for implementing a single already-selected design, translating a supplied design exactly, or reviewing production readiness.

## Evaluation plan

### Execution

1. Ask for several directions for a new SwiftUI episode-status control in a repository with Preview Content fixtures. A successful result contributes distinct ideas, implements only the selected comparison set in a preview or native catalog with shared fixtures, renders it on the native platform, and keeps the experiment reversible.
2. Ask to compare alternative React Native message-reaction treatments in a repository with on-device Storybook. A successful result reuses Storybook and its providers, keeps message data constant across variants, exercises interaction in the simulator, and preserves the production/story boundary.
3. Ask to explore several hover and compact-layout treatments for a Next.js portfolio component without Storybook. A successful result uses a project-local lab or dev control, supports rapid switching in the real page, verifies relevant viewport and pointer states, and identifies the temporary code to remove after selection.

Subjective design quality requires Patrick's review. Deterministic assertions should cover the presence of multiple runnable variants, use of a shared comparison contract, reuse of project-native infrastructure, proportional platform verification, and an explicit graduation boundary.

### Routing

- **Should trigger:** “Show me a few versions of this SwiftUI card”; “Come up with some reaction treatments and let me compare the strongest ones”; “Build several versions of this portfolio module behind a toggle”; “I want to iterate on this component in Storybook before choosing one.”
- **Should not trigger:** “Implement this approved Figma component exactly”; “Audit this screen for accessibility problems”; “Generate image mockups for three landing-page concepts”; “Harden the selected component for release”; “Fix the padding regression in this button.”

### Baseline

Compare against the last released version of `code-native-ui-ideation`. The enhancement is worth retaining if it more reliably distinguishes ideation from immediate implementation, selects the repository's existing comparison surface, keeps content and state comparable across variants, and carries the selected direction through an explicit cleanup handoff without making small explorations heavier.

At the start of the pilot, the released skill already required runnable in-project variants and platform-appropriate rendering. Static inspection identified four claims that it did not yet encode: an ideate-versus-build branch, a shared content and state comparison contract, project-native workbench selection, and an explicit graduation cleanup inventory. The pilot evals targeted those gaps, and the trace-backed behavioral review below completed the provider-backed comparison gate.

### Pilot implementation

- The main skill now contains the shared comparison contract and ideate-versus-build branch.
- Three directly linked references adapt the method for SwiftUI, React Native, and web repositories without duplicating the core workflow.
- Six execution cases cover general exploration plus the three platform adapters.
- Twenty routing cases are balanced between realistic triggers and adjacent near misses.
- Repository verification, Skills CLI discovery, `agent-ecosystem/skill-validator` v1.5.6, and the official Claude plugin validator pass. The tooling audit is complete: the temporary `claude-code-lint` gate was replaced with the exactly pinned official Claude Code CLI.
- An isolated Skills CLI `1.5.21` installation test copies all three skills and their supporting resources to the project locations used by Claude Code, Codex, and Cursor during every `npm run verify`. Live Claude and Codex invocation evidence is recorded below; Cursor packaging is verified without making a live-model claim.

### Behavioral evidence

The 2026-07-30 live review used Claude Code `2.1.220` with `claude-haiku-4-5-20251001`. The personal user-level copy of `code-native-ui-ideation` was disabled for the run, one candidate plugin directory was loaded at a time, and an execution result was accepted only when the stream trace showed an exact `Skill` tool invocation for `patrick-workflows:code-native-ui-ideation`. Plain slash-command text inside non-interactive `claude -p` prompts was found not to guarantee skill loading, so those earlier outputs were discarded.

- **Routing retention:** On one representative positive wording, the released baseline and pilot each invoked the intended skill in four of five trials. On one exact-implementation near miss, neither version invoked it in five trials. The rewrite therefore retained routing behavior but did not claim a routing improvement.
- **Selection-stage behavior:** On the SwiftUI execution case that asks to decide what is worth seeing before building, five pilot trials loaded the exact skill and all five stopped after three to five total directions, named tradeoffs, and a request for Patrick to select two to four. Five released-baseline trials loaded the exact skill, but all five outlined building the complete brainstormed set before the user selected it. The live failure drove the explicit stage gate now encoded in the skill.
- **Build-stage behavior:** A forced React Native run loaded the exact pilot skill, reused the existing on-device Storybook and resettable providers, held conversation fixtures and the long-press interaction constant, proposed three named treatments, required native-simulator verification, and returned an artifact-by-artifact cleanup inventory. A representative web run likewise used the real page, existing URL-backed `VariantPicker`, stable content, compact and wide layouts, hover and focus checks, and post-selection cleanup.
- **Trace review:** The discarded runs exposed two evaluation hazards: a global skill with the same name can contaminate an apparent plugin test, and a generic turn count cannot prove which skill ran. The accepted method hides the duplicate and inspects the exact tool input. No raw credentials or bulky model transcripts are committed.

Codex `0.145.0` also completed a read-only live run from a disposable project containing the pilot under `.agents/skills`. Its trace shows the project-local `SKILL.md` and `references/web.md` being read before it produced the shared comparison contract, real-page `VariantPicker` plan, browser checks, and cleanup inventory.

Cursor Agent `2026.07.23-e383d2b` is installed from Cursor's official installer and exposes read-only plan and ask modes plus local plugin loading. The automated Skills CLI test copies every skill and resource byte-for-byte into Cursor's supported `.agents/skills` project location. No authenticated Cursor account is currently available, so no live model-output claim is made; installation and packaging compatibility are the verified boundary.

All three repository skill pages return successfully from `skills.sh`, and the README now exposes the official install-count badge and catalog link. Discovery is driven by anonymous Skills CLI install telemetry rather than a separate submission workflow; release tags remain the reproducible installation mechanism.

### Release and distribution evidence

- The completed collection is published as [`pdugan20/skills` v2.0.0](https://github.com/pdugan20/skills/releases/tag/v2.0.0), with the skill implementation introduced in v1.1.0 and the canonical repository and package names established in v2.0.0.
- A clean installation from the published v2.0.0 tag succeeded for Claude Code, Codex, and Cursor targets, with every installed skill file matching the tagged source byte-for-byte.
- [`patrick-skills@patrick-plugins`](https://github.com/pdugan20/plugins/releases/tag/v2.0.0) pins the collection's v2.0.0 release, and the public marketplace passed isolated Claude Code and Codex installation smoke tests after release.
- [`agent-tooling` v0.5.0](https://github.com/pdugan20/agent-tooling/releases/tag/v0.5.0) consumes the canonical skill release and marketplace names, preserves Skills CLI provenance in its lockfile, and passed its full release verification.
- Collection-level semantic versions and the central changelog remain authoritative. Individual skills do not carry separate versions or changelogs; skill-specific changes are named in the collection changelog.

## Definition of done

- [x] Mechanism and scope are approved.
- [x] Reusable resources are implemented and referenced.
- [x] Structural and repository validation passes.
- [x] Execution and routing eval coverage passes.
- [x] Representative with-skill and baseline results are reviewed.
- [x] Intended Claude, Codex, and other claimed integrations are checked.
- [x] Version, changelog, distribution metadata, and installation are verified.
- [x] Inventory status and lessons are updated.
