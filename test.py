with open('compound/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
with open('tmp.js', 'w', encoding='utf-8') as f:
    f.write(scripts[0] if scripts else '')
