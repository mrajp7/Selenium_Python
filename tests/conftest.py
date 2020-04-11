# A generic place to define Fixtures, pytest hooks etc
import pytest
from selenium import webdriver
import logging
import inspect

# to add a new command line flag for browser name as input
def pytest_addoption(parser):
    # to have browser_name as cli input, so we can choose which browser to execute at run time
    parser.addoption(
        "--browser_name", action="store", default="chrome", 
        help="accepeted options: chrome | firefox | edge"
    )

    # add another command line flag to set the log level
    parser.addoption(
        "--log_level", action="store", default="info",
        help="accepted options: debug | info | warning | error | critical"
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
    request.cls.log_level = get_log_level(
        request.config.getoption("log_level"))

    # Teardown steps
    yield
    driver.close()

def get_log_level(logger_str):
    if logger_str == "info":
        return logging.INFO
    elif logger_str == "debug":
        return logging.DEBUG
    elif logger_str == "":
        return logging.WARNING
    elif logger_str == "":
        return logging.ERROR
    elif logger_str == "":
        return logging.CRITICAL
    else:
        return logging.INFO
