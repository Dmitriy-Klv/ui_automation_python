from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = ".title"

    def is_opened(self) -> bool:
        self.should_have_text(self.TITLE, "Products")
        return True

