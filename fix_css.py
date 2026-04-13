import os

files_to_fix = [
    'inflation/index.html',
    'dca-calculator/index.html',
    'portfolio-roi/index.html'
]

# We want the SEO block to just be normal div inside the <main> block, but AFTER the <section> or container that holds the calculators.
# Wait, let's look at the structure of <main> from our previous grep of inflation:

#         <!-- Scrollable Main Content -->
#         <main class="flex-1 overflow-y-auto bg-slate-50 p-4 lg:p-8">
#             <div class="max-w-5xl mx-auto">
#                   <div class="mb-8 text-center">...
#                   <!-- Calculator Layout -->
#                   <div class="grid...

# ... then at the end of <main> there is </main>
# And then right after </main>, the SEO block starts:
#         </main>
#         <!-- SEO & FAQ Section -->
#         <div class="mt-12 bg-white ...

# If it's outside <main>, and <main> is `flex-1 overflow-y-auto`, then anything after <main> will NOT scroll with the main content. It will be pushed down or laid out according to the parent container (which might be `flex h-screen`). This explains why it is "frozen" or "floating" over everything or disrupting layout.
# It should be INSIDE <main>, inside the `max-w-5xl mx-auto` or just inside `main` before the `<footer>`.

for filepath in files_to_fix:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Let's fix this by moving the SEO section inside <main>
        # Specifically, right before the Quick Needs Submission / Footer blocks, or just inside </main>.

        # Let's check where the Quick needs block is.
