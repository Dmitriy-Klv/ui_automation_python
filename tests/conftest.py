import datetime
import allure
import pytest
from allure_commons.types import AttachmentType
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("playwright_page")
        if page:
            try:
                screenshot_bytes = page.screenshot(full_page=True, timeout=5000)

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                test_name = item.name.replace("[", "_").replace("]", "").replace("::", "_")

                allure.attach(
                    screenshot_bytes,
                    name=f"Failure Screenshot - {test_name} ({timestamp})",
                    attachment_type=AttachmentType.PNG
                )
                print(f"→ Attached failure screenshot to Allure: {test_name}")

            except Exception as e:
                print(f"Failed to capture screenshot: {e}")
        else:
            print("Warning: 'playwright_page' fixture not found in test → screenshot skipped")
