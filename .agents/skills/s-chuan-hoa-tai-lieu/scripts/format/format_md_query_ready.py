import re
import sys
import datetime
from pathlib import Path

def remove_html_tags(text):
    """Xóa bỏ các tag HTML rác trong văn bản Markdown"""
    return re.sub(r'<[^>]+>', '', text)

def _strip_academic_headers(text: str) -> str:
    """Stage 2: Normalize - Quét và dọn sạch các Header/Footer lặp lại tàn dư từ PDF"""
    # Xoá chuẩn mẫu IRJAEM (cụm header/footer rác)
    pattern = (
        r'IRJAEM\s*\d+\s*'
        r'(?:\n+)?(?:\*\*International Research Journal on Advanced Engineering\*\*|International Research Journal on Advanced Engineering)\s*'
        r'(?:\n+)?(?:\*\*and Management\*\*|and Management)\s*'
        r'(?:\n+)?(?:\[https://goldncloudpublications\.com\]\(about:blank\)|https://goldncloudpublications\.com)\s*'
        r'(?:\n+)?https://doi\.org/10\.47392/IRJAEM\.\d+\.\d+\s*'
        r'(?:\n+)?e ISSN:\s*2584-2854\s*'
        r'(?:\n+)?Volume:\s*03\s*'
        r'(?:\n+)?Issue:08 August 2025\s*'
        r'(?:\n+)?Page No:\s*\d+-\d+'
    )
    # Rút gọn pattern rộng hơn một chút tránh miss
    pattern2 = (
        r'IRJAEM\s*\d+.*?'
        r'e ISSN:\s*2584-2854.*?'
        r'(?:Page No:\s*\d+-\d+|\n)'
    )
    
    text = re.sub(pattern2, '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Xóa các dòng IRJAEM dở dang còn sót
    text = re.sub(r'IRJAEM\s+\d+\s*$', '', text, flags=re.MULTILINE)
    return text

def _promote_bold_to_heading(text: str) -> str:
    """Stage 2: Normalize - Thăng cấp bôi đậm mồ côi thành Heading 2"""
    # Tìm các dòng chỉ chứa chữ bôi đậm, không quá dài (VD tiêu đề mục)
    # Khớp dạng **Chữ bôi đậm** hoặc **1.** **Tiêu đề**
    lines = text.split('\n')
    for i, line in enumerate(lines):
        striped = line.strip()
        # Bắt các pattern tiêu đề rỗng: **References**, **4.** **Results...**
        if re.match(r'^(\*\*[^\*]+\*\*\s*)+$', striped) and len(striped) > 3 and len(striped) < 100:
            clean_title = striped.replace('**', '').strip()
            # Promote to H2
            lines[i] = f"\n## {clean_title}\n"
    return '\n'.join(lines)

def normalize_blank_lines(text):
    """Gộp nhiều dòng trống thành 2 và dọn whitespace"""
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r'[ \t]+$', '', text, flags=re.MULTILINE)
    return text.strip() + '\n'

def _derive_title(text: str, filename: str) -> str:
    # First non-empty line
    first_line = next((line.strip() for line in text.split('\n') if line.strip()), "")
    if first_line and len(first_line) < 120 and '---' not in first_line:
        return first_line.replace('#', '').strip()
    name = filename.rsplit('.', 1)[0]
    return name.replace('_', ' ').replace('-', ' ').title()

def fix_heading_hierarchy(text: str) -> str:
    """Stage 2: Normalize - Đảm bảo heading không nhảy cóc level (vd # xuống ###)"""
    lines = text.split('\n')
    heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$')
    headings = []
    
    for i, line in enumerate(lines):
        match = heading_pattern.match(line)
        if match:
            headings.append((i, len(match.group(1)), match.group(2)))

    if not headings:
        return text

    prev_level = 0
    for idx, (line_idx, level, heading_text) in enumerate(headings):
        if idx == 0:
            fixed = 1 
        else:
            if level <= prev_level:
                fixed = level
            elif level > prev_level + 1:
                fixed = prev_level + 1
            else:
                fixed = level

        fixed = max(1, min(6, fixed))
        lines[line_idx] = f"{'#' * fixed} {heading_text}"
        prev_level = fixed

    return '\n'.join(lines)

def wrap_orphan_content(text: str, source_filename: str) -> str:
    """Stage 2: Normalize - Mọi orphan text đứng trước H1 đầu tiên phải được wrap vào một H1 Title"""
    first_heading = re.search(r'^#{1,6}\s+', text, re.MULTILINE)
    
    if first_heading and first_heading.start() > 0:
        orphan = text[:first_heading.start()].strip()
        if orphan:
            title = _derive_title(orphan, source_filename)
            text = f"# {title}\n\n{orphan}\n\n{text[first_heading.start():]}"
    elif not first_heading:
        title = _derive_title(text, source_filename)
        text = f"# {title}\n\n{text}"
        
    return text

def ensure_yaml_frontmatter(text, original_filename):
    """Stage 3: Enrich - RAG Frontmatter Injection"""
    if text.strip().startswith('---'):
        return text
        
    title_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    title = title_match.group(1) if title_match else original_filename.replace('.md', '')
    
    sections = re.findall(r'^##\s+(.+)$', text, re.MULTILINE)
    
    clean_text = re.sub(r'[#*|`\-\[\]()]', '', text)
    word_count = len(clean_text.split())
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Tạo Frontmatter chuẩn Stage 3
    frontmatter = f"""---
title: "{title.replace('"', '')}"
source_file: "{original_filename}"
source_type: "docx"
doc_type: "document"
date_processed: "{date_str}"
word_count: {word_count}
tags: ["query_ready", "auto_formatted"]
sections: {sections[:10]}
---

"""
    return frontmatter + text

def process_file(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File {file_path} không tồn tại.")
        sys.exit(1)
        
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

    # Nếu file đã có yaml ở đầu, bỏ yaml ra trước khi gọt text kẻo bị loạn
    frontmatter_block = ""
    if content.strip().startswith('---'):
        fm_end = content.find('---', 3)
        if fm_end > 0:
            frontmatter_block = content[:fm_end+3]
            content = content[fm_end+3:]

    # 1. Zero HTML
    content = remove_html_tags(content)
    
    # 2. Stage 2: Normalization (Hierarchy & Orphan)
    content = _strip_academic_headers(content)
    content = _promote_bold_to_heading(content)
    content = fix_heading_hierarchy(content)
    content = wrap_orphan_content(content, path.name)
    content = normalize_blank_lines(content)
    
    # 3. Stage 3: Enrichment (Metadata Frontmatter)
    if not frontmatter_block:
        content = ensure_yaml_frontmatter(content, path.name)
    else:
        content = frontmatter_block + "\n\n" + content
    
    # Ghi đè file mới
    try:
        path.write_text(content, encoding='utf-8')
        print(f"Đã format thành công: {file_path}")
    except Exception as e:
        print(f"Error writing file {file_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
         pass
         
    if len(sys.argv) < 2:
        print("Sử dụng: python format_md_query_ready.py <path_to_md_file>")
        sys.exit(1)
        
    target_file = sys.argv[1]
    process_file(target_file)
