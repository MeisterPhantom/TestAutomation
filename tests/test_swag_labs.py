from modules.pages.login_page import LoginPage
from modules.pages.checkout_page import CheckoutPage
from modules.pages.menu_page import MenuPage
from modules.pages.shop_items_page import ShopItemsPage
from tests.assertions import *
from configurations.conftest import *
import pytest


def test_buy_items(browser):
    login = LoginPage(browser)
    checkout = CheckoutPage(browser)
    menu = MenuPage(browser)
    shop = ShopItemsPage(browser)
    login.login_action("standard_user", "secret_sauce")
    shop.select_item_action()
    menu.cart_shopping_action()
    assert_transaction(checkout.checkout_action("prueba", "last", 203451))
    menu.logout_action()
