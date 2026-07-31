# Skill Candidate: Bootstrap a Repository

- **Inventory ID:** `SC-015`
- **Status:** `validated`
- **Owner:** Patrick
- **Last reviewed:** 2026-07-31

## Intent

- **Outcome:** Create a runnable repository whose code scaffold, local development tooling, documentation, continuous integration, dependency maintenance, and GitHub configuration match its stack, visibility, release surface, and intended maturity.
- **Trigger:** A user asks to start, scaffold, initialize, or properly configure a new Swift, Expo/React Native, Python, TypeScript, or other software repository.
- **Artifact:** A verified local repository, a concise setup and quality report, and—when GitHub configuration is in scope—a verified remote repository with appropriate metadata, security features, rulesets, and release policy.
- **Non-goals:** Implementing the product, deploying it, publishing a first release, forcing an established repository onto a new layout, or applying the most rigorous configuration to every experiment.

## Real evidence

Patrick's active repositories show the same recurring setup outcome across stacks but at materially different levels of rigor. The audit reviewed tracked configuration, README structure, CI jobs, dependency automation, release files, branch policy, security settings, descriptions, topics, tags, and releases as of 2026-07-31.

### Representative examples

1. **Swift:** `nextup-ios-app` has a bootstrap command, pinned tooling, SwiftFormat and SwiftLint enforcement, pre-commit checks, a required aggregate CI gate, test baselines, dependency automation, TestFlight and release jobs, repository topics, and a default-branch ruleset. `audiobook-ios` is intentionally lighter: XcodeGen, a local Swift package with focused tests, direct build commands, and no CI or release path yet. `imessage-swift-prototype` adds lint, format, pre-commit, Dependabot, badges, and one required CI gate. `touchpoint` adds signing, notarization, DMG releases, a release badge, and public-repository security settings.
2. **Expo and React Native:** `passant-prototype` has formatting, linting, type checking, a small CI gate, and no release stream. `chat-app-prototype` adds Jest, coverage, CodeQL, Storybook, build validation, a changelog, and releases. `messenger-proto` pins Node and npm, uses one `verify` command for Expo Doctor, format, lint, types, security boundaries, tests, dead-code checks, and Markdown, then protects the branch with the matching checks.
3. **Python and mixed projects:** `bibliocommons-mcp` and `clickwheel` are published packages with `pyproject.toml`, pre-commit, Ruff, tests, documentation checks, changelogs, PyPI automation, release-please, protected branches, and many releases. `clickwheel` adds a committed `uv.lock`, Mypy, a Python-version and OS test matrix, squash-only history, resolved review threads, and protected immutable `v*` tags. `e-ink-scoreboard` is a maintained hardware application with Python and JavaScript checks, integration tests, setup documentation, and no package release stream.
4. **TypeScript web and services:** `pat-portfolio` uses the framework's normal app structure with project-specific lint and asset validation, tests, builds, Dependabot, CI, and concise repository metadata. `nextup-backend` adds reusable workflows, emulator and integration coverage, infrastructure validation, controlled deployments, a required CI gate, and production safety instructions.

### Repeated corrections

- Choose rigor from intended lifespan and release surface. Do not copy NextUp's self-hosted runner, test-count baselines, deployment machinery, or operational jobs into a short-lived prototype.
- Start from the maintained framework generator—such as `create-expo-app` or `uv init`—and layer Patrick's repository contract on top. Do not freeze a competing copy of framework boilerplate in the skill.
- Treat GitHub configuration as part of completion: description, topics, homepage, default branch, merge policy, automatic branch deletion, rulesets, required checks, Dependabot, secret protection, and tag policy should agree with the repository files.
- Name only checks that actually exist when creating a ruleset. A stale required-check name can lock the default branch.
- Configure dependency automation by ecosystem and compatibility boundary. Expo's React Native dependency set should follow Expo compatibility tooling; Xcode-managed Swift packages require the correct project directory; Dependabot commit titles must satisfy the repository's PR-title convention.
- Keep the README concise and audience-oriented. Use only truthful badges with durable targets, then document purpose, quick start, common commands, important architecture, and release/install information that a user actually needs.
- Add changelogs, release automation, SECURITY and CONTRIBUTING guidance, tag immutability, and distribution badges only when the repository is expected to ship or accept external use.

