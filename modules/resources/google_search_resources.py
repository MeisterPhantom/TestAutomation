from selenium.webdriver.common.by import By


class GoogleLocators:
    SEARCH_BTN = (By.XPATH, '//input[@name="q"]')
    RESULTS = (By.XPATH, '//*[@id="result-stats"]')
