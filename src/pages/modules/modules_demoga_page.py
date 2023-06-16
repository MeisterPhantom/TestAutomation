from src.resources.modules.modules_demoga_resources import *
from helper_methods.helpermethods import *


class ModulesDemogaPage:

    def __init__(self, browser):
        self.browser = browser
        self.helper = HelperMethods(browser)

    def select_list_option(self, option):
        self.helper.get_element(*ModulesLocators.OPTIONS_BTNS, option)
