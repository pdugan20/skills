# Entities and queries

## Model the system-facing value

- Use the app's durable domain identifier. Do not key entities by display text,
  array position, temporary database object identity, or a localized label.
- Expose only values needed for display, resolution, schema requirements, or
  returned results. System metadata can outlive a screen and may appear outside
  the app.
- Prefer a Sendable struct snapshot over conforming an actor-bound persistence
  model directly. Hydrate the snapshot inside the repository-supported actor or
  data-access boundary.
- Keep `displayRepresentation` concise and speech-safe. A compact visual code
  can need a different dialog because Siri may read every character literally.
- Keep entity identifiers stable across indexing, Shortcuts serialization,
  deep links, widgets, and future app versions.

## Choose query capabilities deliberately

- Implement identifier resolution for persisted entities.
- Add suggested entities only when a bounded, useful candidate set exists.
- Add `EntityStringQuery` when the system needs typed or spoken lookup and the
  app can perform an authoritative match.
- Use `IndexedEntity` when app content should be discoverable through the
  system index. Mark the properties that legitimately improve retrieval with
  the current SDK's indexing keys.
- Keep query I/O in the actor or service that owns the data. Returning a value
  snapshot does not make the hydration step actor-free.
- Define signed-out, deleted, stale, and partial-data behavior. Preserve input
  order when the protocol or caller expects results aligned with identifiers.

Avoid returning every private or remote object as a suggestion. Bound queries
for latency, privacy, and relevance.

## Separate schemas from entities

`AppEntity` and `IndexedEntity` are useful without an App Schema. Apply
`@AppEntity(schema:)` only when a current system entity schema genuinely
describes the content and the required properties can be represented honestly.
If no TV-tracking, collection, or other matching domain exists, keep the
app-specific entity instead of claiming a player, book, photo, or file type.

Never guess that an intent domain also contains an entity schema. Inspect the
domain page and the current `AppSchema` API; some domains define actions only.

## Index lifecycle

Define:

- initial indexing and whether it lies on startup's critical path;
- incremental insert or update after app-owned writes;
- deletion when content is removed, unfollowed, or scoped to another account;
- account-switch and sign-out cleanup;
- bounded bulk replacement and retry behavior;
- failures as best-effort or user-visible according to product importance.

Delete only the app-owned entity type or named domain. Never use an all-items
Spotlight deletion as a convenient reset for one feature.
