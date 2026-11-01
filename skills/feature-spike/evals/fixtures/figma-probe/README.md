# Generative plugin probe

Question: can a Figma generative plugin populate and theme `Button/Primary`
from Design System v4?

- `component.json` is the component as exported from the library file.
- `generative/code.ts` is the plugin code the generative plugin tool produced.
- `runs/` holds one run against a local mock of the plugin API and one run in
  Figma desktop.

No normal plugin exists yet.

## Notes from Dana

The desktop run settles it: generative plugins can't reach library variables.
My retry with local variables themed the button fine, so if we export to a
normal plugin and bundle the variables, theming works. Someone on the Figma
forum also said generative plugins can't use `teamlibrary`.
