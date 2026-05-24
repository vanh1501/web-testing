import sys
import re
import yaml
from pathlib import Path

def validate_markdown(file_path):
    """Stage 4: VALIDATE - Gate kiểm định cuối cùng của pipeline."""
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File {file_path} không tồn tại.")
        sys.exit(1)
        
    try:
        md_content = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

    issues = []
    warnings = []
    checks_passed = 0
    total_checks = 4

    # CHECK 1: YAML Frontmatter
    is_marp = False
    if md_content.startswith('---'):
        fm_end = md_content.find('---', 3)
        if fm_end > 0:
            try:
                fm_data = yaml.safe_load(md_content[3:fm_end])
                is_marp = isinstance(fm_data, dict) and fm_data.get('marp') is True
                checks_passed += 1
            except yaml.YAMLError:
                issues.append("FAIL: Lỗi cú pháp YAML Frontmatter")
        else:
            issues.append("FAIL: Không đóng Frontmatter (thiếu ---)")
    else:
        issues.append("FAIL: Thiếu YAML Frontmatter")

    # CHECK 2: Single H1 Document Title (Bypass if Marp)
    h1_count = len(re.findall(r'^#\s+', md_content, re.MULTILINE))
    if is_marp:
        if h1_count >= 1:
            checks_passed += 1
        else:
            issues.append("FAIL: Slide Marp thiếu tiêu đề H1")
    else:
        if h1_count == 1:
            checks_passed += 1
        elif h1_count == 0:
            issues.append("FAIL: Dữ liệu bị câm (Không có thẻ H1 - Document title)")
        else:
            warnings.append(f"WARN: Phát hiện {h1_count} thẻ H1. Khuyên dùng duy nhất 1 thẻ H1.")
            checks_passed += 0.5

    # CHECK 3: Heading Hierarchy Skip
    heading_levels = [
        len(m.group(1))
        for m in re.finditer(r'^(#{1,6})\s+', md_content, re.MULTILINE)
    ]
    skip_found = False
    for i in range(1, len(heading_levels)):
        if heading_levels[i] > heading_levels[i-1] + 1:
            skip_found = True
            break
    if not skip_found:
        checks_passed += 1
    else:
        issues.append("FAIL: Phát hiện lỗi nhảy cóc level Heading (Skip Content).")

    # CHECK 4: Orphan Content Zero-Tolerance (Bypass if Marp)
    if is_marp:
        checks_passed += 1
    else:
        body = md_content
        if body.startswith('---'):
            fm_end = body.find('---', 3)
            body = body[fm_end+3:].strip()
            
        first_heading_pos = re.search(r'^#{1,6}\s+', body, re.MULTILINE)
        if first_heading_pos and first_heading_pos.start() == 0:
            checks_passed += 1
        elif first_heading_pos:
            orphan = body[:first_heading_pos.start()].strip()
            if orphan:
                issues.append(f"FAIL: Text lơ lửng Orphan Content ({len(orphan)} chars) nằm ngoài vùng Heading.")
            else:
                checks_passed += 1
        else:
            checks_passed += 1  # No headings at all means implicitly everything is under title

    # Chấm điểm 
    score = checks_passed / total_checks
    print(f"\n--- SCORE: {score:.2f} ---")
    
    if warnings:
        print("Cảnh báo:")
        for w in warnings:
            print(f" - {w}")
            
    if issues:
        print("Lỗi Ngắt Mạch:")
        for i in issues:
            print(f" - {i}")

    if score >= 0.8 and not issues:
        print("\n✅ VALIDATED OK: Document is Ready for RAG.")
        sys.exit(0)
    else:
        print("\n❌ VALIDATION REJECTED: Tệp chưa đạt chuẩn. Yêu cầu pipeline xử lý lại.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
        
    if len(sys.argv) < 2:
        print("Sử dụng: python validate_markdown.py <path_to_md_file>")
        sys.exit(1)
        
    validate_markdown(sys.argv[1])
