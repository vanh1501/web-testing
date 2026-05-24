import json
import os
import sys

def main():
    evals_path = os.path.join(os.path.dirname(__file__), '../evals/evals.json')
    if not os.path.exists(evals_path):
        print("[FAIL] Missing evals.json")
        sys.exit(1)
    
    with open(evals_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    count = len(data.get("test_cases", []))
    if count >= 2:
        print(f"[PASS] context-engineering evals structured correctly with {count} cases.")
        sys.exit(0)
    else:
        print(f"[FAIL] Need at least 2 test cases. Found {count}")
        sys.exit(1)

if __name__ == "__main__":
    main()
