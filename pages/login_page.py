from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, user: str, password: str):
        self.page.fill(self.USERNAME, user)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MSG).inner_text()
