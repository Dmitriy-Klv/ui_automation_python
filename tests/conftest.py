import datetime
import allure
import pytest
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def playwright_page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            try:
                screenshot_bytes = page.screenshot(full_page=True, timeout=5000)
                request.node._failure_screenshot_bytes = screenshot_bytes
            except Exception as e:
                print(f"Failed to capture screenshot in fixture: {e}")
        page.close()
        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        if hasattr(item, "_failure_screenshot_bytes"):
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace("[", "_").replace("]", "").replace("::", "_")

            allure.attach(
                item._failure_screenshot_bytes,
                name=f"Failure Screenshot - {test_name} ({timestamp})",
                attachment_type=AttachmentType.PNG
            )
            print(f"→ Attached failure screenshot to Allure: {test_name}")
            del item._failure_screenshot_bytes
        else:
            print("Warning: Screenshot not captured (probably page closed too early)")