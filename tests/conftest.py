# A generic place to define Fixtures, pytest hooks etc
import pytest
from selenium import webdriver
from logzero import logfile
import inspect

# to add a new command line flag for browser name as input
def pytest_addoption(parser):
    # to have browser_name as cli input, so we can choose which browser to execute at run time
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="accepeted options: chrome | firefox | edge",
    )

    # add another command line flag to set the log level
    parser.addoption(
        "--log_level",
        action="store",
        default="info",
        help="accepted options: debug | info | warning | error | critical",
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    # Navigate to the AUT URL
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver

    # Teardown steps
    yield
    driver.close()


@pytest.fixture(scope="session")
def init_logger(request):
    # create a filehandler (file location)
    logfile("logfile.txt")
