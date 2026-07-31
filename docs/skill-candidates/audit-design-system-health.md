# Skill Candidate: Audit Design-System Health

- **Inventory ID:** `SC-014`
- **Status:** `released`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-31

## Intent

- **Outcome:** Explain where a code repository's implemented design system is coherent, drifting, missing capabilities, or duplicating semantically similar UI, then prioritize evidence-backed remediation and enforcement opportunities.
- **Trigger:** A user asks for a repository-wide design-system, UI consistency, token drift, hardcoded-value, component-overlap, or consolidation audit.
- **Artifact:** A read-only source-of-truth map, classified findings, consolidation clusters, enforcement recommendations, limitations, and a staged remediation order with exact evidence.
- **Non-goals:** Fixing one completed component, automatically refactoring the repository, creating a greenfield design system, scoring team adoption without evidence, or treating every literal value and duplicate line as design drift.

## Real evidence

Patrick described a recurring system-level pass for hardcoded colors or values, conflicting conventions, visually and semantically overlapping components, consolidation candidates, and rules worth enforcing. Its cost, evidence breadth, and report differ materially from the bounded component-alignment pass.

### Representative examples

1. Audit `pat-portfolio`, where CSS custom properties, Tailwind, component-specific styles, bespoke editorial treatments, and repository scripts coexist. The useful result must distinguish intentional article or visualization treatments from accidental one-offs and identify component families by role, not only duplicated source text.
2. Audit a native repository such as `nextup-ios-app`, where theme constants and shared SwiftUI components coexist with optical media-card values and platform-specific interaction. Hardcoded literals can be intentional, while repeated control labels or card treatments can reveal missing primitives.

### Repeated corrections

- Do not create a giant unverified list of regex matches or assign a synthetic health score without a defensible denominator.
- Similar appearance is not sufficient for consolidation; compare semantic role, states, interaction, accessibility, ownership, and migration cost.
- Recommend linting only for stable, machine-detectable rules with acceptable false positives. Keep judgment-heavy exceptions in review guidance or tests.
- Default to a read-only report; system refactors require separate approval and staged implementation.

### Sensitive material

Commit only safe summaries and generic eval fixtures. Do not include private design files, screenshots with personal data, credentials, proprietary assets, or raw production content.

## Mechanism decision

- **Decision:** Create `audit-design-system-health` without a universal scanner.
- **Classification:** Composite audit skill using repository-native and maintained upstream tools.
- **Rationale:** Deterministic tools can find literals, token usage, source duplication, and accessibility failures, but they cannot decide whether a visual difference is intentional or whether two differently implemented components should consolidate. The skill owns scoping, evidence synthesis, semantic clustering, prioritization, and the enforcement boundary.
- **Scope:** Portable across native and web code repositories, including informal systems whose source of truth must be inferred.

## Reusable contents

- **Instructions:** Map sources of truth and enforcement; choose a representative scan; normalize deterministic signals; inspect rendered or semantic peers; classify findings and candidate clusters; recommend enforcement only after a stable rule is established.
- **Scripts:** None initially. A generic regex scanner would duplicate repository search tools and produce misleading cross-stack results. Add a deterministic helper only after repeated audits reveal the same bounded transformation.
- **References:** A stack-aware signal and enforcement guide for CSS/Tailwind, SwiftUI, React Native, design files, duplication, accessibility, and CI.
- **Assets:** None.
- **Dependencies:** Target repository source and its existing linters, tests, previews, Storybook, simulator, or browser tools. Optional maintained upstream tools should remain optional and separately attributed.

## External overlap gate

Repeated 2026-07-31 `skills@1.5.21 find` searches covered `design system audit`, `design token audit`, `design system drift`, `component consistency audit`, `repository design system drift consolidation`, and `duplicate ui components hardcoded tokens audit`. The closest results were inspected rather than judged from names alone:

