from pages.base_page import BasePage

class InventoryItemPage(BasePage):
    TITLE = ".inventory_details_name"
    ITEM_IMAGE = ".inventory_details_img"
    ITEM_DESC = ".inventory_details_desc"
    ITEM_PRICE = ".inventory_details_price"
    ACTION_BTN = "button.btn_inventory"
    BACK_TO_PRODUCTS_BTN = "#back-to-products"

    def is_opened(self) -> bool:
        assert self.page.locator(self.TITLE).text_content() != ""
        return True

    def get_item_name(self) -> str:
        return self.page.locator(self.TITLE).inner_text()

    def get_item_description(self) -> str:
        return self.page.locator(self.ITEM_DESC).inner_text()

    def get_item_price(self) -> float:
        price_text = self.page.locator(self.ITEM_PRICE).inner_text()
        return float(price_text.replace("$", ""))

    def click_add_or_remove(self):
        self.click(self.ACTION_BTN)

    def is_action_btn_visible(self) -> bool:
        return self.page.locator(self.ACTION_BTN).is_visible()

    def click_back_to_products(self):
        self.click(self.BACK_TO_PRODUCTS_BTN)

    def is_back_to_products_visible(self) -> bool:
        return self.page.locator(self.BACK_TO_PRODUCTS_BTN).is_visible()

    def is_item_image_visible(self) -> bool:
        return self.page.locator(self.ITEM_IMAGE).is_visible()
