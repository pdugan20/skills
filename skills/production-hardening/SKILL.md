---
name: production-hardening
license: MIT
description: Prepare a selected implementation for production through a proportionate release-readiness review of product quality and operational risk. Use only when the user explicitly requests production hardening after exploration or implementation. Do not trigger during lightweight design iteration.
---

# Production Hardening

## Instructions

1. Establish the selected behavior and inspect the current diff before changing it.
2. Remove dead variants, debug affordances, temporary data, and experiment-only code.
3. Review accessibility, loading and empty states, failures, cancellation, concurrency, platform behavior, and localization where relevant.
4. Review data exposure, authorization, secrets, production mutations, and observability where relevant.
5. Add or improve tests according to regression impact; do not force a test-first rewrite of completed code.
6. Run focused checks, then the repository's broader release-relevant checks.
7. Report what is production-ready, what remains risky, and any release action still requiring approval.

Do not deploy, push, open a PR, or mutate production systems without explicit authorization.
