from src.resources.login.login_demoga_resources import *


class LoginDemogaPage:

    def __init__(self, browser):
        self.browser = browser

    def send_login_information(self, username, password):
        self.browser.find_element(*LoginResources.USERNAME_FIELD).send_keys(username)
        self.browser.find_element(*LoginResources.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginResources.LOGIN_BTN).click()

    def invalidate_login(self, message):
        text = self.browser.find_element(*LoginResources.MESSAGE_TEXT).text
        assert text == message
