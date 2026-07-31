# GitHub configuration

Treat checked-in automation and live repository settings as one contract with
two separate write boundaries.

## Inspect

Resolve an exact `OWNER/REPOSITORY`, then run the bundled inspector with
`--github`. Confirm visibility, default branch, description, homepage, topics,
merge policy, branch deletion, security status, and existing rulesets. Do not
infer live settings from `.github/` files.

## Prepare local files

- Give CI one stable aggregate job for branch protection. Other matrix and
  diagnostic jobs may remain visible without becoming required contexts.
- Configure Dependabot or the chosen maintained alternative for every package
  ecosystem and its real directory. Keep framework-coupled dependencies, such
  as Expo and React Native, on a coordinated upgrade path.
- Grant workflow permissions `contents: read` by default. Add the narrowest
  write permission only to the job that needs it.
- Add issue templates, contribution guidance, security reporting, changelog,
  release automation, and code ownership only when the profile and visibility
  justify them.
- Pin third-party actions according to the repository's supply-chain policy.

## Plan remote settings

Report each field as `current`, `proposed`, and `reason`:

- description, homepage, topics, visibility, and default branch;
- squash, merge-commit, and rebase policy plus automatic branch deletion;
- vulnerability alerts, automated fixes, secret scanning, and push protection
  where available;
- branch rulesets, pull-request requirements, review-thread resolution, and
  required status checks;
- deployment or release environments and protected immutable tag patterns.

Required status checks are observed outputs, not guesses. Let CI run first,
confirm the exact context in GitHub, and prefer the stable aggregate gate. A
ruleset plan must include the exact target branch or tag, bypass/recovery path,
and the command or UI path that can disable it if the check was misnamed.

## Apply and verify

Default to a plan. Create a repository or mutate settings only when the user
authorized that external write and the owner, repository, visibility, and
default branch are explicit. Apply one bounded repository at a time.

After applying, read the settings back, compare them with the plan, and report
any host-plan limitation. Do not push commits, create environments, upload
secrets, tag, release, publish, or deploy unless separately requested.
