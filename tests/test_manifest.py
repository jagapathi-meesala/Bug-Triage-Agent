from pathlib import Path
import yaml

ROOT = Path(__file__).parents[1]

def test_manifest_structure():
    data = yaml.safe_load((ROOT / "agent.yaml").read_text())
    assert data["spec_version"] == "0.1.0"
    assert data["name"] == "bug-triage-agent"
    assert data["skills"] == ["bug-triage", "issue-normalization"]
    assert all(isinstance(x, str) for x in data["tools"])
    for tool in data["tools"]:
        assert (ROOT / tool).exists()

def test_no_speculative_manifest_fields():
    data = yaml.safe_load((ROOT / "agent.yaml").read_text())
    forbidden = {"display_name", "entrypoint", "portability"}
    assert forbidden.isdisjoint(data)
