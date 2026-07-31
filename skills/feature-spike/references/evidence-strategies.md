# Evidence Strategies

Use the section that matches the uncertainty. A spike may combine sections, but
each additional question must still affect the same investment decision.

## Capability and integration

Test the dependency boundary itself:

- authenticate through the real supported mechanism;
- use representative resource shapes and failure responses;
- exercise the minimum end-to-end read or write contract;
- include entitlement, permission, compatibility, and network conditions that
  can turn an apparent success into an invalid test;
- preserve sanitized request, response, timing, and environment evidence.

Define invalid conditions before running the probe. For example, an entitlement
test may prove nothing when the account is already privileged or the request is
classified as local. Report that result as inconclusive and preserve the exact
protocol for a valid rerun.

The probe may contain more code than a mock because the dependency boundary is
the uncertainty. Keep product UI, broad domain abstractions, and release
infrastructure out unless they are necessary to reach that boundary.

## Architecture and performance

Choose a representative seam rather than a toy function or the whole
application.

- Measure the existing path first.
- Run equivalent behavior through the proposed architecture.
- Separate clean build, incremental build, startup, execution, memory, and
  operational costs when they have different consequences.
- Repeat noisy measurements and retain the raw samples.
- Record extraction effort, dependency pressure, API churn, test fidelity, and
  migration risk.

A large performance improvement can still yield `defer` when migration cost or
timing outweighs current benefit. Do not force a positive technical result into
an immediate production recommendation.

## Product value

Identify the behavior that would demonstrate value before choosing a surface.

- Prefer a single coherent experience over a tour of partial features.
- Use representative, privacy-safe inputs and the smallest credible audience.
- Measure the behavior or judgment connected to the claim: task completion,
  time saved, repeated use, preference, comprehension, accuracy, or willingness
  to replace the current behavior.
- Establish the current baseline before choosing a threshold.
- Base sample and observation-window proposals on expected signal, available
  participants, and decision stakes. Do not turn a convenient round number into
  an approved experiment design.
- Separate usefulness from feasibility, latency, cost, and production
  readiness. A useful experience may still need a second technical spike.

Fixture-backed or human-generated outputs can validate interaction and perceived
value, but not model quality or system feasibility. Label that boundary.

## Platform and tool feasibility

Exercise the real extension point with the hardest representative operation.
Record:

- what the platform supports directly;
- where the proposed tool or generated output fails;
- which manual or exported path succeeds;
- whether the result changes the implementation medium rather than rejecting
  the user outcome.

`Change` is often the correct result: the goal survives, but the initial tool or
platform does not.

## Evidence quality

Prefer:

- observed behavior over documentation claims;
- representative data over ideal fixtures;
- repeated measurements over one favorable run;
- explicit invalidation over ambiguous success;
- product or architecture consequences over a raw metrics dump.

Avoid:

- success thresholds invented after seeing the result;
- mocks of the only boundary being tested;
- polished demos that hide missing evidence;
- production rollout metrics for code that was never intended to ship;
- treating implementation effort as evidence of user value;
- equating `continue` with production readiness.
