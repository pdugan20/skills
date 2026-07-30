# Skill Authoring Standard

This is the authoring, evaluation, and review standard for Patrick's portable design and development skills. It reconciles the open Agent Skills specification with current Anthropic and OpenAI guidance and records which external tools this repository trusts.

The standard has four layers:

1. Decide whether a recurring process should be a skill at all.
2. Write the smallest portable skill that changes agent behavior usefully.
3. Encode the behavioral claim as execution and routing evals.
4. Enforce objective properties automatically and review judgment-based properties with evidence.

## Decide where the workflow belongs

Use the lightest mechanism that can reliably produce the desired behavior.

| Mechanism | Use it when | Do not use it when |
| --- | --- | --- |
| Skill | A recurring task benefits from specialized context or a flexible method that should load only when relevant. | The instruction must always apply, is a one-off request, or requires a rigid transaction. |
| `AGENTS.md` | A repository rule, safety boundary, or working agreement must remain active across tasks. | The guidance is relevant only to a narrow task family. |
| Script | A deterministic transformation or fragile operation should execute the same way every time. | Judgment, adaptation, or contextual reasoning is the main value. |
| Reference | The agent needs domain knowledge, schemas, examples, or variant-specific detail on demand. | The content is the core procedure and is short enough for `SKILL.md`. |
| Asset | The workflow needs templates, starter files, icons, or other material copied into outputs. | The file is documentation for the agent. |
| Plugin | Distribution also needs runtime metadata, MCP servers, hooks, applications, or several related skills. | One portable skill folder is sufficient. |
| Human documentation | The material explains governance, maintenance, or concepts to people but should not enter task context. | It directly changes how the agent should perform a recurring task. |

A good skill candidate has a recognizable trigger, a repeatable outcome, non-obvious reusable guidance, and enough variation that an agent should still exercise judgment. If a workflow is both deterministic and agent-guided, put the fragile operation in a tested script and let the skill decide when and how to use it.

## Classify the skill

Classification determines the appropriate level of prescription and evaluation.

| Type | Primary value | Typical evaluation |
| --- | --- | --- |
| Technique | Teaches a flexible way to approach a task. | Application quality across varied examples. |
| Pattern | Encodes a reusable structure or decision pattern. | Recognition plus correct adaptation. |
| Reference | Supplies authoritative facts, APIs, schemas, or conventions. | Retrieval accuracy and correct use. |
| Discipline | Prevents rationalization or skipped safeguards under pressure. | Compliance under realistic pressure and near misses. |
| Composite workflow | Coordinates several phases or concerns toward an outcome. | End-to-end behavior, boundaries, and proportionality. |

Do not apply pressure-test conventions to every skill. They are useful for discipline skills, while technique, pattern, and reference skills need realistic application and retrieval tests. Composite workflows usually need both execution coverage and boundary tests.

The current collection classifies `code-native-ui-ideation` as a technique, `feature-delivery` as a composite workflow, and `production-hardening` as a discipline skill with a bounded workflow.

## Capture intent before writing

When Patrick describes a design or development flow, capture:

- the outcome and artifact the flow produces;
- realistic phrases and contexts that should trigger it;
- adjacent requests that should not trigger it;
- the inputs, tools, environment, and platform assumptions;
- the decisions that require judgment versus deterministic execution;
- failure modes, safety boundaries, and approval points;
- examples of a successful result and a poor result;
- repeated work that should become a script, reference, or asset;
- whether the workflow is personal, repository-specific, or broadly portable.

Start from real expertise: a completed task, Patrick's corrections, working code, project artifacts, review history, or actual failure cases. Do not ask a model to invent a generic best-practices skill from its training knowledge alone.

Map the flow to the mechanisms above before drafting. Several smaller skills are preferable only when they have independently useful triggers and outcomes. Keep tightly coupled phases together when splitting them would make routing ambiguous or force users to know implementation details.

Record the initial decision in the [workflow inventory](workflow-inventory.md). When a candidate has enough real evidence to develop, copy the [candidate template](workflows/_template.md) into a descriptively named brief and keep it synchronized with the inventory through validation or rejection.

## Write the portable skill

### Name and metadata

- Use a lowercase hyphenated name of at most 64 characters and match the directory name.
- Keep `name` and `description` in `SKILL.md` frontmatter. Use optional spec fields only when portability requires them.
- Put runtime-specific presentation or invocation policy under `agents/`, not in portable instructions.
- Write a concise description with three parts: capability, concrete trigger contexts, and important negative boundaries.
- Do not put procedural steps in the description. Metadata routes to the skill; the body teaches execution.
- Avoid keyword stuffing. Use representative language and let routing evals expose gaps.

This description convention reconciles a small difference in vendor wording. The Agent Skills specification and OpenAI guidance require both what the skill does and when to use it. Some workflow-writing guidance warns that summarizing the procedure in metadata can cause an agent to skip the body. Capability plus routing context satisfies the first requirement without leaking the procedure.

### Body

