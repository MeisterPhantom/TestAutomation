from src.resources.windows.windows_resources import *


class WindowsDemogaPage:

    def __init__(self, browser):
        self.browser = browser

    def select_new_tab(self):
        self.browser.find_element(*WindowsResources.NEW_TAB_BTN).click()

    def new_tab_validation(self, message):
        for window_handle in self.browser.window_handles:
            if window_handle != 0:
                self.browser.switch_to.window(window_handle)
                break
        text = self.browser.find_element(*WindowsResources.NEW_TAB_TEXT_LABEL).text
        assert text == message

