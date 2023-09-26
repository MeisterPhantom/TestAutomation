from selenium.webdriver.common.by import By


class ProfileLocators:
    BOOK_LIST = (By.XPATH, '//*[@class="action-buttons"]/span/a')
    DELETE_BOOK_BTN = (By.XPATH, '//*[@id="delete-record-undefined"]')
    LOGOUT_BTN = (By.XPATH, '//*[@id="submit"]')
    USERNAME_LABEL = (By.XPATH, '//*[@id="userName-value"]')
