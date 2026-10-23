# Read-only repair checks

The bundled `scripts/repair_guard.py` validates local lossless PNG files using
Pillow. It does not generate, crop, composite, replace, or upload artwork. Use an
existing Python environment with Pillow, or an authorized dependency environment.

Save a JSON record with this shape; paths resolve relative to the record:

```json
{
  "schema": 1,
  "master": { "path": "master.png", "sha256": "actual-sha256", "size": [1254, 1254] },
  "mask": { "path": "mask.png", "sha256": "actual-sha256" },
  "target": { "path": "target.png", "sha256": "actual-sha256", "box": [130, 140, 300, 100] },
  "references": [],
  "diagnosis": "Record the observed source-versus-render finding.",
  "source_comparison": "Record which earlier sources were inspected and why this master is retained.",
  "boundary_review": "Record the inspected repair boundary, including feather.",
  "prompt": "Record the exact local edit prompt and ordered image roles.",
  "candidate_path": "candidate.png",
  "preserve_alpha": true
}
```

`mask.png` is an 8-bit grayscale PNG at master size. Zero protects a pixel;
every nonzero value, including feather coverage, permits a change. The crop box
is `[left, top, width, height]`. The edit target must be a decoded-pixel-identical
crop of the master and must contain the entire mask. A whole-image crop, empty
mask, all-permitting mask, changed input or source-overwriting destination fails.

Run these from the skill directory:

```bash
python scripts/repair_guard.py preflight /absolute/path/repair.json
python scripts/repair_guard.py invocation /absolute/path/repair.json /absolute/path/tool-args.json
python scripts/repair_guard.py composite /absolute/path/repair.json /absolute/path/composite.png
```

Preflight emits file identities, coverage counts and an exact built-in ImageGen
argument packet, with the local edit target first and optional references after
it. Invocation checks that packet without calling the image tool. This argument
adapter covers the built-in editor only; it does not validate Scenario or direct
API schemas, masks, model selection, cost or provider permission. Those paths
need their own established provider checks. Do not substitute this packet for
their request contracts.

Composite checks compare every protected RGBA pixel, including hidden RGB under
zero alpha. With `preserve_alpha: true`, alpha must match across the entire
image. Validate a separate lossless composite before any source replacement;
check delivery derivatives independently. Existing candidate files are allowed
for composite verification but rejected before another generation.

Nonempty diagnosis and review fields establish record completeness, not that
the agent's judgment is correct. Mask selection remains a scoped visual decision.
Passing these checks does not prove a good repair or an active runtime hook.
The checks are an accidental-drift guard, not a security boundary against an
agent that deliberately rewrites its own records, masks or guard code.

Run the executable regression checks with:

```bash
python -B -m unittest discover -s scripts -p 'test_repair_guard.py' -v
```
