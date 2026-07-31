# Skill Candidate: Analyze a UI Screen Recording

- **Inventory ID:** `SC-011`
- **Status:** `classified`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-31

## Intent

- **Outcome:** Turn a UI screen recording into an evidence-backed account of
  what happened over time, what likely should have happened or how a reference
  was plausibly constructed, and which repository-specific investigation or
  implementation steps should follow.
- **Trigger:** Patrick asks an agent to analyze, dissect, reverse engineer, or
  diagnose a screen recording of a competitor interaction, animation, visual
  defect, or unexpected UI behavior. He may identify a time range, interaction,
  triggering context, or expected result.
- **Artifact:** A scoped frame sequence; an observation-first temporal
  narrative; an expected-versus-observed comparison or reference
  reconstruction; clearly labeled facts, inferences, and unknowns; a target
  repository stack and implementation audit; and prioritized next steps.
- **Non-goals:** Automatically implementing a fix or imitation, reviewing
  motion code without a recording, identifying an animation from prose alone,
  comparing several original UI directions, editing the source video, or
  claiming to know a competitor's private implementation from pixels alone.

## Real evidence

The completed examples cover both branches and more than one platform. They
show that the reusable value is not simply extracting frames. It is preserving
the order of evidence: observe the actual rendered sequence, distinguish it
from an implementation theory, then test that theory against the target
repository.

### Representative examples

1. **Rendered-motion diagnosis in `nextup-ios-app`:** The repository-local
   `verify-motion` skill and `contact_sheet.py` script were created after two
   visual defects repeatedly defeated code-first reasoning. A horizontally
   overflowing hero looked impossible from the local frame math, but the
   extracted frames led back to a cloned view that had lost an ancestor
   `GeometryReader`. In another case, three plausible theories for a checkmark
   separating from its circle were wrong; the frames showed that the incoming
   glyph was already at its final position while its container was still
   interpolating. The durable correction was to narrate frames before
   theorizing.
2. **Competitor transition reconstruction in `audiobook-ios`:** A recording of
   a mini-player expanding into a full player was extracted at 60 fps. The
   teardown identified the roughly 150 ms state sequence, whole-surface scale
   and translation, temporary translucency, and leading artwork opacity. A
   repository and platform audit then mapped the behavior to the native iOS 18
   navigation zoom transition and matched transition source rather than a
   custom animation system.
3. **Source-video artifact diagnosis in `pat-portfolio`:** A thin sliver beside
   a composited phone bezel could have prompted a global layout or mask change.
   Extracting and sampling source frames instead showed anomalously bright edge
   pixels introduced by capture and anti-aliasing. The safe fix was a minimal,
   one-sided crop for the affected recording, leaving the shared composition
   system unchanged.

### Repeated corrections

- Scope the relevant interaction and inspect the frames before explaining what
  the UI framework should have rendered. Code-first theories repeatedly fit
  the wrong evidence.
- State what is visibly present, absent, moving, clipping, or changing before
  assigning a cause. Keep observation, implementation inference, and unknowns
  distinct.
- Use a coarse pass to locate an event and a native-rate or otherwise detailed
  pass to understand it. A single arbitrary screenshot or evenly sampled long
  recording can miss the first divergent frame.
- Crop to the changing region when detail matters, but retain enough context to
  see the triggering gesture, parent movement, or neighboring layout.
- Audit the actual target repository, runtime, deployment target, component
  structure, and existing motion primitives before recommending APIs or an
  architecture.
- Treat a competitor reconstruction as plausible, not proven. Recommend the
  closest native or project-consistent implementation that reproduces the
  observable behavior rather than asserting private internals.
- Keep diagnosis and implementation authorization separate. The default result
  is analysis and proposed next steps; code changes begin only when requested.

### Sensitive material

Recordings may contain private messages, account details, customer data,
notifications, unreleased interfaces, or competitor material. Analyze local
files without publishing or committing raw recordings. Crop, redact, or use
sanitized derived frames when an artifact must be retained, and record only the
minimum safe summary in shared documentation.

## Mechanism decision

- **Decision:** Create one portable `analyze-ui-video` skill with a generalized
  frame-probing and contact-sheet script. Keep reference reconstruction and
  visual-bug diagnosis as branches selected after the shared intake and
  observation stages.
- **Classification:** Composite skill with a deterministic script.
- **Rationale:** The temporal analysis, uncertainty discipline, repository
  audit, and branch-specific judgment need agent reasoning, while metadata
  probing, cropping, frame sampling, timestamps, and contact-sheet generation
  are deterministic and repeatedly recreated. Separate competitor, bug,
  mobile, web, and animation skills would duplicate the core method and force
  routing decisions before the evidence is understood.
- **Scope:** Broadly portable across native mobile, web, desktop, and
  cross-platform repositories. Platform implementation knowledge remains in
  the target repository or other focused skills.

The common analysis should proceed in this order:

1. Confirm the recording, target repository, relevant interaction or time
   window, preceding context, and expected behavior when supplied. Do not block
   on missing context that can be discovered from the recording and repository;
   label the resulting uncertainty instead.
2. Probe duration, frame rate, dimensions, and orientation. Make a coarse
   overview when the relevant moment is unknown, then a detailed sequence at an
   appropriate sample rate. Crop only after retaining enough contextual frames
   to understand the trigger.
3. Narrate the visible state sequence before proposing causes: stable state,
   initiating event, intermediate states, first divergence or defining motion,
   settling state, and any persistent artifact.
