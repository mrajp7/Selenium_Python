import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import inspect
import logging

@pytest.mark.usefixtures("setup")
class TestBase:

    def wait_for_element(self,locator_tuple,timeout_in_sec):
        WebDriverWait(self.driver,timeout_in_sec).until(
            expected_conditions.presence_of_element_located(locator_tuple))

    def select_option_by_text(self,webelement,text):
        sel = Select(webelement)
        sel.select_by_visible_text(text)

    def get_logger(self):
        # stack [1][3] provides the test method name
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name) 

        # create a filehandler (file location)
        fileHandler = logging.FileHandler('logfile.log') #,mode="w"
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

        # attach the formatter to filehandler object
        fileHandler.setFormatter(formatter)

        # attach the fileHandler to logger object
        logger.addHandler(fileHandler)

        # set level for the logger.
        logger.setLevel(self.log_level)

        return logger