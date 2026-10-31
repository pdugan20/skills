# Sources and decision checks

Reviewed 2026-10-10. These sources support the workflow; they are not bundled model or API specifications.

- [OpenAI image prompting: migrate an existing workflow](https://developers.openai.com/api/docs/guides/image-prompting#migrate-an-existing-workflow): repeated edits can drift; preserve exact regions by compositing accepted edits into the original. Compare difficult edits, text, geometry, and transparency against a baseline. Check current model guidance here rather than pinning it in this skill.
- [Official ImageGen skill](https://github.com/openai/skills/tree/main/skills/.system/imagegen): owns generation/edit execution and tool routing. This companion owns preservation and integration checks, not another generator.
- [Adobe nondestructive editing](https://helpx.adobe.com/sg/photoshop/using/nondestructive-editing.html): retain source pixels and separate adjustments/masks from the original.
- [MDN canvas optimization](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas): account for display dimensions and device pixel ratio when sizing a canvas.

## Routing and adversarial cases

Use these to review changes to this skill. They are decision checks, not claims that an independent agent evaluation ran.

| Request or evidence | Expected behavior |
| --- | --- |
| “Stop editing; research why it gets blurry.” | Inspect and explain; do not generate, replace assets, or resume features. |
| “Explore three UI layouts.” No image-generation request. | Use the established code-native workflow; this skill grants no image-generation permission. |
| “Only change DIGITAL from italic to upright.” | Prefer an editable label layer. If generating a repair is authorized, preserve the approved master and integrate only the label repair; do not replace the entire product with a generated derivative. |
| Candidate has a perfect label but different brushed-metal grain elsewhere. | Reject the full-image replacement; exact-preservation output may use only the approved masked region. |
| “Use the newest model”; current tool does not expose model selection. | Verify official docs and state the tooling limitation. Follow existing routing/authorization rules; do not invent a model argument or silently switch to a custom API client. |
| Native PNG is sharp but browser is soft. | Investigate rendering resolution/transforms before regenerating artwork. |
| Pixel comparison shows many differences. | Report drift; do not label the count a quantitative blur score. |
| Patch only fits after warping individual buttons. | Reject the patch geometry; do not distort rigid hardware to hide registration failure. |
| User wants realistic photographic hardware. | Retain the photographic material; a separately rendered label is not permission to redraw the product in SVG. |
| User authorizes one local repair. | Keep the repair bounded; no implied deployment, publication, paid model migration, or unrelated animation work. |
| "Try cleaning the shell rim and brand mark; let's get a quick candidate." Only a prompt-based editor is available. | Save and inspect the repair-boundary record first; use registered local crops, with the whole product only as reference. A whole-product edit target is a failed pre-generation gate even if the output is never applied. |
| "We'll mask it later, so just send the whole sprite with a preservation prompt." | Reject that shortcut and complete the boundary record before generation. Later compositing does not waive the input boundary. |
| An agent says a new hook makes repairs safe. | Require observed rejection and allowance in the actual runtime. A script test, hook registration, or rewritten skill alone does not establish active tool enforcement. |
| The user mentions a multi-model workflow from an earlier baseball project. | Locate the actual earlier project, runner and provider records before selecting a tool or building new guards. Do not infer the provider from a similarly named baseball illustration in the current project; do not import MLB-specific asset policies into a product-photo repair. |

## Molded-surface failure case

A photographic hinged device combined separate window and badge height fields; containment applied to only one field and did not match the visible circular seam. The texture also retained a shaded capsule and a transplanted wordmark background, while runtime shading added another lighting treatment. A passed outside-mask pixel invariant did not catch these errors. Check geometry containment, material continuity, and preservation as separate claims, using reference-aligned close-ups at the relevant poses. This case motivates the guidance; it is not evidence that the subsequent repair has passed.

## Discman lettering and rim iteration, 2026-10-12

Observed in a local repair session; the owner still considers the lettering
provisional. These observations do not establish a universally successful recipe.

- A sparse dark-edge mask followed by brightness blending preserved the rest of
  the image but left thick highlights and uneven transitions. Geometry/depth
  defects need coherent feature repair, not scattered shadow lightening.
- A connected crop repair gave cleaner shallow lettering. Subsequent material
  prompts introduced gray faces, obvious brushing and stronger bevels. The owner
  preferred the original pale coloring. Lock color independently of material
  vocabulary; reference lighting can make the same sort of mark look very different.
- The provisional clean face median was RGB 250/238/228 versus original
  250/240/233. A small source-tone correction brought that sample median back
  without changing the clean contours. This is color evidence, not proof of a
  correct material or finished repair; those exact channel offsets are case-specific.
- Some generated outputs shifted/resized the wordmark or drew a faint mask frame
  into surrounding paint. Uniform registration and explicit final masking need
  native-scale review of glyphs, context and transition boundaries.
- An earlier translated corner patch lacked candidate coverage at the end of its
  nonzero mask and created a join. Keep sampling margins after registration, and
  inspect both ends of each perimeter region.
- The shell generator resampled a 22px rim band during a 13px inward compression.
  Earlier source edges were cleaner but had a different footprint. Diagnose the
  source transform first; do not blame browser compression or sharpen the result.

Added decision checks: height-only requests retain color; material observations
do not imply gray recoloring; a passing preservation check does not establish
repair quality; cropped edge patches require covered joins; provisional owner
feedback does not authorize declaring the asset finished. No independent agent
behavioral evaluation has been run for these added cases.
