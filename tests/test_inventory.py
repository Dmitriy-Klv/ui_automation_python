from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings


class TestInventory:

    def test_sort_products_by_price_low_to_high(self, playwright_page):
        login = LoginPage(playwright_page)
        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory = InventoryPage(playwright_page)
        inventory.sort_by("Price (low to high)")

        prices = inventory.get_all_prices()
        assert prices == sorted(prices)


    def test_cart_counter_increment_after_one_item(self, playwright_page):
        login = LoginPage(playwright_page)
        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory = InventoryPage(playwright_page)

        inventory.add_item_to_cart(inventory.ADD_TO_CART_BTN_FIRST_ITEM)

        cart_count = playwright_page.locator(".shopping_cart_badge").text_content()
        assert cart_count == "1"


    def test_cart_icon_counter_for_two_items(self, playwright_page):
        login = LoginPage(playwright_page)
        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory = InventoryPage(playwright_page)
        inventory.is_opened_base_page()

        inventory.add_item_to_cart(inventory.ADD_TO_CART_BTN_FIRST_ITEM)
        inventory.add_item_to_cart(inventory.ADD_TO_CART_BTN_SECOND_ITEM)

        assert inventory.get_cart_badge_value() == 2