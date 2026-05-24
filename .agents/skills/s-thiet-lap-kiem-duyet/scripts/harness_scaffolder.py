import os
import sys

def initialize_harness(workspace_root_path, domain_name):
    print(f"Initializing Harness Layer for Domain '{domain_name}' at {workspace_root_path}")
    
    rules_dir = os.path.join(workspace_root_path, ".agent", "rules")
    memory_dir = os.path.join(workspace_root_path, ".agent", "memory_bus")
    kb_dir = os.path.join(workspace_root_path, "KB")
    artifacts_dir = os.path.join(workspace_root_path, "artifacts", "plans")
    
    os.makedirs(rules_dir, exist_ok=True)
    os.makedirs(memory_dir, exist_ok=True)
    os.makedirs(kb_dir, exist_ok=True)
    os.makedirs(artifacts_dir, exist_ok=True)
    
    # 1. Generate empty progress.md
    progress_file = os.path.join(artifacts_dir, "progress.md")
    if not os.path.exists(progress_file):
        with open(progress_file, "w", encoding="utf-8") as f:
            f.write(f"# Progress Status - Domain: {domain_name}\n\n## Completed\n\n## In Progress\n")
        print(f"Created: {progress_file}")
            
    # 2. Touch ledger
    ledger_file = os.path.join(memory_dir, "ledger.md")
    if not os.path.exists(ledger_file):
        with open(ledger_file, "w", encoding="utf-8") as f:
            f.write("# Memory Bus Ledger\n\n")
        print(f"Created: {ledger_file}")
            
    print("Physical Sandbox ready. Harness layers primed.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python harness_scaffolder.py <workspace_path> <domain_name>")
        sys.exit(1)
        
    initialize_harness(sys.argv[1], sys.argv[2])
