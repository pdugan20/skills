# Per-page review rubric

The operational checklist `review-mintlify-docs` runs on each page. Use it with
`editorial-playbook.md` and the holistic read to build the per-page punch list.
Categories below match the punch-list grouping.

## Frame and title (section 4)

- [ ] `title` set and concise.
- [ ] `description` is a real sentence (SEO/search snippet), not a label.
- [ ] `icon` set, and consistent with the other pages in its tab.
- [ ] `sidebarTitle` used if the title is long.
- [ ] Frontmatter values containing a colon-space are quoted (an unquoted
      `title:`/`description:` value with a colon followed by a space breaks
      YAML parsing and the build).
- [ ] The page leads with the differentiator, not the crowded category.
- [ ] "What it does" is 2 to 4 capability pillars, not a feature dump.

## Voice (section 4)

- [ ] Second person, present tense, imperative.
- [ ] Short paragraphs.
- [ ] No em dashes (grep the em-dash character).
- [ ] No emojis, no exclamation marks.
- [ ] No hardcoded drift-prone counts ("37 tools") in hand-written prose.
- [ ] Implementation jargon stripped from user-facing pages (capability kept,
      mechanism dropped). Reference/concepts pages may be more technical.
- [ ] One consistent fictional example if sample output is shown.

## Callouts (section 4)

- [ ] `<Note>` (blue) is the default for advisories.
- [ ] `<Warning>` (yellow) only for the genuinely irreversible.
- [ ] No `<Tip>` (green); demote nice-to-knows to prose.
- [ ] No stacked callouts (two colored boxes back-to-back).
- [ ] Client-side MCP gating documented once on the MCP server page, not repeated
      per guide.

## Links (section 4)

- [ ] Linked once, on first meaningful mention; not double-linked nearby.
- [ ] Linked to the most specific relevant page (per-domain reference beats a
      generic overview).
- [ ] One source of truth per fact; pages forward to the canonical page.
- [ ] On feature/integration guides: a single one-line "From Claude" nudge that
      links MCP setup and the per-domain tool reference (does not dump tool names
      inline).

## Code examples (section 4)

- [ ] All code blocks language-tagged.
- [ ] Config and `.env` blocks use code-block titles (filename in the title bar).
- [ ] Inline `#` comments short and aligned; block does not scroll horizontally.
- [ ] Runnable copy-paste preferred over shell plumbing in a quickstart.
- [ ] Realistic-but-clean paths; volume prefixes and noise dropped.
- [ ] Real values where safe; placeholders for secrets and domains
      (`<your-token>`, `mcp.example.com`).

## Components by shape (section 4)

- [ ] Linear setup uses `<Steps>` with `titleSize="h3"` (so steps feed the TOC).
- [ ] Client/OS/shell variants use `<Tabs>`.
- [ ] Optional/advanced detail uses `<Accordion>` / `<AccordionGroup>`.
- [ ] Next steps / cross-sell use `<CardGroup>`.
- [ ] Section `##`/`###` headings are short (they feed the right-rail TOC).

## Verify against source (section 4)

- [ ] Command names, arg names, flags, and limits checked against the code.
- [ ] No guessed behavior; tool behavior verified against official docs.
- [ ] Generated pages (reference, changelog) not hand-edited.

## Page-type specifics

- **Quickstart:** zero to first win, linear, no detours; copy-paste works on a
  clean machine.
- **Requirements:** "what each integration needs" as a table (`Extra |
  Credentials`); gotchas surfaced here, not buried in a guide.
- **Troubleshooting:** bucketed by area; points at self-diagnostic (`doctor`)
  tools rather than re-explaining setup.
