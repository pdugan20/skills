# Skill Candidate: End-to-End Feature Development and Staged Rollout

- **Inventory ID:** `SC-002`
- **Status:** `released`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-30

## Intent

- **Outcome:** Turn a feature idea into an approved product and technical design, a coordinated implementation across every affected repository, and a deliberately gated path to real users.
- **Trigger:** Patrick has an idea for a production feature in an iOS app or website and wants to investigate, specify, implement, test, and stage it rather than immediately editing code.
- **Artifact:** An approved design or specification, a repository and environment impact map, an implementation plan, tested changes, and an explicit rollout, observability, rollback, and approval record.
- **Non-goals:** Small isolated changes, code-native UI direction comparison, throwaway feature spikes, hardening an already completed implementation, or deploying and mutating production systems without authorization.

## Real evidence

Patrick described a recurring formal feature-development flow that begins with an idea rather than a selected implementation. The private iOS and backend histories were then reviewed for three shipped features implemented at different times and with different orchestration methods. The safe summaries below record the reusable process without exposing repository URLs, commits, product data, credentials, or private implementation details.

### Representative examples

1. **Catch Me Up:** The feature began as an on-device iOS implementation with a capability gate, local cache, UI, tests, and an internal feature flag. Production-quality findings later changed the architecture: a cross-repository specification split work into backend evaluation, generation, shared caching and streaming, then client routing and fallback. Superpowers specifications and TDD plans were effective inside those bounded phases. The rollout still required an already-live backend contract, kill switches, client compatibility, offline behavior, production-output review, and an evaluation gate that tested the system users actually received.
2. **User-generated lists:** The client used a formal architecture and a long phased implementation plan covering models, synchronization, navigation, UI, editing, sharing, and automated tests. The backend then supplied rules, indexes, count projection, metadata-dispatch and worker jobs, tests, and deletion coverage. Automated client tests could pass while manual UI, real backend integration, deployment verification, TestFlight exposure, and rollback checks remained open. The history demonstrates that “client complete,” “backend deployed,” “integration verified,” and “available to users” are distinct states.
3. **Series-detail trailers:** The backend video pipeline and callable contract existed before the iOS surface. Client work could therefore proceed contract-first through models, service integration, horizontal content rails, playback, error reporting, and show-detail integration. An external player dependency and real-device playback, full-screen, picture-in-picture, and performance checks remained genuine blockers even after a task tracker reached nominal completion. Later backend validation, data-quality, and discovery improvements show that operational ownership continues after the client UI ships.

### Repeated corrections

- Do not begin implementation before understanding the user outcome, current behavior, affected repositories, and unresolved product or architecture decisions.
- Do not treat a green change in one repository as a complete feature when another repository, environment, migration, or client compatibility boundary is affected.
- Do not equate code completion with user availability. Feature flags, backend deployment, internal builds, TestFlight, observability, rollback, and removal of temporary gates are separate delivery decisions.
- Do not collapse feature status into a single percentage or completed checklist. Track specification, client, backend, integration, environment, manual platform verification, distribution, exposure, and cleanup separately when they have independent truth values.
- Do not mark deferred, blocked, or manual verification complete merely because implementation and automated tests are green.
- Do not force strict TDD, worktrees, agent teams, or a particular orchestration plugin merely because the feature is substantial. Select those mechanics explicitly and record the choice.
- Do not deploy, publish a build, mutate live data, merge, push, or open a pull request without the authorization required by the active repository and working agreement.

### Orchestration evidence

Related agent-team retrospectives in the same repositories reinforce the boundary. Parallel teams performed well when work was divided into dependency-ordered waves, interfaces were published before consumers started, file ownership was explicit, and an independent verifier checked the combined result. They did not remove the need for a coordinator: verifier agents sometimes remained idle until resumed, agents occasionally missed repository conventions, and deployments, seed operations, environment flags, device checks, and production observation remained outside the implementation agents' completion claims.

The repeated pattern is therefore specification and integration-led, not agent-led. First establish the cross-repository contract, phase graph, ownership, and release gates; then select Superpowers, an agent team, inline execution, or human implementation for each bounded workstream.

### Sensitive material

Use sanitized summaries for private product plans, user data, credentials, backend configuration, and unreleased business logic. Repository-specific secrets and production data remain outside specifications, prompts, fixtures, and evaluation artifacts.

## Mechanism decision

