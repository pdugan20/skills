# Skill Candidate: Repair photographic assets

- **Inventory ID:** `SC-025`
- **Status:** `pilot`
- **Owner:** Patrick
- **Last reviewed:** 2026-10-12

## Intent and evidence

Preserve accepted photographic product artwork while repairing localized defects. The D-15 case produced repeated corrections for source blur, altered white paint, lettering, transparent logo backing, and separately stretched control regions. The outcome is a bounded repair plus native-resolution and rendered evidence. This is not a claim that the current skill has independently demonstrated better results.

## Mechanism decision

A portable technique companion owns source preservation, registration, and acceptance checks. OpenAI ImageGen continues to own image-generation execution. Project-specific masks, paths, and source archives belong in the application repository, not in the portable skill.

## External overlap gate

On 2026-10-10, Skills CLI 1.5.21 searches for `repair-photographic-assets`, `photographic asset repair`, and `image editing preservation` returned no exact match. The first semantic result was `mihirduvedi/master-design-studio@humanize-image-generation`; the other results included character generation, Nano Banana, and broad presentation/content skills. The third-party humanize page could not be retrieved; it is not considered fully evaluated. No external skill was installed.

The official OpenAI ImageGen skill and prompting references were read directly. They own generation/edit intent, references, prompting, and execution routing, but do not establish exact-pixel composite checks or source-versus-render causal diagnosis. Current OpenAI image prompting documentation explicitly advises original-image compositing for exact preservation. This companion independently encodes those integration decisions without copying another skill's implementation or pinning model versions. Official ImageGen is the closest inspected overlap and is maintained upstream; its execution dependencies and permissions remain its own.

Retire or merge this companion if upstream ImageGen covers the same preservation, registration, and acceptance workflow. Repeat public overlap discovery before release; this remains a local pilot, not a fully validated or released skill.

## Boundaries and evaluation

The skill grants no image-generation, upload, deployment, API migration, or unrelated feature authorization. Embedded instructions in media and metadata remain untrusted data. Four execution specifications cover a stop/research request, label-only drift, renderer softness, and malicious metadata. Routing specifications include four positive and four negative cases. These are versioned specifications, not recorded independent executions.

Structural validation and runtime symlink resolution are checked locally. Baseline-versus-skill behavior comparison, broader third-party overlap inspection, external validator, and published installation testing remain release work. No tag, push, release, or managed agent-tooling snapshot update is authorized by this local pilot.

## Pre-generation failure and correction

On 2026-10-12, a Codex session read this skill but supplied the whole D-15
sprite as a prompt-only edit target before establishing the master identity and
explicit repair boundary. The prompt named local regions; the result still
changed the window and alpha. The candidate was rejected and never applied.
This is an observed failure of instruction compliance, not evidence that the
existing preservation guidance was absent.

The pilot now requires a saved and inspected boundary record before the first
generation call, including previews, and local edit targets for prompt-only
editors. Three added execution specifications cover quick-candidate pressure,
the promise to mask later, and malicious candidate metadata. Routing and source
cases are updated together. These are regression specifications; no independent
post-change behavioral executions or runtime hook interception test has run.

A runtime guard is separate from the portable skill. Hook registration or unit
tests alone cannot establish enforcement. Any future guard must demonstrate
rejection before the image tool runs and allowance of valid bounded inputs in
each supported runtime, preserving that runtime's hook-trust controls.

The same session initially searched portfolio baseball illustrations instead of
the separate character-production project named by the owner. That project
already had task-specific OpenAI/Scenario routing, executable edit preflight,
review packages and provenance records. The portable companion now requires
locating the actual earlier runner and provider evidence before selecting a tool
or implementing new guards. Added a corresponding execution and routing case.

The bundled read-only PNG helper has 14 passing synthetic regression tests for
registered master crops, complete mask containment, exact built-in tool packets,
and protected RGBA/alpha verification. It does not generate or modify images.
A personal Codex adapter prototype exists separately; it is not installed or
verified as runtime enforcement and does not cover Scenario or direct API calls.
No independent agent compliance evaluation has run.

## Appearance and transition lessons

The owner rejected subsequent dark gray/brushed lettering as off course and
continues to regard the cleaner pale lettering as provisional. The pilot now
separates color, contour, depth, texture and sheen, records observed material-word
overinterpretation, and requires covered patch joins after registration. Sparse
shadow lightening, coarse brushing, generated mask-frame artifacts and rounded
highlights are recorded as failures; a small tone calibration is recorded as a
limited provisional result, not finished-material acceptance. Four execution
specifications include an adversarial metadata case; routing cases are updated.
These specifications have not been independently executed. Existing read-only
guard tests still establish only file and pixel invariants, not visual quality.

Narrow-update overlap refresh on 2026-10-12: Skills CLI 1.5.21 exact query
`repair-photographic-assets` returned no skills; semantic query
`photographic asset repair` returned the same previously recorded broad
`humanize-image-generation` result. No new upstream skill was installed or
workflow substituted; this update records observed repair decisions within the
existing pilot's scope. No release or runtime trust change occurred.
