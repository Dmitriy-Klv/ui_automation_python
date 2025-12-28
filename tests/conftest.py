import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def playwright_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless= False)
    context = browser.new_context()
    # context = browser.new_context(base_url= 'https://www.saucedemo.com/')
    page = context.new_page()

    yield page

    page.close()
    context.close()
    browser.close()