from modules.resources.contact_us_resources import *
from selenium.webdriver.common.keys import Keys


class ContactUsPage:
    def __init__(self, browser):
        self.browser = browser

    def click_search(self):
        self.browser.find_element(*ContactUsLocators.SEARCH_BTN).click()

    def send_search(self, search):
        self.browser.find_element(*ContactUsLocators.SEARCH_INPUT).send_keys(search + Keys.ENTER)

    def validate_result(self):
        texts = self.browser.find_elements(*ContactUsLocators.RESULT)
        for t in texts:
            message = []
            message.append(t.text)
        return message

    def send_search_and_validate(self, search):
        self.click_search()
        self.send_search(search)
