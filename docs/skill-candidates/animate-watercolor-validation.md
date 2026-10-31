# Animate watercolor pilot validation — 2026-10-01

## Reference-score audit revision — 2026-10-02

The consuming portfolio's `docs/projects/personal-illustrations/ipod/audit/`
records the source snapshot, score metrics and comparison frames for Ichiro,
Rainier and iPod. The audit found no concurrent paint contacts in Ichiro, specific
extended-glass exceptions in Rainier, and overlapping contacts during 93.22% of
iPod's active painting time. It also identified disconnected ink subpaths joined
by the sampler, named dry returns without an effective dry flag, expanded support
coverage reused for the LCD, and a residual override dominated by the shared curve.

The skill now requires reference-specific choreography and executable-score
inspection. It preserves reference exceptions and distinguishes ink/color overlap
from simultaneous paint contacts; no subject's stroke count or duration becomes a
universal rule. Material diagnostics separate support alpha, pigment and live
screen arrival. Review guidance separates cold preparation, warm drawing and
additional overlay work when investigating stutter.

- Added four execution cases and four routing cases: totals are 17 and 26.
  Cases cover timing, connected paths, actual flags, ineffective overrides and
  support/LCD masks. The audit case includes an embedded instruction attempt
  that must not authorize rewriting accepted references or uploading sources.
- Skill Creator quick validation, repository validation, all 52 repository tests,
  focused Markdown lint, JSON formatting and Git whitespace checks passed.
  The installed skill symlink
  resolves to the edited canonical source; no reinstall is needed.
- The external `skill-validator` executable is unavailable on PATH. No new
  provider-backed execution/routing trials or with/without-skill benchmark ran.
  These additions are regression specifications, not measured improvements in
  model behavior or art quality. The scope and pilot status are unchanged.
- No portfolio runtime, accepted reference score or artwork changed in this
  revision. No release, publication, push or commit was performed.

## iPod failure-mode revision

- Added an explicit still-art phase for new subjects in an existing painting
  family, with a directly routed reference for actual-art quality, medium
  selection, perspective, accessory anatomy, entrance-aware cropping and later
  typography/runtime work.
- Preserved the explicit image-generation boundary and clarified that direct
  approval of a proposed generation step persists; code-variant permission alone
  does not authorize it. Generic image generation remains outside the trigger.
- Updated discovery metadata, checklist, candidate evidence and changelog.
  Execution cases now total 12; routing cases total 21, including new adversarial
  reference-caption coverage. These are regression specifications, not completed
  model trials.
- Skill Creator quick validation passed using an ephemeral `uv` environment with
  PyYAML because the default Python lacks that dependency. Repository validation,
  focused Markdown lint, JSON/YAML formatting and Git whitespace checks passed.
- The pinned external validator is unavailable on the current PATH, so it was
  not rerun for this revision. No provider-backed benchmark, release, push or
  publication occurred. The existing local symlink resolves to the edited
  canonical source; no installation copy or dependency manifest changed.

## Package checks

- `npm run verify`: passed, including 52 repository tests, isolated installation
  checks for 17 skills across Agent Plugin / Claude Code / Codex / Cursor layouts,
  repository validation, official Claude plugin validation, Markdown lint,
  formatting and Skills CLI discovery.
- `skill-validator` v1.5.6, the repository's pinned external validator:
  `check --strict --allow-dirs=agents,evals skills/` passed all 17 skills.
- `gh skill publish --dry-run`: passed; no release or publication was performed.
- Five execution cases and sixteen balanced routing cases are present. Their
  format, assertions and boundaries were reviewed. No provider-backed model
  benchmark or automatic-routing success rate is claimed.
- Local Codex installation is a link from the personal agent skills directory
  to this repository's canonical `skills/animate-watercolor` folder. Reading the
  installed file resolves to the canonical source. No consumer snapshot or
  skills lockfile was overwritten.

## Repeated overlap search

Immediately before the validation pass, the exact and semantic skills.sh queries
were repeated. The semantic results were unchanged. Exact-query results changed
to Rive, SVG, PixiJS and illustration style guides. The newly adjacent
`owl-listener/designer-skills@illustration-style` body was inspected: it specifies
visual-language and application guidance, but not an authored reveal renderer,
material masks, score-time mapping or replay lifecycle. GitHub API evidence:
unarchived, pushed 2026-09-05, MIT. No text or code was copied. The distinct local
technique decision remains appropriate.

## First application to the real project

Applied the installed skill's checklist to both accepted `pat-portfolio`
illustrations after the shared studio consolidation at `c4fce77`.

| Check | Evidence and finding |
| --- | --- |
| Accepted source and geometry | Source watercolor PNG files and painting engine unchanged. Ichiro canonical score modules moved with only import/format changes; prior accepted settings remain 1.8s / white follows brush and Rainier 2.4s / connected surfaces / 8vw, 4svh, 107%. |
| Actual reveal technique | Authored ink paths, sequential pigment contacts and local source glazes remain. The shared engine still includes regional residual interpolation; it is not a recording of real brushwork, nor is every pixel individually authored. |
| White and transparent materials | Ichiro's local cloth arrival remains distinct from its broader interior guard. Rainier's connected support applies to can/lid/napkin, not all clear glass. Saved light/dark frames show the accepted final compositing. |
| Visible gesture budget | Rainier's important initial foam and foot passes remain 2.4 score-seconds, approximately 241ms inside the 2.4s hover mapping. The shared clock preserves bloom lead separately. |
| Shared system | One controller/player/rail with subject-specific adapters. Tests cover settings isolation, preparation cancellation, retry and public triggers without preview query parameters. |
| Lifecycle and motion | Repeat-replay tests cover delayed ambient frames and reset. Timeline tests cover interruption, reduced motion and completion. Renderer ambient tests retain continuous seeded bubbles and one non-looping droplet above the glass base. Browser replay, slow review, keyboard selection and reduced-motion preview were exercised. |
| Actual homepage | Built production homepage exposes both words without developer controls. Desktop and 390 × 844 browser review checked placement and subject switching. Shared-studio frames are saved in the project. |
| Regression gates | Project suite passed 285 tests; repository lint and production build passed. The dev server remains in its detached session on port 3002. |

No new watercolor or image generation was started. The audit preserved the
accepted design rather than opening another speculative art-direction pass.
The remaining texture reconciliation is documented as an approximation, not
misrepresented as a fully painted source.

## Baseline and behavioral claim

The retrospective baseline is the actual project correction history: repeated
whole-region fades, geometry replacement at finishing, source detail appearing
then being covered, and replay clock reuse. The with-skill application explicitly
checked each cause against source and runtime evidence and retained the existing
fixes. This supports the skill's relevance and demonstrates its local use; it
is not a controlled fresh-agent with/without-skill benchmark. Automatic routing
and comparative model effectiveness remain unmeasured, so the inventory status
stays `pilot`. No public release or quality-superiority claim is made.
