// Produced by the Figma generative plugin tool for the Button/Primary probe.
const componentSet = figma.root.findOne(
  (node) => node.type === "COMPONENT_SET" && node.name === "Button/Primary",
) as ComponentSetNode | null;
if (!componentSet) {
  figma.closePlugin("Button/Primary is not in this file.");
} else {
  const instance = componentSet.defaultVariant.createInstance();
  instance.setProperties({ Label: "Start trial", Size: "Large" });

  const collections = await figma.teamLibrary.getAvailableLibraryVariableCollectionsAsync();
  const theme = collections.find((collection) => collection.name === "Theme");
  if (theme) {
    const variables = await figma.teamLibrary.getVariablesInLibraryCollectionAsync(theme.key);
    const accent = variables.find((variable) => variable.name === "Surface/Accent");
    if (accent) {
      const imported = await figma.variables.importVariableByKeyAsync(accent.key);
      const collection = await figma.variables.getVariableCollectionByIdAsync(imported.variableCollectionId);
      const dark = collection?.modes.find((mode) => mode.name === "Dark");
      if (collection && dark) {
        instance.setExplicitVariableModeForCollection(collection, dark.modeId);
      }
    }
  }
  figma.closePlugin("Populated and themed Button/Primary.");
}
