import re

def clean_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Bỏ | 2 chuyên đề
    content = content.replace("42 buổi | 2 chuyên đề", "42 buổi")
    content = content.replace("48 buổi | 2 chuyên đề", "48 buổi")

    # 2. Xóa thẻ <div class="term-tag">Chuyên đề 1: Advanced</div> và <div class="term-tag">Chuyên đề 2: Intensive</div>
    # Sử dụng regex để bao quát mọi trường hợp khoảng trắng
    content = re.sub(r'<div class="term-tag">Chuyên đề 1: Advanced</div>\s*', '', content)
    content = re.sub(r'<div class="term-tag">Chuyên đề 2: Intensive</div>\s*', '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Đã làm sạch file: {file_path}")

# Đường dẫn file
light_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page-light.html"
dark_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page.html"

clean_html(light_path)
clean_html(dark_path)
