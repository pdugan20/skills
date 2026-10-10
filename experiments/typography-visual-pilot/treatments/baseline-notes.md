# Baseline treatment notes

These are proposed designs from ordinary design judgment. The inputs were the repository's `AGENTS.md`, `briefs/experiment.md`, and `briefs/before.json`. I did not load typography or design skills, other treatment files, external references, or research. I did not inspect renderer implementation or run rendering, validation scripts, tests, or installation commands.

## Design reasoning

- **Product new:** IBM Plex Sans supplies a consistent working vocabulary with some editorial character. The title and summary values have compact leading; story names have moderate emphasis; supporting information remains readable at 13–15 pixels. The larger gap before the list is intended to establish a clear shift from issue overview to individual work.
- **Product refine:** Preserve Inter, the primary sizes, and most existing spacing. Concentrate the intervention in display leading and tracking, and reduce the column-heading emphasis. Unchanged body typography is intentional.
- **Editorial new:** Pair Source Serif 4 with IBM Plex Sans. The proposed two-part title emphasizes the subject of attention without adding a decorative device. A substantial deck, more open body leading, and a lightly weighted aside create several reading speeds within the fixed content.
- **Editorial refine:** Preserve Source Serif 4 and Inter and retain natural wrapping. Replace the uniform leading with role-specific leading: close for the title, moderate for the deck, and open for the essay. Keep most sizes unchanged so the improvement depends on rhythm and hierarchy rather than wholesale restyling.
- **Native new:** Georgia gives the title and body a familiar reading texture. System sans supplies utility, deck, and action roles. Regular title weight and a modest deck are intended to keep the small canvas inviting; the explicit title pause parallels the essay's reflective tone.
- **Native refine:** Preserve the system sans and system serif identities and the existing title, deck, and body sizes. Reduce excess display line space and inter-section gaps, then spend a little of that room on body leading. Keep the natural title break as a restrained continuation of the starting treatment.

## Verification and limits

I reviewed the authored data against the brief's contract: six task keys; nine named roles per task; font, size, weight, leading, and tracking for every role; five spacing values; an allowed title-break value; and a three-sentence rationale for each task. All chosen font names come from the allowed palette, and every weight lies within 100–900. Product titles retain natural wrapping. Refine treatments retain the required font identities.

This is an author review, not an automated parse or schema-validation result. There is no screenshot or rendering evidence. I cannot yet verify actual font rendering, apparent weight, glyph-specific alignment, title and deck wrapping, text rags, widows, total height, clipping, footer clearance, or behavior at other viewport sizes. Explicit breaks after “The art of” do not guarantee the remainder fits on one line. The renderer's handling of native leading and tracking also remains uninspected.

The first visual review should check the product's story-column fit and numerical balance; the editorial title width, deck rag, and body/aside relationship; and native paragraph wrapping and footer clearance on the specified 430 × 850 point canvas. No visual superiority or successful fit is claimed before that review. The output only supplies permitted typography data and does not change copy, colors, content order, or the shared layout template.
