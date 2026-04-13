import re

files_to_fix = [
    'inflation/index.html',
    'dca-calculator/index.html',
    'portfolio-roi/index.html'
]

for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    main_start = content.find("<main")
    main_end = content.find("</main>")
    seo_start = content.find("<!-- SEO & FAQ Section -->")

    print(f"{filepath}: <main> at {main_start}, </main> at {main_end}, SEO at {seo_start}")
    if main_start < seo_start < main_end:
        print("  -> OK: SEO is inside <main>")
    else:
        print("  -> ERROR: SEO is outside <main>!")
