---
name: issue-normalization
description: Normalize raw software bug reports into a stable structured representation without changing factual claims.
---

# Issue Normalization Skill

## Purpose
Turn a raw bug report into a stable, structured representation suitable for deterministic triage.

## Inputs
The title and description are required. Optional fields include expected behavior, actual behavior, environment, steps to reproduce, and logs.

## Behavior
Whitespace is normalized without rewriting the user's factual claims. Missing evidence is explicitly listed.

## Outputs
The skill returns normalized fields plus a `missing_information` list.

## Invalid Inputs
Title and description must be non-empty strings. Optional fields must be strings when supplied.
