import re

files_to_fix = [
    'inflation/index.html',
    'dca-calculator/index.html',
    'portfolio-roi/index.html'
]

for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the block:
    # </main>
    # <div class="..."> (Wait, is there a <div class="fixed ... inset-0 z-50"> ? User said: 刪除所有 fixed, absolute, sticky, inset-0, z-50, h-screen 這類的 Tailwind class
    # Let's check for any fixed wrappers around the SEO section!

    match = re.search(r'<div[^>]*fixed[^>]*>[\s\S]*?<!-- SEO & FAQ Section -->', content)
    if match:
        print(f"FOUND fixed wrapper in {filepath}!")
        print(match.group(0)[:200])

    match2 = re.search(r'<div[^>]*absolute[^>]*>[\s\S]*?<!-- SEO & FAQ Section -->', content)
    if match2:
        print(f"FOUND absolute wrapper in {filepath}!")

    # Just look at the exact HTML around SEO in inflation
    seo_idx = content.find("<!-- SEO & FAQ Section -->")
    if seo_idx != -1:
        start = max(0, seo_idx - 300)
        end = min(len(content), seo_idx + 100)
        print(f"--- {filepath} Context ---")
        print(content[start:end])
