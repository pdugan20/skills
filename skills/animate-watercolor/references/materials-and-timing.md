# Material and timing diagnostics

Read this when an illustration flashes, changes geometry or feels like a bitmap
wipe rather than painting. Start with the source and the current renderer;
these are diagnostic patterns, not mandatory algorithms.

| Visible miss | Check first | Useful correction |
| --- | --- | --- |
| Finished detail appears, is covered, returns | Source texture revealed before broad palette deposits; later prepared contacts include earlier completed state | Establish coverage first, then local texture; keep dependent contacts sequential |
| Whole region flashes at the end | Residual blend contains missing geometry or opacity | Author the missing surface early with spatial contacts; shrink the residual's responsibility |
| Band, rim or logo changes dimensions | Early proxy differs from the accepted source silhouette | Share geometry/registration across stages; compare landmarks before and after |
| White material globally fades in | Broad support-opacity ramp unrelated to brush arrival | Local first-contact arrival field constrained to that material |
| Foam ellipse or glass foot still flashes despite a brush mask | Brush radius covers the region at once, or wall-clock duration is too short | Narrower traveling passes with material clipping, then a local return; measure actual milliseconds |
| Dark dots, dashes or thick halos | Raster texture mistaken for ink; threshold alpha holes; contaminated edge RGB | Separate authored contours, pigment granulation and alpha; inspect source versus composited output |
| Can label looks pasted on | Crisp vector/text source over textured watercolor | Match pigment integration and local glazes while preserving correct logo geometry |
| Glass turns solid white | Paper protection applied indiscriminately to transparent space | Separate clear glass, opaque foam, reflections and beer; preserve negative space |
| Artwork is blurry at large size | Upscaled source or render buffer; global RGB blur | Render at adequate native resolution, preserve image aspect and texture; soften only the necessary matte |
| Carbonation looks mechanical | Shared phase, equal intervals or radii | Seeded irregular sites and births, differing travel and lifetimes, size review at display scale |
| Replay immediately returns to finished | Old RAF timestamp/callback survived restart | Cancel pending ownership, zero the clock, clear ambient age, restart from a fresh frame |

## Compare the executable score

When matching an accepted reveal, compare these properties in the actual score
and renderer before proposing another candidate:

- **Contact timing:** Measure maximum concurrent paint contacts and the fraction
  of active painting time with more than one. Use the union of active intervals
  as the denominator; report ink, bloom, support and residuals separately. Read
  explicit timing overrides as well as the scheduler. A mostly sequential score
  with deliberate exceptions on another surface is not a license for pervasive
  overlap. Match the selected reference, not a universal stroke count or duration.
  Serializing all existing contacts can exhaust the accepted time budget; reduce
  redundant visits and preserve important travel/lift time instead of compressing
  every mark or silently extending playback.
- **Ink travel:** Inspect how the renderer samples paths. If it joins sampled
  points across disconnected `M` subpaths, split those into separate contacts with
  lifts. Do not ban compound paths when the renderer already handles subpath
  breaks. Inspect the ink-only phase at display scale: a few geometric outlines
  may leave a device unreadable even when their final positions are correct.
- **Effective pigment:** Check actual source contributions, strengths, material
  clipping, dry-brush flags and highlight behavior. A contact named “dry return”
  may never enable dry brush; a “shadow” stage may contain only palette deposits.
  Compare one reference wash, shadow return and detail return through playback.
  Do not fix the mismatch by renaming stages or revealing all source texture early.
- **Override precedence:** Trace the composed result, not merely the new setting.
  For example, `max(sharedResidual, localResidual)` cannot delay finishing when
  the local curve is everywhere below the shared curve. Compare effective curves
  or pixel output against baseline before claiming a parameter changed anything.
  A final raw-source draw is a risk to inspect immediately before/at completion,
  not proof by itself that a visible pop exists.

Use focused contracts for these factual properties where practical. They detect
specific regressions; they do not establish that the painting looks convincing.

## Coverage is not fidelity

A pale metal wash can establish the full can shape without displaying its final
label texture. Coverage describes where the material is present; fidelity
describes how much shading and texture it carries. Keeping those separate lets
subsequent passes refine a stable object instead of rebuilding its silhouette.

An arrival field may assign each pixel to the brush contact that first reaches
it. Its opacity should progress along that contact, constrained to a material
mask. Do not spread this rule across unrelated transparent glass merely because
it works for cloth or a napkin. Inspect unvisited gaps; a final global blend must
not silently fill the important ones.

Check whether support assigns every region pixel to its nearest contact even
when that contact never physically reaches it. This may intentionally connect
opaque cloth or metal, but it is broader than pigment coverage. Do not reuse that
expanded field for a live display or other interactive overlay without inspecting
its arrival: the interface can appear ahead of the paint. Compare support alpha,
pigment footprint and overlay mask separately, including intermediate dark-mode
frames. Correct the subject's masks without changing accepted materials elsewhere.

## An honest speed example

Suppose the hover renderer maps score seconds 8–30 into the final 92% of a 2.4s
painting. A 2.4-score-second contact occupies `2.4 / 22 × 0.92 × 2400`, roughly
241ms. A 0.2-score-second contact occupies about 20ms and may appear to flash even
with a correct traveling mask. This example does not include an independent
180ms bloom lead, and it is not a universal target. Read the actual mapping.

## Registration before more generation

For a can and glass, compare measured physical ratios and perspective together.
A 4.81in-tall can beside a 6.375in glass has a height ratio of about 0.755 at equal
depth; moving the can behind the glass changes apparent size. Do not stretch a
raster independently in x/y to repair the relationship. Check the tab, rim,
label bounds, top text band, lower star band and partial occlusion against the
reference. Preserve the approved arrangement while fixing a local defect.

## Finishing options

A source-texture glaze can add texture locally to established pigment. A gentle
regional residual can reconcile tiny differences after the major forms already
read. Neither should introduce a new silhouette, an entire opaque white region
or all lettering at once. A real recorded painting process is a different asset
pipeline; do not imply authored masks reproduce actual brush capture.
