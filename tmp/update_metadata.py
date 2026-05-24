import os
import glob
import re

workspace_dir = r'd:\Nathan Job\GenAI\MAS-Master-Repo\managed_workspaces\mindx-agent_v1'

def update_metadata(file_path, prefix):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def repl(match):
        name_val = match.group(2).strip('\"\'')
        if not name_val.startswith(prefix):
            return f'{match.group(1)}"{prefix}{name_val}"'
        return match.group(0)

    # regex to find name: "..." or name: ... in YAML frontmatter
    new_content = re.sub(r'^(name:\s*)(.+)$', repl, content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {os.path.relpath(file_path, workspace_dir).replace(os.sep, "/")}')
        return True
    return False

workflows = glob.glob(os.path.join(workspace_dir, '.agents/workflows/**/*.md'), recursive=True)
skills = glob.glob(os.path.join(workspace_dir, '.agents/skills/**/SKILL.md'), recursive=True)

w_count = 0
for w in workflows:
    if 'WORKFLOW_INDEX.md' in w or 'CHANGELOG.md' in w or 'README.md' in w: 
        continue
    if update_metadata(w, 'w-'):
        w_count += 1

s_count = 0
for s in skills:
    # also skip the legacy 00- prefix by cleaning it first if we want, but let's just prefix it if it lacks 's-'
    # wait, if it already has '00-' maybe we replace it with 's-'? The user said "thẻ metadata để w- hoặc s- cho tôi để phân biệt".
    # I should replace '00-' with 's-' instead of appending 's-00-'. Let's do that!
    
    with open(s, 'r', encoding='utf-8') as f:
        content = f.read()
        
    def repl_skill(match):
        name_val = match.group(2).strip('\"\'')
        if name_val.startswith('00-'):
            name_val = name_val[3:]
        if not name_val.startswith('s-'):
            return f'{match.group(1)}"{"s-"}{name_val}"'
        return match.group(0)

    new_content = re.sub(r'^(name:\s*)(.+)$', repl_skill, content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(s, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {os.path.relpath(s, workspace_dir).replace(os.sep, "/")}')
        s_count += 1

print(f'Updated {w_count} workflows and {s_count} skills.')
