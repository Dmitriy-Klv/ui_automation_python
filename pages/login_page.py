from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_LOCATOR = "[data-test='error']"
    ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
    ERROR_INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def perform_login(self, user: str, password: str):
        self.page.fill(self.USERNAME, user)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_LOCATOR).inner_text()

    def is_opened(self):
        return self.page.is_visible(self.LOGIN_BTN)

    def get_username_field_value(self) -> str:
        return self.page.locator("#user-name").input_value()

    def get_password_field_value(self) -> str:
        return self.page.locator("#password").input_value()


