# Signals and Enforcement

Load only the sections relevant to the repository. Prefer its existing commands and architecture over introducing these tools.

## CSS and Tailwind repositories

Inventory theme definitions, CSS custom properties, Tailwind theme configuration, semantic utilities, arbitrary values, literal hex/rgb/hsl colors, inline styles, radii, shadows, type, breakpoints, motion, and z-index. Distinguish:

- token definitions from token bypasses;
- semantic application colors from brand, data, SVG, image-derived, authored-content, and emergency-fallback colors;
- optical values from repeated layout rules;
- framework adapter aliases from competing authoring vocabularies.

Stylelint allow/disallow rules work for CSS declarations. Tailwind classes embedded in JSX may require an existing ESLint rule, a scoped repository script, or typed component APIs instead. Do not recommend a generic CSS linter for evidence it cannot parse.

## SwiftUI repositories

Map theme constants, semantic `Color` and `Font` APIs, environment values, modifiers, shared views, previews, accessibility scenarios, and platform components. Search for direct color construction, system font sizes, repeated padding/radius/shadow/animation literals, hand-rolled controls, and duplicated view structures.

Optical media overlays, data colors, platform metrics, and one-off transition geometry may be intentional. Stable forbidden literals can use narrowly scoped SwiftLint custom rules; stronger conformance usually comes from typed theme APIs, shared modifiers, previews, accessibility tests, and compiler-visible component boundaries.

## React Native repositories

Map theme providers and hooks, semantic style types, shared pressables and typography, `StyleSheet` modules, Storybook, fixture providers, and platform adapters. Search for inline styles, literal colors and spacing, raw touchables, duplicated variants, and components whose pressed, disabled, selected, focus, or screen-reader states diverge.

Use existing ESLint or typed-theme rules for deterministic source policy. Use Storybook interaction and device tests for state, input, and accessibility behavior that source lint cannot establish.

## Component overlap

Build candidates from several signals: similar names, semantic roles, rendered structure, imports, prop/state shapes, repeated class or modifier groups, and source duplication. Tools such as `jscpd` can reveal copy-paste clusters, but a high score is neither necessary nor sufficient for UI consolidation.

For each cluster, compare role, states, interaction, accessibility, platform behavior, variants, dependencies, and migration cost. Prefer extracting the smallest stable contract. Sometimes the correct action is shared tokens, a small label or modifier, documentation, or no consolidation.

## Rendered and accessibility evidence

Use existing Storybook, SwiftUI previews, component galleries, development routes, browser or simulator checks, accessibility tests, and focused screenshots. Sample representative states and platforms based on risk. Do not claim complete visual or accessibility coverage from static source or a single default render.

Use upstream Figma capabilities when Figma is a named authority. Keep Figma-code discrepancies attributed separately from repository-internal drift.

## Choosing enforcement

| Claim | Best initial mechanism | Avoid |
| --- | --- | --- |
| Known literal duplicates a semantic token | Scoped lint or repository check with allowlist and replacement | Banning all literals across assets, data, or token definitions |
| Shared primitive must own a standard interaction | Typed API, import boundary, or AST-aware lint after migration | Regex before a compatible primitive exists |
| Component states or accessibility semantics drift | Component, interaction, accessibility, or device tests | Inferring runtime behavior from source counts |
| Stable visual contract regresses | Focused visual regression across named states | Exhaustive screenshot suites with unclear ownership |
| Similar source may be duplicated | Informational duplication report plus semantic review | Blocking CI on a global duplication percentage |
| Product-specific exception needs judgment | Documentation and code review guidance | Encoding taste as a brittle lint rule |

Start new enforcement as informational when the repository contains existing debt. Define exclusions and migrate violations before making a rule blocking.
