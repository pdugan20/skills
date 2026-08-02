# Execution and verification

## Process, actor, and dependency boundaries

App Intents may execute after a background or cold launch, before ordinary
screen setup, or while another system process hosts the visible result.

- Register or resolve dependencies in a lifecycle that exists for every
  supported execution mode.
- Do not store non-Sendable repositories, model contexts, or UI routers inside
  a Sendable intent value. Resolve them through actor-isolated computed access,
  an App Intents dependency mechanism verified in the target lifecycle, or a
  small testable action adapter.
- Keep persistence reads and mutations on the actor that owns the store.
- Return value snapshots across the boundary rather than persistence objects.
- Use the same repository mutation path as the app. Direct writes can skip
  sync, validation, pending-write, conflict, analytics, or cache behavior.

## Open and foreground handoff

Route open-style intents through the canonical external-entry service.

- Deliver the same domain URL or route representation used by universal links
  and notifications.
- Queue or cache the route until the scene is ready instead of posting a
  one-shot event that a cold app can miss.
- Test warm foreground, cold terminated, background, signed-out, stale entity,
  and unavailable destination states.
- Use the current open-style intent and supported execution-mode APIs rather
  than obsolete foreground switches from old samples.

## Availability and capability

Separate:

1. compile/link availability for the SDK symbol;
2. OS runtime availability at a shared call site;
3. device, region, language, account, permission, or model capability;
4. the product's rollout decision.

Use declaration availability for new protocol conformances or macros and
runtime availability around shared callers. Preserve older App Shortcuts or
other fallback paths when the new system surface is additive.

## Verification ladder

### Unit and metadata

- Unit-test entity IDs, display values, query ordering and filtering, domain
  mapping, repository calls, errors, and actor-safe seams.
- Compile every app, widget, control, and test target that consumes metadata.
- Treat metadata extraction warnings and schema Fix-Its as integration evidence.

### AppIntentsTesting

Current AppIntentsTesting runs out-of-process from a standard UI-testing bundle.
It locates the app by bundle identifier and addresses intents, entities, and
parameters by metadata names rather than importing app code.

- Configure the runner and app with the signing relationship the framework
  requires.
- Seed deterministic synthetic data through a `#if DEBUG`,
  `isDiscoverable = false` test-only intent when appropriate.
- Test intent execution, returned values, identifier and string queries,
  Spotlight indexing, and view annotations through the framework.
- Keep each test self-contained; app and test runner do not share process state.
- Do not call direct `perform()` unit tests “AppIntentsTesting.”
- Do not assume a signing-disabled Mac Catalyst suite can substitute for the
  UI-test bundle merely because the framework is importable on Catalyst.

### Structured and device acceptance

- Use Shortcuts to inspect parameters, titles, results, and composition.
- Use Spotlight to verify indexing, deletion, ranking inputs, and canonical
  routes.
- Use a supported physical device for Siri wording, disambiguation, speech,
  permissions, personal context, semantic search, background execution, and
  cold-start routing.
- Test every destructive or private action with the intended confirmation and
  authentication state.

Report Simulator, Catalyst, AppIntentsTesting, and physical-device evidence
separately. Each proves a different layer.
