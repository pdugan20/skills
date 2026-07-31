# Skill Candidate: Production Hardening

- **Inventory ID:** `SC-003`
- **Status:** `deprecated`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-31

## Intent

- **Outcome:** Preserve a selected implementation while removing experiment residue, correcting release-relevant defects, verifying the changed surface proportionally, and reporting whether it is ready.
- **Trigger:** Patrick explicitly asks to harden, ship, or prepare a completed implementation for production or a named release channel.
- **Artifact:** A focused patch or evidence-backed readiness assessment with remaining risks and approval-gated release actions.
- **Non-goals:** Lightweight exploration, full feature discovery and delivery, generic pull-request review, or operating a deployment and rollout program.

## Real evidence

The process is real and recurring. The audit question was whether it needs a standalone skill, not whether production hardening matters.

### Representative examples

1. `pat-portfolio` selected the fifth quote-share pill, removed four abandoned variants and the one-off feature flag, then fixed Chrome dismissal and arrival/highlight lifecycle defects in follow-up commits.
2. `nextup-ios-app` converted actionable-notification explorations into a gated client/backend feature, then hardened replay ordering, account handoff, overlapping reminders, analytics isolation, and physical-device acceptance before live category enablement.
3. `messenger-proto` prepared a simulator-focused prototype by correcting reduced-motion startup, consolidating brand color, removing debug logging and dead exports, and constraining the declared device target.

### Repeated corrections

- Preserve the chosen behavior instead of reopening design exploration.
- Distinguish useful developer fixtures and Storybook surfaces from residue that must not reach a release artifact.
- Treat source completion, distribution, exposure, and observation as separate states.
- Keep deployment, production mutation, push, and release actions behind explicit authorization.

### Sensitive material

The evaluation used private repository history through read-only local snapshots. This brief records only safe behavioral summaries, commit classes, and public repository metadata; it does not include credentials, production data, or personal user content.

## Mechanism decision

- **Decision:** Deprecate the standalone `production-hardening` skill and remove it in v3.0.0. Keep it present through the v2 line so existing exact-tag and plugin installs do not break in a patch release.
- **Classification:** No standalone skill after the compatibility window.
- **Rationale:** Natural requests to harden a completed implementation already caused fresh agents to inspect the selected behavior, find real historical defects, preserve scope, give evidence-backed verdicts, and avoid unauthorized release actions. Loading the released seven-step skill did not produce a reliable improvement across the same cases. The remaining value belongs in the user's explicit request, repository production instructions, `feature-delivery` for substantial feature work, and deterministic repository verification.
- **Scope:** The deprecation applies to this portable collection. Repository-specific production rules remain valuable and should stay in `AGENTS.md` or tested scripts.

## External overlap gate

The live Skills CLI was searched on 2026-07-31 for `production hardening`, `production readiness`, `release readiness`, `release preflight`, and `ship feature`.

