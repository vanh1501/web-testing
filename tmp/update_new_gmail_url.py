import re

script_url = "https://script.google.com/macros/s/AKfycbwDz7pwkiVJPV1rDb5bcfzan6qJkzFKyiVRbic7kTgvlolypW_rfQiMaIhjD0CLKDuLOg/exec"

files_to_update = [
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/index.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/landing-page-light.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page-light.html"
]

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Thay thế URL cũ bằng URL mới tinh từ Gmail cá nhân
    pattern = r"const scriptUrl = 'https://script\.google\.com/macros/s/[^']+/exec';"
    replacement = f"const scriptUrl = '{script_url}';"
    
    content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Đã nhúng URL Gmail mới thành công vào file: {file_path}")
