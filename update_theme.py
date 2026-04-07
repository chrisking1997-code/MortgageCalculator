import os

def modify_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Add Google Fonts
                    if '<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:' not in content:
                        content = content.replace('<!-- Tailwind CSS CDN -->',
'''<!-- Google Fonts: Playfair Display & Noto Serif TC for Serif, Inter/Noto Sans TC for Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">

    <!-- Tailwind CSS CDN -->''')

                    # Replace tailwind config
                    if 'theme: {' in content:
                        start_idx = content.find('tailwind.config = {')
                        end_idx = content.find('</script>', start_idx)

                        if start_idx != -1 and end_idx != -1:
                            new_config = '''tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        zinc: {
                            900: '#18181b',
                            950: '#09090b',
                        },
                        amber: {
                            500: '#f59e0b',
                            600: '#d97706',
                            700: '#b45309',
                        }
                    },
                    fontFamily: {
                        serif: ['"Playfair Display"', '"Noto Serif TC"', 'serif'],
                        sans: ['"Inter"', '"Noto Sans TC"', 'sans-serif'],
                    }
                }
            }
        }
    '''
                            content = content[:start_idx] + new_config + content[end_idx:]

                    # Global Body Styles
                    content = content.replace('bg-surface text-gray-800', 'bg-zinc-950 text-zinc-300')
                    content = content.replace('bg-gray-50 text-gray-900', 'bg-zinc-950 text-zinc-300')

                    # Sidebar
                    content = content.replace('bg-white w-64 flex-shrink-0 border-r border-gray-200', 'bg-zinc-950 w-64 flex-shrink-0 border-r border-zinc-800')
                    content = content.replace('border-b border-gray-200', 'border-b border-zinc-800')
                    content = content.replace('text-2xl font-bold text-primary', 'text-2xl font-serif font-bold text-zinc-100')
                    content = content.replace('text-gray-500 hover:text-gray-800', 'text-zinc-500 hover:text-zinc-300')

                    # Sidebar Tools Links
                    content = content.replace('text-xs font-semibold text-slate-500', 'text-xs font-semibold text-zinc-500')
                    content = content.replace('text-gray-600 hover:bg-gray-50 hover:text-primary', 'text-zinc-400 hover:bg-zinc-900 hover:text-zinc-200')
                    content = content.replace('bg-green-50 text-secondary', 'border-l-4 border-amber-600 bg-zinc-800/50 text-amber-500')
                    content = content.replace('bg-gray-50 text-primary', 'border-l-4 border-amber-600 bg-zinc-800/50 text-amber-500')

                    # Header
                    content = content.replace('bg-primary text-white', 'bg-zinc-900 text-zinc-200 border-b border-zinc-800')
                    content = content.replace('text-xl font-bold', 'text-xl font-serif font-bold text-zinc-100')
                    content = content.replace('hover:text-secondary', 'hover:text-amber-500 transition-colors')
                    content = content.replace('bg-white text-primary text-sm rounded px-2 py-1 border-none focus:ring focus:ring-secondary', 'bg-zinc-800 text-zinc-200 text-sm rounded px-2 py-1 border border-zinc-700 focus:ring focus:ring-amber-500 focus:outline-none')

                    # Main content area bg
                    content = content.replace('bg-surface', 'bg-zinc-950')
                    content = content.replace('bg-gray-50', 'bg-zinc-950')

                    # Typography headers
                    content = content.replace('text-primary', 'text-amber-500')
                    content = content.replace('text-2xl font-bold text-gray-800', 'text-2xl font-serif font-bold text-zinc-100')
                    content = content.replace('text-gray-500', 'text-zinc-400')

                    # Forms & Inputs
                    content = content.replace('bg-white p-6 rounded-lg shadow-md border-t-4 border-secondary', 'bg-zinc-900 p-6 rounded-2xl shadow-lg border border-zinc-800 relative overflow-hidden')
                    content = content.replace('bg-white p-6 rounded-lg shadow-md', 'bg-zinc-900 p-6 rounded-2xl shadow-lg border border-zinc-800')
                    content = content.replace('text-gray-800', 'text-zinc-200')
                    content = content.replace('text-gray-700', 'text-zinc-300')
                    content = content.replace('border-gray-300', 'border-zinc-700')
                    content = content.replace('focus:border-secondary focus:ring focus:ring-secondary', 'focus:border-amber-600 focus:ring focus:ring-amber-600')
                    content = content.replace('bg-white', 'bg-zinc-900')
                    content = content.replace('shadow-sm', '')

                    # Tables
                    content = content.replace('border-gray-200', 'border-zinc-800')
                    content = content.replace('text-gray-600', 'text-zinc-400')
                    content = content.replace('divide-gray-200', 'divide-zinc-800')

                    # CTA blocks
                    content = content.replace('bg-primary text-white py-10 border-b border-blue-800', 'bg-zinc-900 py-10 border-t border-b border-zinc-800 text-zinc-200')
                    content = content.replace('text-gray-800 focus:outline-none focus:ring-2 focus:ring-secondary', 'bg-zinc-950 text-zinc-200 focus:outline-none focus:ring-2 focus:ring-amber-600 border border-zinc-700')
                    content = content.replace('bg-secondary hover:bg-green-600', 'bg-amber-700 hover:bg-amber-600 border border-amber-600')

                    # Footers
                    content = content.replace('bg-gray-800', 'bg-zinc-950')
                    content = content.replace('text-gray-400', 'text-zinc-600')

                    # Custom JS replacements for calculators
                    if file == 'index.html' and 'tw-loan-amount' in content:
                        content = content.replace('bg-blue-50 border-blue-100 text-blue-900', 'bg-zinc-950 border-zinc-800 text-zinc-300')
                        content = content.replace('bg-indigo-50 border-indigo-100 text-indigo-900', 'bg-zinc-900 border-zinc-700 text-zinc-200')
                        content = content.replace('bg-green-50 border-green-100 text-green-900', 'bg-zinc-900 border-amber-700 border text-amber-500 shadow-inner')
                        content = content.replace('bg-gray-50 border-gray-200 text-gray-800', 'bg-zinc-950 border-zinc-800 text-zinc-400')
                        content = content.replace('bg-yellow-50 border-yellow-100 text-yellow-900', 'bg-zinc-950 border-amber-900 text-amber-400')

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)

                except Exception as e:
                    print(f"Failed to process {filepath}: {e}")

if __name__ == '__main__':
    modify_html_files('.')