- Assume the model is capable. Include knowledge and decisions it would not reliably infer.
- Use imperative instructions and explain why a constraint matters when that improves generalization.
- Match freedom to fragility: broad heuristics for context-dependent work, parameterized patterns for preferred approaches, and exact steps only for brittle or safety-critical operations.
- Keep the main procedure cohesive and under 500 lines. Remove duplication and information that belongs in ordinary repository documentation.
- State destructive actions, external side effects, approvals, and user-visible boundaries explicitly.
- Avoid runtime-specific tool names unless the skill truly requires that runtime.

### Progressive disclosure

The metadata is always visible, `SKILL.md` loads when selected, and bundled resources load only when referenced. Preserve that progression:

- Put executable, deterministic, or frequently recreated logic in `scripts/` and run representative tests for it.
- Put domain detail and variant-specific guidance in `references/`. Link each reference directly from `SKILL.md` and say when to read it.
- Put output materials in `assets/`.
- Avoid chains of references. Keep resources one level from `SKILL.md` where practical.
- Give long reference files a table of contents.
- Do not put a skill-local `README.md`, changelog, or maintenance notes in the distributed folder.

### Versioning and changelogs

- Version the collection once using semantic versioning; keep `package.json` and both plugin manifests synchronized.
- Do not add a non-standard version field to skill frontmatter. A tag identifies the exact version of every skill it contains.
- Record user-visible changes in the repository `CHANGELOG.md`, naming and linking every affected skill so each skill retains a searchable history.
- Use the matching changelog section verbatim as the GitHub Release body. Release automation must fail when that section is missing or empty.
- Split a skill into its own repository and release stream only when it needs an independent compatibility boundary or publishing cadence.

## Evaluate the behavioral claim

Every skill in this collection carries two versioned eval sets under `evals/`.

### Execution evals

`evals/evals.json` follows the public Agent Skills evaluation guide:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic task prompt",
      "expected_output": "A concise description of a successful result",
      "files": [],
      "assertions": ["A verifiable behavior or output property"]
    }
  ]
}
```

Keep at least three cases that vary context, wording, and difficulty. Use raw task inputs without revealing the desired method in the prompt. Prefer deterministic checks for artifacts and factual properties; use human review or a judge rubric for subjective design quality.

When claiming that a new or changed skill improves behavior, compare the same cases with and without the skill. For an existing skill, compare against the last released version when that is the meaningful baseline. Inspect transcripts as well as final outputs so added cost, wasted work, and unintended actions remain visible.

### Routing evals

`evals/routing.json` uses the trigger-eval shape from Anthropic's description optimization workflow:

```json
[
  { "query": "A realistic user request", "should_trigger": true },
  { "query": "A realistic adjacent request", "should_trigger": false }
]
```

The merge gate requires at least four positive and four negative cases. Negatives must be plausible near misses, not unrelated trivia. For a new skill or material description rewrite, expand toward 16–20 cases, test the intended runtime and model more than once, and keep a held-out set when optimizing wording.

Routing and execution are separate claims. A skill can perform well after explicit invocation while routing poorly, or trigger correctly while adding no value.

Run provider-backed behavioral benchmarks intentionally, never as an unreviewed CI side effect:

```bash
npx --yes agent-skills-eval@0.1.1 ./skills \
  --target <target-model> \
  --judge <judge-model> \
  --baseline \
  --strict \
  --report
