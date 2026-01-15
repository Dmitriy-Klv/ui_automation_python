from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.settings import settings


class TestShoppingCart:

    def test_add_item_to_cart(self, playwright_page):
        login = LoginPage(playwright_page)
        inventory = InventoryPage(playwright_page)
        cart = CartPage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory.is_opened_base_page()
        inventory.add_item_to_cart(InventoryPage.ADD_TO_CART_BTN_FIRST_ITEM)
        inventory.open_cart()
        cart.is_opened_cart_page()

        assert "Sauce Labs Backpack" in cart.get_items_in_cart()

    def test_remove_item_from_cart(self, playwright_page):
        login = LoginPage(playwright_page)
        inventory = InventoryPage(playwright_page)
        cart = CartPage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory.is_opened_base_page()
        inventory.add_item_to_cart(InventoryPage.ADD_TO_CART_BTN_FIRST_ITEM)
        inventory.open_cart()
        cart.is_opened_cart_page()

        cart.remove_backpack()
        assert cart.get_cart_items_count() == 0

    def test_cart_total_price_for_single_item(self, playwright_page):
        login = LoginPage(playwright_page)
        inventory = InventoryPage(playwright_page)
        cart = CartPage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory.add_item_to_cart(InventoryPage.ADD_TO_CART_BTN_FIRST_ITEM)
        inventory.open_cart()
        cart.is_opened_cart_page()
        assert cart.get_cart_items_count() == 1

        item_price = cart.get_first_item_price_value()
        total_price = cart.get_total_price_value()
        assert total_price == item_price

    def test_clear_cart(self, playwright_page):
        login = LoginPage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory = InventoryPage(playwright_page)
        inventory.get_all_prices()
        inventory.open_cart()

        cart = CartPage(playwright_page)
        cart.remove_all()

        assert cart.is_cart_empty()