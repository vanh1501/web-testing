import os
import shutil
import re

# Định nghĩa đường dẫn
SOURCE_DIR = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Kho-Du-Lieu/Du-Lieu-Vao/angle-landing-page-ag-solution"
TARGET_DIR = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/.agents"

def deploy_rules():
    src_rules = os.path.join(SOURCE_DIR, ".agents", "rules")
    dst_rules = os.path.join(TARGET_DIR, "rules")
    os.makedirs(dst_rules, exist_ok=True)
    
    print("--- DEPLOYING RULES ---")
    for file_name in os.listdir(src_rules):
        if file_name.endswith(".md"):
            src_file = os.path.join(src_rules, file_name)
            dst_file = os.path.join(dst_rules, file_name)
            shutil.copy2(src_file, dst_file)
            print(f"Copied rule: {file_name}")

def deploy_skills():
    src_skills = os.path.join(SOURCE_DIR, ".agents", "skills")
    dst_skills = os.path.join(TARGET_DIR, "skills")
    os.makedirs(dst_skills, exist_ok=True)
    
    print("\n--- DEPLOYING SKILLS ---")
    for skill_name in os.listdir(src_skills):
        src_skill_dir = os.path.join(src_skills, skill_name)
        if os.path.isdir(src_skill_dir):
            new_skill_name = f"00-{skill_name}"
            dst_skill_dir = os.path.join(dst_skills, new_skill_name)
            
            # Copy thư mục
            if os.path.exists(dst_skill_dir):
                shutil.rmtree(dst_skill_dir)
            shutil.copytree(src_skill_dir, dst_skill_dir)
            print(f"Copied skill folder to: {new_skill_name}")
            
            # Sửa file SKILL.md
            skill_md_path = os.path.join(dst_skill_dir, "SKILL.md")
            if os.path.exists(skill_md_path):
                with open(skill_md_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Sửa name: phan-tich-angle thành name: 00-phan-tich-angle
                content = re.sub(r"name:\s*" + re.escape(skill_name), f"name: {new_skill_name}", content)
                # Sửa tiêu đề # Skill: phan-tich-angle thành # Skill: 00-phan-tich-angle
                content = content.replace(f"# Skill: {skill_name}", f"# Skill: {new_skill_name}")
                # Sửa mô tả liên kết chéo
                content = content.replace("workflow `tao-landing-page-theo-angle`", "workflow `00-tao-landing-page-theo-angle`")
                
                with open(skill_md_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  -> Enriched SKILL.md metadata for {new_skill_name}")

def deploy_workflows():
    src_workflows = os.path.join(SOURCE_DIR, ".agents", "workflows")
    dst_workflows = os.path.join(TARGET_DIR, "workflows")
    os.makedirs(dst_workflows, exist_ok=True)
    
    print("\n--- DEPLOYING WORKFLOWS ---")
    src_file = os.path.join(src_workflows, "tao-landing-page-theo-angle.md")
    dst_file = os.path.join(dst_workflows, "00-tao-landing-page-theo-angle.md")
    
    if os.path.exists(src_file):
        with open(src_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Sửa tên workflow và lệnh trigger
        content = content.replace("# Workflow — Tạo landing page theo angle", "# Quy Trình: /w-00-tao-landing-page-theo-angle")
        content = content.replace("`/tao-landing-page-theo-angle dau-vao/input-angle-moi.md`", "`/w-00-tao-landing-page-theo-angle dau-vao/input-angle-moi.md`")
        
        # Sửa danh sách skill chain sang tên có tiền tố
        skills_to_replace = [
            "phan-tich-angle",
            "trich-claim-tu-landing-page",
            "viet-lai-copy-landing-page",
            "kiem-tra-message-match",
            "tao-html-landing-page",
            "kiem-tra-html",
            "tao-github-handoff"
        ]
        
        for sk in skills_to_replace:
            content = content.replace(f"1. `{sk}`", f"1. `00-{sk}`")
            content = content.replace(f"2. `{sk}`", f"2. `00-{sk}`")
            content = content.replace(f"3. `{sk}`", f"3. `00-{sk}`")
            content = content.replace(f"4. `{sk}`", f"4. `00-{sk}`")
            content = content.replace(f"5. `{sk}`", f"5. `00-{sk}`")
            content = content.replace(f"6. `{sk}`", f"6. `00-{sk}`")
            content = content.replace(f"7. `{sk}`", f"7. `00-{sk}`")
            
        with open(dst_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Copied and optimized workflow to: 00-tao-landing-page-theo-angle.md")

if __name__ == "__main__":
    deploy_rules()
    deploy_skills()
    deploy_workflows()
    print("\n=== DEPLOYMENT COMPLETED SUCCESSFULY ===")
