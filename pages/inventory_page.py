from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = ".title"
    ADD_TO_CART_BTN_FIRST_ITEM = "//button[contains(@data-test,'backpack')]"
    ADD_TO_CART_BTN_SECOND_ITEM = "//button[contains(@data-test,'light')]]"
    CART_ICON = "//*[@class='shopping_cart_link']"

    def is_opened_base_page(self) -> bool:
        self.should_have_text(self.TITLE, "Products")
        return True

    # def add_item_to_cart(self):
    #     self.click(self.ADD_TO_CART_BTN_FIRST_ITEM)

    def add_item_to_cart(self, add_button_locator):
        self.click(add_button_locator)

    def open_cart(self):
        self.click(self.CART_ICON)