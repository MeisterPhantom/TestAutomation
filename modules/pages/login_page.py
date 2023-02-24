from modules.resources.login_page_resources import *


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login_action(self, user, password):
        self.browser.find_element(*LoginLocators.USER_FIELD).send_keys(user)
        self.browser.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginLocators.BUTTON_LOGIN).click
