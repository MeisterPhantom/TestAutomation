from modules.resources.google_search_resources import *
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    def __init__(self, browser):
        self.browser = browser

    def send_search(self, search):
        self.browser.find_element(*GoogleLocators.SEARCH_BTN).send_keys(search + Keys.ENTER)

    def validate_result(self):
        result = self.browser.find_element(*GoogleLocators.RESULTS).text
        return result.split()
