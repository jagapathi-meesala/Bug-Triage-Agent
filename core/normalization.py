import re
from .validation import require_dict, require_nonempty_string, optional_string

WHITESPACE = re.compile(r"\\s+")

def normalize_issue(payload):
    require_dict(payload)
    require_nonempty_string(payload, "title")
    require_nonempty_string(payload, "description")
    for key in ("expected_behavior", "actual_behavior", "environment", "steps_to_reproduce", "logs"):
        optional_string(payload, key)
    title = WHITESPACE.sub(" ", payload["title"].strip())
    description = WHITESPACE.sub(" ", payload["description"].strip())
    result = {
        "title": title,
        "description": description,
        "expected_behavior": payload.get("expected_behavior"),
        "actual_behavior": payload.get("actual_behavior"),
        "environment": payload.get("environment"),
        "steps_to_reproduce": payload.get("steps_to_reproduce"),
        "logs": payload.get("logs"),
        "missing_information": [],
    }
    required_evidence = {
        "expected_behavior": "expected behavior",
        "actual_behavior": "actual behavior",
        "environment": "environment",
        "steps_to_reproduce": "steps to reproduce",
    }
    for key, label in required_evidence.items():
        if not result[key]:
            result["missing_information"].append(label)
    return result
