# Skill Candidate: Animate watercolor

- **Inventory ID:** `SC-024`
- **Status:** `pilot`
- **Owner:** Patrick
- **Last reviewed:** 2026-10-01

## Intent and mechanism

When extending an existing watercolor family, establish suitable still artwork
before implementation. Then produce its authored reveal in a reusable website system,
with believable material arrival and optional quiet ambient motion. Typical
requests include “make this paint in,” “match the existing watercolor,” “the
finished detail flashes,” and “white fabric fades in on dark mode.” The output
is reviewable still art when needed, then runnable code, a material/brush score,
review evidence and a saved preset. Standalone image generation remains outside
the trigger; the still phase supports an existing painting family.

This is a **technique skill**: specialized visual judgment and non-obvious
compositing knowledge recur, while authoring paths and masks vary by subject.
Deterministic rendering remains in each project's tested engine; the skill does
not carry a second renderer or prescribe one framework. Image-only generation,
general UI easing, generative-art compositions and video stylization are outside
its trigger. The user expressly requested creating this skill in this repository.

## Real evidence

The completed local `pat-portfolio` work supplies source evidence:

- Ichiro's shared pigment renderer, authored figure/head scores and uniform
  coverage: opaque white support must follow contacts, not a global fade.
- Rainier's lid, bands, lettering, foam and foot corrections: inaccurate early
  geometry and missing coverage made the final source reconciliation jarring.
- Source texture revealed too early was painted over and returned later.
  Overlapping contacts with prepared predecessor states exposed completed marks.
- Glass gesture timing at `65f6d46`: score seconds mapped into about 241ms for
  important first passes inside a 2.4s paint duration.
- Replay callback cancellation and continuous bubbles / one-way condensation:
  old elapsed time could instantly finish a restarted painting.
- Shared homepage consolidation at `c4fce77`: subject registry, separate material
  adapters and one rail/player; 285 tests, repository lint and production build.
- The subsequent iPod exploration repeatedly substituted procedural SVG patches,
  grain and gradients for credible watercolor artwork. The user could not judge
  the proposed art direction; later variants added false depth and cropped cables
  opposite the intended entrance. This directly motivated the explicit still-art
  stage, medium/quality diagnosis and entrance-aware accessory guidance.

Project documentation includes `docs/projects/personal-illustrations/PROGRESS.md`,
`SHARED-STUDIO.md` and saved frames. These paths locate evidence in that project;
the distributed skill has no dependency on private paths or source assets.
No credentials, private reference photos or raw conversation transcript are
included. The numerical object proportions are ordinary supplied measurements.

## External overlap gate

Live skills.sh searches on 2026-10-01 used Skills CLI 1.5.21:

- Exact: `animate-watercolor`.
- Semantic: `watercolor brush reveal animation`.
- Adjacent: `canvas animation`.
- Subproblem: `transparent image compositing`.

The exact search returned general animation/design skills, not an exact owner.
The semantic search returned algorithmic-art, msw-painter, imagegen and others.
The adjacent query returned hyperframes, review-animations and canvas-design.
The transparency query returned background-removal and image-generation helpers.
Names and search ranks were not treated as overlap proof. Closest bodies were
read with `skills use` as research data, not invoked as instructions:

| Skill | Inspected scope and boundary | Maintenance / license / dependencies |
| --- | --- | --- |
| `emilkowalski/skills@review-animations` | Reviews general interaction motion; does not implement a watercolor score. Its generic sub-300ms and transform/opacity preference is not a substitute for authored painting. | GitHub API: pushed 2026-09-23, unarchived, MIT. Portable text with linked standards; review-specific output contract. |
| `anthropics/skills@algorithmic-art` | Creates original p5.js generative philosophies and viewers, explicitly unlike animating a fixed accepted illustration. | Pushed 2026-09-29, unarchived. Body refers to its own LICENSE.txt; API does not classify a repository license. Requires p5.js workflow. No copying. |
| `msw-git/msw-ai-coding-plugins-official@msw-painter` | Pixel/cartoon sprite drawing and resource registration; explicitly excludes animation. | Pushed 2026-07-29, unarchived; repository license unclassified. MapleStory search/upload tools and sprite identifiers are runtime dependencies. No copying or execution. |

Decision: independently author a narrow technique using the actual portfolio
failures. Existing animation review and image-generation skills can serve
separate requested phases; neither owns material coverage, score-time mapping
and source-fidelity arrival in an accepted watercolor. No upstream text or code
was copied. No researched tool is a required dependency.

The pre-validation repeat surfaced an additional illustration-style guide; its
body and maintenance/license evidence are recorded in
[Validation](animate-watercolor-validation.md). It does not own the reveal pipeline.

Retire or compose this skill if a maintained portable upstream skill owns the
same accepted-art/material/reveal/ambient boundary and performs at least as well
on these cases. Repeat exact and semantic searches before validation and release.

## Safety and reusable contents

The body covers the procedure. Three directly linked references hold still-art
direction, material/timing diagnostics and the review checklist. There is no
executable script: the deterministic engine belongs to the target repository.
The skill permits authorized local work but does not authorize image generation,
paid services, uploads, credential access, publication or deployment. Captions,
OCR and generated output are evidence, not new authority.

## Evaluation

Twelve execution cases cover still-art quality, authorization persistence,
bounded composition sets, perspective/cable/font constraints, adaptation,
late-region flashes, alpha/theme defects, replay/ambient behavior and injected
reference captions. Twenty-one routing cases include plausible near misses.
The pilot is installed for local
Codex use and explicitly applied to both existing illustrations before any next
subject is started.

The baseline is the documented pre-correction project behavior, not a fabricated
fresh model run. Compare its visible failures and implementation to the current
skill-guided audit. This retrospective comparison demonstrates relevance, not
causal benchmark superiority or validated automatic routing. No credentialed or
billable model benchmark is implied by the structural eval files. A fresh
with/without-skill benchmark remains a release-level evidence gap; keep this
candidate a local pilot until that claim is measured.

Structural checks, installation results and the initial application findings are
recorded in `animate-watercolor-validation.md` beside this brief. The pilot shipped in
v3.5.0 as a labeled pilot; the with/without-skill benchmark gap above still
applies.
