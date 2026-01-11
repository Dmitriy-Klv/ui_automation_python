import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def playwright_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        yield page

        page.close()
        context.close()
        browser.close()