# Bug Triage Skill

## Purpose
Classify a supplied software defect report into a severity and priority while preserving the evidence used for the decision.

## Inputs
A title and description are required. Expected behavior, actual behavior, environment, reproduction steps, and logs are optional but improve triage completeness.

## Behavior
The skill normalizes the report, applies the rules in `RULES.md`, records every triggered rule, and identifies missing evidence. It does not infer a root cause or claim a fix.

## Outputs
A structured object contains the normalized issue, severity, priority, triggered rules, confidence, and decision explanation.

## Invalid Inputs
Missing or non-string title/description values are rejected with a validation error. Unknown fields are ignored by the core calculation rather than treated as trusted evidence.
