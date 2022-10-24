from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
