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

def test_logout_via_burger_menu(playwright_page):
    login = LoginPage(playwright_page)
    login.open()
    login.perform_login(settings.test_username, settings.test_password)

    inventory = InventoryPage(playwright_page)
    inventory.is_opened_base_page()
    assert inventory.is_burger_menu_visible()

    inventory.logout()

    login_page = LoginPage(playwright_page)
    login_page.is_opened()
    assert login_page.get_username_field_value() == ""
    assert login_page.get_password_field_value() == ""

    login_page.perform_login(settings.test_username, settings.test_password)
    inventory.is_opened_base_page()
