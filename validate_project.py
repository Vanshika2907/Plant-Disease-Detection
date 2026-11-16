"""
Project validation utility. Run from the project root:
    python validate_project.py
"""
import json
from pathlib import Path
from knowledge_base import KNOWLEDGE_BASE, validate_knowledge_base

ROOT = Path(__file__).resolve().parent
MAPPING_PATH = ROOT / "models" / "class_mapping_68.json"

def normalise_class_names(mapping):
    if not isinstance(mapping, dict) or not mapping:
        raise ValueError("Class mapping must be a non-empty JSON object.")
    first_key = next(iter(mapping))
    if str(first_key).isdigit():
        return [str(value) for value in mapping.values()]
    return [str(key) for key in mapping.keys()]

def main():
    print("=== Plant Health Project Validation ===")
    print(f"Knowledge-base entries: {len(KNOWLEDGE_BASE)}")
    expected = None

    if MAPPING_PATH.exists():
        with MAPPING_PATH.open("r", encoding="utf-8") as handle:
            expected = normalise_class_names(json.load(handle))
        print(f"Expanded mapping entries: {len(expected)}")
    else:
        print("WARNING: class_mapping_68.json not found; exact key comparison skipped.")

    errors = validate_knowledge_base(expected)
    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for issue in errors:
            print(" -", issue)
        raise SystemExit(1)

    if len(KNOWLEDGE_BASE) != 68:
        print("FAILED: expected exactly 68 knowledge entries.")
        raise SystemExit(1)

    print("PASS: structural and safety checks.")
    if expected is not None:
        print("PASS: keys match the expanded class mapping.")
    print("Reminder: this does not verify scientific accuracy; source review is still required.")

if __name__ == "__main__":
    main()
