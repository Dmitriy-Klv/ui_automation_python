from pages.base_page import BasePage

class CartPage(BasePage):
    TITLE = ".titTTle"
    REMOVE_BACKPACK_BTN = "#remove-sauce-labs-backpack"
    CHECKOUT_BTN = "#checkout"

    def is_opened_cart_page(self) -> bool:
        self.should_have_text(self.TITLE, "Your Cart")
        return True

    def get_items_in_cart(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BTN)

    def get_cart_items_count(self) -> int:
        return self.page.locator(".cart_item").count()

    def get_first_item_price_value(self) -> float:
        price_text = self.page.locator(".inventory_item_price").first.inner_text()
        return float(price_text.replace("$", ""))

    def get_total_price_value(self) -> float:
        prices = self.page.locator(".inventory_item_price")
        return sum(
            float(prices.nth(i).inner_text().replace("$", ""))
            for i in range(prices.count())
        )

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def remove_all(self):
        for btn in self.page.query_selector_all("button[id^='remove']"):
            btn.click()

    def get_items_count(self):
        return len(self.page.query_selector_all(".cart_item"))

    def is_cart_empty(self):
        return self.get_items_count() == 0

