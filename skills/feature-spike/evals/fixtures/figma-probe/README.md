# Generative plugin probe

Question: can a Figma generative plugin populate and theme `Button/Primary`
from Design System v4?

- `component.json` is the component as exported from the library file.
- `generative/code.ts` is the plugin code the generative plugin tool produced.
- `runs/` holds one run against a local mock of the plugin API and one run in
  Figma desktop against the real library file.

No normal plugin exists yet.
