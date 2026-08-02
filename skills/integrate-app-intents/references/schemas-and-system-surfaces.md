# Schemas and system surfaces

## App Schema gate

Use current official Apple documentation and Xcode's schema snippets. As of the
WWDC26 App Schema API, new integrations use `@AppIntent(schema:)`,
`@AppEntity(schema:)`, and `@AppEnum(schema:)`; older
`@AssistantIntent`, `@AssistantEntity`, and `AssistantSchemas` guidance is
deprecated. Recheck the active SDK rather than treating this note as permanent
API truth.

For each candidate schema:

1. Confirm the domain describes the app's actual role.
2. Confirm the schema's generated protocol and required properties.
3. Confirm any companion schema group Xcode requires.
4. Map the schema parameters and result to existing app logic.
5. Leave optional schema properties nil only when the system contract permits.
6. Build and inspect metadata diagnostics before planning broader adoption.

Some domains require complete groups, not cherry-picked actions. A build Fix-It
for a companion schema is a product-contract warning, not boilerplate to evade.

The system domain can offer open and in-app search actions without supplying a
matching entity schema for every app-specific noun. A search schema requires a
real searchable destination and criteria handling; it is not a semantic label
to attach to unrelated read intents.

### Current system-search checkpoint

As of the WWDC26 beta documentation, a general in-app search action uses
`@AppIntent(schema: .system.searchInApp)` with
`ShowInAppSearchResultsIntent`, `static searchScopes`, and a
`StringSearchCriteria` value. The older `.system.search` spelling is
deprecated. Choose an honest scope such as `.tv` for structured television
content or `.general` for an app-wide search. The system open adapter uses
`@AppIntent(schema: .system.open)` with `OpenIntent`.

Treat these spellings as a migration checkpoint, not timeless source code.
Reconfirm them in the active SDK's generated completion and current domain
page before implementation, especially while the API is beta.

## Registration and rollout

Schema macros contribute metadata at build time. A remote or local runtime flag
inside `perform()` can reject execution, but it cannot reliably remove the
action already advertised to Siri or Shortcuts. Therefore:

- do not claim a runtime flag makes schema metadata ship dark;
- do not put a default-off guard into an existing intent if that breaks its
  older App Shortcut or widget path;
- prefer branch, build, TestFlight cohort, or OS availability staging for new
  metadata;
- when a runtime denial is necessary, give it an honest user-facing error and
  treat continued discoverability as a known degraded state;
- isolate schema-specific wrappers only when duplicating the adapter does not
  create competing behavior or identity.

## Shortcuts, Spotlight, and Siri

- Keep App Shortcut phrases natural, localized, and compliant with the current
  app-name placeholder requirements.
- Avoid enumerating every phrase as a substitute for correct parameters and
  entity queries.
- Test system-spoken dialogs separately from compact visual representations.
- Use Spotlight for indexed content and link each result back through the
  canonical open route.
- Test Siri after structured Shortcuts and Spotlight behavior is sound; natural
  language adds resolution, disambiguation, permissions, and device state.

## Snippets and context

- A result view is not automatically an interactive snippet. Use the current
  interactive intent host when controls must execute intents.
- Give snippet views concrete, bounded values and prepared artwork when they do
  not inherit the app's dependency or image-loading environment.
- On current systems, attach an `EntityIdentifier` to the stable view that
  actually renders the entity; avoid a transient child that can scroll away.
- Keep `NSUserActivity.appEntityIdentifier` as an earlier-OS or existing
  activity-handoff fallback when appropriate.
- Use per-view entity identifiers or UI elements for multiple meaningful
  visible items.
- Annotate only content that supports a real request such as open, share,
  compare, or act on “this”; more annotations are not inherently better.

Keep accessibility, redaction, authentication, and destructive confirmation
appropriate for a surface that may appear outside the app.
