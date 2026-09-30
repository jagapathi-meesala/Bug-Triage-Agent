from pathlib import Path
import yaml

ROOT = Path(__file__).parents[1]
REQUIRED = ["agent.yaml", "SOUL.md", "AGENTS.md", "DUTIES.md", "RULES.md", "EXPLAINABILITY.md", ".env.example", "requirements.txt"]

def main():
    missing = [name for name in REQUIRED if not (ROOT / name).exists()]
    manifest = yaml.safe_load((ROOT / "agent.yaml").read_text())
    tools_ok = all((ROOT / p).exists() for p in manifest.get("tools", []))
    skills_ok = all((ROOT / "skills" / s / "SKILL.md").exists() for s in manifest.get("skills", []))
    explain = (ROOT / "EXPLAINABILITY.md").read_text()
    headings_ok = all(h in explain for h in ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"])
    print(f"required_files={'PASS' if not missing else 'FAIL'}")
    print(f"manifest_tools={'PASS' if tools_ok else 'FAIL'}")
    print(f"manifest_skills={'PASS' if skills_ok else 'FAIL'}")
    print(f"explainability_headings={'PASS' if headings_ok else 'FAIL'}")
    return 1 if missing or not tools_ok or not skills_ok or not headings_ok else 0

if __name__ == "__main__":
    raise SystemExit(main())
