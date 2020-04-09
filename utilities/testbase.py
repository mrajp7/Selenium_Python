import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.mark.usefixtures("setup")
class TestBase:
    
    def wait_for_element(self,locator_tuple,timeout_in_sec):
        WebDriverWait(self.driver,timeout_in_sec).until(
            expected_conditions.presence_of_element_located(locator_tuple))
