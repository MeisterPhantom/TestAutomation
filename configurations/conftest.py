from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()
    driver.get("https://www.hexacta.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()
