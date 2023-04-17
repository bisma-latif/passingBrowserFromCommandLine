import time
import pytest
from selenium import webdriver
from Tests import settings



def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser", action="store", default=settings.browser)
    parser.addoption("--env", action="store", default=settings.env)


@pytest.fixture(scope='class')
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser

@pytest.fixture(scope='class')
def getenv(request):
    _env =request.config.getoption("--env")
    return _env

@pytest.fixture(scope='class')
def getDriver(request, getBrowser, getenv):
    _driver = None
    print("browser from getBrowser method - " + getBrowser)
    if getBrowser == "chrome":
        _driver = webdriver.Chrome("drivers/chromedriver/chromedriver.exe")
    elif getBrowser == "firefox":
        _driver = webdriver.Firefox("./drivers/geckodriver/geckodriver.exe")
    if getenv == "qa":
        print("env selected by the user is" + getenv)
        _driver.get("https://www.saucedemo.com/")
    elif getenv =="qa2":
        print("env selected by the user is" + getenv)
        _driver.get("https://yahoo.com")
    _driver.implicitly_wait(20)
    request.cls.driver = _driver
    yield request.cls.driver
    #yield _driver
    time.sleep(2)
    request.cls.driver.quit()
    #_driver.quit()