4. Choose the branch:
   - **Visual-bug diagnosis:** compare expected and observed behavior, identify
     the earliest visible divergence, and form ranked hypotheses tied to
     evidence that could confirm or reject them.
   - **Reference reconstruction:** describe the state model, moving layers,
     continuity, timing, easing or spring character, opacity and masking,
     gesture relationship, and the confidence of each inference.
5. Inspect the target repository's stack, supported platform versions,
   component boundaries, state ownership, layout hierarchy, existing motion
   conventions, and relevant implementation. Hold API and architecture choices
   as hypotheses until this inspection is complete.
6. Report observations, expected behavior or reconstruction, repository
   findings, hypotheses and confidence, and the smallest useful next steps. If
   Patrick asks to fix or build it, use this analysis as evidence for a separate
   implementation pass and verify the result against a new recording.

## Reusable contents

- **Instructions:** Intake, event scoping, coarse-to-fine frame analysis,
  observation-before-theory discipline, bug and reference branches,
  repository audit, confidence labeling, reporting, and implementation handoff.
- **Scripts:** Generalize the existing platform-neutral `contact_sheet.py` from
  `nextup-ios-app` to probe video metadata, emit representative frames or a
  contact sheet, support coarse and detailed windows and crops, and make frame
  timestamps unambiguous. Do not copy SwiftUI-specific diagnoses into the
  script.
- **References:** A compact temporal-observation checklist and branch-specific
  guidance for visual defects and reference reconstruction. Platform API
  catalogs should remain separate and be loaded only when relevant.
- **Assets:** An optional analysis report template only if forward evaluation
  shows that free-form reports omit important evidence boundaries.
- **Dependencies:** Local access to the recording and target repository;
  `ffmpeg` and `ffprobe` for deterministic extraction. No network or paid client
  is required for the core analysis.

## Safety and boundaries

- Treat recordings as potentially sensitive local artifacts. Do not upload,
  publish, commit, or retain them outside an appropriate temporary or ignored
  location without explicit authorization.
- Never expose credentials, personal data, private notifications, or customer
  content in contact sheets, logs, eval fixtures, or reports.
- Do not infer accessibility semantics, exact durations below the recording's
  temporal resolution, hidden state, source code, or proprietary algorithms
  solely from pixels.
- Do not broaden a localized visual diagnosis into architecture changes until
  source-frame, layout, state, and repository evidence rule out a narrower
  cause.
- `review-animations` owns a craft review of known motion code;
  `animation-vocabulary` helps name an effect; `code-native-ui-ideation` owns
  original UI direction comparison; `feature-spike` owns a bounded runnable
  investment decision. None replaces recording-led temporal analysis.
- Analysis is read-only by default. Building or fixing the behavior requires an
  explicit implementation request and the target repository's normal safety
  and verification rules.

## Evaluation plan

### Execution

1. An iOS recording with a brief symbol/container separation should isolate
   the native-rate window, narrate the first divergent frame before proposing a
   cause, inspect the SwiftUI hierarchy, rank falsifiable hypotheses, and stop
   before editing code.
2. A web recording with a one-frame clipping or edge artifact should distinguish
   source-media pixels from CSS layout and compositing, inspect the relevant
   media pipeline, and recommend the narrowest confirming check before a global
   fix.
3. A competitor mobile transition should reconstruct observable states,
   timing, layer relationships, and gesture continuity; label internal details
   as inferences; inspect the target app's platform and deployment target; and
   propose native or project-consistent implementation options.
4. A long recording with only a user-described interaction should make a coarse
   overview, narrow to the relevant interval, and produce a detailed sequence
   without treating irrelevant frames as equal evidence.
5. A recording with insufficient resolution or missing precondition context
   should state what can and cannot be concluded and request or recommend the
   smallest better capture rather than fabricating precision.

### Routing

- **Should trigger:** “Dissect this competitor animation,” “look at this screen
  recording and tell me why the card jumps,” “what happens between these two
  states in this video,” “compare what I expected with what the recording
  shows,” “analyze the clipping around 12 seconds,” and “how could we build a
  similar transition in this repository?”
- **Should not trigger:** A static screenshot review, a request to invent and
  compare original UI directions, a code-only animation audit, a prose request
  to name an effect, video editing or transcoding for publication, ordinary
  non-visual bug diagnosis, or an already approved implementation task with no
  recording to analyze.

### Baseline

Use no skill across both branches. Also compare the visual-bug cases with the
repository-local `verify-motion` skill as strong prior art. The candidate earns
its place only if fresh-context responses consistently inspect video evidence
before theorizing, preserve observation-versus-inference boundaries, scope long
recordings efficiently, audit the target repository before prescribing an
implementation, and remain useful for both reference and bug recordings
without becoming platform-specific.

The first forward evaluation should use Patrick's next real representative
recording. Existing written teardowns and diagnosis histories justify the
classification and initial contents, but a real video is necessary to validate
the media intake, extraction artifacts, and usefulness of the final report.

## Definition of done

- [x] Mechanism and scope are classified.
- [ ] Reusable resources are implemented and referenced.
- [ ] Structural and repository validation passes.
- [ ] Execution and routing eval coverage passes.
- [ ] Representative with-skill and baseline results are reviewed.
- [ ] Intended Claude, Codex, and other claimed integrations are checked.
- [ ] Version, changelog, distribution metadata, and installation are verified.
- [x] Inventory status and initial evidence are updated.
