import pytest
from core.normalization import normalize_issue
from core.triage import triage_issue
from core.registry import discover_tools, execute_tool

BASE = {"title": "Login fails", "description": "Major production login failure blocks all users."}

def test_normalization_is_stable():
    a = normalize_issue({**BASE, "expected_behavior": "login", "actual_behavior": "error"})
    b = normalize_issue({**BASE, "expected_behavior": "login", "actual_behavior": "error"})
    assert a == b

def test_critical_data_loss():
    result = triage_issue({"title": "Production data loss", "description": "Users report confirmed data loss."})
    assert result["severity"] == "critical"
    assert result["priority"] == "P0"

def test_security_signal_is_high():
    result = triage_issue({"title": "Auth bypass", "description": "Authentication bypass permits unauthorized access."})
    assert result["severity"] == "high"
    assert result["priority"] == "P1"

def test_medium_workaround():
    result = triage_issue({"title": "Feature impaired", "description": "Feature is impaired but a workaround exists."})
    assert result["severity"] == "medium"
    assert result["priority"] == "P2"

def test_low_cosmetic():
    result = triage_issue({"title": "Typo", "description": "Minor wording issue on the settings page."})
    assert result["severity"] == "low"
    assert result["priority"] == "P3"

def test_missing_evidence_reported():
    result = normalize_issue(BASE)
    assert "environment" in result["missing_information"]
    assert "steps to reproduce" in result["missing_information"]

def test_invalid_input_rejected():
    with pytest.raises(ValueError):
        triage_issue({"title": "Only title"})

def test_registry_discovers_declared_tools():
    assert discover_tools() == ["normalize_issue", "triage_issue"]
    assert execute_tool("triage_issue", BASE)["priority"] == "P1"

def test_unknown_tool_rejected():
    with pytest.raises(KeyError):
        execute_tool("does_not_exist", BASE)
