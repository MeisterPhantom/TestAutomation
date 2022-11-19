from selenium.webdriver.common.by import By


class ContactUsLocators:
    SEARCH_BTN = (By.XPATH, '//*[@id="menu-social-menu"]/li/ul/li[1]/a/span')
    SEARCH_INPUT = (By.XPATH, '//*[@id="search-field"]')
    RESULT = (By.XPATH, '//article[@class="display-flex"]//div//h3')
