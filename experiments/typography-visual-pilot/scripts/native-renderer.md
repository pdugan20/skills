# Native rendering method

`render-native.swift` is a standalone **native SwiftUI macOS canvas** renderer. It uses real macOS fonts and SwiftUI `Text` rasterized by `ImageRenderer`; this is not an iOS simulator capture, an iOS application, or a browser approximation. The execution host is macOS 27.0 (26A428). No product project or simulator was changed.

Run from the experiment directory:

```sh
swiftc -parse-as-library -module-cache-path /tmp/typography-native-module-cache scripts/render-native.swift -o /tmp/typography-native-renderer
/tmp/typography-native-renderer "$PWD"
```

The renderer reads `briefs/before.json` and any available `treatments/{baseline,impeccable,original}.json`. It writes `renders/native-{new,refine}-{arm}.png` and `renders/native-render-report.json`. The before treatment is rendered under both case names for comparison convenience; those canvases have identical content. Missing arm files are explicitly reported and skipped. No treatment configuration is changed, and no automatic fit adjustment is applied.

## Shared layout and palette

- 430 × 850 points at 2×, producing 860 × 1700 pixel PNG files.
- 28-point horizontal margins and a 374-point article measure.
- Brand and Saved story share a native first-baseline-aligned horizontal header at y=28. A 0.5-point rule sits at y=76.
- Article begins at y=112. The gap between eyebrow and title is fixed at 14 points. Title-to-deck, deck-to-author, date-to-section, section-to-body, and paragraph gaps use the corresponding treatment values. Author-to-date spacing is fixed at 4 points.
- Footer rule y=764; Continue reading y=783; Saved to your library y=813. The article has a conservative clearance threshold of y=748, 16 points above the rule. Reports flag content beyond that threshold instead of shrinking or moving it.
- Shared palette: paper `#F6F3EB`, ink `#262A27`, muted `#626960`, rule `#CFCFC3`, accent `#52604E`. The accent is applied to Continue reading.
- All native fixed copy is included. Quotation marks around the source brief's paragraph examples are treated as delimiters rather than literal paragraph content. No decorative icons, status bar, device chrome, or extra text was introduced.

## Font and leading calibration

Native system, serif, and rounded selections resolve through `NSFont.systemFont` and its font descriptor's system design. Georgia resolves to its regular or bold installed master; it does not supply nine discrete weights. Numeric weights select the nearest native system weight. Actual resolved PostScript font names and metrics are written to the report.

This is a hybrid **TextKit wrapping + SwiftUI drawing** method. TextKit computes word wrapping from the actual `NSFont`, font size, and `tracking × size` kern, with zero text-container inset. Each resulting line is drawn by SwiftUI `Text` at its intrinsic size. A custom SwiftUI layout reads each line's native first-baseline metric and places consecutive baselines exactly `size × leading` points apart. Leading is not passed unchanged to `.lineSpacing`, and tight display leading is not silently clamped to the font's natural line height. The report includes ascender, descender, intrinsic leading, native line height, requested baseline advance, and their difference.

For example, the before body resolves to `.NewYork-Regular` at 17 points. Its reported native line height is 20 points and its requested advance is 24.65 points. Baseline body at 17 points and 1.5 leading advances 25.5 points. Georgia body in baseline-new has its own native font metrics and the same requested 25.5-point advance. Single-line roles have no second baseline, so leading does not add synthetic top or bottom padding.

## Verification

Compilation and rendering succeeded on the execution host. The final set contains before plus baseline, impeccable, and original, for eight PNG files and seven distinct canvases. All seven distinct images were opened for visual inspection. Header, title, deck, author, date, Opening note, both complete paragraphs, and both footer strings are visible; no clipped glyphs, horizontal overflow, or footer collision was observed. The final measured article bottoms are:

| Treatment | Article bottom | Clearance to footer rule |
| --- | ---: | ---: |
| Before (both cases) | 655.85 pt | 108.15 pt |
| Baseline new | 590.88 pt | 173.12 pt |
| Baseline refine | 632.02 pt | 131.98 pt |
| Impeccable new | 649.70 pt | 114.30 pt |
| Impeccable refine | 639.02 pt | 124.98 pt |
| Original new | 597.54 pt | 166.46 pt |
| Original refine | 644.66 pt | 119.34 pt |

Every final report has an empty `issues` array. An initial diagnostic conversion incorrectly added the canvas offset twice; inspection exposed the discrepancy, it was corrected, and those reports were regenerated. The image layout itself was unaffected. The renderer now retains the SwiftUI layout's measured canvas coordinates directly.

Observable typography details were preserved rather than corrected: baseline-new and original-new both end the second paragraph with the one-word line “notice.”; treatments with a natural title break end the title on the single-word line “attention”, while explicit after-art treatments produce “The art of” / “paying attention”. These are treatment comparison evidence, not clipping failures. No choice was retuned in response to inspection.

Wrapping asserts that normalized source copy equals normalized concatenated lines, preventing dropped words from passing silently. The report records all article text, actual wrapped strings, line counts, baseline advances, and measured block frames. This supports copy checks and spacing review alongside the pixels.

## Limits

- All three treatment arms were present for the final execution. Future configuration changes require a new render and inspection; the current evidence applies to these saved configurations.
- The canvas exercises typography, not scrolling, interaction, accessibility, Dynamic Type, device safe areas, or iOS font rendering. A 430-point canvas alone is not evidence of an iPhone build.
- Word wrapping is deliberately delegated to TextKit, not SwiftUI's full paragraph layout. Individual lines are native SwiftUI text. This choice enables exact baseline control but can differ from a single SwiftUI `Text` paragraph in a production app.
- macOS font versions and system serif optical behavior can differ from other operating-system versions. The PNG files and resolved metrics are the record of this execution, not a cross-platform rendering guarantee.
- Geometry reports detect measured block overflow, not every possible ink overhang. Visual inspection is still required, particularly for a newly supplied treatment.
- The brief's `value` role has no corresponding native content and therefore does not appear on this canvas. All other roles are exercised. No invented numeric content was added to force coverage.
- This renderer never tunes treatment values after seeing the output. Visual differences and unusual rags remain evidence for the comparison.
