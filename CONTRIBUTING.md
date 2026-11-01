# Contributing

These notes are for maintaining the collection. To install the skills, see the
[README](README.md#install).

## Set up

Install two tools:

- [Node.js](https://nodejs.org/) 22.22.2 or later. `.nvmrc` pins the version CI uses.
- [uv](https://docs.astral.sh/uv/) 0.11 or later. You don't need to install
  Python yourself.

Then install dependencies and run the checks:

```bash
npm ci
npm run verify
```

`npm ci` also installs the pinned Claude Code CLI that `verify` uses to validate
the plugin. The first command that runs Python creates `.venv` from
`.python-version` and `uv.lock`, so local runs, CI and releases use the same
environment.

## Common commands

| Command | What it does |
| --- | --- |
| `npm run verify` | Every local check: tests, repository validation, linting, type checks and formatting |
| `npm run validate` | Repository validation only: manifests, versions, eval files and README groups |
| `npm run format` | Format JSON and YAML with Prettier |
| `npm run evals:codex -- --skill <name> --max-runs <n>` | Run a skill's evals through Codex; this calls a model and uses your Codex allowance |
| `npm run check:skills-sh` | Compare the live skills.sh listing and security audits with this repository |

## The check only CI runs

CI also runs `npm run validate:external`, which needs
[skill-validator](https://github.com/agent-ecosystem/skill-validator) v1.8.0 on
your `PATH`. To run it locally without installing it:

```bash
go run github.com/agent-ecosystem/skill-validator/cmd/skill-validator@v1.8.0 check --strict --allow-dirs=agents,evals skills/
```

## Guides

- [Skill authoring standard](docs/skill-authoring.md): how skills, evals and
  their tooling are written and reviewed.
- [Skill candidate inventory](docs/skill-candidates.md): every candidate and its
  status.
- [Release guide](RELEASING.md): versioning, tagging and post-release checks.
