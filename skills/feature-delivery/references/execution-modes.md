# Execution Modes

Select and record the implementation machinery after the product and technical
contract is stable enough to hand off. The feature specification and rollout
model remain canonical regardless of runtime.

Every delivery plan includes `Execution mode: <mode> — <rationale>`. If the
user has not selected strict machinery, choose proportional inline execution
unless the inspected work and active working agreement justify another mode.

## Proportional inline execution

This is the default. Use a concise checkpoint plan, coherent implementation
batches, risk-based tests, focused review, and production-relevant verification.
Do not require a plan file, worktree, strict red-green-refactor cycle, agent
team, branch, or commit solely because the feature is substantial.

## Explicit Superpowers execution

Use Superpowers only when the user names a Superpowers skill or explicitly asks
for that strict mode. Compose its inner loops instead of copying them:

- `superpowers:brainstorming` when the user wants its formal discovery and
  design-approval flow;
- `superpowers:writing-plans` after the feature specification is approved;
- `superpowers:test-driven-development` only when strict TDD is explicitly
  selected;
- `superpowers:using-git-worktrees` only with the required consent or standing
  preference;
- `superpowers:subagent-driven-development` or
  `superpowers:executing-plans` for the selected execution style;
- `superpowers:requesting-code-review` and
  `superpowers:verification-before-completion` for bounded review and evidence;
- `superpowers:finishing-a-development-branch` for source integration choices.

Feature delivery still owns cross-repository dependencies, environments,
deployment, distribution, exposure, monitoring, rollback, and gate cleanup.

## Agent-team execution

Use an available agent team when the user requests it or the active working
agreement permits it and the feature contains genuinely independent workstreams.
Give every member the same approved specification and stable interfaces. Assign
one owner per repository or workstream, explicit file/service ownership, and an
integration coordinator. Run dependent work in waves. An independent verifier
checks the combined result after implementers finish.

An agent report is evidence about its workstream, not proof that another
repository, a live environment, a distributed build, or user exposure is ready.

## Mixed or human handoff

The same specification can hand backend work to one runtime, client work to
another, and approval or deployment to a person. Record owners, inputs, outputs,
and evidence at each boundary so the skill does not depend on a particular
plugin being installed.

## Selection record

Record:

- chosen mode and why it fits;
- explicitly invoked strict skills, if any;
- repository/workstream ownership;
- sequential and parallel checkpoints;
- test discipline;
- workspace and branch approach;
- review and verification owner;
- actions that still require user authorization.
