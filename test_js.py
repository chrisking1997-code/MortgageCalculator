with open('compound/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
js = scripts[1] if len(scripts)>1 else scripts[0]
print(js[js.find('nav-compound'):js.find('nav-compound')+200])
