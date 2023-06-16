from selenium.webdriver.common.by import By


class TextBoxLocators:
    FULL_NAME_FIELD = (By.XPATH, '//*[@id="userName"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="userEmail"]')
    CURRENT_ADDRESS_FIELD = (By.XPATH, '//*[@id="currentAddress"]')
    PERMANENT_ADDRESS_FIELD = (By.XPATH, '//*[@id="permanentAddress"]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="submit"]')
