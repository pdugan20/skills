# Skill Candidate: Feature Spike

- **Inventory ID:** `SC-010`
- **Status:** `released`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-30

## Intent

- **Outcome:** Resolve one important product or technical uncertainty with the
  smallest credible runnable slice, then make a `continue`, `change`, `stop`,
  `defer`, or `inconclusive` decision before production investment.
- **Trigger:** Patrick asks to spike, probe, prototype, or prove a feature,
  capability, integration, or architecture before deciding whether or how to
  build it.
- **Artifact:** A lightweight decision contract, bounded implementation,
  observed evidence and limitations, a decision, resulting plan changes, and an
  explicit disposition for the spike code.
- **Non-goals:** Comparing multiple UI directions, implementing an approved
  production feature, hardening completed code, tuning an established system
  through its existing experiment harness, or research that needs no runnable
  evidence.

## Real evidence

Three completed examples show that the reusable result is not merely "write less
code." The spike must preserve the real uncertainty, identify invalid test
conditions, and support more outcomes than a binary go or no-go.

### Representative examples

1. **Third-party audiobook capability probe:** A dependency-free native CLI
   exercised authentication, server discovery, real library shapes, remote
   chapter extraction, direct playback, progress write-back, and an entitlement
   question before committing to a client. The probe removed a planned backend
   service after demonstrating that remote chapter extraction was fast on the
   client, exposed contract and real-data traps that documentation did not, and
   left the entitlement result explicitly inconclusive because the account and
   network conditions invalidated the test. The source was deliberately
   throwaway; findings and discovered contract cases moved into the real app.
2. **Headless native-test proof of concept:** A representative Swift package
   extraction demonstrated a 9–12x test speedup. The evidence supported the
   architecture, but the migration was deferred because release timing and
   extraction cost made immediate production investment wrong. The proof of
   concept was removed while the measurements and phased migration plan were
   retained.
3. **Generative design-tool experiment:** A proof of concept tested whether a
   new platform capability could populate a real design-system component. The
   experiment exposed limits in the agentic tool, so the objective survived
   while the implementation medium changed: the idea was exported and built as
   a conventional plugin. A failed first path therefore produced a successful
   `change` decision rather than a rejected product outcome.

The related-shows recommendation system supplies an adjacent negative boundary.
Its versioned `ship`, `iterate`, and `abandon` experiments tune an already
approved production capability through a dedicated harness. Those runs should
not trigger a general feature spike unless the question is whether the feature
or architecture should exist at all.

### Repeated corrections

- Do not shrink the implementation until it no longer exercises the risky
  boundary. Build the smallest decisive slice, not the fewest lines of code.
- Do not invent a universal success threshold. Establish a current baseline or
  record an explicit user decision rule.
- Do not interpret an observation from invalid conditions as a pass.
- Do not reduce every result to go or no-go. `Change`, `defer`, and
  `inconclusive` preserved important distinctions in the completed examples.
- Do not let polished UI, generalized architecture, strict TDD, or release
  machinery turn a bounded experiment into an accidental production feature.
- Do not let throwaway code silently graduate. Carry findings, fixtures, and
  contract tests forward deliberately; production delivery starts separately.

### Sensitive material

The evidence above is sanitized. Credentials, account identifiers, private
server names, real user data, production configuration, and unreleased product
details remain outside this repository and its evals.

## Mechanism decision

- **Decision:** Create a portable `feature-spike` skill with one evidence
  reference and one reusable decision-brief asset.
- **Classification:** Pattern skill.
- **Rationale:** Capable agents already infer that a spike should be small and
  reversible. The non-obvious recurring value is the decision pattern:
  preserve the uncertainty under test, define conclusive and invalid
  conditions, avoid invented thresholds, distinguish five decision outcomes,
  and control whether the code is discarded or carried forward. This requires
  judgment across products and platforms, so a script or always-on instruction
  would be too rigid.
- **Scope:** Broadly portable across native, web, backend, platform, and tool
  feasibility questions. Repository-specific commands and safety rules remain
  local.

## Reusable contents

- **Instructions:** Routing boundaries, the decision contract, slice selection,
  proportional implementation, evidence evaluation, decision semantics, and
  production handoff.
- **Scripts:** None. Measurements and probe commands are project-specific.
- **References:** Evidence strategies for capability, architecture, product
  value, and platform/tool questions.
- **Assets:** A durable feature-spike brief with validity, results, decision,
  remaining-evidence, and code-disposition sections.
- **Dependencies:** Only the target project's runtime, representative safe
  inputs, and any explicitly authorized external access.

## Safety and boundaries

- Use local, development, synthetic, anonymized, or otherwise safe data by
  default.
- Never commit credentials, personal data, private responses, or production
  configuration to a probe or findings report.
