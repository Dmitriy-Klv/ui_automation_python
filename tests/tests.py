from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings



def test_login2(playwright_page):
    login = LoginPage(playwright_page)
    inventory = InventoryPage(playwright_page)

    login.open()
    login.login(settings.test_username, settings.test_password)

    assert inventory.is_opened()