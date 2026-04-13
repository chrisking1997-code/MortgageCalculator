import re
import os

files_to_fix = [
    'inflation/index.html',
    'dca-calculator/index.html',
    'portfolio-roi/index.html'
]

# The goal is simple:
# 1. The SEO block `<!-- SEO & FAQ Section -->` should be inside the scrollable `<main>` content area.
# 2. It should have the correct container classes (e.g., `w-full mt-12 p-8 bg-white/50 rounded-2xl` or similar, as specified by the user: `w-full mt-12 p-8 bg-white/50 rounded-2xl` but the user says "例如：w-full mt-12 p-8 bg-white/50 rounded-2xl").
# Let's check what it currently has:
# `<div class="mt-12 bg-white p-8 sm:p-10 rounded-2xl shadow-lg shadow-slate-200/50 border border-slate-100 mb-12 max-w-5xl mx-auto">`
# This looks standard, so the issue is likely that it's just outside the `<main>` container, or wrapped in a fixed overlay.

for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Are there any 'fixed' or 'absolute' classes on the SEO block?
    # User said: 立即尋找 SEO 文字區塊的父層容器 (<div>)，刪除所有 fixed, absolute, sticky, inset-0, z-50, h-screen 這類的 Tailwind class

    # Let's look for any fixed containers around SEO section
    seo_block = re.search(r'(<div[^>]*>)\s*<!-- SEO & FAQ Section -->', content)
    if seo_block:
        print(f"[{filepath}] wrapper: {seo_block.group(1)}")
    else:
        seo_start_tag = re.search(r'<!-- SEO & FAQ Section -->\s*(<div[^>]*>)', content)
        if seo_start_tag:
             print(f"[{filepath}] main tag: {seo_start_tag.group(1)}")
