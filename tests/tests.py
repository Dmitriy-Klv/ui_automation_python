import time

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings


def test_login(playwright_page):
    login = LoginPage(playwright_page)
    inventory = InventoryPage(playwright_page)

    login.open()
    login.perform_login(settings.test_username, settings.test_password)

    assert inventory.is_opened_base_page

def test_locked_out_user(playwright_page):
    login = LoginPage(playwright_page)

    login.open()
    login.perform_login("locked_out_user", settings.test_password)

    error_text = login.get_error_message()
    assert error_text == login.ERROR_MESSAGE

def test_login_invalid(playwright_page):
    login = LoginPage(playwright_page)

    login.open()
    login.perform_login("invalidlogin", "invalidpassword")

    error_text = login.get_error_message()
    assert error_text == login.ERROR_INVALID_CREDENTIALS

def test_add_item_to_cart(playwright_page):
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

def test_remove_item_from_cart(playwright_page):
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
    assert  cart.get_cart_items_count() == 0

def test_cart_total_price_for_single_item(playwright_page):
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

def test_checkout_complete_flow(playwright_page):
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

def test_checkout_without_first_name(playwright_page):
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