- `edenspiekermann/skills@audit-design-system` (123 installs) audits Figma nodes through Figma read tools and should remain the upstream choice for Figma-only conformance.
- `mohitagw15856/pm-claude-skills@design-system-audit` (31 installs) targets formal design-system teams, adoption, governance, documentation, Figma-code parity, and health scoring; it requires organizational inputs that a code-repository audit often does not have.
- `murphytrueman/design-system-ops@drift-detection` (15 installs) is the closest system-wide overlap, with useful drift classes and integrations, but assumes a formal source of truth, recurring enterprise operations, and Figma/GitHub/Chromatic-style infrastructure.
- `owl-listener/designer-skills@design-token-audit` (984 installs) is a concise token adoption audit, not a semantic component-consolidation or cross-platform repository audit.
- `affaan-m/everything-claude-code@design-system` (4,900 installs) and `shipshitdev/library@design-consistency-auditor` (268 installs) provide broad web-oriented visual checklists and scores rather than a repository-evidence and migration-boundary method.
- `heyeddi-com/skills@no-duplicate-ui` (28 installs) runs a Vue template-similarity scanner and recommends immediate consolidation; it is a useful Vue-specific lead generator but does not test semantic compatibility.
- `terrylica/cc-skills@code-hardcode-audit` (143 installs) orchestrates nine general magic-number, secret, and source-duplication tools. It is broader code-security tooling rather than a design-system audit and its raw results still require UI-specific normalization.
- `dragoon0x/optik@system-audit` (5 installs) checks dead, undefined, inconsistent, and missing token categories only. A high-install `drift` search result was inspected and proved unrelated: it integrates the Drift sales platform, demonstrating why names and search rank are insufficient overlap evidence.
- `kensaurus/cursor-kenji@audit-uiux-design-system` (24 installs) is a large web audit that auto-detects CSS and component frameworks, mandates current-product research and browser tooling, applies prescriptive anti-template aesthetics, and can lead to fixes. Use it when that web-specific visual program and its companion tools are desired; it does not fit an informal native system or a narrow technical health report.
- `kensaurus/cursor-kenji@plan-uiux-unification` (21 installs) is the closest conceptual overlap: a read-only, exhaustive IA, UX, content, per-surface, token, component, research, burndown, and unification plan. Use it for a comprehensive redesign-planning document. This candidate remains narrower and proportional: implemented-system authority, normalized drift signals, semantic component clusters, system gaps, and enforceability across native and web code.

The new name avoids the existing generic `audit-design-system` collision. Re-run exact and semantic searches before validation and release. Retire or narrow this candidate if a maintained portable skill gains the same repository-first, native-and-web, informal-system, semantic-consolidation behavior.

## External tools and delegation

