import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def answer_calculate():
    answer = math.log(int(time.time()))
    return str(answer)


@pytest.fixture(scope="function")
def browser():
    print('\nbrowser open')
    # options = Options()
    # options.headless = True
    browser = webdriver.Chrome()
    # (options=options)
    yield browser
    print('\nbrowser quit')
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print('\nstart chrome browser for test')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome of firefox')
    yield browser
    print('\nquit browser')
    browser.quit()
