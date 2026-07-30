# SwiftUI Comparison Surfaces

## Inspect first

Search for existing `#Preview` declarations, Preview Content, preview traits, fixture factories, mock services, component catalogs, debug menus, and simulator instructions. Reuse the project's environment and dependency-injection conventions.

## Choose the lightest surface

- Use `#Preview` or an existing preview catalog for isolated components, layout alternatives, appearance modes, and deterministic data states.
- Use separate named previews when side-by-side inspection is more useful than toggling.
- Use a small picker or gallery inside the existing preview or debug surface when rapid switching is the important comparison behavior.
- Use an in-app development screen when the comparison depends on navigation, lifecycle, environment objects, services, or a multi-step flow.
- Use the simulator when animation, gestures, keyboard behavior, safe areas, scrolling, Dynamic Type, or device-specific behavior affects the decision.

Do not introduce a new catalog architecture for a single experiment when a few local previews are sufficient.

## Keep variants comparable

- Drive every variant from the same Preview Content fixtures and mocked dependencies.
- Cover the states that expose the design decision, such as empty, populated, selected, loading, error, long-content, and accessibility-size states.
- Keep a variant enum or switching control in preview or debug code unless the selection is itself a production setting.
- Avoid network-dependent previews and never use production user data.

## Verify and graduate

Render the chosen comparison surface and use the target simulator for interaction-sensitive work. Run the smallest relevant build or focused check available in the repository.

After selection, remove abandoned variants and preview-only switches. Retain fixtures and catalog entries only when they remain useful for development, regression review, or documentation. Confirm debug-only entry points are not exposed to users.
