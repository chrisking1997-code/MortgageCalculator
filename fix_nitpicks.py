import os

def fix_nitpicks(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Fix missed gray borders
                    content = content.replace('border-gray-100', 'border-zinc-800')
                    content = content.replace('border-gray-200', 'border-zinc-800')

                    # Fix sidebar group headers
                    content = content.replace('text-xs font-semibold text-zinc-500 uppercase', 'text-xs font-semibold text-amber-700/70 uppercase')

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)

                except Exception as e:
                    print(f"Failed to process {filepath}: {e}")

if __name__ == '__main__':
    fix_nitpicks('.')
