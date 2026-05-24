# -*- coding: utf-8 -*-
import re

file_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Thay thế mã màu RGB của màu cam cũ (255, 107, 0) sang màu đỏ thương hiệu MindX (227, 31, 38)
content = content.replace("255, 107, 0", "227, 31, 38")

# 2. Thay thế gradient cam trong .submit-btn sang màu đỏ
content = content.replace("linear-gradient(135deg, var(--primary), #ffa000)", "linear-gradient(135deg, var(--primary), #a61217)")

# 3. Chuyển đổi icon quote-icon màu cam sang đỏ mờ trong CSS
content = content.replace("color: rgba(255, 107, 0, 0.08);", "color: rgba(227, 31, 38, 0.08);")

# 4. Sửa form đăng ký ở cuối trang để có id="register-form" để các nút CTA neo vào mượt mà
content = content.replace('<div class="hero-form-card">', '<div class="hero-form-card" id="register-form">')

# 5. Định nghĩa các khối CTA sẽ chèn vào cuối các section
cta_html = """
            <!-- Section CTA Button -->
            <div class="section-cta">
                <a href="#register-form" class="cta-button-red">
                    Đăng Ký Đánh Giá Năng Lực Miễn Phí Cho Con <i class="fa-solid fa-arrow-right"></i>
                </a>
            </div>
"""

# Chèn CTA vào cuối Problems Section (trước thẻ </div></section> kết thúc section)
# Cấu trúc:
#                 </div>
#             </div>
#         </div>
#     </section>
# Chúng ta sẽ tìm thẻ kết thúc problems: </section> của class="problems"
problems_pattern = r'(<section class="problems">.*?</div>\s*</div>\s*)(</div>\s*</section>)'
content = re.sub(problems_pattern, r'\1' + cta_html + r'\2', content, flags=re.DOTALL)

# Chèn CTA vào cuối Solution Section
solution_pattern = r'(<section class="solution">.*?</div>\s*</div>\s*)(</div>\s*</section>)'
content = re.sub(solution_pattern, r'\1' + cta_html + r'\2', content, flags=re.DOTALL)

# Chèn CTA vào cuối Roadmap Section
roadmap_pattern = r'(<section class="roadmap">.*?</div>\s*</div>\s*)(</div>\s*</section>)'
content = re.sub(roadmap_pattern, r'\1' + cta_html + r'\2', content, flags=re.DOTALL)

# Chèn CTA vào cuối Sponsorship Section
sponsorship_pattern = r'(<section class="sponsorship">.*?</div>\s*</div>\s*)(</div>\s*</section>)'
content = re.sub(sponsorship_pattern, r'\1' + cta_html + r'\2', content, flags=re.DOTALL)

# Chèn CTA vào cuối USPs Section
usps_pattern = r'(<section class="usps">.*?</div>\s*</div>\s*)(</div>\s*</section>)'
content = re.sub(usps_pattern, r'\1' + cta_html + r'\2', content, flags=re.DOTALL)

# Chèn CTA vào cuối Testimonials Section
testimonials_pattern = r'(<section class="testimonials">.*?</div>\s*</div>\s*)(</div>\s*</section>)'
content = re.sub(testimonials_pattern, r'\1' + cta_html + r'\2', content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Brand color applied and CTA buttons injected successfully!")
