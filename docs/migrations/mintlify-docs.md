# Migrate from Mintlify Docs

The four skills formerly distributed from `pdugan20/mintlify-docs` now live in
the `pdugan20/skills` collection. Install the combined collection once:

```bash
npx skills@latest add pdugan20/skills
```

Marketplace users should replace `mintlify-docs@patrick-plugins` with
`patrick-skills@patrick-plugins`.

## Skill names

| Former name | Current name |
| --- | --- |
| `scaffold-mintlify-site` | [`scaffold-mintlify-site`](../../skills/scaffold-mintlify-site/SKILL.md) |
| `review-docs` | [`review-mintlify-docs`](../../skills/review-mintlify-docs/SKILL.md) |
| `document-reference` | [`generate-mintlify-reference`](../../skills/generate-mintlify-reference/SKILL.md) |
| `changelog-writer` | [`write-mintlify-changelog`](../../skills/write-mintlify-changelog/SKILL.md) |

The explicit names avoid collisions in global Skills CLI installations. The
new copies are self-contained: references, scripts, assets, runtime metadata,
and evaluations travel with each skill rather than depending on files at the
old repository root.

## Invocation

Use the current skill name for explicit invocation. Plugin namespaces depend on
the client, but the package is now `patrick-skills` instead of `mintlify-docs`.
Existing installations of the old plugin remain pinned to their historical
release; remove that plugin after the combined collection is installed.

## Version history

`pdugan20/skills` versions the collection as a whole. Skill-specific changes
are named and linked in the repository [changelog](../../CHANGELOG.md). The old
repository remains archived as read-only migration and release history.