```

Configure the provider and API-key environment variable without committing credentials. Benchmark artifacts go under the ignored `agent-skills-workspace/` directory. Keep useful conclusions in the skill, evals, or changelog rather than committing bulky model transcripts by default.

## Enforcement model

| Concern | Enforcement | Gate |
| --- | --- | --- |
| Agent Skills structure, frontmatter, links, orphaned resources, context size, and content heuristics | `agent-ecosystem/skill-validator` pinned in CI | Automatic |
| Claude plugin manifest and component schema | Official `claude plugin validate --strict` from the exactly pinned Claude Code CLI | Automatic |
| Secrets and executable script security | GitHub secret scanning and push protection, plus language-appropriate script tests and linters | Secret protection is enabled; script-specific gates become required when executable resources are introduced |
| Package versions, inventory, runtime policy, Skills CLI grouping, and eval coverage | `scripts/validate_repository.py` | Automatic |
| Claude Code, Codex, and Cursor installation layout and packaged resources | Isolated Skills CLI copy installation with source-tree comparison | Automatic |
| Markdown, formatting, spelling, action syntax, and workflow security | Existing repository tooling | Automatic |
| Trigger precision, near-miss behavior, and observable workflow outcomes | Versioned routing and execution evals | Evidence-based review |
| Taste, proportionality, novelty, overlap, and whether the workflow should exist as a skill | Author review using this rubric | Human judgment |

Do not turn subjective heuristics into brittle regex gates. Automated checks should reject objective defects and require evidence for semantic claims, not claim to understand design quality.

## External tooling decision

This assessment was last reviewed on 2026-07-30.

- [Agent Skills specification](https://agentskills.io/specification), [authoring guide](https://agentskills.io/skill-creation/best-practices), [evaluation guide](https://agentskills.io/skill-creation/evaluating-skills), and [description guide](https://agentskills.io/skill-creation/optimizing-descriptions) are the portability and authoring baseline.
- The official [`skills-ref`](https://github.com/agentskills/agentskills/tree/main/skills-ref) implementation validates the core schema, but its maintainers explicitly label it demonstration-only and unsuitable for production use.
- [Anthropic skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) automates baseline comparison, qualitative review, benchmarking, and trigger optimization.
- [OpenAI skill-creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) supplies initialization and basic validation, but its `quick_validate.py` checks only frontmatter and naming.
- [skill-validator](https://github.com/agent-ecosystem/skill-validator) is the selected third-party structural and content gate. Version `v1.5.6` is pinned because this is supply-chain executable code.
- [claude-code-lint](https://github.com/pdugan20/claudelint) version `0.7.0` is not an authoritative portable-skill gate. The scope audit below found duplicate, ineffective, and non-portable checks, so this collection now uses the pinned official Claude validator instead. `claudelint` can continue evolving as a separate product without defining this repository's acceptance criteria.
- Claude Code `2.1.220` exposes a first-party `claude plugin eval` runner with no-plugin ablation, cost ceilings, thresholds, and HTML or JSON reports. Its command currently reports that the feature is early access, and the public plugin reference does not yet document it. Reassess it when the feature is documented and stable; do not make an early-access runner a required gate.
- [agent-skills-eval](https://github.com/darkrishabh/agent-skills-eval) version `0.1.1` can run the adopted `assertions` format against OpenAI-compatible providers with with-skill/baseline comparison. Use it for opt-in benchmarks, not as a required CI gate, because model runs are nondeterministic, credentialed, and billable and the project is still young.
- [Skills CLI](https://github.com/vercel-labs/skills) validates discovery and distribution. It does not judge authoring quality.

The repository therefore extends its own tooling only for collection-specific policy and eval coverage. Reimplementing the external validator's structural checks would add maintenance without improving portability. A custom model runner is not justified; use Anthropic skill-creator for guided iteration or the portable runner for repeatable provider-backed benchmarks, and prefer Claude's first-party runner for Claude-specific evidence once it leaves early access.

### `claude-code-lint` scope audit

The 2026-07-30 audit resulted in removing `claude-code-lint` from this repository after its useful Claude packaging responsibility was replaced with the exactly pinned official CLI:

- The Agent Skills specification places no format restrictions on the `SKILL.md` body. The recommended `skill-body-missing-usage-section` rule nevertheless requires one of a small set of level-two headings; with warnings treated as errors, it rejects valid portable structure and influences writing style without evidence of better behavior.
- The strict preset activates 41 skill rules, including skill-local version and changelog requirements. This collection versions the package as a whole and intentionally forbids changelogs inside distributed skill folders.
- The current `validate-skills --path skills` command scans no skills because discovery patterns are evaluated relative to the supplied path and expect `skills/*/SKILL.md`. The preceding `check-all` command already performs the successful skill scan, so the second command adds no coverage.
- The Skills validator checks executable files immediately inside each skill directory but does not descend into the standard `scripts/` directory. Its dangerous-command and path-traversal rules therefore do not cover portable skill scripts as packaged here.
- Its `allowed-tools` documentation still says only YAML arrays are accepted, although the runtime schema now accepts both Claude's list form and the Agent Skills string form. This is documentation drift, not an active validation conflict.
- The official Claude Code `claude plugin validate . --strict` command passes this repository and catches more manifest and component-path defects than `claude-code-lint` on the same invalid fixture.

Keep responsibilities separated:

1. Use `agent-ecosystem/skill-validator` for portable skill structure, frontmatter, links, resources, context size, and content heuristics.
2. Use `scripts/validate_repository.py` for collection membership, synchronized versions, runtime policy, and eval coverage.
3. Use the exactly pinned official Claude Code CLI in local installs and CI, and run `claude plugin validate . --strict` for Claude packaging. This is implemented by `validate:claude-plugin` and included in `npm run verify`.
4. Keep GitHub secret scanning and push protection enabled. Add language-appropriate tests or linters when the collection gains executable skill resources; add a local scanner such as Gitleaks only if pre-commit or off-GitHub coverage becomes necessary.
5. Keep `claude-code-lint` and its duplicate strict skill command out of this collection. The dependency was removed after the official validator passed this repository and rejected a known-invalid plugin fixture.

Improving `claude-code-lint` remains worthwhile as a separate product effort. Its own backlog should cover standard resource-directory discovery, portable-versus-Claude-specific presets, conformance fixtures against upstream examples, and stale rule documentation. Those fixes should not block this collection or make it the tool's integration test bed.

## Review checklist

Before merging a skill change:

- Confirm the workflow belongs in a skill and record its classification.
- Read the description alone and verify its positive and negative routing boundaries.
- Read the body for non-obvious value, proportional freedom, safety, and runtime portability.
- Move deterministic repetition into tested scripts and bulky detail into linked references.
- Add or update three execution evals and at least eight balanced routing evals.
- Run `npm run verify` and the external validator.
- For material behavior changes, run representative with-skill and baseline cases and review the outputs.
- Test the intended Claude, Codex, or Cursor integrations before release when their behavior is part of the claim.
- Update the changelog and version according to user-visible impact.
