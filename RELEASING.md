# Releasing

`pdugan20/skills` is a versioned skill collection and dual-runtime plugin. It is
not published to npm. A release is complete only when the tagged source,
curated GitHub Release, packaged archive, and exact-tag installation agree.

## Prerequisites

- Work from a release branch based on current `main`.
- Keep `package.json`, `package-lock.json`, and both plugin manifests on the
  same semantic version.
- Protect `main` with pull requests and the `Verify skills` and
  `Audit workflow security` checks.
- Protect `refs/tags/v*` from deletion and updates so release tags are
  immutable.
- Authenticate `gh` before the external publication steps.

## Prepare the release

1. Move completed entries from `[Unreleased]` into a dated version section.
2. Update the package and plugin versions. Use a minor release for compatible
   skill additions and a major release only for breaking collection contracts.
3. Keep skill candidate inventory rows at `validated` until exact-tag
   installation succeeds.
4. Run the release gates:

   ```bash
   npm ci
   npm run verify
   npm run validate:external
   gh skill publish --dry-run
   python3 scripts/validate_repository.py --release-tag "v$VERSION"
   python3 scripts/release_notes.py "$VERSION"
   ```

5. Open a pull request and merge only after the required checks pass.

The GitHub skill command remains a preview audit. Do not run
`gh skill publish` without `--dry-run`; this repository's release workflow
publishes the curated changelog section instead of generated notes.

## Publish and verify

After the release commit is merged:

```bash
git switch main
git pull --ff-only
git tag -a "v$VERSION" -m "v$VERSION"
git push origin "v$VERSION"
gh run watch --repo pdugan20/skills \
  "$(gh run list --repo pdugan20/skills --workflow Release --limit 1 --json databaseId --jq '.[0].databaseId')" \
  --exit-status
```

Then verify:

1. The GitHub Release notes equal the matching changelog section.
2. The attached archive contains the same skill folders as the tag.
3. A clean installation from `pdugan20/skills@v$VERSION` succeeds for Claude
   Code, Codex, and Cursor and matches the tagged files byte-for-byte.
4. The skills appear through Skills CLI discovery.
5. Only after those checks pass, change the skill candidate inventory rows from
   `validated` to `released` and update downstream marketplace pins.

If publication fails after the tag is pushed, repair or rerun the release
workflow. Do not move or recreate the tag at a different commit.
