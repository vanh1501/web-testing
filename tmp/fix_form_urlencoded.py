import re

script_url = "https://script.google.com/macros/s/AKfycbwsPBDBbvBmUDQHSRQdMje7dxSURiRwp9jEWdDgi9w0Tp2YgDjxhJqMunMRJTS4CANbSA/exec"

new_js_code = """        function handleFormSubmit(event) {
            event.preventDefault();
            
            // Xác định form được submit
            const form = event.target;
            let parentName = '';
            let phone = '';
            let childAge = '';
            
            // Trích xuất dữ liệu dựa theo form đầu hay form cuối
            const parentInput = form.querySelector('#parent-name') || form.querySelector('#parent-name-bottom');
            const phoneInput = form.querySelector('#phone') || form.querySelector('#phone-bottom');
            
            if (parentInput) parentName = parentInput.value;
            if (phoneInput) phone = phoneInput.value;
            
            // Trích xuất radio button được chọn
            const selectedAge = form.querySelector('input[type="radio"]:checked');
            if (selectedAge) childAge = selectedAge.value + ' tuổi';
            
            // ⚠️ THAY THẾ ĐƯỜNG URL DƯỚI ĐÂY BẰNG URL GOOGLE SCRIPT CỦA BẠN SAU KHI DEPLOY
            const scriptUrl = 'https://script.google.com/macros/s/AKfycbwsPBDBbvBmUDQHSRQdMje7dxSURiRwp9jEWdDgi9w0Tp2YgDjxhJqMunMRJTS4CANbSA/exec'; 
            
            // Thay đổi trạng thái nút Submit để tạo trải nghiệm mượt mà
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Đang gửi...';
            
            // Sử dụng URLSearchParams để gửi dữ liệu dạng form truyền thống (tránh lỗi CORS và JSON)
            const formData = new URLSearchParams();
            formData.append('parentName', parentName);
            formData.append('phone', phone);
            formData.append('childAge', childAge);
            
            // Gửi dữ liệu về Google Sheets thông qua Google Apps Script Web App
            fetch(scriptUrl, {
                method: 'POST',
                mode: 'no-cors', // Tránh lỗi CORS trên trình duyệt
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: formData.toString()
            })
            .then(() => {
                alert('Cảm ơn bạn đã đăng ký trải nghiệm! Chuyên gia MindX sẽ liên hệ hỗ trợ bạn kiểm tra năng lực công nghệ và sắp xếp lịch học thử miễn phí cho con trong vòng 24 giờ tới.');
                form.reset();
            })
            .catch(error => {
                console.error('Lỗi gửi form:', error);
                alert('Có lỗi xảy ra khi gửi thông tin. Bạn vui lòng liên hệ hotline hoặc thử lại nhé!');
            })
            .finally(() => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            });
        }"""

files_to_update = [
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/index.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/landing-page-light.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page.html",
    "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page-light.html"
]

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Thay thế hàm handleFormSubmit cũ bằng phiên bản URLSearchParams mới
    pattern = r'function handleFormSubmit\(event\) \{[\s\S]*?\}'
    content = re.sub(pattern, new_js_code, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Đã cập nhật xong form handler URL-encoded cho file: {file_path}")
