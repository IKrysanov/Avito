from typing import Any

from playwright.sync_api import BrowserContext, Playwright, Route, sync_playwright

counter2idx = {"co2": 2, "water": 4, "energy": 6}


def get_counter_json(counter_name: str, value: Any):
    response_json = {
        "result": {
            "blocks": {
                "personalImpact": {
                    "data": {
                        "co2": 0,
                        "energy": 0,
                        "materials": 0,
                        "pineYears": 0,
                        "water": 0,
                    }
                }
            },
            "isAuthorized": True,
        },
        "status": "ok",
    }
    response_json["result"]["blocks"]["personalImpact"]["data"][counter_name] = value
    return response_json


def test_counter(
    context: BrowserContext, test_num: int, counter_name: str, value
) -> None:
    page = context.new_page()

    def handle(route: Route):
        response_json = get_counter_json(counter_name, value)
        route.fulfill(json=response_json)

    page.route("**/*/1/charity/ecoImpact/init", handle)
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_idx = counter2idx[counter_name]
    page.locator(
        f".desktop-impact-items-F7T6E > div:nth-child({counter_idx})"
    ).screenshot(path=f"./output/{test_num}.png")
    page.close()


def run_tests(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    tests = [
        {
            "counter_name": "co2",
            "value": 0,
        },
        {
            "counter_name": "water",
            "value": 0,
        },
        {
            "counter_name": "energy",
            "value": 0,
        },
        {
            "counter_name": "co2",
            "value": 1,
        },
        {
            "counter_name": "water",
            "value": 1,
        },
        {
            "counter_name": "energy",
            "value": 1,
        },
        {
            "counter_name": "co2",
            "value": 1000,
        },
        {
            "counter_name": "water",
            "value": 1000,
        },
        {
            "counter_name": "energy",
            "value": 1000,
        },
                {
            "counter_name": "co2",
            "value": 1000000,
        },
        {
            "counter_name": "water",
            "value": 1000000,
        },
        {
            "counter_name": "energy",
            "value": 1000000,
        },
                {
            "counter_name": "co2",
            "value": "a",
        },
        {
            "counter_name": "water",
            "value": "a",
        },
        {
            "counter_name": "energy",
            "value": "a",
        },
    ]

    for i, test in enumerate(tests):
        # time.sleep(1)
        test_counter(context, i + 1, test["counter_name"], test["value"])


    context.close()
    browser.close()


with sync_playwright() as p:
    run_tests(p)