from src.resources.modals.modals_demoqa_resources import *


class ModalsDemoqaPage:

    def __init__(self, browser):
        self.browser = browser

    def show_small_modal_and_validate(self, message):
        self.browser.find_element(*ModalsResources.SMALL_MODAL_BTN).click()
        text = self.browser.find_element(*ModalsResources.TEXT_SMALL_MODAL).text
        assert text == message