- [`chandima/opencode-config@production-hardening`](https://skills.sh/chandima/opencode-config/production-hardening) was the only exact-name result, with 3 installs, but its GitHub repository was unavailable and the skill could not be fetched. It is not a maintainable dependency.
- [`petrkindlmann/qa-skills@release-readiness`](https://skills.sh/petrkindlmann/qa-skills/release-readiness) had 229 installs, an MIT license, and a repository updated on 2026-06-10. It owns evidence-based go/no-go decisions, smoke suites, staged rollout, rollback criteria, and post-deployment verification. It is a useful optional capability when the task is release operation, not a replacement for code hardening.
- [`adamos486/skills@production-ready`](https://skills.sh/adamos486/skills/production-ready) had 67 installs, an MIT license, and a repository updated on 2026-07-18. It is primarily a security-scanner installation and report-generation process, with substantially heavier dependencies and a different outcome.
- [`LerianStudio/ring@ring:production-readiness-audit`](https://skills.sh/lerianstudio/ring/ring:production-readiness-audit) had 31 installs, an Apache-2.0 license, and a repository updated on 2026-07-30. Its source runs an exhaustive Ring-specific service audit across up to 44 dimensions with many agents, a score, and an HTML dashboard; that conflicts with the proportional native-and-web boundary here.
- [`aws/agent-toolkit-for-aws@analyzing-release-readiness`](https://skills.sh/aws/agent-toolkit-for-aws/analyzing-release-readiness) had 391 installs, an Apache-2.0 license, and a repository updated on 2026-07-31. It depends on the AWS DevOps Agent and remote branch/PR analysis, so it is vendor- and runtime-specific.

Do not fork or copy these skills. Use the QA release-readiness skill only when its distinct go/no-go and rollout artifact is requested. The absence of an exact upstream replacement does not justify retaining generic local guidance that fails to change behavior.

## Reusable contents

- **Instructions:** No standalone portable instructions after v3. Keep the production-mode boundary in repository or user instructions.
- **Scripts:** Use each repository's deterministic lint, test, build, archive, and release preflight commands.
- **References:** None required.
- **Assets:** None required.
- **Dependencies:** Repository source, its normal verification tools, and explicit authorization for external release actions.

## Safety and boundaries

- Do not remove a published skill in a patch release. Remove it with a documented major release and synchronize downstream plugins and lockfiles.
- Do not turn deprecation into silent deployment, production mutation, or release authorization.
- Do not replace a proportional code-hardening request with an exhaustive operational audit unless the user asks for that separate outcome.

## Evaluation plan

### Execution

1. A selected web UI variant needs to become the sole production implementation. A useful response preserves its visual contract, removes residue, finds interaction/lifecycle defects, verifies real browsers, and avoids reopening design.
2. A green mobile client with default-off backend gates needs a TestFlight verdict. A useful response distinguishes dormant distribution from exposure, inspects account/concurrency/compatibility risks, and keeps gate changes behind approval.
3. A simulator-focused prototype needs a 1.0 pass. A useful response removes debug residue, reviews accessibility/motion/configuration, and does not invent a hosted service or App Store scope.

### Routing

- **Should trigger while the v2 compatibility skill exists:** Explicit requests to harden a selected implementation, prepare it for production, or run a final release-readiness pass.
- **Should not trigger:** Lightweight visual exploration, initial feature design, a normal read-only code review, or an operational rollout request whose primary artifact is a go/no-go checklist.

### Baseline

Use natural prompts without disclosing the desired review dimensions. Compare the same repository snapshot with no skill and with the last released skill. Retain the skill only if it reliably improves defect discovery, proportional scope, verification evidence, or approval boundaries rather than merely changing formatting.

### Behavioral evidence

An initial comparison was discarded because its prompts listed the expected review dimensions and therefore taught the no-skill control the method. Fresh controls used only natural hardening requests.

- The no-skill quote-share review found the disabled default, abandoned variants, ambiguous quote matching, route lifecycle leak, touch gap, and import failure.
- The no-skill notification review found a same-process account handoff defect and correctly separated a gates-off TestFlight build from live category enablement.
- The no-skill Messenger review found overlapping AI turns, release gating, stale async preview work, accessibility gaps, metadata drift, and missing exact-revision verification.
- Released-skill runs found comparable defects, including notification retry triggers and Messenger cancellation, logging, accessibility, device-target, and dependency concerns. They did not consistently discover more, scope more proportionally, or produce stronger approval boundaries than the controls.

The result supports deprecation rather than expansion. It does not claim that the skill is harmful or that every model will behave identically; it records that the local collection lacks evidence for the skill's incremental value.

## Definition of done

- [x] Mechanism and scope decision recorded.
- [x] Real examples and repeated corrections recorded safely.
- [x] Live public overlap searched and source-inspected.
- [x] Natural-prompt no-skill and released-skill results reviewed.
- [x] Leading execution eval prompts replaced.
- [ ] Deprecation published in the final v2 release.
- [ ] Skill, README entry, grouping, and packaged metadata removed in v3.0.0.
- [ ] Patrick Plugins and Agent Tooling updated to the v3 removal after the release exists.
