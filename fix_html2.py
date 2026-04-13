import re
import os

files_to_fix = [
    'inflation/index.html',
    'dca-calculator/index.html',
    'portfolio-roi/index.html'
]

for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. We want to find the SEO & FAQ Section and make sure it is inside <main>...
    # The user says the SEO block is overflowing and covering the UI.
    # User instructions:
    # 1. Remove Fixed/Absolute: find the parent container of SEO text block and remove `fixed`, `absolute`, `sticky`, `inset-0`, `z-50`, `h-screen`.
    # 2. Standard Block Flow: set it to `w-full mt-12 p-8 bg-white/50 rounded-2xl` (or similar standard block) and place it directly below the calculator card block.
    # 3. Scroll to read: user must scroll down to see it.

    # Let's inspect the SEO section HTML explicitly.
    seo_match = re.search(r'<!-- SEO & FAQ Section -->(.*?)<!-- Quick Needs Submission -->', content, flags=re.DOTALL)
    if not seo_match:
        seo_match = re.search(r'<!-- SEO & FAQ Section -->(.*?)(?=<(?:footer|/body|/html|script))', content, flags=re.DOTALL)
    if seo_match:
        print(f"--- {filepath} SEO BLOCK ---")
        print(seo_match.group(0)[:500])
        print("...")
        print(seo_match.group(0)[-500:])
