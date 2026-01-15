from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings


class TestLogin:

    def test_successful_login(self, playwright_page):
        login = LoginPage(playwright_page)
        inventory = InventoryPage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)
        assert inventory.is_opened_base_page

    def test_locked_out_user(self, playwright_page):
        login = LoginPage(playwright_page)
        login.open()
        login.perform_login("locked_out_user", settings.test_password)
        error_text = login.get_error_message()
        assert error_text == login.ERROR_MESSAGE

    def test_invalid_credentials(self, playwright_page):
        login = LoginPage(playwright_page)
        login.open()
        login.perform_login("invalidlogin", "invalidpassword")
        error_text = login.get_error_message()
        assert error_text == login.ERROR_INVALID_CREDENTIALS