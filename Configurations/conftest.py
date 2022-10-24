from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    driver.implicity_wait(10)
    driver.get("http://automationpractice.com/index.php")
    driver.maximaze_window()
    yield driver
    driver.quit()