- **Decision:** Expand the existing `feature-delivery` skill into a portable outer coordinator and use linked references for formal specification, cross-repository delivery, staged rollout, and optional execution-engine adapters.
- **Classification:** Composite skill.
- **Rationale:** The valuable Patrick-specific behavior is not another implementation loop. It is the lifecycle that discovers the real scope, produces a handoff-quality contract, selects proportional execution mechanics, coordinates repositories and environments, and carries code through controlled exposure. Existing Superpowers skills implement strict inner loops but do not own this cross-repository product and rollout context. Duplicating their detailed procedures would create drift and make the skill dependent on one plugin.
- **Scope:** Broadly portable across native and web products, with repository-specific commands, schemas, environments, branch policy, and release operations supplied by each project.

### Superpowers composition boundary

The skill should lean heavily on Superpowers when Patrick selects the strict flow, but it should compose rather than copy those skills:

| Phase | Owner | Recommended Superpowers use |
| --- | --- | --- |
| Product outcome and current-state investigation | `feature-delivery` | Borrow the discipline of inspecting context and clarifying decisions; do not automatically invoke the rigid brainstorming gate. |
| Cross-repository and environment impact | `feature-delivery` | None. The outer skill must map repositories, contracts, data, deployment order, compatibility, gating, and rollback. |
| Design document and specification approval | `feature-delivery` by default | Offer `brainstorming` as an explicit full-Superpowers mode when its question-by-question and approval gates are desired. |
| Implementation plan | Selected execution engine | Invoke `writing-plans` after the specification is approved when strict Superpowers execution is selected. |
| Test discipline | Selected execution engine | Invoke `test-driven-development` only when strict TDD is explicitly selected; the `feature-spike` skill remains an explicit exception. |
| Workspace isolation | Selected execution engine per repository | Use `using-git-worktrees` only with the required consent or standing preference. The outer skill coordinates branch and environment relationships across repositories. |
| Task execution | Selected execution engine | Choose `subagent-driven-development` for review-gated task handoffs or `executing-plans` for inline checkpoint execution. An available Claude agent team can consume the same specification and task boundaries as an alternative adapter. |
| Parallel work | `feature-delivery` | Use parallel agents only for independent investigations or implementation streams after interfaces and ownership are stable; never parallelize coupled tasks merely for speed. |
| Review and verification | Shared | Reuse `requesting-code-review` and `verification-before-completion` principles strongly, then add cross-repository integration and release-gate evidence. |
| Source integration | Selected execution engine | `finishing-a-development-branch` can own branch integration choices, but the outer skill still owns backend deployment, build distribution, feature exposure, monitoring, rollback, and gate cleanup. |

Superpowers is therefore an optional strict implementation backend, not the definition of the `feature-delivery` skill. The canonical specification, repo impact map, acceptance criteria, and rollout plan must remain useful to Codex, Claude Code, Cursor, a human engineer, or another execution system without Superpowers installed.

## Reusable contents

- **Instructions:** Intake and scope discovery; current-state investigation; product and technical decision gates; cross-repository impact mapping; specification approval; execution-mode selection; staged rollout; and final outcome verification.
- **Scripts:** None initially. Repository discovery or release automation should remain in tested project tooling until repeated use proves a safe portable script is possible.
- **References:** A formal feature-specification method, a cross-repository dependency and compatibility checklist, a staged-rollout method, and a small execution-engine adapter explaining normal, Superpowers, and agent-team handoffs.
- **Assets:** A concise feature specification and rollout-state template captures the recurring decision and evidence fields without copying private project documents or preserving historical ceremony that did not add value.
- **Dependencies:** Read access to every potentially affected repository; repository instructions and tests; access to development or emulator environments where applicable; and explicit authorization for external writes or releases. Superpowers and agent-team support are optional execution dependencies, not portability requirements.

## Safety and boundaries

- Identify each target as local, development, staging, TestFlight/internal distribution, or production before mutating it.
- Prefer emulators, synthetic fixtures, test users, and development services while resolving behavior and data-model decisions.
- Make backward and forward compatibility explicit when backend and client versions can coexist.
- Treat schema migrations, privileged backend code, authentication, remote configuration, feature flags, build distribution, and production deployment as separate risk and approval boundaries.
- Do not let a hidden flag become permanent architecture without an owner and removal or graduation condition.
- Do not trigger for a bounded learning spike, several UI variants, a small isolated change, or a hardening-only request.

## Evaluation plan

### Execution

1. Begin with a NextUp feature idea that may affect the iOS app, backend functions, data contracts, and TestFlight delivery. A successful result investigates both repositories, resolves compatibility and environment questions, produces an approved specification before implementation, and separates backend deployment, client distribution, and feature exposure.
2. Begin with a production web feature that crosses UI, API, database, analytics, and a third-party service. A successful result maps dependencies, scales the design document and task boundaries, selects an execution engine deliberately, and includes migration, failure, observability, rollback, and staged-release evidence.
3. Begin with an apparently client-only iOS feature. A successful result verifies that assumption, keeps the process proportional if it is true, preserves platform testing and gating decisions, and does not manufacture backend work, agent teams, or strict ceremony without value.

