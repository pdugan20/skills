# Findings and next decision

**Do not promote the original method to an installed skill on this evidence.** In this small first-pass comparison, the independent blind reviewer preferred ordinary design judgment for all three new-design tasks. Impeccable-guided settings performed better on two refinements and tied ordinary judgment on the product refinement. The original guidance produced no outright preferred result. Patrick has not reviewed or selected a direction yet.

## Decoded blind results

| Case | Reviewer preference, best first | Strength of evidence |
| --- | --- | --- |
| Product new | Baseline > Impeccable > Original | Medium-low; subtle hierarchy differences |
| Product refine | Baseline = Impeccable > Original > Before | Low; all changes modest |
| Editorial new | Baseline > Impeccable > Original | Medium; original strands “day.” and “city.” |
| Editorial refine | Impeccable > Baseline = Original > Before | Medium-low; reviewer prefers more decisive title silhouette |
| Native new | Baseline > Original > Impeccable | Medium; calmer title wins, despite remaining body rag |
| Native refine | Impeccable > Baseline > Original > Before | Medium; better title phrase break and spacing |

These are ordinal preferences, not a beauty score or a claim of significance. The unmodified [blind review](blind-review.md) gives evidence, costs and pairwise ties; [identity-key.json](identity-key.json) maps labels to methods. Product differences are particularly small. A different reader may prefer a more expressive or more conservative choice.

## Useful failures

The original editorial setting has a plausible rationale and passes numerical checks, yet its deck ends with “day.” alone and its first paragraph with “city.” alone. The brief needs rendered judgment, not confidence in a tidy role scale. The baseline native-new setting wins this review while still leaving “notice.” alone at the end of the second paragraph. Impeccable native-new avoids that ending but makes the title more dominant and strands “city.” in the first paragraph. All native refinements retain the latter rag. No arm solves everything.

The refinement results also show why identity preservation matters: all preserve the required family roles, but the reviewer prefers the larger title intervention in two cases. That is a contextual compositional choice, not a rule that every audit should introduce line breaks. A reader who prefers near-invisible refinement could choose a different treatment.

## Recommendation

Use the boards to establish Patrick's taste before adopting a method. The provisional lowest-maintenance route is ordinary art direction for new work, with the reviewed Impeccable typesetting method as a refinement reference. This is not authorization to install its broad package or execute its detector. The original method should remain an experiment, not a routable personal skill.

The next useful step is Patrick's selection or tie on each board, plus one concrete reason: voice, hierarchy, apparent weight, spacing or rag. If he sees a recurring unmet need, run a small held-out task with equal render-and-revise opportunities for all arms, including a strong existing design where no change can win. Only then decide whether to adapt focused upstream guidance, compose references, independently author a skill, or take no further action.

## Limits

This experiment tests one generation per arm under a fixed font palette, layout and copy. It does not test the full iterative workflows, full Impeccable runtime, free font discovery, Figma editing, responsive behavior, other writing systems, Dynamic Type or production iOS layout. There is one independent AI reviewer and no human preference evidence. Familiarity with typography may be common to all models; “baseline” means no supplied specialist skill, not absence of learned expertise. The method inputs have unequal length and no repeated random seeds. These constraints prevent causal or statistical claims about a skill's general effectiveness.

The native images are actual SwiftUI macOS canvases with TextKit wrapping and exact native baselines. They are not web approximations, but also not iOS simulator captures. Source-backed technical rules are distinct from contextual aesthetic heuristics; no golden ratio, character count or line-height threshold is used as a universal beauty test.

Library upload was unavailable. The draft repository contains the inspected images and report; no Library file IDs were created. See [verification](verification.md) for technical checks and provenance.
