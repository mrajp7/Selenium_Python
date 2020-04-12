import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import inspect
import logging


@pytest.mark.usefixtures("setup","init_logger")
class TestBase:
    def wait_for_element(self, locator_tuple, timeout_in_sec):
        WebDriverWait(self.driver, timeout_in_sec).until(
            expected_conditions.presence_of_element_located(locator_tuple)
        )

    def select_option_by_text(self, webelement, text):
        sel = Select(webelement)
        sel.select_by_visible_text(text)
