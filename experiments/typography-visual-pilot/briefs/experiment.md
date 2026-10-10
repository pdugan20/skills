# Typography comparison briefs

Create new typography and refine existing typography for three matched surfaces. Prioritize visual character, clear hierarchy, apparent size/weight, spacing, rag, rhythm and optical alignment. Preserve all copy, colors, major layout and content order. No images or decorative additions. All content is fictional and original for this experiment.

## Available fonts

Web: Inter, Source Serif 4, IBM Plex Sans; all provided locally under SIL OFL 1.1. Native SwiftUI: system sans, system serif, system rounded, Georgia. Fonts are a shared palette, not required pairings. Each role chooses one font. Native system fonts and Georgia are rendered on macOS; their binaries are not redistributed.

## Six tasks

1. product-new: Design a compact editorial workspace for a small independent publisher. Calm, capable, precise; neither corporate dashboard nor fashion magazine. 1100 × 760.
2. product-refine: Refine that same workspace from the supplied before treatment. Preserve its sans-serif identity. Improve typography only, with restraint.
3. editorial-new: Design an essay opening for Field Notes, a contemporary journal about attention and everyday life. Intelligent, warm and assured; expressive without theatrical nostalgia. 1100 × 900.
4. editorial-refine: Refine that essay opening from the supplied before treatment. Preserve a serif title/body and sans utility identity. Improve typography only.
5. native-new: Design a saved essay detail view for Field Notes. An inviting reading companion, quiet and editorial but comfortable as a native app. 430 × 850 point canvas.
6. native-refine: Refine that view from the before treatment. Preserve system sans for utility and serif for title/body. Improve typography only.

## Output contract

Create one JSON object keyed by the six task IDs. Each value has `roles`, `space`, `titleBreak`, and `rationale`. Roles are `brand`, `eyebrow`, `title`, `deck`, `body`, `meta`, `section`, `item`, `value`. Each role has `font` (allowed names above; native uses system/serif/rounded/Georgia), `size` (pixels or native points), `weight` (100–900), `leading` (baseline multiplier), `tracking` (em). `space` has `titleAfter`, `deckAfter`, `sectionBefore`, `rowGap`, `paragraphAfter` (pixels/points). `titleBreak` is `natural` or `after-art`; after-art breaks only the editorial/native title after “The art of”. The product title remains Issue 08. `rationale` is 2–4 sentences of design reasoning. Do not change other content.

The renderer uses the same page template for every approach. Role changes affect text flow, and role spacing is intentionally variable. It renders font weight, size, tracking, line-height and line breaks from your data; it does not choose the design for you. Do not create a deliberately weak treatment. A restrained unchanged role can be the right result. Without screenshots, mark decisions as proposed rather than visually verified.

## Fixed copy

Product: Index / Editorial workspace; Autumn 2026; Issue 08; A place for things worth keeping.; 12 Stories; 04 In review; Oct 28 Publish date; Story / Author / Status / Updated. Rows: The quiet work of restoration / Nora Ellis / In review / Today; An ordinary kind of wonder / Theo Park / Draft / Yesterday; A room of one's own / June Hara / Ready / Oct 08; Objects that stay / Luca Reed / In review / Oct 07. Footer: Every story starts with a good question. / View archive →.

Editorial: FIELD NOTES / A journal of everyday life / Vol. 08 · Autumn 2026; ESSAY / 01; The art of paying attention; A walk without a destination can change the shape of a day.; Nora Ellis / October 10, 2026 / 8 min read; Opening note. Body: “We had walked this street a hundred times. That morning, with no appointment ahead of us, it seemed to contain an entirely different city.” “There was a seam of light beneath the bookshop door, a pear tree leaning over a wall, the sound of someone practising a difficult piece of music. Nothing had changed. We had simply begun to notice.” Aside: “Attention is a way of making room.” Footer: FIELD NOTES / 01—08.

Native: Field Notes / Saved story; ESSAY · 8 MIN READ; The art of paying attention; A walk without a destination can change the shape of a day.; By Nora Ellis / October 10, 2026; Opening note; same two body paragraphs as editorial. Footer: Continue reading / Saved to your library.
