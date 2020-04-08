# A generic place to define Fixtures, pytest hooks etc
import pytest
from selenium import webdriver

# to add a new command line flag
def pytest_addoption(parser):
    # to have browser_name as cli input, so we can choose which browser to execute at run time
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox or edge"
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
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    driver.maximize_window()
    request.cls.driver = driver

    # Teardown steps
    yield
    driver.close()