# Python projects

Use current `uv` project generation as the starting point unless the user or an
existing repository family has another maintained standard.

## Scaffold

- Run `uv init --help`, then choose the current application, package, library,
  or script shape that matches the distribution surface. Prefer a `src` layout
  for distributed packages when the generator supports it.
- Keep authoritative metadata in `pyproject.toml` and commit `uv.lock` for
  applications, tools, and reproducible development. Record supported Python
  versions instead of assuming the interpreter currently installed is the
  entire compatibility range.
- Do not hand-author a replacement for generator output merely because the
  generator cannot write cache state. Redirect its cache to a task-specific
  temporary directory or report the blocker.

## Local contract

- Use Ruff for format and lint when no repository standard overrides it. Add
  pytest when behavior exists and choose a maintained type checker when the
  package's users benefit from typed compatibility.
- Expose one repository-native verification entry point that CI also runs.
  This may be a checked-in script or the existing task runner; do not add a
  task-runner dependency only to rename a short command.
- Set coverage thresholds from regression risk and existing evidence. Never
  impose 100% merely because the placeholder currently achieves it.
- Validate a shipping package with a wheel and source build plus package
  metadata inspection.

## Publication readiness

For a public distributed package, resolve the license, package name, repository
URLs, supported Python classifiers, changelog/version policy, security contact,
and contribution boundary. Prefer trusted publishing with a protected GitHub
environment over stored registry tokens.

Do not select a license, author or publisher identity, security contact,
repository URL, or registry owner on the user's behalf. A conventional choice
is still an ownership decision: leave it explicit and deferred until confirmed.

Keep the release workflow inert until the repository and registry identity
exist. Scaffolding may verify build artifacts; it must not reserve a name,
configure credentials, tag, create a release, or publish.
