# React Native and Expo Performance Triage

Use this reference after the core workflow selects a React Native or Expo
client. Locate whether React/JavaScript work, UI-thread motion, native layout,
or network completion owns the first visible miss.

## Motion and element ownership

- Identify the one progress value or platform mechanism that should own the
  transition. Reuse one continuous field, surface, or element when possible;
  coordinating two lookalikes often preserves a first-frame geometry jump.
- Derive dependent entrances from the mechanism that displaces their content.
  Do not add a second timer, distance, or easing curve for the same motion.
- Let the keyboard-aware scroll mechanism own composer clearance. A second
  anchor-preservation or translation mechanism can fight it even when both are
  individually smooth.
- Reduced motion should preserve state continuity while reducing displacement.

## React, JavaScript, and UI-thread work

- Determine whether motion runs on the UI thread or depends on JavaScript.
  UI-thread animation can remain smooth while React mounts or JS work delays
  content; it can also reveal stale or wrong first-frame geometry.
- Inspect what mounts when the transition begins. Reuse the moving element and
  defer expensive results, lists, or panels until travel finishes when they are
  not part of the visible contract.
- Narrow Zustand or other store selectors to the fields the open surface uses.
  A broad subscription can re-render an active thread because unrelated inbox
  state changed.
- Use React Profiler and bounded render counts over the same interaction. Avoid
  applying web DOM/CSS performance rules to native views without checking the
  actual renderer and animation mechanism.

## Layout and first visibility

- Geometry measured after mount cannot repair the first visible frame. When the
  contract requires correct first paint, prepare or preload enough state before
  navigation reveals the destination.
- Bound preload by the initiating gesture or likely destination, cancel stale
  work, and avoid turning every touch into an unbounded cache.
- Distinguish a late mount from a deliberately low opacity or delayed reveal;
  both look like content arriving late but have different owners.

## Network and publication

- Profile request time separately from JavaScript work, React commit, and state
  publication. A slow endpoint matters only when required content blocks the
  visible contract.
- Preserve truthful loading behavior when the endpoint dominates. Hand server
  optimization to its repository instead of masking latency with client churn.
- Batch related visible publication where safe; several small store updates can
  interrupt a transition even when fetches ran concurrently.

## Verification

- Step the same short frame window and compare the first moving frame, geometry,
  content availability, and settled state.
- Test interrupted and reversed transitions, warm and cold preparation, and the
  relevant keyboard state.
- Use aggregate FPS only as supporting evidence. A two-frame freeze or wrong
  first paint can be important while the average remains high.
