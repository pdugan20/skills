# Feature Spike: [Title]

- **Status:** Proposed | Running | Complete
- **Decision owner:** [Name or role]
- **Decision needed by:** [Date or milestone]
- **Budget:** [Approved time, effort, sample, data, external access]
- **Code disposition:** Throwaway | Salvageable | Contract fixture

## Decision contract

- **Decision:** [What commitment will this evidence inform?]
- **Unknown:** [What claim is uncertain?]
- **Options:** Continue | Change | Stop | Defer | Inconclusive
- **Non-goals:** [What this spike will not build or establish]

## Evidence plan

| Unknown | Test | Valid only if | Supports | Rejects |
| --- | --- | --- | --- | --- |
| [Claim] | [Smallest decisive slice] | [Required conditions] | [Evidence] | [Evidence] |

## Results

| Observation | Validity | Result | Confidence | Limitation | Consequence |
| --- | --- | --- | --- | --- | --- |
| [What happened] | Valid | Supported | [Basis] | [Remaining gap] | [Plan change] |

Include failed attempts and invalid observations when they change confidence.

## Decision

Decision outcome: Continue | Change | Stop | Defer | Inconclusive

[Explain how the evidence supports the decision. Mixed decisions may be listed
per unknown.]

## What changes

- [Product, scope, architecture, or sequencing consequence]
- [Assumption removed or retained]

## Remaining evidence

- [Unanswered question and the smallest valid next test]

## Code disposition

- **Keep:** [Evidence, fixtures, contract tests, or reusable seams]
- **Remove:** [Throwaway code after approval]
- **Owner:** [Cleanup owner]

## Production handoff

Production implementation has not begun. If the decision is `continue`, carry
this evidence into `feature-delivery` only after the user asks to proceed.
