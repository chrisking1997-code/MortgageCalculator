import os
import re

# The user explicitly said:
# 在 inflation.html (以及其他有加 SEO 文字的頁面) 中，SEO 文章區塊變成了「凍結/懸浮」狀態，佔據了整個版面並遮擋住了核心的計算機 UI。
# The reason is NOT the class on the SEO block itself (it has `mt-12 bg-white...`), but the fact that the SEO block is placed OUTSIDE the `<main>` container, inside the parent `div` that is `flex h-screen`! Wait, if it's placed after `<main class="flex-1 overflow-y-auto...">`, then it sits as a sibling to `<main>` in the `flex h-screen bg-slate-50 overflow-hidden` wrapper. Because `<main>` has `flex-1`, the SEO block takes up the rest of the space, OR it overflows strangely, OR it pushes the main content.

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The structure should be:
    # <main>
    #   <div class="max-w-5xl mx-auto">
    #     <!-- Calculator Layout -->
    #   </div>
    #   <!-- SEO & FAQ Section -->
    #   <!-- Quick Needs Submission -->
    #   <!-- Footer -->
    # </main>

    # Let's extract everything from SEO & FAQ Section to Footer and put it inside `<main>` if it's not.
    # Actually, in inflation, we know `</main>` is right BEFORE `<!-- SEO & FAQ Section -->`.
    if "<!-- SEO & FAQ Section -->" in content:
        # Let's check if `</main>` is before it
        main_end_idx = content.find("</main>")
        seo_idx = content.find("<!-- SEO & FAQ Section -->")

        # We want `</main>` to be at the very end of the visual content, right before `</div> <script>`
        # So we can just remove `</main>` from its current position and put it before `<script>` or right after the footer.

        # Let's see where the footer ends
        footer_end = content.find("</footer>")
        if footer_end != -1:
            footer_end += len("</footer>")

            # Let's remove all occurrences of `</main>`
            new_content = content.replace("</main>", "")

            # Insert `</main>` after `</footer>`
            # Wait, there might be another wrapper `</div>` after `</main>`.
            # Let's just do a targeted replacement.
            pass

fix_file("inflation/index.html")
