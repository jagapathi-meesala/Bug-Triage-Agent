from .validation import require_dict, require_nonempty_string, optional_string
from .normalization import normalize_issue

SEVERITY_RANK = {"low": 0, "medium": 1, "high": 2, "critical": 3}


def triage_issue(payload):
    require_dict(payload)
    require_nonempty_string(payload, "title")
    require_nonempty_string(payload, "description")
    for key in ("expected_behavior", "actual_behavior", "environment", "steps_to_reproduce", "logs"):
        optional_string(payload, key)
    normalized = normalize_issue(payload)
    text = " ".join(filter(None, [normalized["title"], normalized["description"], normalized["actual_behavior"]])).lower()
    rules = []
    severity = "low"
    if any(term in text for term in ("data loss", "lost data", "complete outage", "service outage", "confirmed compromise")):
        severity = "critical"
        rules.append("critical-impact")
    security_terms = ("authentication bypass", "credential exposure", "unauthorized access", "security compromise")
    if any(term in text for term in security_terms):
        if "confirmed compromise" in text or "security compromise" in text:
            severity = "critical"
            rules.append("confirmed-security-compromise")
        elif SEVERITY_RANK[severity] < SEVERITY_RANK["high"]:
            severity = "high"
            rules.append("security-signal")
    if any(term in text for term in ("production unusable", "major production", "blocks all users", "severe regression")):
        if SEVERITY_RANK[severity] < SEVERITY_RANK["high"]:
            severity = "high"
        rules.append("major-production-impact")
    if any(term in text for term in ("workaround", "subset of users", "intermittent", "feature impaired")):
        if SEVERITY_RANK[severity] < SEVERITY_RANK["medium"]:
            severity = "medium"
        rules.append("moderate-impact")
    if any(term in text for term in ("typo", "cosmetic", "wording", "minor ui", "minor usability")):
        rules.append("minor-impact")
        if severity == "low":
            severity = "low"
    priority = {"critical": "P0", "high": "P1", "medium": "P2", "low": "P3"}[severity]
    if not rules:
        rules.append("default-low-impact")
    return {
        "normalized_issue": normalized,
        "severity": severity,
        "priority": priority,
        "triggered_rules": rules,
        "confidence": "high" if len(rules) > 1 or severity in {"critical", "high"} else "moderate",
        "decision_explanation": f"Classified as {severity} because the supplied report matched: {', '.join(rules)}.",
    }
