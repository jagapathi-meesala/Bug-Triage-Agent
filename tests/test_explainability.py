from pathlib import Path
import re

ROOT = Path(__file__).parents[1]

def test_explainability_checkpoint_structure():
    text = (ROOT / "EXPLAINABILITY.md").read_text()
    required = ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"]
    for heading in required:
        assert heading in text
        section = text.split(heading, 1)[1]
        assert len(re.findall(r"(?<=[.!?])\s+", section.split("\n## ", 1)[0])) >= 1
    assert "\n## Inputs\n" not in text
    assert "\n## Decision\n" not in text
    assert "\n## Limits\n" not in text
