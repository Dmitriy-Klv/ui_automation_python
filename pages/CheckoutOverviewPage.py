from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    TOTAL = ".summary_total_label"

    def get_item_total(self) -> float:
        text = self.get_text(self.ITEM_TOTAL)
        return float(text.replace("Item total: $", ""))

    def get_tax(self) -> float:
        text = self.get_text(self.TAX)
        return float(text.replace("Tax: $", ""))

    def get_total(self) -> float:
        text = self.get_text(self.TOTAL)
        return float(text.replace("Total: $", ""))
