# This file is used to demonstrate the use of params and request in fixture
# which is used to run a test with different inputs

# if a fixture has 3 params, the test will run for 3 times
import pytest
from selenium import webdriver
import time

@pytest.fixture(params=[("Mohan",30),("Praveena",29),("Dhanu",3)])
def age_group(request):
    return request.param


def test_to_run_multiple_times(age_group):
    print("Name", age_group[0],"Age", age_group[1])


# Another example on cross browser using fixtures
@pytest.fixture(params=['Chrome','Firefox'])
def cross_browser(request):
    return request.param

def driver_factory(browser_name):
    if browser_name == "Chrome":
        return webdriver.Chrome()
    elif browser_name == "Firefox":
        return webdriver.Firefox()
    else:
        return webdriver.Chrome()

def test_open_google_on_all_browser(cross_browser):
    #driver = webdriver.Chrome()
    driver = driver_factory(cross_browser)
    driver.get("https://www.google.com/")
    time.sleep(2)
    #driver.quit()