from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = ".title"
    ADD_TO_CART_BTN = "//button[contains(@data-test,'backpack')]"
    CART_ICON = "//*[@class='shopping_cart_link']"

    def is_opened_base_page(self) -> bool:
        self.should_have_text(self.TITLE, "Products")
        return True

    def add_item_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def open_cart(self):
        self.click(self.CART_ICON)