- Use repository-native lint, tests, token APIs, Storybook, previews, and visual regression infrastructure first.
- Use [Google DESIGN.md](https://github.com/google-labs-code/design.md) and its linter only when the repository already adopts or explicitly wants that alpha contract. Google's Stitch skills are useful upstream for frontend extraction, not required dependencies.
- Use maintained linters such as Stylelint or SwiftLint to encode approved, low-false-positive rules in the target repository; do not install or configure them during a read-only audit.
- Use [jscpd](https://github.com/kucherenko/jscpd) as one source-duplication signal. It cannot establish semantic UI redundancy on its own.
- Use upstream Figma skills when Figma is a named source of truth. Keep the portable audit useful without Figma.

## Safety and boundaries

- Preserve dirty work and keep the audit read-only unless the user separately authorizes implementation.
- Scope commands to named repositories and avoid long builds or exhaustive renders unless they materially change confidence.
- Do not present inferred rules, counts, percentages, or accessibility compliance as facts without evidence and a known denominator.
- Do not recommend consolidating components without comparing role, state, interaction, accessibility, dependencies, and migration risk.
- Do not install tools, change CI, or create lint policy during an audit.

## Evaluation plan

### Execution

1. Audit a Next.js portfolio with CSS variables, Tailwind, component CSS, custom visualizations, and bespoke editorial exceptions. Success requires normalized evidence, semantic consolidation clusters, and selective enforcement recommendations.
2. Audit a SwiftUI application with theme constants, optical media values, repeated card and overflow treatments, and platform accessibility requirements. Success distinguishes intentional literals from drift and proposes native enforcement only for stable rules.
3. Audit a React Native messenger with semantic theme hooks, Storybook, repeated interaction components, and fixture providers. Success combines static signals with state and on-device evidence rather than scoring source alone.

### Routing

- **Should trigger:** “Audit this repository's design-system health”; “Find token drift and overlapping UI components”; “Where should we consolidate or enforce our visual rules?”; “Review the whole component library for hardcoded values and inconsistent primitives.”
- **Should not trigger:** “Align this one finished card”; “Show three UI directions”; “Create a greenfield token system”; “Implement all audit fixes”; “Audit only this Figma frame.”

### Baseline

Use a no-skill, read-only replay against `pat-portfolio`. Retain the candidate only if it turns raw static matches into a defensible source-of-truth map, classified findings, semantic consolidation clusters, and low-false-positive enforcement recommendations while clearly stating sampling and render limitations.

The no-skill replay already met much of that bar. It mapped the distributed CSS, documentation, component, and feature-palette authorities; found independently introduced tag-filter duplication, repeated media controls, literal colors that duplicate semantic tokens, drifting edge fades, and a missing visualization theme; preserved brand, data, dynamic, error-page, and experimental exceptions; and recommended a repository-specific Tailwind-class check instead of generic Stylelint. It used history and an existing guard script, remained read-only, and stated that rendering was skipped. The candidate should be retired if its forward replay adds a generic checklist, synthetic scoring, or ceremony without improving reproducibility, evidence normalization, semantic clustering, uncertainty, or enforcement decisions.

### Behavioral evidence

The forward replay retained the baseline's strongest findings and read-only proportionality while making the consolidation boundaries more precise. It separated legacy media retirement from an active media-control presentation primitive, recommended extracting only the noninteractive edge-fade surface rather than merging `PosterRail` behavior, distinguished an exact token bypass from a possible missing subtle-boundary token, and kept different skeleton geometries separate. Its enforcement matrix named scope, exclusions, migration prerequisites, and informational rollout, and it explicitly deferred four conclusions that require rendering instead of turning them into backlog claims.

The final skills.sh overlap pass inspected the closest newly surfaced public skills as well as the earlier token, Figma, drift, and consistency candidates. The exact name remains distinct, and the narrower proportional technical-health outcome remains justified against the exhaustive `plan-uiux-unification` alternative. OpenAI's quick validator, the pinned `agent-ecosystem/skill-validator` v1.5.6, repository tests, Claude plugin validation, Skills CLI discovery, and isolated installation checks for all eleven skills across Claude Code, Codex, and Cursor layouts pass.

### Release evidence

- Patrick Skills [v2.4.0](https://github.com/pdugan20/skills/releases/tag/v2.4.0)
  points to merge commit `27f786b3d5d239f3bdf7f15eed774883ea0a7ef3`.
- The checksum-verified release archive contains `audit-design-system-health`
  and matches the tagged source byte-for-byte.
- A clean Skills CLI installation from the exact tag copied all eleven skill
  trees into the Claude Code, Codex, and Cursor layouts. Cursor packaging is
  verified without a paid-client behavior claim.

## Definition of done

- [x] Mechanism and scope are approved.
- [x] Reusable resources are implemented and referenced.
- [x] Structural and repository validation passes.
- [x] Execution and routing eval coverage passes.
- [x] Representative with-skill and baseline results are reviewed.
- [x] Intended Claude, Codex, and other claimed installation layouts are checked.
- [x] Version, changelog, distribution metadata, and installation are verified.
- [x] Inventory status and lessons are updated.
