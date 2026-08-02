# iOS Development Capability Evaluation

- **Inventory IDs:** `SC-017`, `SC-018`, `SC-019`, `SC-020`
- **Last reviewed:** 2026-08-02
- **Scope:** Four independent iOS capabilities. They are not one proposed skill
  and are not part of `tune-mobile-client-performance` merely because one
  external plugin bundles them together.

## Decision summary

| ID | Capability | Decision | Status |
| --- | --- | --- | --- |
| `SC-017` | Structured Apple build, Simulator, and runtime debugging | Run a pinned Codex-first XcodeBuildMCP pilot; keep computer use as its visual complement and Instruments as the profiler | `pilot` |
| `SC-018` | Memgraph leak and retained-growth investigation | Wait for one real lifetime bug before authoring or cataloging a workflow | `needs-evidence` |
| `SC-019` | Focused iOS CPU profiling with ETTrace | Keep as a task-level fallback after Instruments or `xctrace`, not a managed dependency | `needs-evidence` |
| `SC-020` | App Intents feature integration | Use the validated compact first-party skill derived from NextUp and a three-way forward comparison; do not import the external skills | `validated` |

## Shared evidence

The local iOS projects currently combine project scripts, raw `xcodebuild` or
`simctl`, XCUITest where appropriate, and screen-driven Simulator control.
Computer use is installed and works well for visual judgment, simulator chrome,
permissions, gestures, and custom rendered content. It does not provide a
semantic control tree, deterministic build context, structured build results,
runtime logs, or LLDB state.

OpenAI's MIT-licensed `build-ios-apps` v0.1.2 plugin is available but remains
uninstalled. It combines five skills derived from Dimillian's MIT collection
with App Intents, Memgraph, ETTrace, Simulator browser, and XcodeBuildMCP
capabilities. The bundle is not the right adoption unit:

- its MCP manifest launches `xcodebuildmcp@latest`, and its browser skill uses
  `serve-sim@latest`;
- it contains no tests and two author-machine source paths;
- its debugger skill names commands that no longer match XcodeBuildMCP 2.7.0;
- its App Intents templates repeatedly use `openAppWhenRun`, which current Apple
  documentation marks deprecated in favor of `supportedModes`; and
- its ETTrace workflow defaults to v1.1.0 even though the latest upstream tag is
  v1.1.1.

Do not install or fork the plugin as a unit. Evaluate its differentiated
capabilities independently and preserve upstream provenance.

## SC-017: Structured Apple runtime control

### Structured runtime outcome

Give an agent deterministic Apple project discovery, build, test, launch,
Simulator interaction, log evidence, and LLDB inspection without relying on
screen coordinates or reconstructing raw command pipelines each time.

### XcodeBuildMCP evidence

[XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP) is MIT-licensed,
actively maintained, and released v2.7.0 on 2026-07-23. That release was still
the latest on review day, and its repository was active on 2026-08-02. The
project publishes separate official skills for its MCP and CLI modes.

Pinned `xcodebuildmcp@2.7.0` launched locally and exposed 72 canonical tools
across 12 workflows. A read-only CLI call against the already booted Messenger
Simulator returned a 301-element semantic UI snapshot with action references
for the composer, voice-note controls, and scroll containers. This is concrete
lift over pixel coordinates: an agent can observe once, target a semantic
element, wait for a UI predicate, and refresh after navigation. Build-and-run
also returns structured results and captures runtime log paths; the debugging
workflow exposes attach, breakpoints, stack frames, variables, and LLDB
commands.

The Codex-first pilot is now managed by `agent-tooling`. Its exact MCP manifest
enables `simulator`, `ui-automation`, and `debugging`, disables XcodeBuildMCP's
own Sentry telemetry, and pins both the npm server and official upstream skill
to v2.7.0. Runtime logging is part of the current Simulator launch workflow;
the `logging` value copied by `build-ios-apps` is not a v2.7.0 workflow.

The live Messenger exercise covered both pilot cases. The semantic snapshot
returned 301 elements and stable action references for the composer, voice-note
controls, and scroll containers. A structured launch then returned separate
runtime and OS log paths. A brief LLDB attach paused the running Expo app,
captured the main-thread stack, and detached successfully. No project source or
simulator data was changed.

The tool does not replace computer use. Semantic automation can miss poorly
labeled accessibility elements, canvas or Metal content, visual defects,
Simulator chrome, and perceptual animation quality. It also does not replace
Instruments, `xctrace`, MetricKit, or physical-device evidence for performance.

### XcodeBuildMCP decision

- **Decision:** Adopt the maintained standalone tool, not `build-ios-apps`, and
  do not write a competing Patrick skill.
- **Mechanism:** A pinned external CLI or MCP plus its official upstream skill.
- **Catalog boundary:** `agent-tooling` now has an exact standalone Codex MCP
  manifest and setup drift checks rather than disguising the server as a copied
  skill or broad plugin install.
