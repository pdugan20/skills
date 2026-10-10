# Verification record

Executed 2026-10-10 in an isolated checkout of `pdugan20/skills` on branch `codex/typography-visual-pilot`. Source base: `f2f8bed2407eee3884ebc3ef6fe8e2447e7d191a`.

- Chrome 155.0.8059.39; web capture at exact 1100×760 and 1100×900 viewports.
- Apple Swift 6.4, arm64 macOS 27.0; native `ImageRenderer` output 860×1700 pixels.
- Python 3.14 and Pillow 11.3.0 for assembling labeled boards and checking image files.
- Node 24.19.0 for repository checks, using the repository lockfile.
- No product checkout, running simulator, installed skill, release tag or global font installation changed.

## Completed checks

`validate-pilot.py` passed: six cases per arm, 54 roles per arm, allowed font/number contracts, all 18 treatment image dimensions, font file hashes, three OFL notices, actual page font-loading evidence for all fourteen web specimens, whitespace-normalized web copy equality across arms, no measured horizontal overflow or footer collision, no native geometry issues, and byte-identical duplicated native before images. Native wrapping also asserts preservation of normalized source text.

The native implementation agent inspected all seven unique native images. The orchestrator inspected all six comparison boards and individual browser/native examples. A separate reviewer inspected anonymous images; see its own record for aesthetic evidence. Technical checks do not resolve taste, rag quality or subtle optical balance.

Repository unit tests passed: 52. The source-tree installation check passed for 16 existing skills across portable Agent Plugin, Claude Code, Codex and Cursor packaging. Repository validator, strict Claude plugin validator, Markdown lint, JSON/YAML formatting and the existing Skills CLI catalog listing passed. The typography experiment is outside `skills/`, so it is intentionally absent from installed/routed skill catalogs.

The initial aggregate verify command stopped at a network-restricted installation check. That check was rerun with network access and passed; remaining stages were run individually. The first strict plugin validation lacked the native development binary because dependencies were initially installed with scripts disabled; the official locked dependency's setup was completed locally and strict validation then passed. No candidate's executable code was run.

The pinned dependency install reported 11 existing dependency audit findings (3 low, 2 moderate, 6 high). This experiment does not change the lockfile or claim to remediate those unrelated dependencies. External Agent Skills validation remains the repository's CI responsibility; no skill definition changed here.

## Delivery limitation

The supported Library upload helper reported that `prepare_uploads` was unavailable before uploading the batch. No confirmed Library files or IDs exist. Repository-hosted boards and report are the delivery fallback. Do not turn local paths or generated labels into invented Library IDs.
