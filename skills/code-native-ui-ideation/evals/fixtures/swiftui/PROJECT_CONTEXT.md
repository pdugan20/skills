# SwiftUI evaluation fixture

This sanitized fixture represents an existing episode-tracking app.

- `EpisodeStatusControl` is a SwiftUI component used in episode rows.
- `PreviewCatalogView` is the existing native component-review surface.
- Preview Content already provides watched, unwatched, airing, long-title, and Dynamic Type fixtures.
- The app has established color, spacing, typography, and motion tokens.
- The comparison must be evaluated in Xcode previews or the iOS simulator.
- Preview-only controls and fixtures must not enter the production application path.

The fixture is intentionally descriptive rather than compilable. Evaluate process decisions, comparison quality, platform choice, and cleanup boundaries—not Swift syntax.
