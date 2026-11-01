# Run: Figma desktop, 2026-10-29

Ran the generative plugin from the Figma desktop app in the `Probe sandbox`
file.

| Check | Result |
| --- | --- |
| Instance created | pass |
| Label set to "Start trial" | pass |
| Size set to Large | pass |
| Icon swapped to Icon/Check | no error, but the instance still shows Icon/ArrowRight |
| Theme collection found | fail |

`figma.teamLibrary.getAvailableLibraryVariableCollectionsAsync()` threw:

```text
Error: figma.teamLibrary is not available in this context.
```

Asking the generative plugin tool to add a `teamlibrary` permission returned:

```text
Manifest changes are not supported for generative plugins.
```

## Retry with local variables

Dana replaced the `teamLibrary` lookup with
`figma.variables.getLocalVariableCollectionsAsync()`. It found a `Theme`
collection in the file, and the Dark mode applied to the instance.

| Check | Result |
| --- | --- |
| Theme collection found | pass |
| Dark mode applied | pass |

## File setup

`Probe sandbox` was duplicated from the Design System v4 source file on
2026-09-14, so its `Button/Primary`, `Icon/*` components and `Theme`
collection are local copies. In Assets > Libraries, the published Design System
v4 library is listed but switched off for this file.
