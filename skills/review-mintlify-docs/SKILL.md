---
name: review-mintlify-docs
license: MIT
description: Reviews a Mintlify documentation site's information architecture, editorial quality, source fidelity, and launch readiness in navigation order, then makes approved targeted edits. Use for Mintlify site audits, content passes, or page-level reviews; do not use for general code review, changelog entries, or generated reference pages.
---

# Review Mintlify documentation

Run the house-style content and polish pass on a Mintlify docs site. This is the
editorial review, not the mechanics. When the official `mintlify` capability is
available, use it for current component and `docs.json` syntax. Otherwise inspect
the site's existing patterns and current Mintlify documentation instead of
guessing.

The authority for every rule cited here is the bundled editorial playbook:
[references/editorial-playbook.md](./references/editorial-playbook.md). Read it
first. This skill is the procedure that applies it; the operational rubric is in
[references/review-rubric.md](./references/review-rubric.md).

## The two non-negotiable habits

1. **Holistic read before edits.** For each page, first answer "what should this
   page do, and what is wrong, redundant, or missing?" Then recommend, then edit.
   Not every page needs work; say so when a page is already strong.
2. **Options-first.** For any wording or structure choice, present 2 to 3 options
   plus a recommendation and let the maintainer pick. Do not unilaterally rewrite
   while riffing.

## Instructions

### Step 1: Locate the site and read the nav

Find `docs-mintlify/docs.json` (or the path requested by the user). Read its
`navigation` to get the canonical page order. **The review walks pages in nav
order**, not file order. If the request names a single page, review just that
page but still load the nav for cross-link context.

Count the pages before starting the walk. Review up to 12 pages in one pass. For
larger sites, return the complete IA assessment plus a nav-ordered batch plan,
then review batches of at most 12 pages so findings stay specific and usable.
Do not silently sample pages or claim a full-site review from a partial read.

### Step 2: IA check first, before any page edits

Before walking pages, audit the navigation itself against the editorial
playbook:

- **Is any group a flat list longer than ~5 entries?** If so, it should be split
  into topic groups (Getting started / Everyday use / Integrations / Concepts /
  Help, plus domain-specific groups).
- **Is this an MCP server?** (Check for an `mcp-server`/`mcp-tools` page or an MCP
  reference.) If so, a dedicated **Claude (MCP)** group is mandatory, not folded
  into a generic guides list.
- **Are the "pages every project needs" present?** Quickstart, Requirements (or
  supported-X), Troubleshooting. Flag any that are missing.
- **Is the Reference tab split by domain** (CLI / MCP groups with per-domain
  pages plus an overview landing) once it has more than a couple of pages?

Report the IA findings and proposed nav reorg first. Reorganizing the nav is
step one of the pass; pages are then walked in the new order.

### Step 3: Per-page punch list

For each page in nav order, run the rubric in
[references/review-rubric.md](./references/review-rubric.md). Produce a per-page
punch list grouped by category (Frametitle / Voice / Callouts / Links / Code /
Components / Verify). Mark each item as a recommendation, not a done deal.
Omit empty categories and collapse consecutive strong pages into a concise
"no material findings" note. Report findings after the read; do not narrate the
file-by-file inspection process.

### Step 4: Apply, options-first

After the maintainer picks from the options, make targeted edits. Commit per page
if the user wants commits (small, logical commits). Never hand-edit generated
pages (reference, changelog); change the generator instead (see
`generate-mintlify-reference` and `write-mintlify-changelog`).

### Step 5: Link check and build

Run `mint validate` and
`mint broken-links --check-anchors --check-redirects` in `docs-mintlify/` after
the pass. Use `mint dev` when visual, interaction, responsive, or theme behavior
changed. Add `mint a11y` when final colors or media are in scope.

### Step 6: Pre-launch checklist

Before declaring done, run the playbook's launch-readiness checklist.
Report each item as pass/fail with the specific offending page or value.

## Brand red flags to always catch

These recur and are quick wins:

- **Generic indigo primary** (`#6366f1` or the Mintlify default) chosen by
  accident rather than deliberately.
- **Em dashes in body prose.** When
  fixing these, watch the frontmatter: a colon-space in an unquoted `title:`/
  `description:` breaks the build, so quote any value that gains a colon.
- **`<Tip>` callouts** or stacked callouts.
- **Pages with no `description` or no `icon`**.
- **Hardcoded drift-prone counts** ("37 tools") in hand-written prose.
- **Implementation jargon** on user-facing pages.

## Scope

This skill reviews and edits hand-authored MDX pages and the `docs.json` nav. It
does not touch generated reference/changelog output, deployment configuration,
or CI unless the user expands the scope explicitly.
