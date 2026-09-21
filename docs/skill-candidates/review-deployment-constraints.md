# Skill Candidate: Review Deployment Constraints

- **Inventory ID:** `SC-021`
- **Status:** `pilot`
- **Owner:** Patrick
- **Last reviewed:** 2026-09-08

## Intent and evidence

Review a feature, integration, or tooling proposal against the requirements of
its actual target environments. Produce a sourced requirements inventory and
scoped findings, including missing authority and applicability evidence.

The originating private task concerned a feature-flag proposal whose draft
treated government hosting as a blanket hosted-service ban. Following its sources
revealed a mix of engineering decisions, recommendations, historical assessments,
customer-specific requests and a separate maintained accreditation library.
Repeated corrections distinguished what a document says from an approved rule,
platform authorization from application responsibility, and an internal prototype
from an operational deployment. A related feedback/screenshot workflow exercises
the same outcome with different data and external-service paths.

Private sources, customer names, control packages and implementation findings are
kept in the customer's internal documentation. This brief records only the
reusable failure pattern; all distributed fixtures are invented.

## Mechanism decision

Use a composite skill for applicability, source reconciliation and proposal review.
Keep customer requirements in internal human-maintained records; keep deterministic
code checks in their existing tools. A hardcoded compliance catalog would become
stale and overgeneralize. Always-on instructions would overtrigger on ordinary UI
changes. No new plugin, policy engine or credential integration is needed.

The method is portable. It does not certify compliance, perform general security
hardening, implement changes, or grant messaging/publication/deployment authority.

## External overlap gate

Skills CLI 1.5.21 searches on 2026-09-08 used `review-deployment-constraints`,
`deployment constraints`, `compliance requirements`, and `requirements traceability`.
The three closest accessible bodies were read with the CLI's `use` command for
inspection only, without adopting their instructions or installing them:

