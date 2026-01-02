from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    THANK_YOU_MESSAGE = ".complete-header"

    def is_thank_you_message_displayed(self):
        return self.page.is_visible(self.THANK_YOU_MESSAGE)