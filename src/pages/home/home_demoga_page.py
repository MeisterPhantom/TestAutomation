from src.resources.home.home_demoga_resources import *
from helper_methods.helpermethods import *


class HomeDemogaPage:

    def __init__(self, browser):
        self.browser = browser

    def select_section_option(self, option):
        HelperMethods(self.browser).get_element(HomeLocators.SECTIONS_BTNS, option)
