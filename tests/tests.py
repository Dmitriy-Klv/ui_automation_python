from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings


def test_login(playwright_page):
    login = LoginPage(playwright_page)
    inventory = InventoryPage(playwright_page)

    login.open()
    login.perform_login(settings.test_username, settings.test_password)

    assert inventory.is_opened()

def test_locked_out_user(playwright_page):
    login = LoginPage(playwright_page)

    login.open()
    login.perform_login("locked_out_user", settings.test_password)

    error_text = login.get_error_message()
    assert error_text == login.ERROR_MESSAGE

