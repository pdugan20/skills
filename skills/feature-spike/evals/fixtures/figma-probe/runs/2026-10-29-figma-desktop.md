# Run: Figma desktop, 2026-10-29

Ran the generative plugin from the Figma desktop app in the `Probe sandbox`
file, which uses the Design System v4 library.

| Check | Result |
| --- | --- |
| Instance created | pass |
| Label set to "Start trial" | pass |
| Size set to Large | pass |
| Icon swap kept the library icon | pass |
| Theme collection found | fail |

`figma.teamLibrary.getAvailableLibraryVariableCollectionsAsync()` threw:

```text
Error: figma.teamLibrary is not available. Add "teamlibrary" to permissions in manifest.json.
```

Asking the generative plugin tool to add the permission returned:

```text
Manifest changes are not supported for generative plugins.
```

The theme steps did not run, so mode switching on the instance is untested.
