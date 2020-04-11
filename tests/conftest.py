# A generic place to define Fixtures, pytest hooks etc
import pytest
from selenium import webdriver
import logging
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
    request.cls.log_level = get_log_level(request.config.getoption("log_level"))
    init_logger(request.cls.log_level)

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


def init_logger(log_level):
    # create object for the logging

    # getLogger accepts a optional param name: and
    # assigns the value to logging objects global variable 'name'

    # inspect,stack() provides the stack trace of the caller
    # [1][3] gives the method that was calling the logger instance
    # since pytest considers method as testname we select that as logger name
    caller_name = inspect.stack()[1][3]
    logger = logging.getLogger()

    # create a filehandler (file location)
    fileHandler = logging.FileHandler("logfile.txt")  # ,mode="w"

    # create a formatter object
    # <timestamp> : asctime
    # <log_type> : levelname [info/debug/warning/error/critical]
    # <testcase_name> : name [__name__] (we have set while creating logger object line:15)
    # <log_message> : message (which will be called as logger.info(message))
    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(name)s : %(message)s"
    )

    # attach the formatter to filehandler object
    fileHandler.setFormatter(formatter)

    # attach the fileHandler to logger object
    logger.addHandler(fileHandler)

    # set level for the logger.
    # logger.setLevel is the hierarchy for logging
    # hierarchy is 1.debug, 2.info, 3.warning, 4.error, 5.critical
    # if 'debug is set all logs level will be captured
    # if 'info' is set except debug all types will be captured

    logger.setLevel(log_level)
