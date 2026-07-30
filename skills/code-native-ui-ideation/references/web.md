# Web Comparison Surfaces

## Inspect first

Search for Storybook, component examples, development routes, labs, preview panels, feature flags, query-parameter switches, local-storage helpers, fixture data, visual tests, and responsive browser tooling.

## Choose the lightest surface

- Prefer an existing Storybook for isolated components and deterministic component states.
- Use the running application's page or a project-local lab when routing, page composition, real layout constraints, hover, focus, scrolling, or live application context affects the decision.
- Add a development-only panel, route, query parameter, local switch, or small variant picker when no comparison surface exists.
- Prefer a shareable query parameter when collaborators need to open a specific variant; prefer ephemeral local state when persistence adds no value.

Do not create a detached option-picker site when the target application can host the variants directly.

## Keep variants comparable

- Hold content, data snapshot, state, viewport, and interaction scenario constant.
- Reuse the application's tokens, components, assets, and responsive breakpoints.
- Separate independent decisions into independent controls only when testing their combinations is useful; otherwise keep each variant coherent.
- Include long content, empty or error states, keyboard focus, reduced motion, and color-scheme variants when they reveal material tradeoffs.

## Verify and graduate

Exercise the variants in the browser at the relevant compact and wide viewports. Check pointer, keyboard, touch emulation, focus, scrolling, and responsive behavior as applicable. Run the smallest relevant lint, type, render, or interaction check.

After selection, remove abandoned branches, temporary panels, stale query parameters, local-storage keys, data attributes, and experiment-only styles. Retain a lab or story only when it has continuing development or regression value, and keep it out of user-facing production paths.
