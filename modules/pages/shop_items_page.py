from modules.resources.shop_items_page_resources import *


class ShopItemsPage:
    def __init__(self, browser):
        self.browser = browser

    def select_item_action(self):
        elements = self.browser.find_elements(*ShopItemLocators.BUTTON_ITEM)
        for e in elements:
            e.click

