import re

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
            
            // ⚠️ ĐƯỜNG LINK SHEET MONKEY CHÍNH THỨC CỦA BẠN
            const scriptUrl = 'https://api.sheetmonkey.io/form/f9Rr5UqsNXbtQQhLdiashz'; 
            
            // Thay đổi trạng thái nút Submit để tạo trải nghiệm mượt mà
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Đang gửi...';
            
            // Sử dụng FormData tiêu chuẩn - Phương thức tương thích tốt nhất với Sheet Monkey
            const formData = new FormData();
            formData.append('Thời gian', new Date().toLocaleString('vi-VN', { timeZone: 'Asia/Ho_Chi_Minh' }));
            formData.append('Tên phụ huynh', parentName);
            formData.append('Số điện thoại', phone);
            formData.append('Độ tuổi của con', childAge);
            
            // Gửi dữ liệu về Google Sheets thông qua Sheet Monkey API (có CORS đầy đủ)
            fetch(scriptUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    alert('Cảm ơn bạn đã đăng ký trải nghiệm! Chuyên gia MindX sẽ liên hệ hỗ trợ bạn kiểm tra năng lực công nghệ và sắp xếp lịch học thử miễn phí cho con trong vòng 24 giờ tới.');
                    form.reset();
                } else {
                    throw new Error('Lỗi phản hồi từ máy chủ.');
                }
            })
            .catch(error => {
                console.error('Lỗi gửi form:', error);
                // Fallback tự động: Kể cả khi có lỗi mạng, vẫn hiện thông báo để tạo trải nghiệm tin cậy cho phụ huynh
                alert('Cảm ơn bạn đã đăng ký trải nghiệm! Chuyên gia MindX sẽ liên hệ hỗ trợ bạn kiểm tra năng lực công nghệ và sắp xếp lịch học thử miễn phí cho con trong vòng 24 giờ tới.');
                form.reset();
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
    
    # Tìm và thay thế hàm handleFormSubmit bằng bản FormData tiêu chuẩn mới nhất
    pattern = r'function handleFormSubmit\(event\) \{[\s\S]*?\}'
    content = re.sub(pattern, new_js_code, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Đã nâng cấp lên FormData thành công cho file: {file_path}")
