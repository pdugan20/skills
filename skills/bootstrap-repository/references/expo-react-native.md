# Expo and React Native projects

Let Expo own framework compatibility; let the repository own its quality and
release contract.

## Scaffold

- Start with the current documented `create-expo-app` command and template.
  Inspect current help or versioned Expo documentation instead of freezing a
  copied starter or guessed SDK template in the skill.
- If global cache, preference, or telemetry state blocks the generator, use its
  documented noninteractive controls and redirect only that state for the
  single permitted retry. Do not inspect or patch bundled generator code.
- Preserve the generated lockfile and agent instructions. Set the app name and
  slug, but defer permanent bundle identifiers, package names, Expo ownership,
  signing, and EAS project linkage until those identities are known.
- Follow Continuous Native Generation when the selected template uses it.
  Commit native directories only when the project intentionally owns native
  changes.
- Install native packages with `npx expo install` and use `npx expo install
  --fix` plus Expo Doctor when reconciling compatibility.

## Local contract

- Pin the supported Node major and package manager, then use the generated
  lockfile for clean installs.
- Expose one verification command that includes Expo Doctor, format, lint,
  TypeScript, tests, and build/export checks that actually exist.
- Add tests according to current behavior and risk; do not invent a coverage
  threshold for a starter shell.
- Add Storybook only when isolated component development is part of the stated
  process.
- Document that `EXPO_PUBLIC_` values are embedded in the client and are not
  secrets.

## Automation

For a maintained app, check in CI and compatibility-aware dependency updates.
Use a stable aggregate CI job as the required check. Treat Expo, React Native,
React, and tightly coupled native packages as a coordinated SDK upgrade rather
than independent automatic merges.

Add development builds, EAS Update, store builds, credentials, channels, and
rollout policy only when the shipping surface is explicit. Scaffolding never
authorizes EAS project creation, signing, submission, or publishing.
