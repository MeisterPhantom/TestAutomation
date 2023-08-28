from selenium.webdriver.common.by import *


class BooksResources:
    ADD_BOOK_BTN = (By.XPATH, '//*[@id="addNewRecordButton"]')
    BOOK_LIST = (By.XPATH, '//*[@class="action-buttons"]/span/a')
    TITLE_BOOK_LABEL = (By.XPATH, '//*[@id="tittle-label"]')

