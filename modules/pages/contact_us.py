from modules.resources.contact_us_resources import *


class ContactUsPage:
    def __init__(self, browser):
        self.browser = browser

    def get_text_result_send_form(self):
        return self.browser.find_element(*ContactUsLocators.RESULT).text

    def select_attach_file(self):
        self.browser.find_element(*ContactUsLocators.ATTACH_FILE_FIELD).click()

    def select_contact_us(self):
        self.browser.find_element(*ContactUsLocators.CONTACT_US_BTN).click()

    def select_subject(self):
        self.browser.find_element(*ContactUsLocators.SUBJECT_FIELD).click()
        # self.browser.find_elements(By.XPATH("//select/option[text()="+subject_type+"]")).click()

    def send_email(self, email):
        self.browser.find_element(*ContactUsLocators.EMAIL_FIELD).send_keys(email)

    def send_message(self, message):
        self.browser.find_element(*ContactUsLocators.MESSAGE_FIELD).send_keys(message)

    def send_order_reference(self, order):
        self.browser.find_element(*ContactUsLocators.ORDER_REFERENCE_FIELD).send_keys(order)

    def send_form(self, email, message, order):
        self.select_contact_us()
        self.select_subject()
        self.send_email(email)
        self.send_order_reference(order)
        self.send_message(message)
        self.browser.find_element(*ContactUsLocators.SEND_BTN).click()