from modules.resources.checkout_page_resources import *


class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    def checkout_action(self, name, lastname, zipcode):
        self.browser.find_element(*CheckoutLocators.BUTTON_CHECKOUT).click
        self.browser.find_element(*CheckoutLocators.INPUT_FIRST_NAME).send_keys(name)
        self.browser.find_element(*CheckoutLocators.INPUT_LAST_NAME).send_keys(lastname)
        self.browser.find_element(*CheckoutLocators.INPUT_ZIPCODE).send_keys(zipcode)
        self.browser.find_element(*CheckoutLocators.BUTTON_CONTINUE).click
        self.browser.find_element(*CheckoutLocators.BUTTON_FINISH).click
        return self.browser.find_element(*CheckoutLocators.LABEL_FINISH_ORDER)

