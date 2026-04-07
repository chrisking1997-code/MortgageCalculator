import os
import glob

def add_language_label():
    html_files = glob.glob('**/*.html', recursive=True)

    search_string = '<select id="language-selector" class="bg-white text-primary text-sm rounded px-2 py-1 border-none focus:ring focus:ring-secondary">'
    replace_string = '''<div class="flex items-center space-x-2">
                    <span class="text-white text-sm font-medium">Language:</span>
                    <select id="language-selector" class="bg-white text-primary text-sm rounded px-2 py-1 border-none focus:ring focus:ring-secondary">'''

    # We also need to close the div tag that we opened
    search_string_close = '''<option value="en">English</option>
                </select>'''
    replace_string_close = '''<option value="en">English</option>
                </select>
                </div>'''

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'id="language-selector"' in content and '<span class="text-white text-sm font-medium">Language:</span>' not in content:
            new_content = content.replace(search_string, replace_string)
            new_content = new_content.replace(search_string_close, replace_string_close)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")

if __name__ == "__main__":
    add_language_label()
