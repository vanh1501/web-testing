import re

# Định nghĩa CSS mới cho Dark Theme
dark_css_replacement = """        /* --- Section: Special Sponsorship (2 Chương trình bảo trợ) --- */
        .sponsorship {
            padding: 100px 0;
            background: linear-gradient(180deg, rgba(11, 15, 25, 0.5) 0%, rgba(21, 28, 46, 0.3) 100%);
            border-top: 1px solid rgba(255, 255, 255, 0.02);
        }

        .sponsor-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 32px;
            margin-top: 48px;
        }

        @media (max-width: 991px) {
            .sponsor-grid {
                grid-template-columns: 1fr;
                gap: 40px;
            }
        }

        .sponsor-card {
            background-color: var(--bg-card);
            border-radius: 24px;
            padding: 44px;
            position: relative;
            display: flex;
            flex-direction: column;
            transition: var(--transition);
            overflow: hidden;
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.25);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .sponsor-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.35);
        }

        .sponsor-card.business {
            border-top: 8px solid var(--primary);
            border-color: rgba(227, 31, 38, 0.15);
        }

        .sponsor-card.study-abroad {
            border-top: 8px solid var(--accent-green);
            border-color: rgba(0, 168, 89, 0.15);
        }

        .sponsor-badge-top {
            position: absolute;
            top: 20px;
            right: -35px;
            background: linear-gradient(135deg, var(--accent-yellow) 0%, #ffc000 100%);
            color: var(--accent-navy);
            font-size: 10px;
            font-weight: 900;
            padding: 6px 36px;
            transform: rotate(45deg);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .sponsor-card h3 {
            font-size: 24px;
            color: #fff;
            margin-bottom: 12px;
            font-weight: 800;
            line-height: 1.4;
        }

        .sponsor-desc {
            font-size: 14.5px;
            color: var(--text-muted);
            margin-bottom: 28px;
            line-height: 1.6;
        }

        .sponsor-levels {
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin-bottom: 28px;
            flex-grow: 1;
        }

        .sponsor-level-box {
            background-color: rgba(255, 255, 255, 0.02);
            border-radius: 16px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            transition: var(--transition);
        }

        .sponsor-level-box:hover {
            background-color: rgba(255, 255, 255, 0.04);
        }

        .sponsor-card.business .sponsor-level-box:hover {
            border-color: rgba(227, 31, 38, 0.4);
            box-shadow: 0 0 20px rgba(227, 31, 38, 0.15);
        }

        .sponsor-card.study-abroad .sponsor-level-box:hover {
            border-color: rgba(0, 168, 89, 0.4);
            box-shadow: 0 0 20px rgba(0, 168, 89, 0.15);
        }

        .sponsor-level-title {
            font-size: 15px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .sponsor-level-title i {
            font-size: 16px;
        }

        .sponsor-card.business .sponsor-level-title i {
            color: var(--primary);
        }

        .sponsor-card.study-abroad .sponsor-level-title i {
            color: var(--accent-green);
        }

        .sponsor-level-desc {
            font-size: 13.5px;
            color: var(--text-muted);
            line-height: 1.5;
        }

        .sponsor-result-badge {
            margin-top: auto;
            background-color: rgba(227, 31, 38, 0.04);
            border: 2px dashed rgba(227, 31, 38, 0.2);
            border-radius: 16px;
            padding: 18px;
            font-size: 14px;
            color: #fff;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .sponsor-card.study-abroad .sponsor-result-badge {
            background-color: rgba(0, 168, 89, 0.04);
            border-color: rgba(0, 168, 89, 0.2);
        }

        .sponsor-result-badge i {
            font-size: 20px;
        }

        .sponsor-card.business .sponsor-result-badge i {
            color: var(--primary);
        }

        .sponsor-card.study-abroad .sponsor-result-badge i {
            color: var(--accent-green);
        }"""

