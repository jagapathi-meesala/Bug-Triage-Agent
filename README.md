# Bug Triage Agent

A framework-independent OpenGAP agent for deterministic software bug triage.

## Capabilities
- Normalize issue reports and identify missing evidence.
- Classify severity using explicit impact/security rules.
- Map severity to priority P0-P3.
- Return triggered rules and a human-readable decision explanation.

## Structure
- `agent.yaml` — OpenGAP manifest.
- `SOUL.md`, `RULES.md`, `DUTIES.md`, `AGENTS.md` — agent identity and operating boundaries.
- `skills/` — declared reusable capabilities.
- `tools/` — declarative tool contracts.
- `contracts/`, `core/` — framework-independent execution layer.
- `adapters/` — portability boundary.
- `tests/` — automated tests.
- `verification/` — structural readiness audit.

## Validation
Run:

```bash
python3 -m pytest -q
python3 verification/readiness_audit.py
opengap validate
```

The first two commands are local checks. `opengap validate` is the authoritative CLI check when the CLI is installed; its absence must not be treated as a pass.

## Security
No secrets are required by the deterministic core. Runtime secrets, if later introduced by an adapter, must be supplied through environment variables and excluded from Git.
