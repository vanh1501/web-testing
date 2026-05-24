import os
import sys
import subprocess
from pathlib import Path
import pandas as pd
import pymupdf4llm

# Ensure the format_md_query_ready can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from format_md_query_ready import process_file

def extract_excel_to_md(src_path, dest_path):
    print(f"Extracting Excel: {src_path.name}")
    try:
        excel_data = pd.read_excel(src_path, sheet_name=None)
        md_content = f"# {src_path.stem}\n\n"
        md_content += "## Mục lục các Sheet\n"
        for sheet_name in excel_data.keys():
            md_content += f"- {sheet_name}\n"
        md_content += "\n"

        for sheet_name, df in excel_data.items():
            md_content += f"## {sheet_name}\n\n"
            md_content += f"**Natural Language Summary:** Bảng dữ liệu này mô tả nội dung của phần {sheet_name} trong tài liệu {src_path.stem}.\n\n"
            # Format table
            md_table = df.to_markdown(index=False)
            if md_table:
                md_content += md_table + "\n\n"
        
        dest_path.write_text(md_content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Lỗi extract Excel {src_path.name}: {e}")
        return False

def extract_pdf_to_md(src_path, dest_path):
    print(f"Extracting PDF: {src_path.name}")
    try:
        md_text = pymupdf4llm.to_markdown(str(src_path))
        dest_path.write_text(md_text, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Lỗi extract PDF {src_path.name}: {e}")
        return False

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
        
    source_dir = Path(r"d:\Nathan Job\GenAI\MAS-Master-Repo\inputs\02_business_briefs\MindX_HR_SOP_extracted")
    dest_dir = Path(r"d:\Nathan Job\GenAI\MAS-Master-Repo\artifacts\formatted_md\MindX_HR_SOP")
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    validate_script = Path(__file__).parent / "validate_markdown.py"
    
    failed_files = []
    passed_files = []

    files_to_process = list(source_dir.rglob("*.*"))
    print(f"Tìm thấy {len(files_to_process)} files.")

    for file_path in files_to_process:
        if file_path.name.startswith('~') or file_path.name.startswith('.'):
            continue
            
        rel_path = file_path.relative_to(source_dir)
        # Create subdirectories in dest if needed
        dest_file_dir = dest_dir / rel_path.parent
        dest_file_dir.mkdir(parents=True, exist_ok=True)
        
        dest_md_path = dest_file_dir / f"{file_path.stem}.md"
        
        ext = file_path.suffix.lower()
        success = False
        
        if ext == ".pdf":
            success = extract_pdf_to_md(file_path, dest_md_path)
        elif ext in [".xlsx", ".xls"]:
            success = extract_excel_to_md(file_path, dest_md_path)
        else:
            print(f"Bỏ qua file không hỗ trợ: {file_path.name}")
            continue
            
        if success:
            print(f"Normalizing & Enriching: {dest_md_path.name}")
            try:
                # Gọi hàm process_file từ format_md_query_ready.py
                process_file(str(dest_md_path))
                
                print(f"Validating: {dest_md_path.name}")
                # Gọi validate_markdown.py qua subprocess để không bị sys.exit
                result = subprocess.run(
                    [sys.executable, str(validate_script), str(dest_md_path)],
                    capture_output=True, text=True, encoding='utf-8'
                )
                
                if result.returncode == 0:
                    print(f"✅ OK: {dest_md_path.name}")
                    passed_files.append(dest_md_path.name)
                else:
                    print(f"❌ FAIL: {dest_md_path.name}")
                    print(result.stdout)
                    failed_files.append(dest_md_path.name)
            except Exception as e:
                print(f"Lỗi khi xử lý post-extract cho {dest_md_path.name}: {e}")
                failed_files.append(dest_md_path.name)
        else:
            failed_files.append(file_path.name)

    print("\n--- TỔNG KẾT ---")
    print(f"Thành công: {len(passed_files)}")
    print(f"Thất bại / Cần review: {len(failed_files)}")
    
    if failed_files:
        print("Danh sách file lỗi:")
        for f in failed_files:
            print(f" - {f}")

if __name__ == "__main__":
    main()
