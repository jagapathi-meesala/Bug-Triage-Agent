from contracts.tool_contract import ToolContract
from core.normalization import normalize_issue
from core.triage import triage_issue
from core.validation import require_dict, require_nonempty_string


def _normalize_validate(payload):
    require_dict(payload)

def _triage_validate(payload):
    require_dict(payload)
    require_nonempty_string(payload, "title")
    require_nonempty_string(payload, "description")

REGISTRY = {
    "normalize_issue": ToolContract(
        name="normalize_issue",
        purpose="Normalize a bug report and identify missing evidence.",
        input_schema={"type": "object", "required": ["title", "description"]},
        output_schema={"type": "object"},
        validator=_normalize_validate,
        executor=normalize_issue,
    ),
    "triage_issue": ToolContract(
        name="triage_issue",
        purpose="Classify severity and priority using documented deterministic rules.",
        input_schema={"type": "object", "required": ["title", "description"]},
        output_schema={"type": "object", "required": ["severity", "priority", "triggered_rules"]},
        validator=_triage_validate,
        executor=triage_issue,
    ),
}

def discover_tools():
    return sorted(REGISTRY)

def execute_tool(name, payload):
    if name not in REGISTRY:
        raise KeyError(f"Unknown tool: {name}")
    return REGISTRY[name].execute(payload)
