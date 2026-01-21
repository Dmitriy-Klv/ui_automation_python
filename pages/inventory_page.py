from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = ".title"
    ADD_TO_CART_BTN_FIRST_ITEM = "//button[contains(@data-test,'backpack')]"
    ADD_TO_CART_BTN_SECOND_ITEM = "//button[contains(@data-test,'light')]"
    CART_ICON = "//*[@class='shopping_cart_link']"
    BURGER_MENU_BTN = "//button[@id='react-burger-menu-btn']"
    LOGOUT_LINK = "//a[@id='logout_sidebar_link']"
    CART_BADGE = ".shopping_cart_badge"
    ITEM_NAME_BACKPACK = "//div[contains(@class,'inventory_item_name') and contains(text(),'Backpack')]"

    def is_opened_base_page(self) -> bool:
        self.should_have_text(self.TITLE, "Products")
        return True

    def add_item_to_cart(self, add_button_locator):
        self.click(add_button_locator)

    def open_cart(self):
        self.click(self.CART_ICON)

    def get_all_prices(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def sort_by(self, label_text):
        self.page.locator("select.product_sort_container").select_option(label=label_text)

    def logout(self):
        self.page.click(self.BURGER_MENU_BTN)
        self.page.click(self.LOGOUT_LINK)

    def get_cart_badge_value(self) -> int:
        if self.page.locator(self.CART_BADGE).is_visible():
            return int(self.page.locator(self.CART_BADGE).text_content())
        return 0

    def open_backpack_details(self):
        self.click(self.ITEM_NAME_BACKPACK)