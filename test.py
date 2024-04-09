from playwright.sync_api import Playwright, sync_playwright


def test2_counter_water(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)").screenshot(path='output/1.png')
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(2)").screenshot(path='output/2.png')
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(6)").screenshot(path='output/3.png')
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test2_counter_water(playwright)