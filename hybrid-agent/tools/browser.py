from playwright.sync_api import sync_playwright

def open_and_search(keyword: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.bing.com", timeout=60000)
        page.fill("input[name=q]", keyword)
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)