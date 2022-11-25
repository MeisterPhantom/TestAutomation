from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="session")
def browser():
    driver_options = Options()
    driver_options.add_argument("--headless")
    driver = webdriver.Chrome(options=driver_options)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()
