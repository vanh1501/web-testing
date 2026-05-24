import os
import glob

workflow_dir = r'd:\Nathan Job\GenAI\MAS-Master-Repo\managed_workspaces\mindx-agent_v1\.agents\workflows'
md_files = glob.glob(os.path.join(workflow_dir, '**/*.md'), recursive=True)

shells = []
for file in md_files:
    if 'WORKFLOW_INDEX.md' in file or 'CHANGELOG.md' in file or 'README.md' in file:
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    size = len(content.encode('utf-8'))
    has_skills = 'Assigned Skills' in content or 'Skill Target' in content
    has_contract = 'Output Contract' in content
    has_circuit = 'Circuit Breaker' in content
    
    if size < 3000 or not has_contract or not has_circuit:
        shells.append({
            'file': os.path.relpath(file, workflow_dir).replace('\\', '/'),
            'size': size,
            'has_skills': has_skills,
            'has_contract': has_contract,
            'has_circuit': has_circuit
        })

print(f'Total workflows checked: {len(md_files)}')
print(f'Found {len(shells)} potential shell workflows:')
for s in shells:
    print(f"- {s['file']} (Size: {s['size']}B, Skills: {s['has_skills']}, Contract: {s['has_contract']}, Circuit: {s['has_circuit']})")
