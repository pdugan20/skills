# Mintlify site scaffold playbook

Use this playbook to make project-specific scaffolding decisions. Verify
Mintlify syntax and deployment behavior against the current official
documentation whenever those mechanics matter.

## Contents

- [Establish the source and boundary](#establish-the-source-and-boundary)
- [Shape the information architecture](#shape-the-information-architecture)
- [Set editorial defaults](#set-editorial-defaults)
- [Choose brand defaults](#choose-brand-defaults)
- [Wire the local toolchain](#wire-the-local-toolchain)
- [Treat publishing separately](#treat-publishing-separately)
- [Scaffold completion checklist](#scaffold-completion-checklist)

## Establish the source and boundary

Inspect the project before proposing a structure:

- Identify the product's primary users, first useful outcome, and unusual hook.
- Detect CLI entry points, MCP servers, HTTP APIs, SDKs, and existing guides.
- Locate authoritative sources such as command introspection, MCP schemas, and
  OpenAPI documents.
- Preserve existing documentation, build tooling, branding, and repository
  conventions.
- Distinguish local scaffolding from Git provider setup, hosted deployment,
  custom domains, and DNS changes. The latter are separate external actions.

Do not create a parallel source of truth. Documentation belongs beside the
product source when that is the repository's chosen model. If documentation is
hosted elsewhere, document how it stays synchronized before generating a second
copy.

## Shape the information architecture

Keep tutorial, how-to, reference, and explanation content distinct:

- **Tutorial:** a linear quickstart from zero to the first useful result.
- **How-to:** task-focused guides that assume setup is complete.
- **Reference:** exhaustive, source-backed CLI, MCP, API, and configuration
  material.
- **Explanation:** architecture, concepts, and rationale.

Organize navigation for how readers scan, not around these abstract labels. A
typical technical product might use:

```text
Guides
  Getting started
  Everyday use
  Integrations
  Claude (MCP), when relevant
  Concepts
  Help

Reference
  CLI, when relevant
  MCP, when relevant
  API reference, when relevant
  Configuration
```

Avoid a flat group longer than roughly five pages. Include Quickstart,
Requirements, and Troubleshooting unless the project genuinely has no need for
one. Add only pages that the project can support with real content.

For OpenAPI 3.0 or 3.1 sources, prefer Mintlify's native `openapi` navigation to
hand-generated endpoint pages. Keep an overview page only when it adds useful
framing that the specification does not contain.

## Set editorial defaults

- Give every page a specific title, sentence-length description, and consistent
  icon treatment.
- Lead with the project's differentiator, then explain two to four capability
  pillars.
- Write in second person, present tense, with short paragraphs and concrete
  nouns.
- Use `<Note>` for important advice and `<Warning>` only for destructive or
  difficult-to-reverse consequences.
- Prefer `<Steps>` for linear setup, `<Tabs>` for real variants,
  `<AccordionGroup>` for optional troubleshooting, and `<CardGroup>` for next
  steps.
- Use placeholders only as valid MDX comments. Starter pages must parse before
  their TODOs are completed.
- Never guess commands, flags, fields, limits, or tool names. Point reference
  generation at authoritative source instead.

## Choose brand defaults

Offer two or three plausible visual directions derived from the product rather
than defaulting to template indigo. For each direction, provide:

- a primary color with legible light and dark variants;
- a short rationale connected to the product;
- a differentiator-led introduction hook;
- any logo or favicon work that remains intentionally placeholder.

Do not claim accessibility from intuition. Run
`scripts/check_contrast.py <foreground> <background>` with the exact surface
colors before reporting a ratio or pass level. Label candidate values
provisional when their surfaces are unknown. Keep logos and social images
project-owned; the scaffold supplies only clearly marked placeholders.

## Wire the local toolchain

Adapt the bundled Makefile targets to the project's package manager instead of
overwriting an existing Makefile. Current Mintlify CLI checks include:

- `mint dev` for local preview;
- `mint validate` for strict configuration, content, and OpenAPI validation;
- `mint broken-links --check-anchors --check-redirects` for internal link and
  navigation integrity;
- `mint a11y` when visual assets and final colors are present.

Add source-freshness checks only for generated material. A drift job should run
the same generator used locally and fail on a resulting diff.

## Treat publishing separately

Local scaffolding does not authorize publication. When publishing is requested:

1. Check Mintlify's current onboarding and Git provider guidance.
2. Prefer the direct repository or supported subdirectory configuration unless
   the user has a concrete reason for a separate documentation repository.
3. Identify every external mutation: GitHub App installation, repository
   creation, dashboard configuration, deployment, domain, and DNS.
4. Obtain explicit authorization before performing those actions.
5. Verify the live deployment and rollback path independently from local
   validation.

Do not encode historical pricing or account-limit workarounds as permanent
architecture. Re-check current product capabilities when a constraint matters.

## Scaffold completion checklist

- [ ] Existing documentation and tooling were inspected and preserved.
- [ ] Product surfaces and authoritative reference sources were detected.
- [ ] Brand and navigation choices were presented and confirmed.
- [ ] The generated `docs.json` contains only relevant groups and valid paths.
- [ ] Starter MDX parses with valid frontmatter and comments.
- [ ] Local preview, validation, and link commands are wired proportionally.
- [ ] Generated reference work is clearly handed off.
- [ ] No repository, account, deployment, domain, or DNS mutation occurred
      without authorization.
