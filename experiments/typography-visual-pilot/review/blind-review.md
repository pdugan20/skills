# Blind visual review

Independent AI visual judgment, not a measurement of human or user preference. I read only `briefs/experiment.md`, the six blind comparison boards, and all 21 individual blind screenshots. I did not read treatment data, rationales, identities, or other reviews. Judgments are from rendered screenshots; native screenshots are the supplied macOS SwiftUI 430 × 850 point canvas at 2×, not an iOS simulator or a dynamic-type test. No numeric beauty scores.

Groups in the ranking are ordered best first; `=` means no reliable preference. Confidence describes the ranking, not rendering correctness. Screenshot links below are the evidence examined at original resolution.

| Case | Preference | Confidence |
| --- | --- | --- |
| product-new | A > B > C | Medium-low |
| product-refine | A = C > B > BEFORE | Low |
| editorial-new | B > C > A | Medium |
| editorial-refine | A > B = C > BEFORE | Medium-low |
| native-new | C > A > B | Medium |
| native-refine | A > C > B > BEFORE | Medium |

## product-new

[A](product-new-A.png), [B](product-new-B.png), [C](product-new-C.png), [board](product-new-board.png).

A is the calmest and most precise: the issue heading is substantial without overpowering the workspace, story names have clear priority over author and status, and the smaller table headings feel like useful labels. B is very close, but the larger/heavier issue heading, numbers and table labels add a little unnecessary insistence. C's serif deck supplies warmth and connects with the serif issue heading, but it becomes a second editorial statement between the title and working table. Its lighter values also reduce the pleasing emphasis on the small summary block. These are fine differences, not distinct success and failure classes. All three fit the independent-publisher setting; none looks obviously theatrical or corporate. Columns and right-aligned dates read cleanly.

Pairwise: A over B; A over C; B over C. Main cost of A: the table utility labels are small, so B is preferable if size/readability is weighted above calmness.

## product-refine

[BEFORE](product-refine-BEFORE.png), [A](product-refine-A.png), [B](product-refine-B.png), [C](product-refine-C.png), [board](product-refine-board.png).

All three retain the supplied sans identity. Each tightens the loose heading-to-deck relationship and brings the table up, making the upper information group more coherent. A and C offer similarly restrained improvements: compact title, subordinate author/status information, and regular rows. A is a little more compact; C gives the table slightly more room and visual presence. I cannot defend a clear winner between them. B also improves the header rhythm, but its larger apparent author/body type competes a little more with story titles. BEFORE remains competent and readable; its more separated title/deck and lower table make the page feel less settled, not broken.

Pairwise: A ties C; both over B and BEFORE; B over BEFORE. The advantage over BEFORE is modest. No refinement is a transformative improvement.

## editorial-new

[A](editorial-new-A.png), [B](editorial-new-B.png), [C](editorial-new-C.png), [board](editorial-new-board.png).

B best balances a warm, assured serif title with a quiet utility layer. The break after “The art of” keeps the meaningful phrase “paying attention” together. Its single-line deck and two-line first paragraph avoid awkward fragments and give the page an even descending rhythm. C is nearly as successful, with a somewhat larger title and stronger masthead; this adds authority but slightly more display emphasis than the brief needs. A has the same attractive broad voice, but its deck leaves “day.” alone and its first paragraph leaves “city.” on a short final line. Those two abrupt endings are visible distractions in an otherwise very sparse page. A's larger content footprint fills more of the page, but the rag costs outweigh that benefit.

Pairwise: B over C; B over A; C over A. The B–C preference is weak; the preference over A is clearer. The aside is legible in all three and does not collide with the body.

## editorial-refine

[BEFORE](editorial-refine-BEFORE.png), [A](editorial-refine-A.png), [B](editorial-refine-B.png), [C](editorial-refine-C.png), [board](editorial-refine-board.png).

A retains serif title/body and sans utility while giving the opening a more deliberate title silhouette. The phrase-preserving title break creates a focal point and shifts the text lower, reducing the conspicuous vacant lower field of BEFORE. The deck remains a clean single line and the body retains comfortable lines. Its cost is a more substantial editorial gesture than B or C, and the aside now ends its first line with “of,” which is a slightly weaker phrase break than the alternatives.

B and C are effectively tied: both reduce the oversized vertical gaps around the original single-line heading and improve body leading/paragraph separation while staying extremely close to the source identity. C's quieter masthead and B's slightly firmer masthead are defensible alternatives. BEFORE has the loosest opening spacing and a more compressed body texture; still no serious functional defect. A's larger change is justified here by the better overall page silhouette, but a user who values near-invisible refinement could reasonably choose B or C.

Pairwise: A over B, C and BEFORE; B ties C; both over BEFORE. This is a subjective composition preference, not proof that introducing a title break is universally better.

## native-new

[A](native-new-A.png), [B](native-new-B.png), [C](native-new-C.png), [board](native-new-board.png).

C is the strongest quiet reading companion: moderate serif title scale, an intentional break that keeps “paying attention” together, a clean system-sans utility layer, and an inviting body. A is close and has a similarly comfortable body, but its first title line ends at “paying,” making the isolated “attention” feel less intentional. B's larger and heavier title is striking but starts to dominate this narrow reading view; the larger text also leaves “city.” alone at the end of paragraph one and expands the text block substantially. B's second paragraph has the best ending, a complete final phrase instead of the isolated “notice.” in A and C. That is a real cost in the preferred C, not a solved rag.

Pairwise: C over A; C over B; A over B. All three remain readable and fit on the canvas. Large empty space above the footer is shared, particularly evident in A/C; it is not a collision or missing-content failure.

## native-refine

[BEFORE](native-refine-BEFORE.png), [A](native-refine-A.png), [B](native-refine-B.png), [C](native-refine-C.png), [board](native-refine-board.png).

All preserve the system-sans utility/serif reading identity. A has the best refinement: tighter headline leading, a more considered phrase break, and more coherent spacing through the deck, byline and opening note. C and B retain the original title wrap but make its two lines feel like one heading rather than BEFORE's loosely separated blocks. C is slightly quieter and more compact through the byline/opening section; B's utility/byline presence is a little stronger. That C–B difference is small. BEFORE's title leading and accumulated opening gaps feel unnecessarily loose.

Pairwise: A over C, B and BEFORE; C over B and BEFORE; B over BEFORE. All four retain the awkward one-word “city.” paragraph ending, so none fully resolves the body rag. A improves the composition without changing the evident type identity; it does not fix every issue.

## Secondary rendering/readability check

All expected visible copy appears present in the inspected screenshots. I saw no clipped glyphs, overlapping text, missing table rows, or footer collisions. All left text edges and tabular columns appear consistently aligned; the right-aligned updated dates are clean. Tiny web utility text is readable at original resolution but inevitably weak in the comparison boards. This is visual inspection only, not OCR, accessibility/contrast testing, interaction testing, or proof at other viewport sizes. Main visible weaknesses are rags and hierarchy/spacing tradeoffs described above, not functional text failures.
