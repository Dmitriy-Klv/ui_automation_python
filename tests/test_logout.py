from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings


def test_logout_burger_menu(playwright_page):
    login = LoginPage(playwright_page)
    login.open()
    login.perform_login(settings.test_username, settings.test_password)

    inventory = InventoryPage(playwright_page)
    inventory.logout()

    assert login.is_opened(), "Login page was not opened after logout"

    playwright_page.go_back()
    assert login.is_opened(), "User should not access inventory after logout"