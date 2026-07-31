# Mintlify editorial playbook

Use this playbook for judgment during a Mintlify content and information
architecture review. Use the separate review rubric for the per-page checklist.
Verify current component, configuration, and CLI mechanics against official
Mintlify documentation rather than treating this editorial guidance as a schema
reference.

## Contents

- [Review the site as a system](#review-the-site-as-a-system)
- [Information architecture](#information-architecture)
- [Page framing and voice](#page-framing-and-voice)
- [Callouts, components, and links](#callouts-components-and-links)
- [Code and source fidelity](#code-and-source-fidelity)
- [Brand and accessibility](#brand-and-accessibility)
- [Generated content](#generated-content)
- [Validation and launch readiness](#validation-and-launch-readiness)

## Review the site as a system

Read `docs.json` before individual pages. Establish the navigation order, the
site's intended audience, the first useful reader outcome, and which product
sources can verify claims. Then review pages in navigation order so repetition,
missing transitions, and misplaced content stay visible.

For each page, first answer:

1. What job should this page perform?
2. Is it the right page type and location?
3. What is missing, redundant, unsupported, or misleading?
4. Does it need a change at all?

Present consequential wording or structural choices as two or three bounded
options plus a recommendation. Do not manufacture choices for objective defects
such as broken links or invalid frontmatter.

## Information architecture

Keep four content modes distinct:

- **Tutorial:** linear learning path to a first result.
- **How-to:** a focused procedure for an already oriented reader.
- **Reference:** exhaustive facts generated or verified from source.
- **Explanation:** concepts, architecture, and rationale.

Group navigation around reader tasks. Split flat groups that no longer scan
well, usually once they exceed roughly five pages. A CLI or MCP product often
benefits from separate Getting started, Everyday use, Integrations, Claude
(MCP), Concepts, Help, and Reference surfaces, but use only groups supported by
the product.

Check for Quickstart, Requirements, and Troubleshooting. Reference navigation
should separate CLI, MCP, API, and configuration domains when they are large
enough to deserve independent pages. Avoid `api` as a page path because
Mintlify reserves it in production.

## Page framing and voice

- Give every page a specific `title` and a sentence-length `description`.
- Keep navigation labels short with `sidebarTitle` when necessary.
- Apply page icons consistently within a navigation surface.
- Lead with the reader's outcome or the project's differentiator, not a broad
  category claim.
- Write in second person, present tense, and active voice.
- Prefer short paragraphs, concrete nouns, and named commands or fields.
- Remove implementation jargon from user-facing guides unless readers must
  invoke or observe it.
- Avoid hardcoded counts and time-sensitive claims unless they are generated or
  directly maintained from a source of truth.
- Quote frontmatter values containing a colon followed by a space.

Do not rewrite strong pages merely to impose a different personal cadence.
Review is successful when it improves reader outcomes and source fidelity, not
when every page changes.

## Callouts, components, and links

- Use `<Note>` for important advice.
- Reserve `<Warning>` for destructive, security-sensitive, or difficult-to-
  reverse consequences.
- Avoid decorative `<Tip>` callouts and stacked callout blocks.
- Use `<Steps>` for linear setup, `<Tabs>` for genuine variants,
  `<AccordionGroup>` for optional detail, and `<CardGroup>` for next steps.
- Link once on the first meaningful mention and target the most specific
  canonical page.
- Do not repeat reference facts in guides. Link to the generated reference.

When a project exposes an MCP surface, a guide may include one concise link to
the MCP setup and relevant domain reference. Do not dump tool inventories or
repeat client gating details on every page.

## Code and source fidelity

- Verify commands, options, fields, limits, and behavior against product source
  or current authoritative documentation.
- Prefer runnable examples over shell plumbing in quickstarts.
- Add language identifiers and meaningful titles to code blocks.
- Use safe real values where stable and explicit placeholders for credentials,
  domains, account IDs, and destructive targets.
- Never place production data, secrets, personal data, or private identifiers in
  documentation examples.
- Keep one coherent fictional data set across related examples.

If a claim cannot be verified, mark it as an open question instead of smoothing
it into confident prose.

## Brand and accessibility

Flag template defaults that were never deliberately chosen, including generic
indigo, placeholder logos, and mixed icon treatments. Review light and dark
modes, visible focus, text contrast, image alt text, and any custom components.
Use measured contrast results rather than visual intuition.

Check logo dimensions and aspect ratio to prevent layout shift. Treat the
favicon, social image, colors, domain, and logo as project-specific assets, not
shared house-style values.

## Generated content

Reference pages and other generated outputs are never hand-edited as their
long-term source. Find the generator or authoritative specification, change it,
regenerate, and verify a clean subsequent run.

For OpenAPI 3.0 or 3.1 documents, prefer Mintlify's native `openapi` navigation
and generated endpoint pages. Hand-author only framing that the specification
cannot express. For CLI and MCP references, require deterministic sorting,
generated banners, and CI that fails when regeneration changes committed output.

Mintlify changelog pages use their dedicated writing skill. Repository
`CHANGELOG.md` files are a separate release artifact.

## Validation and launch readiness

Run the checks relevant to the change:

- `mint validate` for strict configuration, content, and OpenAPI validation;
- `mint broken-links --check-anchors --check-redirects` for internal links;
- `mint a11y` for contrast and missing alternative text;
- `mint dev` for interaction and visual review.

Before calling a site launch-ready, also check:

- the quickstart on a clean environment;
- generated-content freshness;
- relevant desktop and mobile layouts;
- light and dark appearance;
- example safety and source accuracy;
- custom domain, HTTPS, deployment, and repository integration only when those
  external surfaces are actually in scope.

Report local content readiness separately from hosted deployment readiness.
