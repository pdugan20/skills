# Synthetic Delta design

D-1 source: <https://example.org/policies/delta-audit>, version 2, approved for Delta.
Requirement: application mutations must produce an event with actor and outcome.

The design specifies recording actor and outcome for each mutation. Implementation
has not started. The design says tests will pass. A draft review register proposes
checking one sanitized event as a verification method; the policy does not prescribe
that test method. No logs, code or executed test results are supplied.
