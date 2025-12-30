from pages.base_page import BasePage

class CartPage(BasePage):
    TITLE = ".title"

    def is_opened_cart_page(self) -> bool:
        self.should_have_text(self.TITLE, "Your Cart")
        return True

    def get_items_in_cart(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()
