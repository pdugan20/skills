# Staged Rollout

Treat source readiness, live infrastructure, build distribution, feature
exposure, and stable user availability as separate claims.

## Status dimensions

Track only the dimensions that are independently true for the feature:

| Dimension | Example evidence |
| --- | --- |
| Specification | Approved product and technical contract |
| Source | Repository checks and review complete |
| Integration | Supported layers exercised together |
| Environment | Migration or backend live in the named environment |
| Manual platform | Required browser, simulator, or device behavior verified |
| Distribution | Internal, TestFlight, preview, or production build available |
| Exposure | Flag or cohort enabled at the named level |
| Observation | Health, product, data, and support signals reviewed |
| Cleanup | Temporary gates, compatibility paths, and follow-ups owned |

Use states such as `not started`, `in progress`, `blocked`, `at risk`, and
`evidence complete`. Do not replace this matrix with a percentage.

## Gate sequence

Adapt this sequence to the product:

1. local and automated verification;
2. development or staging integration;
3. backend or infrastructure live but dark;
4. internal build or preview with allowlisted exposure;
5. TestFlight, beta, or limited production cohort;
6. wider distribution with exposure still independently controllable;
7. gradual general availability;
8. observation, ownership transfer, and temporary-gate cleanup.

Each gate names entry evidence, exit evidence, observation window, halt
condition, owner, rollback action, and authorization required. A binary can be
widely distributed while the feature remains off; a backend can be deployed
while no client consumes it.

## Compatibility and rollback

For every separately deployable layer, define:

- safe state when the feature is disabled;
- behavior with old clients or old services;
- independent pause, disable, rollback, or forward-fix path;
- data compatibility and repair after rollback;
- owner and time limit for temporary compatibility code or flags.

Rehearse high-risk rollback controls before expanding exposure. A client-side
flag alone is not an immediate kill switch for offline or already-running
clients; document that limitation and bound stale behavior.

## Observation and closure

Select signals from the actual risk: crashes, latency, errors, queue health,
data correctness, privacy/security events, quality evaluations, cost, adoption,
support reports, or business outcomes. Do not invent numeric launch thresholds
without product or historical evidence.

Call the feature available to users only when the intended cohort can use it and
the required observation gate is satisfied. Closure also assigns remaining
risks, rollback ownership, and removal or graduation of temporary flags,
compatibility paths, test data, and operational workarounds.
