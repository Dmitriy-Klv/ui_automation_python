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

    def test_continue_shopping_keeps_cart_state(self, playwright_page):
        login = LoginPage(playwright_page)
        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory = InventoryPage(playwright_page)
        inventory.is_opened_base_page()

        inventory.add_item_to_cart(inventory.ADD_TO_CART_BTN_FIRST_ITEM)
        assert inventory.get_cart_badge_value() == 1

        inventory.open_cart()

        cart = CartPage(playwright_page)
        cart.is_opened_cart_page()
        assert cart.get_cart_items_count() == 1

        cart.click_continue_shopping()

        inventory.is_opened_base_page()
        assert inventory.get_cart_badge_value() == 1

    def test_cart_badge_persistence_after_refresh(self, playwright_page):
        login = LoginPage(playwright_page)
        cart = CartPage(playwright_page)
        inventory = InventoryPage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory.is_opened_base_page()

        product1 = inventory.add_product_to_cart_by_index(0)
        product2 = inventory.add_product_to_cart_by_index(1)

        assert inventory.get_cart_badge_count() == 2

        playwright_page.reload()

        assert inventory.get_cart_badge_count() == 2

        inventory.open_cart()

        cart_items = cart.get_cart_items()
        names = [item["name"] for item in cart_items]
        prices = [item["price"] for item in cart_items]

        assert product1["name"] in names
        assert product2["name"] in names

        assert product1["price"] in prices
        assert product2["price"] in prices