### Sensitive material

Do not commit credentials, signing material, environment values, private project identifiers, personal data, or raw private artifacts. The audit records safe summaries only.

## Mechanism decision

- **Decision:** Create one `bootstrap-repository` skill backed by read-only inspection and explicit-apply scripts, stack references, and small verified configuration assets. Do not create separate Swift, React Native, Python, and web skills initially.
- **Classification:** Composite skill.
- **Rationale:** Selecting a maturity profile, upstream generator, quality floor, release surface, and GitHub policy requires contextual judgment. Inspecting files and remote settings, rendering a change plan, applying known settings, and verifying the result are deterministic enough for scripts. The trigger and outcome remain the same across stacks, while framework mechanics can load from focused references or upstream skills only when relevant.
- **Scope:** Broadly portable, with Patrick's defaults and real repositories providing the evidence base.

## Maturity profiles

| Profile | Appropriate for | Default repository contract |
| --- | --- | --- |
| `exploration` | A prototype, spike, visual experiment, or short-lived proof | Upstream scaffold; runnable quick start; root agent instructions; ignore and editor basics; formatter/linter and type check where applicable; focused test or build; one lightweight CI gate when remote collaboration or preservation matters; truthful description and topics. No release ceremony. |
| `maintained` | An app, service, site, or tool expected to evolve | Everything above plus pinned runtime and package manager, lockfile, reproducible bootstrap command, tests, pre-commit or equivalent, one authoritative verification command, dependency automation for every ecosystem, required CI, protected default branch, secret protection, architecture/setup notes, and useful badges. |
| `shipping` | An App Store app, deployed service, or distributed package/desktop app | Everything above plus changelog and semantic version policy, release or deployment automation, environment and secret boundaries, rollback or post-deploy verification where relevant, SECURITY and CONTRIBUTING files for public projects, distribution badges, release notes, and protected immutable release tags. |

Profiles are starting points, not scores. A hardware app can be maintained without package publishing; a private production app can need deployment safety without public contribution files; a polished prototype can use Storybook without inheriting a release process.

## External overlap gate

The 2026-07-31 live skills.sh pass searched `repository scaffolding ci lint format`, `swift ios project setup`, `react native expo project setup`, `python project setup uv ruff pytest`, `github repository best practices`, and `new project bootstrap`. The closest bodies were inspected:

