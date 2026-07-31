---
name: analyze-ui-video
license: MIT
description: Use when a user supplies a UI screen recording or video and asks to dissect, diagnose, reverse engineer, compare expected and observed behavior, or explain how it could map to a target repository. Do not use for static screenshots, code-only motion review, video editing, or implementation requests without video evidence.
---

# Analyze UI video

Treat rendered frames as temporal ground truth. Observe the recording before
forming a code theory, then test the theory against the target repository.

Keep the analysis read-only unless the user also asks to fix or build the
behavior. Keep recordings and derived frames local and uncommitted by default.

## Establish the question

Identify what is available:

- recording and target repository;
- relevant interaction, time range, or screen region;
- preceding context and triggering action;
- expected behavior or reference intent.

Classify the request as visual-bug diagnosis, reference reconstruction, or
ambiguous. Missing context does not block inspection. State what remains unknown
instead of inventing a defect or intended behavior.

## Create temporal evidence

Use the bundled [video frame helper](./scripts/video_frames.py). Run `--help` for
all parameters.

1. Run `--probe` to confirm dimensions, duration, observed and nominal frame
   rates, orientation, and a useful crop.
2. Run `--overview` when the relevant moment is unknown. It caps the sheet at 30
   cells by default.
3. Run a detail sheet for the selected window. Use the observed frame rate for
   very short motion and 4–15 fps for slower scrolling or multi-second events.
4. Crop tightly enough to see the behavior while retaining the trigger, parent
   movement, and neighboring layout needed to interpret it.
5. Read the PNG row-major and use its JSON manifest for absolute timestamps.

The helper distinguishes a container's nominal frame rate from the observed
average. Preserve that distinction when reporting timing. If deterministic
extraction is unavailable, disclose that the analysis used direct playback and
avoid frame-precise claims.

## Narrate before explaining

Describe the visible sequence before reading implementation code:

1. stable starting state;
2. initiating visible event;
3. intermediate states;
4. first defining change or divergence;
5. settled state and any persistent artifact.

Separate three evidence classes:

- **Observed:** directly visible in frames or measured from media metadata.
- **Corroborated:** matched to repository code, platform behavior, or another
  authoritative artifact.
- **Inferred:** plausible internal behavior that the recording cannot prove.

Read [analysis cues](./references/analysis-cues.md) when ownership, gesture
timing, animation phases, layout, or capture artifacts are subtle.

## Follow the relevant branch

### Visual-bug diagnosis

State expected versus observed behavior. Identify the earliest visible
divergence, then rank a small set of hypotheses. For each hypothesis, name the
recording or repository evidence that supports it and the smallest check that
would confirm or reject it. Check source-media artifacts before proposing global
layout or rendering changes.

### Reference reconstruction

Describe the state sequence, moving layers, spatial continuity, clipping and
masking, opacity, timing, gesture relationship, and settling behavior. Separate
platform-owned motion from app-authored motion. Reconstruct the observable
contract, not a competitor's unknowable private implementation.

## Audit the target repository

Inspect repository instructions, runtime and supported platform versions,
component and state ownership, layout hierarchy, existing motion primitives,
media pipeline, and nearby conventions. Hold API or architecture choices as
hypotheses until this inspection is complete.

For bugs, trace the first divergence to the narrowest relevant source boundary.
For references, recommend the closest native or project-consistent mechanism
that reproduces the observed contract.

## Report the result

Return these sections in order:

1. **Finding:** the shortest defensible conclusion, including whether a defect
   is actually visible.
2. **Evidence window:** recording metadata, analyzed interval and crop, and any
   temporal-resolution limitation.
3. **Observed sequence:** timestamped facts before interpretation.
4. **Expected behavior or reconstruction:** the comparison target and visible
   contract.
5. **Repository mapping:** relevant stack, files, state/layout ownership, and
   existing primitives.
6. **Hypotheses and confidence:** corroborated facts, ranked inferences, and
   unresolved unknowns.
7. **Next steps:** the smallest confirming check or implementation approach,
   with implementation left pending unless requested.

When implementation is requested, change one relevant variable at a time,
record the same interaction again, and compare the new evidence before claiming
the behavior is fixed or reproduced.
