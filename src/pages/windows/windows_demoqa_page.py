from src.resources.windows.windows_resources import *


class WindowsDemoqaPage:

    def __init__(self, browser):
        self.browser = browser

    def select_new_tab(self):
        self.browser.find_element(*WindowsResources.NEW_TAB_BTN).click()

    def new_tab_validation(self, message):
        window_handle = self.browser.window_handles
        self.browser.switch_to.window(window_handle[1])
        text = self.browser.find_element(*WindowsResources.NEW_TAB_TEXT_LABEL).text
        assert text == message

