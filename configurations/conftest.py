import json
import pytest
from selenium import webdriver


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


@pytest.fixture
def config(scope='session'):
    with open("config.json") as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Firefox', 'Headless Chrome']
    assert config['type'] in ['local', 'remote']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    assert isinstance(config['url_remote'], str)
    assert len(config['url_remote']) > 0
    return config


@pytest.fixture
def browser(config):
    if config['type'] == 'local':
        if config['browser'] == 'Firefox':
            opts = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=opts)
        elif config['browser'] == 'Chrome':
            opts = webdriver.ChromeOptions()
            driver = webdriver.Chrome(options=opts)
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported in local mode')
    elif config['type'] == 'remote':
        if config['browser'] == 'Firefox':
            opts = webdriver.FirefoxOptions()
        elif config['browser'] == 'Headless Chrome':
            opts = webdriver.ChromeOptions()
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported in remote mode')

        # opts.add_argument('--no-sandbox')
        # opts.add_argument('--headless')
        # opts.add_argument('--disable-gpu')

    driver.get("https://demoqa.com/")
    driver.maximize_window()
    driver.implicitly_wait(config['implicit_wait'])
    yield driver
    driver.quit()
