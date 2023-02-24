from selenium.webdriver.common.by import By


class CheckoutLocators:
    BUTTON_CHECKOUT = (By.XPATH, '//button[@class="btn btn_action btn_medium checkout_button"]')
    BUTTON_CONTINUE = (By.XPATH, '//input[@class="submit-button btn btn_primary cart_button btn_action"]')
    BUTTON_FINISH = (By.XPATH, '//button[@class="btn btn_action btn_medium cart_button"]')
    INPUT_FIRST_NAME = (By.XPATH, '//input[@id="first-name"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id="last-name"]')
    INPUT_ZIPCODE = (By.XPATH, '//input[@id="postal-code"]')
    LABEL_FINISH_ORDER = (By.XPATH, '//h2[@class="complete-header"]')