- [security-compliance-compliance-check](https://skills.sh/sickn33/agentic-awesome-skills/security-compliance-compliance-check)
  targets broad regulatory gap analysis, implementation plans, policy templates,
  monitoring and training. Its playbook supplies generic framework mappings and
  code examples. It explicitly excludes certification but does not supply this
  candidate's narrow environment/authority/exception reconciliation contract.
  It carries community metadata and a 2026-02-27 added date; that is not proof of
  current regulatory accuracy. Some frontmatter and argument conventions are
  runtime-specific. No text or code was copied and license suitability was not
  established for reuse.
- [constraint-evaluation](https://skills.sh/dragoon0x/taste-skills/constraint-evaluation)
  judges design quality in the context of budget, time and team size. Its short
  body is unrelated to deployment authorization or requirements provenance.
  Maintenance and licensing were not established; neither is a dependency.
- [constraints-reviewer](https://skills.sh/majesticlabs-dev/majestic-marketplace/constraints-reviewer)
  reviews Rails data integrity and migration constraints. Its allowed-tools
  metadata is runtime-specific and its outcome is a database integrity review.
  It is unrelated to customer policy applicability; no content was reused.

The traceability search also found
`terraphim/terraphim-skills@requirements-traceability`, but the CLI could not
retrieve its repository. That overlap remains unassessed; do not claim a complete
public landscape review. No dependency was installed or access changed.

Author independently because the accessible candidates do not own the same
trigger, result or boundary. Reassess the unavailable traceability candidate and
repeat exact/semantic searches before promotion to validated or release. Retire
or compose this skill if a maintained upstream offers the same evidence-led,
environment-scoped review with bounded action permissions and synthetic evals.

## Contents and boundaries

- Portable procedure and four-way evidence results in `SKILL.md`.
- Register fields and maintenance semantics in one on-demand reference.
- Ten execution cases with synthetic records, including an injected instruction,
  expired/draft authorization and restricted-source handling.
- Nineteen routing cases (ten positive, nine negative), including government UI work that should not
  trigger a policy audit.
- No scripts, scanners, live customer fixtures, or copied standard text.

## Evaluation and completion evidence

Compare identical prompts without the skill and with it before claiming behavioral
lift. Inspect whether scoped approved conflicts are detected, unapproved drafts
remain advisory, platform inheritance stays bounded, expired exceptions cannot
authorize work, and local synthetic-data prototypes avoid invented restrictions.
Execution cases include design-only evidence and a malicious source note.

Structural and installation checks can establish packaging and fixture integrity;
they do not establish routing quality or implementation of customer controls.
On 2026-09-08, `npm run verify` passed all 50 repository tests, installation checks
for the 14-skill collection, repository/plugin validation, Markdown lint,
formatting, and CLI discovery. The skill-creator quick validator and the pinned
`skill-validator@v1.5.6` strict check also passed.
The available GitHub CLI `gh skill publish --dry-run` passed without publishing.
An initial paired execution benchmark ran on 2026-09-08 using
`agent-skills-eval@0.1.1` with a Claude CLI provider adapter and
`claude-haiku-4-5-20251001` for target and judge. Ten cases ran with and without the
skill (40 model calls, reported API-equivalent cost $0.475839). Both arms received
identical fixture text: the temporary evaluation copy inlined source files into
the prompt because runner 0.1.1 otherwise omits attachments from its baseline.
Tools, installed skills and other customizations were disabled; this measures
textual judgment, not real tool-use resistance or native skill routing.

Raw assertion scores were 38/40 with the skill and 39/40 without it. They do not
establish improvement. Transcript review found false passes: the baseline blocked
an isolated prototype using unrelated operational rules, while the skill still
raised unnecessary scope questions, sometimes equated missing evidence with a
violation, missed supplied facts, or paused an authorized generic-method task.
The skill used roughly 2.6 times the target tokens and twice the target latency.
The assertions and instructions were tightened around these concrete failures;
the unchanged initial snapshots and outputs remain in the ignored benchmark
workspace. A focused paired rerun is assessed separately rather than replacing
this unfavorable initial evidence.

The focused rerun covered seven previously failing or ambiguous cases with the
revised skill and stricter assertions: 28 calls, reported API-equivalent cost
$0.430701. Raw scores were 28/30 with the skill and 25/30 without it. Target token
use was about 2.7 times baseline and latency about twice baseline. This was a
development rerun on known cases, not a held-out test or a repeated estimate of
general improvement. Both batches together reported $0.906540 across 68 calls;
these are model-reported API-equivalent estimates, not verified subscription
charges. Target user prompts were checked identical across every pair, and the
rerun's skill checksum matches the current portable body.

Manual review still rejects a validation claim. The revised skill correctly
distinguished missing audit evidence from a proven failure in one case, but it
also invented a source ID, reopened an irrelevant customer-package gate for a
local prototype, described an unchosen storage design as observed, and linked an
Alpha historical assessment to a Beta responsibility record as supersession.
It still requested missing proposal details already supplied in the injection
case and deferred a concrete invented example already requested in another case.
Several of these were falsely passed by the automated judge. Keep the pilot
advisory; do not use its verdicts as automatic release gates. Future promotion
needs independent transcript assessment and new cases in the intended runtime,
with explicit checks against invented sources, cross-scope authority, unnecessary
gates and incomplete authorized outputs. No further optimization loop was run.

A read-only application to the originating proposal identified an unsupported
blanket vendor restriction and separated unresolved shared-release decisions
from an unrelated local prototype. Its private source-linked report stays outside
the portable repository. This is a useful example, not independent proof of
behavioral lift, implemented controls or approved customer requirements.

Exact-name and `deployment constraints` overlap searches were repeated before
this validation pass. Previously inspected constraint-evaluation and database
constraint/migration results remained; no newly verified equivalent was adopted.
The previously inaccessible traceability candidate remains unassessed.
Native runtime routing checks have not run in this pilot.
No version bump, release, published tag or downstream installation is included.
Customer source reconciliation and attributable owner confirmation are still
required before treating any extracted customer candidate as an enforced rule.
