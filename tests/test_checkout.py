from pages.CheckoutOverviewPage import CheckoutOverviewPage
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from config.settings import settings


class TestCheckoutFlow:

    def test_checkout_complete_flow(self, playwright_page):
        login = LoginPage(playwright_page)
        inventory = InventoryPage(playwright_page)
        cart = CartPage(playwright_page)
        checkout = CheckoutPage(playwright_page)
        complete = CheckoutCompletePage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory.add_item_to_cart(InventoryPage.ADD_TO_CART_BTN_FIRST_ITEM)

        inventory.open_cart()
        cart.is_opened_cart_page()
        cart.click_checkout()

        checkout.fill_checkout_info("Alex", "Anderson", "12345")
        checkout.click_continue()

        checkout.click_finish()

        assert complete.is_thank_you_message_displayed()

    def test_checkout_without_first_name(self, playwright_page):
        login = LoginPage(playwright_page)
        inventory = InventoryPage(playwright_page)
        cart = CartPage(playwright_page)
        checkout = CheckoutPage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory.add_item_to_cart(InventoryPage.ADD_TO_CART_BTN_FIRST_ITEM)
        inventory.open_cart()
        cart.is_opened_cart_page()
        cart.click_checkout()

        checkout.fill_checkout_info("", "Anderson", "12345")
        checkout.click_continue()

        error_text = checkout.get_error_message()
        assert error_text == checkout.ERROR_FIRST_NAME_REQUIRED

    def test_check_total_sum(self, playwright_page):
        login = LoginPage(playwright_page)
        inventory = InventoryPage(playwright_page)
        cart = CartPage(playwright_page)
        checkout = CheckoutPage(playwright_page)

        login.open()
        login.perform_login(settings.test_username, settings.test_password)

        inventory.add_item_to_cart(InventoryPage.ADD_TO_CART_BTN_FIRST_ITEM)
        inventory.open_cart()
        cart.is_opened_cart_page()
        cart.click_checkout()

        checkout.fill_checkout_info("Alex", "Anderson", "12345")
        checkout.click_continue()

        overview = CheckoutOverviewPage(playwright_page)

        item_total = overview.get_item_total()
        tax = overview.get_tax()
        total = overview.get_total()

        assert round(item_total + tax, 2) == total