### Routing

- **Should trigger:** “I have an idea for a NextUp feature and want to work through the design, backend impact, implementation, and TestFlight rollout”; “Write the spec and then hand this production feature to an agent team”; “Use the full Superpowers TDD flow for this cross-repository feature”; “Take this web feature from idea through a gated production rollout.”
- **Should not trigger:** “Spike the smallest version of this and tell me whether it is worth building”; “Show me three runnable card designs”; “Change this isolated label”; “Harden the implementation we already finished”; “Deploy the existing build now.”

### Baseline

Compare against the released `feature-delivery` skill. Retain the expansion only if it more reliably delays implementation until the product and technical contract is approved, discovers affected repositories and environments, makes execution-engine selection explicit, and distinguishes source completion from gated user availability without imposing the full strict flow on a genuinely bounded feature.

### Baseline observations

Three fresh-context replays on 2026-07-30 used the released `feature-delivery`
skill before the expansion:

- The bounded single-repository web case chose a concise working contract,
  proportional inline implementation, risk-based tests, browser verification,
  and normal preview gates. The expansion must preserve that behavior.
- The ambiguous client/backend case produced strong compatibility and rollout
  detail but recommended a backend-centric architecture before inspecting the
  repositories or obtaining approval for the material split. It also never
  selected an execution mode.
- The partially implemented client/backend case separated backend, client,
  internal distribution, TestFlight, and exposure states well, but its process
  was generated from the prompt rather than guaranteed by the released skill.
  It did not record execution machinery or provide a canonical handoff artifact.

The baseline therefore shows that a capable model can infer much of the
delivery discipline, but the released skill does not reliably enforce the
distinctive boundaries this skill exists to preserve.

### Forward-test observations

Fresh-context replays against the expanded skill used the same three scenarios:

- The bounded web feature selected proportional inline execution, kept the
  delivery contract in the working plan, and retained risk-based tests,
  browser verification, and normal preview gates without strict ceremony.
- The partially implemented client/backend feature produced a canonical brief,
  old/new version matrix, real integration gate, independent rollback model,
  and separate backend, distribution, exposure, observation, and cleanup
  states.
- The first ambiguous client/backend replay still led with a provisional
  architecture recommendation and two initial cross-repository replays omitted
  the execution-mode record. The instructions were tightened to prohibit
  recommendations without repository evidence and require an explicit
  `Execution mode` line. Fresh retries then kept architectures as hypotheses
  until discovery and recorded proportional inline execution.

These are Codex fresh-agent behavior checks, not a multi-provider benchmark.
The clean-install test verifies packaged layout for Claude Code, Codex, and
Cursor; paid Cursor behavior was intentionally not claimed or required.

## Pilot decisions

- Invoking `feature-delivery` does not authorize strict TDD. Proportional
  risk-based testing remains the default; strict Superpowers TDD requires an
  explicit user request.
- The pilot uses two sanitized historical replays plus a bounded
  single-repository counterexample so cross-repository rigor does not become
  universal ceremony.
- The portable template retains outcome, behavior, current-state evidence,
  selected design, impact, acceptance, execution, rollout, and status fields.
  Repository-specific schemas and commands remain in project documentation.
- Agent-team work uses separate repository or workstream owners and one
  integration coordinator after interfaces stabilize. A single team for the
  entire plan is not a default.

## Release evidence

- [`pdugan20/skills` v2.2.0](https://github.com/pdugan20/skills/releases/tag/v2.2.0)
  contains the expanded `feature-delivery` skill and its complete resources.
- The GitHub Release body matches the curated changelog section, and the
  checksum-verified archive contains the same seven skill folders as the tag.
- A clean Skills CLI installation from `pdugan20/skills@v2.2.0` copied all
  seven skills into Claude Code, Codex, and Cursor layouts, with every installed
  file matching the tag byte-for-byte.

## Definition of done

- [x] Mechanism and scope are approved.
- [x] Reusable resources are implemented and referenced.
- [x] Structural and repository validation passes.
- [x] Execution and routing eval coverage passes.
- [x] Representative with-skill and baseline results are reviewed.
- [x] Intended Claude, Codex, and other claimed integrations are checked within
      the stated packaging and behavior boundaries.
- [x] Version, changelog, distribution metadata, and installation are verified.
- [x] Inventory status and lessons are updated.
