# React Native evaluation fixture

This sanitized fixture represents an existing messenger application.

- The app has an on-device Storybook that is excluded from production bundles.
- Message stories use resettable providers for navigation, state, theme, and data.
- Sanitized conversation fixtures cover short and long messages, incoming and outgoing messages, existing reactions, and multiple reaction counts.
- Design tokens and message primitives are shared with the production app.
- Storybook controls can switch component props without changing fixture data.
- The comparison must be exercised in the native simulator or development client.

The fixture is intentionally descriptive rather than compilable. Evaluate workflow decisions, comparison quality, platform choice, and cleanup boundaries—not React Native syntax.
