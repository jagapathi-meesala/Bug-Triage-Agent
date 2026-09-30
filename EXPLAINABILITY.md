# Bug Triage Agent Explainability

## Inputs and Data Sources
The agent accepts a bug title and description as required inputs, with optional expected behavior, actual behavior, environment, reproduction steps, and logs. Its data source is the issue report supplied to the tool; the agent does not silently query external systems or invent evidence.

### Input Requirements
The title and description must be non-empty strings. Optional evidence is preserved as supplied and missing evidence is listed explicitly.

### Input Mechanisms
The framework-independent tool contract accepts a JSON-like object, and the portable adapter forwards that object to the registry. No API key is required for the deterministic core implementation.

## Decision and Reasoning
The agent determines severity by applying the documented rules in `RULES.md` to explicit impact and security signals in the supplied text. Priority is then derived deterministically from severity: critical maps to P0, high to P1, medium to P2, and low to P3.

### Rules Applied
Critical signals include data loss, complete outage, and confirmed security compromise; high signals include major production impact and specified security indicators. Moderate-impact and cosmetic indicators map to medium and low respectively when no higher-severity rule applies, and all triggered rules are returned in the result.

### Expected Outputs
The result contains the normalized issue, severity, priority, triggered rules, confidence, and a decision explanation. The explanation identifies the rules that caused the classification rather than presenting an unexplained score.

### Worked Example
For a report stating that authentication bypass permits unauthorized access, the security rule is triggered and the result is high severity with P1 priority. For a report stating that users experienced confirmed data loss, the critical-impact rule is triggered and the result is critical severity with P0 priority.

### Explainability of Calculated Results
The severity is selected using the highest-ranked triggered rule, and priority is a direct mapping from that severity. Because the rules are deterministic and the output lists the triggered rules, the same supplied evidence produces the same classification.

## Limits and Constraints
The agent cannot establish root cause, reproduce a defect, inspect a private production environment, or determine whether a proposed fix actually works. Its classification is limited to evidence present in the supplied issue report and should be reviewed by an engineer when evidence is incomplete or consequences are significant.

### Constraints
The agent does not execute arbitrary commands, access credentials, modify source code, close tickets, deploy releases, or contact external parties. Framework integrations are compatibility boundaries only; an integration is not considered tested unless an actual test has been run.

### Failure Handling
Invalid required inputs are rejected with a validation error instead of being classified. Missing optional evidence is reported as missing information so downstream reviewers can request it.

### Output Contract
The tool returns structured fields suitable for downstream ticket systems, but consumers must not interpret the classification as proof of root cause or a completed remediation. The provenance of the decision is the supplied issue text plus the named deterministic rules.

### Provenance
The implementation is based on the repository's `RULES.md` and the input issue payload. No external dataset or hidden production telemetry is used by the deterministic core.

### Complete Execution Lifecycle
A request enters through the portable adapter, reaches the dynamic registry, passes input validation, executes normalization and deterministic triage logic, and returns a structured result. Tests cover the core rules, registry, adapter boundary, manifest references, and the required explainability headings.