- [`patinaproject/skills@scaffold-repository`](https://www.skills.sh/patinaproject/skills/scaffold-repository) (124 installs, MIT, active) is the closest broad overlap. It maintains a detailed Patina baseline and realignment process, including GitHub settings, but hard-codes Patina's PNPM, issue-tracker, commit, skill-vendoring, and repository conventions. It does not select platform-native generators or an intended-maturity profile. Do not fork it; independently reuse the useful idea that local files and live GitHub settings must be audited together.
- [`thatrebeccarae/claude-marketing@repo-scaffold`](https://www.skills.sh/thatrebeccarae/claude-marketing/repo-scaffold) (57 installs, MIT, active) creates common repository files and a generic CI skeleton after conflict confirmation. It does not own framework-native app creation, maturity selection, reproducible commands, live GitHub configuration, release/tag policy, or verification against actual checks.
- [`laurigates/claude-plugins@project-init`](https://www.skills.sh/laurigates/claude-plugins/project-init) (55 installs, MIT, active) creates a universal directory tree and placeholder CI before delegating language setup. It is Claude-command-specific, uses placeholder Make targets and mutable action tags, and can initialize and commit automatically. Use it only when that plugin's generic convention is explicitly desired.
- [`tenequm/skills@python-dev`](https://www.skills.sh/tenequm/skills/python-dev) (54 installs, MIT, active) is a focused opinionated Python recipe for uv, Ruff, ty, pytest, and just. It is useful comparison material for the Python reference but does not own multi-stack repository or GitHub policy. Do not vendor its pinned versions or beta type-checker choice.
- [`storybookjs/react-native@setup-react-native-storybook`](https://www.skills.sh/storybookjs/react-native/setup-react-native-storybook) (354 installs, MIT, maintained by Storybook) owns one optional React Native component-development layer. Compose it when isolated component work is part of the repository's intended process.
- Expo's maintained `expo-project-structure` skill and current `create-expo-app` output own new-app layout and Expo-specific agent context. Vercel's maintained `bootstrap` skill owns safe linking and environment/resource provisioning for repositories that already depend on Vercel resources. Delegate those phases; neither owns the cross-stack repository contract.

**Decision:** Implement independently as a thin coordinator and verifier; compose official generators and narrower maintained skills. Do not fork or copy their text or templates.

**Distinct value:** Select a proportional maturity profile from real repository evidence, coordinate official stack scaffolds, and make local tooling plus live GitHub policy one verifiable outcome across native, web, service, and package repositories.

**Retirement condition:** Retire or narrow this candidate if a maintained portable skill supports the same maturity selection, official-generator composition, local quality contract, safe GitHub settings plan/apply loop, and cross-stack verification.

## External tools and template strategy

- Prefer official project generators and their lockfiles: [`create-expo-app`](https://docs.expo.dev/more/create-expo/) for Expo, [`uv init`](https://docs.astral.sh/uv/concepts/projects/init/) for Python, the selected web framework's generator for React applications, and Xcode/[XcodeGen](https://github.com/yonaskolb/XcodeGen) or another explicitly chosen Swift project source of truth.
- Use [GitHub template repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) only when a stable family of repositories genuinely shares files. They copy the initial tree but do not provide an update channel to generated repositories.
- Reconsider [Copier](https://copier.readthedocs.io/en/stable/updating/) if repeated use proves that Patrick needs versioned cross-stack templates that can update existing generated projects. Copier records template answers, selects Git tags, and can merge template evolution, but adds a Python dependency and conflict-management contract that is not yet justified.
- Use [projen](https://projen.io/docs/introduction/) only for a repository family willing to make generated configuration authoritative. Its synthesis model fits TypeScript and Python but is not a common denominator for Swift or Expo projects and would be invasive in repositories where configuration remains hand-maintained.
- Keep reusable GitHub ruleset JSON, README sections, Dependabot fragments, and CI fragments as small versioned assets only after the baseline evaluations show that agents repeatedly recreate the same content incorrectly. Avoid a giant universal repository template.

## Reusable contents

- **Instructions:** Inspect intent and constraints; choose platform and maturity; select the maintained upstream generator; establish local commands and verification; prepare the remote repository; configure proportional GitHub policy; verify from a clean checkout; report intentional omissions and next promotion triggers.
- **Scripts:** Start with one read-only inspector that reports local files, runnable commands, CI jobs and stable check names, dependency automation, release files, and—when an exact remote exists—relevant GitHub settings. Test it against fixtures. Defer a GitHub mutation helper until a separately authorized live-settings evaluation shows that instructions plus an inspect-and-plan artifact are insufficient.
- **References:** `profiles.md`, `github.md`, and focused `swift.md`, `expo-react-native.md`, `python.md`, and `node-web.md` references. Each should name maintained upstream generators and describe only Patrick-specific selection and verification guidance.
- **Assets:** Initially none beyond small machine-validated settings or workflow fragments justified by baseline failures. Promote repeated stable bundles into a versioned template only after real use.
- **Dependencies:** Git, GitHub CLI for remote inspection/configuration, the selected stack's runtime and official generator, and access to any required macOS runner or release account. Paid hosted services remain optional and separately authorized.

## Safety and boundaries

- Separate local file creation, GitHub repository creation, repository-settings mutation, deployment, and publishing. Execute only the external writes included in the user's request or separately authorized.
- Resolve the exact owner, repository, visibility, default branch, and profile before remote writes. Never target a repository through an unresolved environment variable or broad loop.
- Preserve existing files in a nonempty directory and present conflicts. Do not force an established repository into a starter layout.
- Keep workflow permissions read-only by default and grant narrow write permissions only to jobs that require them.
- Enable required checks only after those checks have run or their stable names are known. Provide a recovery path before applying rulesets.
- Enable release and tag policy only when a release path exists. Do not create tags, releases, packages, deployments, signing credentials, or production environments as part of scaffolding.
- Never print or copy secrets, signing certificates, provisioning profiles, production data, or environment values. Commit example keys only.

## Evaluation plan

### Execution

1. Start a lightweight SwiftUI prototype modeled on `audiobook-ios`. Success uses an appropriate Xcode project source of truth, adds focused package tests and proportional lint/format/build checks, writes a useful README and agent guide, and deliberately omits release and NextUp-specific infrastructure.
2. Start a maintained Expo/React Native app modeled on `messenger-proto`. Success begins with current `create-expo-app`, pins runtime and package manager, exposes one verification command covering Expo compatibility, format, lint, types, and tests, configures compatible Dependabot groups and required checks, and adds Storybook only when requested by the intended component process.
3. Start a shipping Python CLI or MCP package modeled on `clickwheel` and `bibliocommons-mcp`. Success uses current `uv init`, a `src` layout, Ruff and tests, a supported type-checker decision, package build and publish verification, concise public docs, changelog-backed releases, squash-only protected main, and immutable `v*` tags without publishing anything.
4. Start a maintained React/TypeScript site or service. Success uses the framework generator, includes its real build and type checks, adds project-specific validation without generic placeholder jobs, configures repository metadata and dependency updates, and delegates Vercel resource linking only when the project actually uses those resources.

### Routing

- **Should trigger:** “Set up a new Swift repo with the right CI and GitHub settings”; “Bootstrap this Expo prototype but keep it lightweight”; “Create a production-ready Python package repository”; “Turn this new app directory into a properly configured maintained GitHub repo.”
- **Should not trigger:** “Add one CI job to this mature repository”; “Audit this existing repo without changing it”; “Implement the first product feature”; “Deploy this service”; “Create an empty GitHub repository with no project scaffold”; “Modernize every config file in this legacy monorepo.”

### Baseline

Use no-skill runs against the four execution prompts before creating any skill files. Inspect whether agents overbuild prototypes, underconfigure GitHub, invent generic placeholder CI, copy stale framework boilerplate, misname required checks, omit dependency compatibility boundaries, or conflate scaffolding with deployment. Retain the candidate only if the skill produces more proportional and reproducible repositories without adding unnecessary ceremony.

### Candidate-absent results

Four fresh ephemeral Codex runs on 2026-07-31 used natural prompts and did not
have the candidate skill. Plugins were disabled to isolate the proposed
collection behavior; the already installed narrow SwiftUI skill remained
available in the Swift case, which is acceptable because the candidate must add
repository coordination rather than duplicate stack expertise. Raw transcripts
and generated repositories remained temporary and were not committed.

An initial Swift prompt was discarded because “run on my Mac” ambiguously led
to a macOS app and implementation of the page-turn interaction. The counted
prompt explicitly requested an iPhone starting point and no feature work; it
did not disclose the desired repository checklist.

| Case | Baseline strengths | Missing or unstable behavior |
| --- | --- | --- |
| Lightweight iPhone SwiftUI prototype | Used XcodeGen as a reproducible project source, kept the app minimal, documented setup, performed a signing-disabled simulator build, and avoided remote or signing changes. | Defaulted to an iOS 26-only target and placeholder bundle identifier without promotion criteria; added no agent guide, formatter/linter, reusable quality command, or explicit future CI threshold; initialized and committed Git history without making that local side effect explicit up front. |
| Maintained Expo app | Used the current `create-expo-app` template, pinned Node, preserved Expo-compatible dependencies, added one `check` command, passed TypeScript, ESLint, Expo Doctor, and a web export, and documented secrets and SDK upgrades. | Added no tests, CI workflow, Dependabot configuration, or machine-readable GitHub plan despite the maintained lifespan; repository settings remained four prose recommendations with no stable required-check name. |
| Shipping Python CLI package | Produced a `src` layout, lockfile, typed CLI, tests, Ruff, strict mypy, build validation, CI, public-project documents, and a careful release checklist without publishing. | Hand-authored the package instead of starting from `uv init`; imposed a 100% placeholder coverage gate; omitted a single verification command, dependency automation, pre-commit, release automation, and exact branch/tag policy artifacts. |
| Maintained React/TypeScript site | Selected current Next.js, React, TypeScript, Tailwind, and ESLint versions; kept product work minimal; passed lint, typecheck, and a production build; avoided Vercel linking and deployment. | Reconstructed the framework scaffold manually after the official generator could not persist preferences; omitted a pinned package-manager/runtime file, tests, one aggregate verification command, CI, Dependabot, agent guidance, and any GitHub settings plan. |

The repeated failure is orchestration, not basic framework knowledge. Agents can
usually create runnable code, but do not reliably connect intended maturity to
generator provenance, one local quality contract, dependency compatibility,
checked-in automation, and exact remote policy. The candidate remains justified
only if the with-skill runs improve those properties without making the Swift
prototype resemble a shipping repository.

### Minimum pilot contents

- Keep `SKILL.md` as the thin coordinator for intent, profile selection,
  upstream generator choice, local-versus-remote boundaries, verification, and
  a concise completion report.
- Add `profiles.md` and `github.md` references plus short `swift.md`,
  `expo-react-native.md`, `python.md`, and `node-web.md` references. These should
  contain selection and verification guidance, not copied framework templates.
- Add one fixture-tested, read-only inspector. It may inspect an exact GitHub
  remote but must not create repositories or mutate settings.
- Add no starter-template assets, CI fragments, Dependabot fragments, or remote
  apply helper in the first pilot. Reconsider them only after repeated
  with-skill failures demonstrate a deterministic resource is necessary.

### Forward results

Four fresh with-skill runs on 2026-07-31 replayed the counted baseline prompts
in temporary directories. Every case selected the proportional maturity
profile, used the platform generator, exposed one verification command,
separated local files from unauthorized remote work, and passed its available
build surface.

| Case | Improvement over the candidate-absent run | Refinement from the replay |
| --- | --- | --- |
| Lightweight iPhone SwiftUI prototype | Stayed intentionally small while adding root agent guidance, one reusable verification command, a signing-disabled simulator build, and concrete promotion triggers without CI or release machinery. | None; the exploration profile remained proportional. |
| Maintained Expo app | Preserved the official Expo template and added clean-install verification, CI, compatibility-aware Dependabot, runtime pins, and an explicit GitHub settings plan without EAS or remote mutation. | Generator recovery needed a strict retry boundary after several cache and telemetry attempts. |
| Shipping Python CLI package | Used `uv init`, then added one quality command, strict checks, package builds, CI, dependency automation, public-project documentation, and an inert release path without publishing. | The first replay chose MIT without authorization, so the skill now treats license, author, security contact, registry ownership, and repository URLs as unresolved owner decisions. |
| Maintained React/TypeScript site | Used the official Next.js generator and added runtime pins, one aggregate check, CI, Dependabot, agent guidance, a GitHub plan, and production build/server verification without Vercel linking. | Generator recovery escalated into internal inspection and a platform shim, so the skill now permits one task-local state retry and explicitly prohibits generator inspection, patching, shims, and hand reconstruction. |

The replays establish behavioral lift without just adding more files: the Swift
case remained exploratory, while the maintained and shipping cases gained the
specific durability their baselines lacked. Focused follow-up evaluations also
confirmed that a failed generator stops after the permitted retry and that an
unspecified package license remains deferred. No reusable templates or remote
mutation helper were justified.

## Definition of done

- [x] Mechanism and scope are classified from repository evidence.
- [x] Natural candidate-absent baselines are captured and reviewed.
- [x] The profile contract and minimum pilot resource set are selected from the baseline evidence.
- [x] Scripts and assets are implemented test-first and referenced.
- [x] Structural and repository validation passes.
- [x] Execution and routing eval coverage passes.
- [x] Representative with-skill and baseline results are reviewed.
- [x] Intended Claude Code, Codex, and Cursor installation layouts are checked.
- [ ] Version, release metadata, and installation from a published tag are verified.
- [x] Inventory status and lessons are updated.
