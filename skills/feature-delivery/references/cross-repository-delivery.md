# Cross-Repository Delivery

Use this guide when one feature crosses repositories, services, environments,
schemas, distributed client versions, or separately deployable layers.

## Impact map

For each affected layer, record:

- repository or service and its responsibility;
- current branch, deployed state, and target environment;
- contract produced or consumed;
- compatibility window and supported client versions;
- data migration, index, rule, or backfill requirements;
- implementation owner and verification evidence;
- deploy, distribution, exposure, and rollback controls.

Mark uncertain entries explicitly. Inspect the likely repositories before
deciding that work belongs on the client, server, or both.

## Contract before consumers

Publish stable interfaces before parallel consumer work:

- request, response, event, or stored-data schema;
- authorization and privacy boundaries;
- version and unknown-field behavior;
- error, retry, cancellation, idempotency, and partial-failure semantics;
- offline, cache, invalidation, and deletion behavior;
- observability fields without sensitive payloads.

Prefer additive changes while old and new clients coexist. Define how every
supported client behaves against the new backend and how the new client behaves
against an old or rolled-back backend.

## Dependency graph

Order work by real dependencies, not repository convenience. A typical graph is:

1. contract and compatibility fixtures;
2. producer implementation behind a safe default;
3. consumer implementation behind independent exposure control;
4. per-repository verification;
5. real development or staging integration;
6. deployment and distribution;
7. exposure and observation.

Parallelize only workstreams whose inputs are stable and whose file or service
ownership does not overlap. Assign an integration owner even when agents or
teams own individual repositories.

## Integration evidence

Per-repository tests are necessary but insufficient. Exercise:

- supported client/backend version combinations;
- real authorization, indexes, rules, migrations, and external dependencies;
- cancellation, retries, partial failure, concurrency, and data repair;
- offline transitions and stale clients where relevant;
- rollback of each layer while other layers remain deployed.

Do not call the feature complete while integration or required manual platform
evidence is deferred or blocked.
