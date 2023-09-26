from selenium.webdriver.common.by import By


class TextBoxLocators:
    FULL_NAME_FIELD = (By.XPATH, '//input[@id="userName"]')
    EMAIL_FIELD = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS_FIELD = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS_FIELD = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT_BTN = (By.XPATH, '//button[@id="submit"]')
