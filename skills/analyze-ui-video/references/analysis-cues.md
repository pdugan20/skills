# UI video analysis cues

Use these cues only after creating a temporal overview. They help distinguish
what the recording proves from what still requires repository evidence.

## Temporal ownership

| Visible behavior | Plausible owner | What the video cannot prove |
| --- | --- | --- |
| Content tracks a finger continuously | Direct gesture or scroll view | Exact finger-down/up time without touch indicators |
| Motion continues and decelerates | Platform scroll physics or custom inertia | Which API owns the curve |
| Content moves without a visible gesture | Programmatic scroll, data mutation, layout, or an off-screen gesture | Which cause occurred without code or input evidence |
| Preview lifts while the background dims | Platform context menu or app-authored presentation | Ownership until platform and code are inspected |
| One element arrives after its container | Async asset/state arrival or split animation transactions | Whether network, decode, identity, or transaction timing caused it |

Do not estimate gesture velocity or easing from positions unless the recording's
frame timing is trustworthy and the input interval is observable.

## First-divergence checks

For a visual defect, find the last correct frame and first incorrect frame. Then
ask which boundary changed:

- **Source artifact:** the unexpected pixel already exists in captured media.
- **Geometry:** frame, proposal, safe area, clipping, or coordinate space changes.
- **Identity:** a view or item is reused, removed, reordered, or re-anchored.
- **State:** a value changes earlier, later, or in a different transaction than
  its visual container.
- **Asset arrival:** placeholder, decoded image, font, or provider mark arrives
  during motion.
- **Composition:** mask, blend, opacity, transform, or overlay separates layers.
- **Capture artifact:** variable frame timing, dropped/duplicated frames,
  rounded-corner bleed, color conversion, or recording chrome creates the issue.

Prefer the narrowest check that separates two hypotheses. Examples include
sampling source-edge pixels, logging item identities, temporarily outlining
layout bounds, disabling one transition, or re-recording with a cold cache.

## Reference reconstruction

Describe the observable contract before choosing an implementation:

- start and end states;
- elements that remain spatially continuous;
- elements that enter, exit, replace, cross-fade, or remain fixed;
- shared versus independent transforms;
- clipping, corner-radius, blur, translucency, and z-order changes;
- direct manipulation versus triggered motion;
- approximate duration and settling character within recording resolution;
- interruption, reversal, and reduced-motion behavior when visible.

Map that contract to the target repository only after checking platform version,
existing navigation and animation primitives, component ownership, and current
design conventions. Prefer a native primitive when it matches the contract; do
not force a native primitive when the frames show materially different behavior.

## Confidence labels

- **High:** visible across several frames and corroborated by repository or
  platform evidence.
- **Medium:** visible but ownership or cause remains ambiguous.
- **Low:** depends on missing input indicators, low resolution, compression,
  uncertain timing, or private implementation details.

Request a better capture only when it would change the next decision. Ask for
the smallest improvement: a tighter reproduction, touch indicators, a cold-cache
run, a longer lead-in, or a higher-frame-rate crop.
