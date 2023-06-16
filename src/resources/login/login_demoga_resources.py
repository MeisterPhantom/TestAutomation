from selenium.webdriver.common.by import *


class LoginResources:
    USERNAME_FIELD = (By.XPATH, '//*[@id="userName"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]')
    MESSAGE_TEXT = (By.XPATH, '//*[@id="name"]')

