from modules.resources.menu_page_resources import *


class MenuPage:
    def __init__(self, browser):
        self.browser = browser

    def cart_shopping_action(self):
        self.browser.find_element(*MenuLocators.BUTTON_CART_SHOPPING).click

    def menu_action(self):
        self.browser.find_element(*MenuLocators.BUTTON_MENU).click

    def logout_action(self,):
        self.menu_action()
        self.browser.find_element(*MenuLocators.BUTTON_LOGOUT).click





