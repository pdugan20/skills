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
