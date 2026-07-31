# Node, React, and TypeScript projects

Use the selected framework's maintained generator and keep provider setup
separate from the local scaffold.

## Scaffold

- Choose the framework from the product's rendering, routing, hosting, and
  runtime requirements. Use its current official generator and noninteractive
  options rather than recreating remembered output.
- If the generator cannot write user cache or preference state, redirect that
  state to a task-specific temporary directory and make the single permitted
  retry. Do not inspect or patch the generator, spoof the runtime platform,
  query current package versions, or hand-build a lookalike scaffold.
- Preserve the generator's structure and lockfile. Pin the package manager and
  supported Node range using the repository family's established mechanism.
- Keep the generated screen minimal; scaffolding does not include the first
  product feature.

## Local contract

- Enable strict TypeScript for TypeScript projects and use the framework's
  maintained lint configuration.
- Expose one verification command that composes the checks that exist: format,
  lint, typecheck, tests, project-specific validation, and production build.
- Add tests based on behavior and risk. A placeholder can be verified by lint,
  types, and build without a synthetic coverage target.
- For maintained repositories, check in CI, dependency automation, runtime
  pins, agent guidance, and a stable aggregate required job.

## Hosting and services

Link Vercel or another provider only when the repository actually depends on
that provider and the user authorized resource access. Environment download,
project linking, analytics, flags, storage, cron, and deployment are separate
operations, not defaults of a React scaffold.

Do not accept a forced audit fix that downgrades or replaces the selected
framework. Explain upstream advisories, verify the maintained compatible
version, and leave risky upgrades or overrides for an explicit decision.
