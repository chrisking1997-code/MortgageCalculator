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

        seo_start = -1
        seo_end = -1
        main_end = -1

        for i, line in enumerate(lines):
            if "<!-- SEO & FAQ Section -->" in line:
                seo_start = i
            if seo_start != -1 and "<!-- Quick Needs Submission -->" in line:
                seo_end = i
            if "</main>" in line and "footer" not in line: # For the formatted ones
                main_end = i

        print(f"{filepath}: main_end={main_end}, seo_start={seo_start}, seo_end={seo_end}")
