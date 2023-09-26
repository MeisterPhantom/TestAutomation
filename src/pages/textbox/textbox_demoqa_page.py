from src.resources.textbox.textbox_demoqa_resources import *
from helper_methods.helpermethods import *


class TextBoxPage:

    def __init__(self, browser):
        self.browser = browser

    def fill_form(self, full_name, email, current_address, permanent_address):
        self.browser.find_element(*TextBoxLocators.FULL_NAME_FIELD).send_keys(full_name)
        self.browser.find_element(*TextBoxLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*TextBoxLocators.CURRENT_ADDRESS_FIELD).send_keys(current_address)
        self.browser.find_element(*TextBoxLocators.PERMANENT_ADDRESS_FIELD).send_keys(permanent_address)

    def send_information_form(self):
        self.browser.find_element(*TextBoxLocators.SUBMIT_BTN).click()
