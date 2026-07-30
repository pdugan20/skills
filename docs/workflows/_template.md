# Workflow Candidate: [Name]

- **Inventory ID:** `WF-000`
- **Status:** `captured`
- **Owner:** Patrick
- **Last reviewed:** YYYY-MM-DD

## Intent

- **Outcome:** What recurring result should this flow produce?
- **Trigger:** What would Patrick or another user naturally ask for?
- **Artifact:** What code, design, document, decision, or other output results?
- **Non-goals:** Which adjacent requests should remain outside this flow?

## Real evidence

Describe or link safe, representative source material. Prefer completed tasks, Patrick's corrections, diffs, review comments, traces, or failure cases over hypothetical examples.

### Representative examples

1. [Example and what happened]
2. [Example and what happened]

### Repeated corrections

- [What agents tend to miss or do incorrectly]
- [Patrick's preferred correction and why]

### Sensitive material

Record only a safe summary and the private location category. Do not commit credentials, personal data, or confidential source artifacts.

## Mechanism decision

- **Decision:** Skill, `AGENTS.md`, script, reference, asset, plugin, human documentation, or no action.
- **Classification:** Technique, pattern, reference, discipline, or composite workflow when the decision is a skill.
- **Rationale:** Why is this the lightest reliable mechanism?
- **Scope:** Personal, repository-specific, or broadly portable.

## Reusable contents

- **Instructions:** Non-obvious procedural or decision guidance.
- **Scripts:** Deterministic or repeatedly recreated operations.
- **References:** Domain knowledge, schemas, examples, or variants loaded on demand.
- **Assets:** Templates or source materials used in outputs.
- **Dependencies:** Required tools, runtimes, permissions, or external services.

## Safety and boundaries

- [Approvals, destructive actions, external writes, privacy, or production boundaries]
- [Important negative routing cases]

## Evaluation plan

### Execution

List at least three realistic tasks and the observable properties of a successful result.

1. [Task, expected output, assertions]
2. [Task, expected output, assertions]
3. [Task, expected output, assertions]

### Routing

- **Should trigger:** [At least four representative intents]
- **Should not trigger:** [At least four plausible near misses]

### Baseline

State whether comparison should use no skill, the last released version, or another mechanism. Explain what improvement would justify keeping the candidate.

## Definition of done

- [ ] Mechanism and scope are approved.
- [ ] Reusable resources are implemented and referenced.
- [ ] Structural and repository validation passes.
- [ ] Execution and routing eval coverage passes.
- [ ] Representative with-skill and baseline results are reviewed.
- [ ] Intended Claude, Codex, and other claimed integrations are checked.
- [ ] Version, changelog, distribution metadata, and installation are verified.
- [ ] Inventory status and lessons are updated.