- **Initial scope:** Simulator build/run, semantic UI automation, runtime logs,
  and LLDB. Enable only the workflows the pilot needs.
- **Pinning:** Keep the reviewed npm server and official upstream skill on the
  same exact release. Do not use `@latest` in canonical configuration.

The managed capability remains a reversible pilot. The initial semantic and
debugging exercises established that it works; the next two natural Apple tasks
should determine whether it reduces coordinate retries, manual context setup,
and ambiguous evidence in normal use. Keep computer use installed throughout
the comparison.

### XcodeBuildMCP retirement condition

Remove the managed capability if direct shell commands plus computer use remain
equally reliable on real work, or if its tool/context overhead and maintenance
cost exceed the reduction in brittle interaction and debugging steps.

## SC-018: Memgraph lifetime investigation

### Memgraph outcome

Prove why an app-owned object or allocation survives past its intended lifetime,
make the smallest ownership correction, and compare the same flow afterward.

### Memgraph evidence and limits

Apple's built-in Memory Graph Debugger and `leaks` CLI can export and inspect
`.memgraph` files. The OpenAI plugin adds a useful exact-process capture script
and a bounded summary helper. Its core rule—prove an ownership path or grouped
cycle rather than celebrating a smaller graph—is sound.

The bundled workflow is not complete enough to catalog unchanged:

- `leaks` detects unreachable allocations and root cycles, but an object kept
  alive by a legitimate root can cause persistent growth while producing zero
  reported leaks;
- the summary depends on `leaks --list`, which the local manual marks as a
  format that may be removed;
- the helper does not use the available `--diffFrom` comparison directly; and
- memgraphs and raw outputs can expose in-process content, so capture and
  sharing need an explicit privacy boundary.

The maintained `dpearson2699/swift-ios-skills@ios-memgraph-analysis` result is a
strong technical comparator because it separates unreachable leaks, reachable
growth, expected caches, and fragmentation and preserves raw artifacts. Its
PolyForm Perimeter license is not suitable for copying into or redistributing
through this public skill catalog. Use its existence as overlap evidence, not
as source material.

### Memgraph decision

- **Decision:** Do not install, copy, or author a general Memgraph skill yet.
- **Next evidence:** Use Apple's tools on the next real leak or persistent-growth
  investigation. Define the intended lifetime, preserve a before/after flow,
  distinguish unreachable leaks from reachable growth, and record where the
  agent needed reusable help.
- **Likely future mechanism:** A script-backed first-party skill only if the
  real case shows recurring capture, parsing, ownership, or comparison errors.
  Independently implement any helper against current local tool output.

### Memgraph promotion gate

Require one real app-owned lifetime defect, a successful same-flow comparison,
and a helper that preserves raw evidence and fails safely when Apple changes its
text output. A synthetic parser smoke test is not enough.

## SC-019: ETTrace CPU profiling

### ETTrace outcome

Attribute a short iOS launch or runtime interval to symbolicated CPU stacks when
the standard profiling path cannot answer the focused question.

### ETTrace evidence and limits

