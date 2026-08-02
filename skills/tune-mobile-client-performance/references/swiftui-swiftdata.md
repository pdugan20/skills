# SwiftUI and SwiftData Performance Triage

Use this reference after the core workflow selects a native Apple client. These
are routing cues for evidence, not a generic optimization checklist.

## Observation and identity

- Count observation ownership at the screen and row levels. A small number of
  property wrappers in one row can become hundreds of live subscriptions in a
  large list.
- Prefer one screen-level observation of data already needed for the feature,
  then build stable value projections or lookup maps for rows. Preserve
  reactivity; do not replace observation with stale ad hoc caches.
- Use domain identity for `List` and `ForEach`. Index identity makes insertion,
  filtering, and publication churn appear as unrelated row changes.
- Avoid mutating an observed model merely to hydrate a visible row during
  scroll. When appropriate, publish view-local preparation or batch model
  changes outside the critical window.
- Use SwiftUI Instruments update groups and causes, render/update counts, and
  Time Profiler over the exact hitch window to distinguish broad invalidation
  from expensive work inside one valid update.

## Images and first paint

- Separate network completion, image decode, and first draw. `UIImage(data:)`
  can defer decode until rendering even when download and cache work were async.
- Match decode target to rendered size and use the same target in preload and
  read paths when target size participates in the cache key.
- Compare cold and warm memory/disk-cache behavior before ranking image work.
  Bound prefetch windows and check eviction, cancellation, and memory cost.

## Fetching and publication

- Actor hops and observable assignments can place otherwise fast work on the
  main thread. Locate publication, not merely the async function declaration.
- Fetch independent secondary data concurrently when appropriate, but avoid
  publishing each result into a visible transition separately. Prepare while
  hidden and apply one coherent state when that preserves the product contract.
- Awaiting a slow request does not block the main thread. Confirm that the
  request lies on the visible critical path before changing client or server
  behavior.

## Build and observability differences

- Compare Debug, Release-device, internal TestFlight, and App Store settings.
  Compiler behavior, flags, diagnostics, tracing, profiling, replay, and logging
  can differ materially.
- Error-triggered session replay can still maintain a rolling capture buffer.
  Isolate replay without removing unrelated tracing when testing its overhead.
- Use one-shot signposts for milestones. Remove temporary high-frequency logs
  and unusually low stall thresholds after they answer the question.

## Source note

The observation, identity, image, and Instruments intake categories were
cross-checked against Dimillian's MIT-licensed
[`swiftui-performance-audit`](https://github.com/Dimillian/Skills/tree/main/swiftui-performance-audit).
This reference is independently written around causal gaps found across
repeated SwiftUI performance investigations; consult current Apple Developer
documentation for exact Instruments and platform APIs.
