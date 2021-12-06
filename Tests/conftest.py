import pytest
from selenium import webdriver
from Base.webdriverfactory import WebDriverFactory
from Pages.home.login_page import LoginPage


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebdriverInstance()

    lp = LoginPage(driver)
    lp.login("romin@taskulu.com","Romin123456789")
    """ 
    if browser == 'firefox':

        #baseUrl = "https://taskulu.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        #driver.get(baseUrl)

        print("Running tests on FF")
    else:
        #baseUrl = "https://taskulu.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        #driver.get(baseUrl)
        print("Running tests on chrome") """

    if request.cls is not None:
        request.cls.driver = driver     # return driver

    yield driver      # when i return driver, i can use the same driver instance, in test classes and page classes
    driver.quit()    # like teardown
    print("Running one time tearDown")




def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")