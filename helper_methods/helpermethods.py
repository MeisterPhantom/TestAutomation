from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HelperMethods:

    def __init__(self, browser):
        self.browser = browser

    def get_element(self, webElement, text):
        elements = self.browser.find_elements(By.XPATH, webElement)
        for e in elements:
            if e.text == text:
                HelperMethods(self.browser).action_click_element(e)

    def action_click_element(self, element):
        ActionChains(self.browser).move_to_element(element).click().perform()