from selenium.webdriver.common.by import By


class MenuLocators:
    BUTTON_CART_SHOPPING = (By.XPATH, '//div[@id="shopping_cart_container"]')
    BUTTON_MENU = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    BUTTON_LOGOUT = (By.XPATH, '//a[@id="logout_sidebar_link"]')


