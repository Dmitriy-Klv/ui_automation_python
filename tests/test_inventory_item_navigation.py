from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.inventory_item_page import InventoryItemPage
from config.settings import settings

class TestInventoryItem:

    def test_open_backpack_details_from_inventory(self, playwright_page):
        login = LoginPage(playwright_page)
        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory = InventoryPage(playwright_page)
        inventory.is_opened_base_page()

        inventory.open_backpack_details()

        item_page = InventoryItemPage(playwright_page)
        item_page.is_opened()

        assert item_page.is_item_image_visible()
        assert item_page.is_back_to_products_visible()
        assert item_page.is_action_btn_visible()
