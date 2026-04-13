# The user mentioned "在 inflation.html (以及其他有加 SEO 文字的頁面) 中...".
# Let's ensure ALL calculators have the same structure.
# Did we break any other pages by committing extra files? No, the commit just included the modified html files.
import os

html_files = [
    'mortgage/index.html',
    'compound/index.html',
    'exchange/index.html',
    'fire/index.html',
]

# We need to verify if any other pages have SEO block outside <main>
for filepath in html_files:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    main_start = content.find("<main")
    main_end = content.find("</main>")
    seo_start = content.find("<!-- SEO & FAQ Section -->")

    if seo_start != -1:
        if main_start < seo_start < main_end:
            print(f"{filepath} OK")
        else:
            print(f"{filepath} ERROR - Fixing")
            content = content.replace("</main>", "")
            content = content.replace("</footer>", "</footer>\n        </main>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    else:
        print(f"{filepath} NO SEO")
