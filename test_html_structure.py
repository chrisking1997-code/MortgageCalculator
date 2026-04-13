# The user issue: "The SEO article block has become 'frozen/floating', occupying the entire layout and blocking the core calculator UI."
# User says we need to remove `fixed`, `absolute`, `sticky`, `inset-0`, `z-50`, `h-screen` from the SEO block's parent container.
# Looking at the earlier output:
# inflation/index.html main_end=194, seo_start=196
# dca-calculator/index.html main_end=221, seo_start=170
# Wait, dca-calculator/index.html seo_start=170, main_end=221. This means SEO block IS inside <main> for dca!
# But in inflation, main_end is BEFORE seo_start! So the SEO block in inflation is OUTSIDE <main>.
# And in portfolio-roi, it was compressed into a single line, but we can search for `</main>` and see it is far down.

import re

for filepath in ['inflation/index.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the <main> block
    print(content.find('</main>'))
    print(content.find('<!-- SEO & FAQ Section -->'))
