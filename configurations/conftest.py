from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="session")
def browser():
    driver_options = Options()
    # driver_options.add_argument("--headless")
    driver_options.set_preference("browser.download.folderList", 2)
    driver_options.set_preference("browser.download.manager.showWhenStarting", False)
    driver_options.set_preference("browser.download.dir", "C:\Tests")
    driver_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")
    # Line for execute the tests with Google Chrome
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
    #                          options=driver_options)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                               options=driver_options)
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()
