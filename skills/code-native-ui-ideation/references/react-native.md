# React Native Comparison Surfaces

## Inspect first

Search for React Native Storybook configuration, `*.stories.*` files, story providers, fixture stores, reset helpers, development clients, debug routes, simulator scripts, and tests that protect the production/story boundary.

## Choose the lightest surface

- Prefer an existing on-device Storybook for isolated components, screen states, and interaction treatments.
- Use the repository's story providers and decorators so fonts, themes, navigation, safe areas, and stores match the app.
- Use a development-only screen or route when the comparison depends on app navigation, native modules, or a flow that Storybook cannot represent faithfully.
- Do not install or configure a full Storybook stack for one experiment when the repository has a cheaper development surface.

## Keep variants comparable

- Reset mutable stores before each story or variant and seed them from the same fixture snapshot.
- Keep content, provider configuration, device, and starting interaction state constant while varying the named treatment.
- Expose variants as clear stories, controls, or an in-surface picker. Do not hide meaningful differences behind undocumented state.
- Include realistic long text, keyboard, loading, empty, error, and accessibility font-scale states when relevant.

## Verify and graduate

Exercise the comparison in the primary simulator or development client. Check touch targets, gestures, keyboard behavior, safe areas, scrolling, and platform differences that affect the choice. Run existing Storybook generation, type, or boundary checks when present.

After selection, remove abandoned stories or keep only those with continuing regression value. Remove temporary controls and ensure story modules, fixtures, and debug routes remain outside production bundles according to the repository's existing boundary.
