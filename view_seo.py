import os

files_to_fix = [
    'inflation/index.html',
    'dca-calculator/index.html',
    'portfolio-roi/index.html'
]

for filepath in files_to_fix:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"--- {filepath} ---")
            for i, line in enumerate(lines):
                if "SEO & FAQ Section" in line:
                    start_idx = max(0, i - 5)
                    end_idx = min(len(lines), i + 5)
                    print("".join(lines[start_idx:end_idx]))
