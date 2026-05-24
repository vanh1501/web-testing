import os

def sync_all():
    # 1. Cập nhật DANH-SACH-QUY-TAC.md
    rules_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Bang-Dieu-Khien/DANH-SACH-QUY-TAC.md"
    new_rules = [
        "| l0-khong-tu-publish | .agents/quan-ly-quy-tac/l0-khong-tu-publish.md | L0 | Hoạt động |",
        "| l1-can-duyet-truoc-khi-chay | .agents/quan-ly-quy-tac/l1-can-duyet-truoc-khi-chay.md | L1 | Hoạt động |",
        "| l1-giu-nguyen-section-co-dinh | .agents/quan-ly-quy-tac/l1-giu-nguyen-section-co-dinh.md | L1 | Hoạt động |",
        "| l1-khong-bia-claim-marketing | .agents/quan-ly-quy-tac/l1-khong-bia-claim-marketing.md | L1 | Hoạt động |"
    ]
    
    with open(rules_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Cập nhật ngày
    for i, line in enumerate(lines):
        if "Cập nhật lần cuối" in line:
            lines[i] = "Cập nhật lần cuối: 2026-05-23\n"
            break
            
    # Thêm các quy tắc mới vào cuối bảng
    last_idx = len(lines)
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip().startswith("|"):
            last_idx = i + 1
            break
            
    for r in new_rules:
        # Tránh trùng
        rule_name = r.split("|")[1].strip()
        already_exists = False
        for line in lines:
            if rule_name in line:
                already_exists = True
                break
        if not already_exists:
            lines.insert(last_idx, r + "\n")
            last_idx += 1
            
    with open(rules_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("Updated DANH-SACH-QUY-TAC.md successfully")

    # 2. Cập nhật DANH-SACH-KY-NANG.md
    skills_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Bang-Dieu-Khien/DANH-SACH-KY-NANG.md"
    new_skills = [
        "| 00-phan-tich-angle | .agents/skills/00-phan-tich-angle/SKILL.md | Hoạt động | — |",
        "| 00-trich-claim-tu-landing-page | .agents/skills/00-trich-claim-tu-landing-page/SKILL.md | Hoạt động | — |",
        "| 00-viet-lai-copy-landing-page | .agents/skills/00-viet-lai-copy-landing-page/SKILL.md | Hoạt động | — |",
        "| 00-kiem-tra-message-match | .agents/skills/00-kiem-tra-message-match/SKILL.md | Hoạt động | — |",
        "| 00-tao-html-landing-page | .agents/skills/00-tao-html-landing-page/SKILL.md | Hoạt động | — |",
        "| 00-kiem-tra-html | .agents/skills/00-kiem-tra-html/SKILL.md | Hoạt động | — |",
        "| 00-tao-github-handoff | .agents/skills/00-tao-github-handoff/SKILL.md | Hoạt động | — |"
    ]
    
    with open(skills_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if "Cập nhật lần cuối" in line:
            lines[i] = "Cập nhật lần cuối: 2026-05-23\n"
            break
            
    last_idx = len(lines)
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip().startswith("|"):
            last_idx = i + 1
            break
            
    for s in new_skills:
        skill_name = s.split("|")[1].strip()
        already_exists = False
        for line in lines:
            if skill_name in line:
                already_exists = True
                break
        if not already_exists:
            lines.insert(last_idx, s + "\n")
            last_idx += 1
            
    with open(skills_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("Updated DANH-SACH-KY-NANG.md successfully")

    # 3. Cập nhật DANH-SACH-QUY-TRINH.md
    workflows_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Bang-Dieu-Khien/DANH-SACH-QUY-TRINH.md"
    new_workflow = "| `/w-00-tao-landing-page-theo-angle` | Biến content angle thành landing page HTML hoàn chỉnh (có kiểm claim, message match, HTML QA và GitHub handoff). |"
    
    with open(workflows_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    # Tìm chỗ để chèn (Phần 1. Quy Trình Nghiệp Vụ)
    target_idx = -1
    for i, line in enumerate(lines):
        if "## 1. Quy Trình Nghiệp Vụ" in line:
            # Tìm dòng cuối cùng của bảng quy trình nghiệp vụ
            for j in range(i+1, len(lines)):
                if lines[j].strip().startswith("|") and not lines[j+1].strip().startswith("|"):
                    target_idx = j + 1
                    break
            break
            
    if target_idx != -1:
        already_exists = False
        for line in lines:
            if "/w-00-tao-landing-page-theo-angle" in line:
                already_exists = True
                break
        if not already_exists:
            lines.insert(target_idx, new_workflow + "\n")
            
    with open(workflows_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("Updated DANH-SACH-QUY-TRINH.md successfully")

    # 4. Cập nhật BANG-DIEU-KHIEN.md
    bdk_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Bang-Dieu-Khien/BANG-DIEU-KHIEN.md"
    with open(bdk_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Cập nhật số lượng
    # - Kỹ năng đang hoạt động: 17 -> 24
    # - Quy tắc đang hoạt động: 14 -> 18
    # - Quy trình đang hoạt động: 19 -> 20
    content = content.replace("Kỹ năng đang hoạt động: 17", "Kỹ năng đang hoạt động: 24")
    content = content.replace("Quy tắc đang hoạt động: 14", "Quy tắc đang hoạt động: 18")
    content = content.replace("Quy trình đang hoạt động: 19", "Quy trình đang hoạt động: 20")
    
    # Cập nhật hoạt động gần đây
    recent_activity_marker = "| Ngày | Hoạt động | Trạng thái |\n|------|-----------|------------|\n"
    new_activity = "| 2026-05-23 | Deploy và tối ưu giải pháp Dual-Route Spec Pack tạo Landing Page theo Angle (`/w-00-tao-landing-page-theo-angle`) | Hoàn thành |\n"
    
    if recent_activity_marker in content and new_activity not in content:
        content = content.replace(recent_activity_marker, recent_activity_marker + new_activity)
        
    with open(bdk_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated BANG-DIEU-KHIEN.md successfully")

if __name__ == "__main__":
    sync_all()
