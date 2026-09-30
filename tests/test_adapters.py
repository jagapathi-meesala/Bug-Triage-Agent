from adapters.portable_adapter import PortableAdapter

def test_portable_adapter_invokes_core_contract():
    result = PortableAdapter().invoke("triage_issue", {"title": "Typo", "description": "Cosmetic typo."})
    assert result["priority"] == "P3"
