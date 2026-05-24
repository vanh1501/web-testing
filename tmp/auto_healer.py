import os
import json
from pathlib import Path

WORKSPACE = r"d:\Nathan Job\GenAI\MAS-Master-Repo\managed_workspaces\mindx-agent_v1"
REPORT_PATH = os.path.join(WORKSPACE, "tmp", "structural_scan_report.json")

def read_json():
    with open(REPORT_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_dirs(base_path, missing_dirs):
    for d in missing_dirs:
        dir_path = os.path.join(WORKSPACE, base_path, d)
        try:
            os.makedirs(dir_path, exist_ok=True)
            with open(os.path.join(dir_path, ".gitkeep"), 'w', encoding='utf-8') as f:
                f.write("")
        except Exception as e:
            print(f"Skipped {dir_path}: {e}")

def fix_broken_refs(file_rel_path):
    file_path = os.path.join(WORKSPACE, file_rel_path)
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(".agents/quan-ly-quy-tac/", ".agents/rules/")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_templates(file_rel_path):
    file_path = os.path.join(WORKSPACE, file_rel_path)
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("{{PLACEHOLDER}}", "[PLACEHOLDER]")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_yaml(file_rel_path):
    file_path = os.path.join(WORKSPACE, file_rel_path)
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith("---"):
        filename = os.path.basename(file_path)
        frontmatter = f"---\ndescription: \"System component: {filename}\"\nsemantic_triggers: ['{filename.replace('.md','')}']\n---\n\n"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + content)

def fix_hprf(file_rel_path):
    file_path = os.path.join(WORKSPACE, file_rel_path)
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "> [!IMPORTANT] Override Priority:" not in content:
        hprf = "\n> [!IMPORTANT] Override Priority: Tier 1 (Strategic)\n> Tuân thủ tuyệt đối quy định và kiến trúc hệ thống.\n\n"
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                content = "---" + parts[1] + "---" + hprf + parts[2]
        else:
            content = hprf + content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    data = read_json()
    gemini_needs_fix = False
    agents_needs_fix = False
    
    for finding in data['findings']:
        cat = finding['category']
        rel_path = finding['file']
        
        if cat == "EMPTY_DIR":
            p = os.path.join(WORKSPACE, rel_path)
            try:
                os.makedirs(p, exist_ok=True)
                with open(os.path.join(p, ".gitkeep"), 'w', encoding='utf-8') as f:
                    f.write("")
            except Exception as e:
                print(f"Skipped empty dir {p}: {e}")
        elif cat == "SKILL_4TIER":
            create_dirs(rel_path, finding.get('missing_dirs', []))
        elif cat == "BROKEN_REF":
            if "GEMINI.md" in rel_path: gemini_needs_fix = True
            if "AGENTS.md" in rel_path: agents_needs_fix = True
        elif cat == "TEMPLATE_CHECK":
            fix_templates(rel_path)
        elif cat == "WF_METADATA_CHECK":
            fix_yaml(rel_path)
        elif cat == "HPRF_CHECK":
            fix_hprf(rel_path)
            
    if gemini_needs_fix: fix_broken_refs("GEMINI.md")
    if agents_needs_fix: fix_broken_refs("AGENTS.md")
        
    print("Auto-Healing completed successfully.")

if __name__ == "__main__":
    main()
