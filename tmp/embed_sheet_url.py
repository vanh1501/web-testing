import re

script_url = "https://script.google.com/macros/s/AKfycbwsPBDBbvBmUDQHSRQdMje7dxSURiRwp9jEWdDgi9w0Tp2YgDjxhJqMunMRJTS4CANbSA/exec"

files_to_update = [
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/index.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/landing-page-light.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page-light.html"
]

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Thay thế YOUR_GOOGLE_SCRIPT_URL bằng URL thực
    old_line = "const scriptUrl = 'YOUR_GOOGLE_SCRIPT_URL';"
    new_line = f"const scriptUrl = '{script_url}';"
    
    if old_line in content:
        content = content.replace(old_line, new_line)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Đã nhúng URL thành công vào file: {file_path}")
    else:
        print(f"Không tìm thấy placeholder trong file (hoặc đã được cập nhật): {file_path}")
