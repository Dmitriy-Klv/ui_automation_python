from pages.base_page import BasePage

class CartPage(BasePage):
    TITLE = ".title"
    REMOVE_BACKPACK_BTN = "#remove-sauce-labs-backpack"

    def is_opened_cart_page(self) -> bool:
        self.should_have_text(self.TITLE, "Your Cart")
        return True

    def get_items_in_cart(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BTN)

    def get_cart_items_count(self) -> int:
        return self.page.locator(".cart_item").count()
