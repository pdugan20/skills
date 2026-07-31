# Maturity profiles

Select rigor from intended lifespan, collaboration, and release surface. The
profile is a starting contract, not a score.

## Selection

| Profile | Use when |
| --- | --- |
| `exploration` | A prototype, spike, visual experiment, or short-lived proof may be discarded or revisited by a small team. |
| `maintained` | An app, site, service, or tool will evolve, accept regular dependency changes, or support multiple contributors. |
| `shipping` | An app, service, desktop build, or package reaches users through a store, deployment, installer, or registry. |

Choose the highest profile justified by the actual release surface. A private
production service can be `shipping`; a polished public demo can remain
`exploration`.

## Repository contract

| Concern | Exploration | Maintained | Shipping |
| --- | --- | --- | --- |
| Platform scaffold | Maintained upstream generator | Maintained upstream generator | Maintained upstream generator |
| Runtime and package manager | Record requirements | Pin supported versions | Pin supported versions and release environment |
| Lockfiles | Commit when generated | Required | Required |
| Root agent instructions | Short project boundaries | Setup, architecture, quality, and safety | Add release and environment boundaries |
| README | Purpose and runnable quick start | Add commands and important architecture | Add installation, distribution, and release facts |
| Quality checks | Build plus the cheapest useful checks | Format, lint, types, tests, and build as applicable | Add package, archive, integration, or deployment validation |
| One verification command | Recommended | Required | Required and used by CI |
| Tests | Focused behavior when present | Risk-based automated coverage | Release-critical and compatibility coverage |
| Pre-commit | Optional | Use when it makes the local gate cheaper | Use when it protects release-critical hygiene |
| CI | Add when sharing or preserving the experiment | Required stable aggregate gate | Required gate plus release-path validation |
| Dependency automation | Optional | Every ecosystem, compatibility-aware | Every ecosystem, compatibility-aware |
| Default-branch policy | Optional until remote collaboration | Pull requests and required aggregate CI | Add review and release protections proportionally |
| Security features | No secrets; enable host defaults when remote | Secret scanning and dependency alerts where available | Add reporting, environment, and release protections |
| Changelog and version policy | Omit | Add only if changes are distributed | Required for user-visible releases |
| Release automation | Omit | Omit unless already releasing | Verified but inert until explicitly invoked |
| Tag protection | Omit | Add only if versioned artifacts exist | Protect immutable release tags |
| Public contribution files | Omit | Add when accepting outside use | Required when accepting outside use |

Do not add empty ceremony. A `SECURITY.md` without a reporting path, a release
workflow without a package destination, or a badge for a check that has never
run makes the repository less trustworthy.

## Promotion triggers

Record what would move the repository to the next profile, such as:

- another contributor or required review;
- persistence beyond the experiment;
- credentials, user data, or a backend dependency;
- TestFlight, a hosted environment, PyPI, npm, an installer, or an app store;
- compatibility guarantees or external users.

Promote deliberately. Do not copy the infrastructure of a larger sibling
repository unless the new repository now shares the same operational needs.