- Identify the environment and require explicit approval before live mutation,
  paid resource creation, deployment, destructive cleanup, or exposure.
- `code-native-ui-ideation` owns comparison between visual directions.
- `feature-delivery` owns approved production implementation and rollout.
- `production-hardening` owns explicit release-readiness review.
- Ordinary research owns questions that do not require runnable evidence.

## Evaluation plan

### Execution

1. A third-party media integration probe should exercise the real boundary,
   define invalid entitlement conditions, protect credentials, return mixed
   evidence, and exclude product architecture.
2. A native-package performance proof of concept should compare equivalent
   representative behavior, separate and repeat measurements, avoid an invented
   threshold, record migration friction, and permit `defer`.
3. An AI summary value slice should use privacy-safe representative inputs,
   establish usefulness evidence, separate value from feasibility, avoid
   production infrastructure, and declare code disposition.
4. A platform extension proof of concept should test the real extension point
   and allow a `change` decision that preserves the product objective.
5. A mixed-results follow-up should reject a false green when one observation
   was produced under invalid conditions.

### Routing

- **Should trigger:** Kill-or-continue feature spikes, capability probes,
  architecture proofs of concept, bounded product-value slices, external
  platform feasibility tests, and experiments that decide whether to invest.
- **Should not trigger:** UI direction comparison, approved production feature
  implementation, hardening, documentation-only research, post-spike
  production migration, established parameter experiments, bug fixes,
  deployments, operational metric spikes, and implementation planning.

### Baseline

Use no skill. Three fresh-context baseline responses on 2026-07-30 showed that
capable agents already proposed bounded, reversible slices with reasonable
evidence:

- The integration response identified five pass/fail probes and excluded
  production architecture, but did not define invalid or inconclusive
  conditions or the broader decision semantics.
- The package response selected a representative seam and before/after
  measurement, but invented a roughly 2x success threshold and reduced the
  result to proceed or do not proceed.
- The product-value response proposed privacy-safe snapshots and useful
  feedback, but invented "most reviewers" as a gate and omitted explicit
  disposition, invalid-result handling, and the distinction between useful
  fixtures and system feasibility.

Keeping the skill requires fresh forward responses to preserve the concise
default behavior while consistently adding validity conditions, accepted
decision rules, non-binary outcomes, and code disposition without escalating
into production delivery.

### Forward evidence

The first three fresh-context responses loaded the pilot skill and preserved the
concise default scope:

- The architecture case compared equivalent representative seams, retained raw
  repeated samples, avoided an invented performance threshold, and kept the
  production migration separate.
- The integration case added real-boundary validity conditions and explicit
  code disposition, but initially treated five unknowns as one all-or-nothing
  gate.
- The product-value case separated value from production feasibility, but
  initially invented a five-day budget and a participant count despite the
  rule against invented decision thresholds.

Those failures produced two tighter rules: classify each unknown as a blocker,
modifier, or commercial or exposure gate before aggregating results; and keep
budgets, samples, audiences, and observation windows provisional until their
basis is known and the decision owner accepts them.

Three fresh retries then:

- classified authentication, browsing, playback, and progress as blockers,
  chapters as a scope modifier, and entitlement as a commercial gate;
- kept arbitrary budgets and samples provisional;
- used current baselines or owner-approved thresholds;
- stated all five decision outcomes, including `defer`;
- preserved throwaway-code boundaries and a separate production handoff.

The pilot therefore adds observable decision quality without making the default
responses substantially heavier.

### Release evidence

- Patrick Skills
  [v2.3.0](https://github.com/pdugan20/skills/releases/tag/v2.3.0) points to
  merge commit `02c72fede745213fc4f3807b4d213567d170d762`.
- The release job completed successfully and used the matching curated
  changelog section.
- The release archive digest is
  `d596343375178e26cbb0f1a7748f8a2f25624e76e34d925aa99e921248629ebd`;
  its eight skill folders match the tag.
- A clean Skills CLI installation from `pdugan20/skills@v2.3.0` copied all
  eight tagged skill trees byte-for-byte into the Claude Code, Codex, and Cursor
  layouts.
- Patrick Plugins
  [v3.2.0](https://github.com/pdugan20/plugins/releases/tag/v3.2.0) pins the
  exact skill release. Its Claude Code and Codex marketplace installation smoke
  test passed before publication.

## Definition of done

- [x] Mechanism and scope are approved.
- [x] Reusable resources are implemented and referenced.
- [x] Structural and repository validation passes.
- [x] Execution and routing eval coverage is authored.
- [x] Representative with-skill and baseline results are reviewed.
- [x] Claude Code, Codex, and Cursor installation layouts are checked.
- [x] Version, changelog, distribution metadata, and installation are verified.
- [x] Inventory status and lessons are updated.