# Định nghĩa CSS mới cho Light Theme
light_css_replacement = """        /* --- Section: Sponsorship --- */
        .sponsorship {
            padding: 95px 0;
            background-color: #f8fafc;
            border-top: 2px solid rgba(227, 31, 38, 0.05);
            border-bottom: 2px solid rgba(227, 31, 38, 0.05);
        }

        .sponsor-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
            margin-top: 45px;
        }

        @media (max-width: 991px) {
            .sponsor-grid {
                grid-template-columns: 1fr;
            }
        }

        .sponsor-card {
            background-color: var(--bg-light);
            border-radius: 24px;
            padding: 38px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
            border: 2px solid var(--border-color);
            transition: var(--transition);
        }

        .sponsor-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.06);
        }

        .sponsor-card.business {
            border-top: 8px solid var(--primary); /* Đỏ nổi bật */
            border-color: rgba(227, 31, 38, 0.1);
        }

        .sponsor-card.study-abroad {
            border-top: 8px solid var(--accent-green);
            border-color: rgba(0, 168, 89, 0.1);
        }

        .sponsor-badge-top {
            position: absolute;
            top: 20px;
            right: -35px;
            background: linear-gradient(135deg, var(--accent-yellow) 0%, #ffc000 100%);
            color: var(--accent-navy);
            font-size: 10px;
            font-weight: 900;
            padding: 6px 36px;
            transform: rotate(45deg);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .sponsor-card h3 {
            font-size: 21px;
            margin-bottom: 12px;
            color: var(--accent-navy);
            font-weight: 800;
            line-height: 1.4;
        }

        .sponsor-desc {
            font-size: 15px;
            color: var(--text-muted);
            margin-bottom: 26px;
            line-height: 1.6;
        }

        .sponsor-levels {
            display: flex;
            flex-direction: column;
            gap: 18px;
            margin-bottom: 26px;
            flex-grow: 1;
        }

        .sponsor-level-box {
            background-color: var(--bg-gray);
            border-radius: 16px;
            padding: 18px;
            border: 2px solid var(--border-color);
            transition: var(--transition);
        }

        .sponsor-level-box:hover {
            background-color: #ffffff;
        }

        .sponsor-card.business .sponsor-level-box:hover {
            border-color: var(--primary);
            box-shadow: 0 4px 12px rgba(227, 31, 38, 0.05);
        }

        .sponsor-card.study-abroad .sponsor-level-box:hover {
            border-color: var(--accent-green);
            box-shadow: 0 4px 12px rgba(0, 168, 89, 0.05);
        }

        .sponsor-level-title {
            font-size: 14.5px;
            font-weight: 800;
            color: var(--accent-navy);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .sponsor-level-title i {
            font-size: 16px;
        }

        .sponsor-card.business .sponsor-level-title i {
            color: var(--primary);
        }

        .sponsor-card.study-abroad .sponsor-level-title i {
            color: var(--accent-green);
        }

        .sponsor-level-desc {
            font-size: 13.5px;
            color: var(--text-muted);
            line-height: 1.5;
        }

        .sponsor-result-badge {
            margin-top: auto;
            background-color: rgba(227, 31, 38, 0.04);
            border: 2px dashed rgba(227, 31, 38, 0.3);
            border-radius: 16px;
            padding: 18px;
            font-size: 14.5px;
            color: var(--accent-navy);
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 12px;
            box-shadow: 0 4px 12px rgba(227, 31, 38, 0.02);
        }

        .sponsor-card.study-abroad .sponsor-result-badge {
            background-color: rgba(0, 168, 89, 0.04);
            border-color: rgba(0, 168, 89, 0.3);
        }

        .sponsor-result-badge i {
            font-size: 20px;
        }

        .sponsor-card.business .sponsor-result-badge i {
            color: var(--primary);
        }

        .sponsor-card.study-abroad .sponsor-result-badge i {
            color: var(--accent-green);
        }"""

# File paths
dark_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page.html"
light_path = "/Users/vanh1501/Downloads/mindx-agent_v1 (2)/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page-light.html"

# 1. Update Dark Theme
with open(dark_path, 'r', encoding='utf-8') as f:
    dark_content = f.read()

# Replace CSS
css_pattern_dark = r'\/\* --- Section: Special Sponsorship \(2 Chương trình bảo trợ\) ---\s*\*\/[\s\S]*?\/\* --- Section: Testimonials ---\s*\*\/'
dark_content = re.sub(css_pattern_dark, dark_css_replacement + "\n\n        /* --- Section: Testimonials --- */", dark_content)

# Replace HTML class
dark_content = dark_content.replace('<div class="sponsor-cards">', '<div class="sponsor-grid">')

with open(dark_path, 'w', encoding='utf-8') as f:
    f.write(dark_content)

print("Đã cập nhật xong file Dark Theme!")

# 2. Update Light Theme
with open(light_path, 'r', encoding='utf-8') as f:
    light_content = f.read()

# Replace CSS
css_pattern_light = r'\/\* --- Section: Sponsorship ---\s*\*\/[\s\S]*?\/\* --- Section: Testimonials ---\s*\*\/'
# Tìm dòng bắt đầu Testimonials trong light
light_content = re.sub(r'\/\* --- Section: Sponsorship ---\s*\*\/[\s\S]*?\/\* --- Section: Testimonials ---\s*\*\/', light_css_replacement + "\n\n        /* --- Section: Testimonials --- */", light_content)

# Replace HTML class
light_content = light_content.replace('<div class="sponsor-cards">', '<div class="sponsor-grid">')

with open(light_path, 'w', encoding='utf-8') as f:
    f.write(light_content)

print("Đã cập nhật xong file Light Theme!")
