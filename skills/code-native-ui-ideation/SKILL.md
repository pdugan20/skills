---
name: code-native-ui-ideation
description: Explore and compare UI, interaction, layout, visual, or motion directions as runnable code in the existing project, browser, or relevant simulator. Use for lightweight design exploration, UI variants, visual revisions, prototypes, pixel tuning, or requests to brainstorm and compare interface directions. Do not use for production feature delivery, audit-only requests, or when the user explicitly asks for generated images or static image mockups.
---

# Code-Native UI Ideation

## Instructions

1. Inspect the current interface, applicable instructions, design system, and the smallest relevant implementation surface.
2. Build real variants in the existing project. Use a lightweight project-native workbench, route, flag, or reversible switch when simultaneous comparison is useful.
3. Render web work in the browser, React Native work in the primary simulator, and Swift work in the target Apple simulator. Prefer the project's actual platform over a detached HTML approximation.
4. Reuse real content, assets, tokens, and component patterns where practical so the comparison reveals genuine layout and interaction tradeoffs.
5. Exercise the important interaction and capture screenshots when they materially help comparison. Run only focused compile, lint, type, or behavior checks proportional to exploration.
6. Keep experiments easy to inspect and undo. Do not require a spec, plan, worktree, test-first cycle, commit, or production hardening.
7. After the user selects a direction, preserve that direction and remove abandoned variants only when asked to productionize or clean up the experiment.

Do not invoke Product Design image ideation or ImageGen unless the user explicitly requests generated images or image mockups. Do not create a separate browser-based option picker; the live coded variants are the comparison surface.