[ETTrace](https://github.com/EmergeTools/ETTrace) is MIT-licensed and provides a
sampling profiler with a host runner and app-linked framework. It can produce a
useful flamegraph and supports explicit flow events, launch capture, dSYMs, and
multi-thread recording. The OpenAI plugin adds careful dSYM collection and a
processed-JSON analyzer; both helpers passed local syntax and synthetic-data
checks.

The cost and maintenance boundary are substantial:

- the app target must temporarily link ETTrace, and the host runner must be
  installed separately;
- upstream warns that launching through Xcode can distort results;
- symbolication requires UUID-matched dSYMs and preserved processed JSON;
- the plugin's parser accepts one historical output shape and pins v1.1.0;
- upstream's latest tag, v1.1.1, dates to 2024-10-22, while the latest source
  changes relevant to profiling landed in April 2025; and
- Simulator CPU evidence does not prove physical-device behavior.

A more current ETTrace skill exists in `dpearson2699/swift-ios-skills`, but it
has the same restrictive PolyForm Perimeter redistribution boundary as that
repository's Memgraph skill.

### ETTrace decision

- **Decision:** Do not install ETTrace globally, fork its workflow, or add it to
  the managed catalog now.
- **Use condition:** Reach for it only when one focused CPU question remains
  unanswered after Instruments or `xctrace`, a Simulator result is relevant,
  and temporary app linkage is acceptable.
- **Method:** Run it as a bounded feature spike with exact runner/framework
  versions, verified dSYMs, one flow, one comparison contract, and explicit
  cleanup.

Promote it only if a real case produces better actionable attribution than the
standard tools and the capture remains reproducible with current Xcode.

## SC-020: App Intents integration

### App Intents outcome

Turn one or more app actions and entities into reliable Siri, Shortcuts,
Spotlight, widget, control, or other system experiences while preserving app
architecture, process and actor boundaries, routing, privacy, and testability.

### App Intents evidence and overlap

The OpenAI plugin contains useful first-pass scope guidance: start with a few
high-value actions, model only the entities the system needs, share action
logic across system surfaces, and use one explicit app-scene handoff. Its code
templates are generic and behind the current API. Apple's current
[`AppIntent`](https://developer.apple.com/documentation/appintents/appintent)
documentation deprecates `openAppWhenRun`; the plugin still teaches it as the
primary switch instead of leading with `supportedModes`, open-style intents,
and foreground continuation.

The MIT-licensed [Axiom](https://github.com/CharlesWiltgen/Axiom) collection is
far more current, including `supportedModes`, snippets, indexed entities,
visual intelligence, and newer App Schema concepts. Its App Intents reference
alone is about 1,700 lines, with separate 500- and 800-line discoverability and
App Shortcuts guides. That packaging is too large for this collection's
progressive-disclosure standard and still needs verification against current
Apple documentation during implementation.

NextUp supplies stronger real evidence than either generic guide. Its current
`AppIntents` tree is roughly 960 lines and includes value-snapshot entities
rather than SwiftData models, main-actor query and dependency boundaries,
repository-backed mutations, `OpenIntent` deep-link routing, App Shortcuts,
interactive `SnippetIntent` hosts, scoped Spotlight indexing, artwork
preparation, three Swift Testing suites, and an on-device verification contract.

This is not merely one initial implementation. The history includes the Phase
0 foundation, Phase 1 actions, Phase 2 indexing, later interactive snippets,
and durable corrections: scoping Spotlight deletion to NextUp entities, moving
reindex work off the critical startup path, routing cold and warm opens through
the shared deep-link service, preserving actor-safe test seams, fixing
system-spoken episode labels, and correcting image identity and size on system
surfaces. The repository also has a concrete next App Intents feature: the
planned App Schemas and `AppIntentsTesting` upgrade. That supplies enough real
implementation, correction, negative, and forward evidence;
waiting for an imaginary future App Intents feature would discard evidence
already present locally.

The MIT-licensed `n0an/app-intents-agent-skill` was included in the forward
comparison. It is technically strong and broad, but its large core imposes
universal App Shortcuts and dependency rules that do not fit every existing
architecture and mixes current schema guidance with deprecated Assistant
naming. The later-discovered `dpearson2699/swift-ios-skills@app-intents` result
is a strong current API comparator, but its roughly 1,800-line surface omits
AppIntentsTesting and process-aware rollout guidance and uses the restrictive
PolyForm Perimeter license. It is overlap evidence, not a catalog source.

### App Intents decision

- **Decision:** Validate the first-party `integrate-app-intents` skill. Do not
  add the OpenAI, Axiom, n0an, or dpearson skills to the managed catalog and do
  not fold App Intents into the performance skill.
- **Authority:** Use current Apple documentation for API availability and exact
  declarations, NextUp history for architectural and verification evidence,
  and external skills only as attributed comparison inputs.
- **Mechanism:** A compact composite skill with small conditional references for
  entities and data boundaries, execution and app handoff, discoverability and
  system surfaces, and testing plus on-device verification. Do not copy an API
  encyclopedia into the skill.
- **Forward feature:** NextUp's App Schemas and `AppIntentsTesting` upgrade
  confirmed the need for current SDK validation, actor and process boundaries,
  fallback preservation, and an explicit simulator-versus-device verification
  split.

### App Intents validation result

Natural requests were replayed against the historical unsafe Spotlight and
cold-deep-link states and the current App Schemas plan. The no-skill and n0an
passes were strong. The first local pass failed exact API precision by using
deprecated `.system.search`; a corrected reference and eval produced a fresh
replay using `.system.searchInApp` and `.tv` while preserving NextUp's existing
intents, phrases, account isolation, queued routing, Spotlight lifecycle,
signed XCUITest placement, and physical-device acceptance. Structural,
routing, repository, installation, and strict external validation passed.

## Catalog sequencing

1. Release and exact-tag install `tune-mobile-client-performance`
   independently.
2. Continue the pinned XcodeBuildMCP pilot in normal Apple tasks while retaining
   computer use and Instruments; do not install `build-ios-apps` to obtain it.
3. Use the validated compact `integrate-app-intents` skill on future Apple
   system-integration work; its authorized v3.2.0 release remains pending.
4. Dogfood Apple's Memgraph tooling on the next real lifetime investigation and
   ETTrace only on a focused CPU case that survives the Instruments gate.

The official XcodeBuildMCP skill and pinned Codex server pilot were added to
`agent-tooling`. The App Intents skill was authored and validated locally. No
`build-ios-apps` installation, external-skill install or fork, App Intents skill
release, or external App Intents publication was performed.
