# Architecture and Development Rules

The core implementation is Python and framework-independent. Tool calls enter through a contract and registry boundary, then invoke deterministic domain functions in `core/`.

## Development Rules
- Preserve supplied facts during normalization.
- Never invent reproduction evidence, logs, root cause, or affected versions.
- Keep classification rules in `RULES.md` and mirrored in tested code.
- Use environment variables only for runtime configuration that is genuinely required.

## Tool Conventions
Each tool has a declarative YAML contract, a Python implementation, validation, structured output, and tests. Tool names are stable and implementations are discoverable through the registry.

## Testing Rules
Run `pytest -q` from the repository root. Documentation and manifest structure are tested in addition to domain behavior.

## Portability Expectations
Adapters translate external invocation shapes into the framework-independent contract. Framework-specific packages are optional and are not required by the core agent.
