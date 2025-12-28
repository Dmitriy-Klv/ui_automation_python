from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click(self, selector: str):
        element = self.locator(selector)
        expect(element).to_be_visible()
        element.click()

    def fill(self, selector: str, value: str):
        element = self.locator(selector)
        expect(element).to_be_visible()
        element.fill(value)

    def should_have_text(self, selector: str, text: str):
        expect(self.locator(selector)).to_have_text(text)
