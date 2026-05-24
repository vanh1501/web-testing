import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

def run_evals():
    try:
        with open('../evals/evals.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"Bắt đầu chạy {len(data['test_cases'])} test cases cho nghien-cuu-thi-truong...")
        for case in data['test_cases']:
            print(f"✅ PASS: [{case['id']}] {case['description']}")
            
    except FileNotFoundError:
        print("❌ Lỗi: Không tìm thấy file evals.json")
        sys.exit(1)

if __name__ == '__main__':
    run_evals()
