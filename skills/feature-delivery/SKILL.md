---
name: feature-delivery
description: Implement a substantial production-ready feature with proportional planning, coordinated implementation, risk-based testing, review, and verification. Use when the user asks to build, implement, or ship a production feature that spans multiple meaningful behaviors or subsystems, changes important data or security boundaries, or requires coordinated release checks. Do not use for lightweight UI iteration, visual exploration, prototypes, copy or motion tuning, small fixes, or ordinary isolated changes.
---

# Feature Delivery

## Instructions

1. Read applicable instructions, inspect the relevant architecture and tests, and preserve unrelated user work.
2. Establish the selected behavior, boundaries, and success criteria. Ask only about unresolved decisions that would materially change the implementation.
3. Form a concise checkpoint plan proportional to the work. Do not require a formal spec, plan file, approval ceremony, worktree, branch, or commit.
4. Implement in coherent batches that leave the repository inspectable and usable. Follow existing patterns unless the feature requires a deliberate boundary change.
5. Add tests according to regression, data, security, and platform risk. Use strict red-green-refactor only when the user explicitly requests strict TDD.
6. Exercise user-visible behavior in the real browser or relevant simulator. For visual decisions, implement directly in code; do not use ImageGen, static generated mockups, or a browser-based option picker unless explicitly requested.
7. Review relevant accessibility, loading and empty states, failure handling, cancellation, concurrency, authorization, privacy, performance, observability, and platform behavior.
8. Run focused verification throughout, then the repository's broader production or CI gate before claiming readiness.
9. Report the delivered outcome, verification evidence, remaining risks, and any deploy, data mutation, push, or PR action still requiring authorization.

Do not invoke explicit-only Superpowers skills merely because this skill is active. Apply their underlying rigor proportionally; invoke one only when the user names it or explicitly requests that workflow.
