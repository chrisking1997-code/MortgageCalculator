from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    errors = []
    page.on("pageerror", lambda err: errors.append(err.message))
    page.goto("http://localhost:3000/compound/index.html")
    page.wait_for_load_state("networkidle")

    print("Page Errors:", errors)
    browser.close()
