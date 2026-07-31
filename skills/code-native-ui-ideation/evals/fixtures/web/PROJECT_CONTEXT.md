# Web evaluation fixture

This sanitized fixture represents an existing Next.js portfolio.

- The application has no Storybook.
- Related-project cards render on the real portfolio page with stable sanitized project fixtures.
- A development-only `VariantPicker` pattern already persists a selected variant in a URL parameter.
- The application has established color, spacing, typography, radius, shadow, and motion tokens.
- Development-only routes and controls can be excluded from production builds.
- The comparison must cover pointer hover plus compact and wide browser layouts.

The fixture is intentionally descriptive rather than compilable. Evaluate process decisions, comparison quality, platform choice, and cleanup boundaries—not React syntax.
