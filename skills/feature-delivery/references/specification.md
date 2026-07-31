# Feature Specification

Create the smallest durable contract that prevents expensive product,
architecture, integration, and rollout mistakes. Scale the artifact to the
feature; do not manufacture ceremony.

## Investigate first

Before recommending an architecture:

- inspect applicable repository instructions and current implementation;
- identify every repository, service, data store, third party, and client
  version that may participate;
- identify local, development, staging, internal distribution, and production
  environments;
- locate existing contracts, feature flags, release tooling, tests, and
  observability;
- record assumptions as assumptions until evidence confirms them.

When repository evidence is unavailable, compare candidate architectures and
state what would distinguish them, but do not recommend one. An architecture
recommendation must cite the current-state evidence that supports it.

## Required decisions

Capture:

1. **Outcome:** user problem, target users, measurable success, and why the
   feature merits production investment.
2. **Behavior:** selected experience, important states, accessibility, failure
   and offline behavior, and explicit non-goals.
3. **Current state:** relevant architecture and constraints discovered in the
   actual repositories.
4. **Selected design:** options considered, decision, evidence, tradeoffs, and
   unresolved questions. Do not silently convert a recommendation into user
   approval.
5. **Impact map:** repositories, subsystems, data, contracts, environments,
   client versions, external services, privacy/security boundaries, and owners.
6. **Acceptance:** observable product, technical, compatibility, manual
   platform, and operational criteria.
7. **Delivery:** dependency order, execution mode, integration environment,
   rollout gates, monitoring, rollback, and cleanup.

Use [../assets/feature-delivery-template.md](../assets/feature-delivery-template.md)
for a durable specification or handoff. For a bounded single-repository feature
whose behavior is already selected, keep these decisions concise in the working
plan instead of creating a formal document.

## Approval gate

Pause before implementation only when an unresolved decision would materially
change user behavior, architecture, data, security, compatibility, cost, or
release strategy. Present the evidence, recommendation, and tradeoff clearly.
Once the user selects the direction—or the repository already contains an
approved decision—continue without asking for ceremonial approval.
