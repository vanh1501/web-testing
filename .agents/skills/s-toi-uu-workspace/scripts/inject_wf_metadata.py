import os
import re
import sys
from pathlib import Path

def heal_workflow_metadata(workspace_path: str):
    ws = Path(workspace_path).resolve()
    workflows_dir = ws / '.agents' / 'workflows'
    if not workflows_dir.exists():
        print(f"Directory not found: {workflows_dir}")
        return

    fixed_count = 0
    for md_file in workflows_dir.rglob('*.md'):
        try:
            text = md_file.read_text(encoding='utf-8')
            has_yaml = text.startswith('---')
            has_desc = re.search(r'^description:', text, re.MULTILINE)
            has_triggers = re.search(r'^semantic_triggers:', text, re.MULTILINE)
            
            if not has_yaml or not has_desc or not has_triggers:
                print(f"Healing metadata for: {md_file.name}")
                
                # Default frontmatter
                desc = f"Auto-generated description for {md_file.stem}"
                trigger = md_file.stem.replace('-', ' ')
                frontmatter = f"---\ndescription: {desc}\nsemantic_triggers: ['{trigger}']\n---\n\n"
                
                if has_yaml:
                    # Strip existing broken yaml block to avoid duplication
                    end_idx = text.find('---', 3)
                    if end_idx != -1:
                        text = text[end_idx+3:].lstrip()
                
                new_text = frontmatter + text
                md_file.write_text(new_text, encoding='utf-8')
                fixed_count += 1
        except Exception as e:
            print(f"Error reading {md_file.name}: {e}")

    print(f"Healed metadata for {fixed_count} workflows.")

if __name__ == '__main__':
    ws_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    heal_workflow_metadata(ws_path)
