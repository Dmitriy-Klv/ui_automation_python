from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BTN = "#continue"
    FINISH_BTN = "#finish"

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def click_finish(self):
        self.click(self.FINISH_BTN)
