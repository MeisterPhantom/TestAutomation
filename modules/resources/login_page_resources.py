from selenium.webdriver.common.by import By


class LoginLocators:
    USER_FIELD = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    BUTTON_LOGIN = (By.XPATH, '//input[@id="login-button"]')
