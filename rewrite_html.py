import re

files_to_fix = [
    'inflation/index.html',
    'dca-calculator/index.html',
    'portfolio-roi/index.html'
]

for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The user says:
    # "SEO 文章區塊變成了「凍結/懸浮」狀態，佔據了整個版面並遮擋住了核心的計算機 UI。"
    # "解除錯誤的定位 (Remove Fixed/Absolute): > 立即尋找 SEO 文字區塊的父層容器 (<div>)，刪除所有 fixed, absolute, sticky, inset-0, z-50, h-screen 這類的 Tailwind class。"

    # Wait, earlier I ran a script that formatted the SEO text and might have accidentally wrapped it in something, or just having it outside `<main>` causes it to cover the screen?
    # Ah, let's look at `inflation/index.html` structure:
    # <body>
    #   <div class="flex h-screen bg-slate-50 overflow-hidden">
    #     <aside id="sidebar" class="... h-screen overflow-y-auto hide-scrollbar">
    #     <div class="flex-1 flex flex-col h-screen overflow-hidden">
    #       <header>
    #       <main class="flex-1 overflow-y-auto...">
    #         <div class="max-w-5xl mx-auto">
    #           ... calculators ...
    #         </div>
    #       </main>
    #       <!-- SEO & FAQ Section -->
    #       <!-- Quick Needs -->
    #       <!-- Footer -->
    #     </div>
    #   </div>

    # If the SEO section, Quick Needs, and Footer are placed directly inside `div.flex-1.flex-col` AFTER `<main class="flex-1 overflow-y-auto">`, they will be part of the flex column but `<main>` is `flex-1` so it takes all available space. The SEO section might be pushed out of bounds, OR if it has a lot of content, it might squish `<main>` or overflow on top.
    # We must move the SEO section, Quick Needs, and Footer INSIDE `<main>`.

    # Let's remove `</main>` from its current position and place it AFTER the Footer!

    # 1. Remove all `</main>` tags
    content = content.replace("</main>", "")

    # 2. Find `</footer>` and insert `</main>` right after it.
    # But we also need to make sure the SEO section doesn't have absolute/fixed classes. It starts with `<div class="mt-12 bg-white...` which is standard.
    # Wait, look at the Quick Needs Section:
    # `<section class="bg-white border-t border-slate-200 mt-auto">`
    # `<footer class="bg-white border-t border-slate-200 mt-auto">`
    # The `mt-auto` pushes them to the bottom.

    content = content.replace("</footer>", "</footer>\n        </main>")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
