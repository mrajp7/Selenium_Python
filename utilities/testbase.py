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
        # create object for the logging
            
        # getLogger accepts a optional param name: and 
        # assigns the value to logging objects global variable 'name'
        
        # inspect,stack() provides the stack trace of the caller
        # [1][3] gives the method that was calling the logger instance
        # since pytest considers method as testname we select that as logger name
        caller_name = inspect.stack()[1][3]
        logger = logging.getLogger(caller_name) 

        # create a filehandler (file location)
        fileHandler = logging.FileHandler('logfile.txt') #,mode="w"

        # create a formatter object
        # <timestamp> : asctime
        # <log_type> : levelname [info/debug/warning/error/critical]
        # <testcase_name> : name [__name__] (we have set while creating logger object line:15)
        # <log_message> : message (which will be called as logger.info(message))
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        # attach the formatter to filehandler object
        fileHandler.setFormatter(formatter)

        # attach the fileHandler to logger object
        logger.addHandler(fileHandler)

        # set level for the logger.
        # logger.setLevel is the hierarchy for logging
        # hierarchy is 1.debug, 2.info, 3.warning, 4.error, 5.critical
        # if 'debug is set all logs level will be captured
        # if 'info' is set except debug all types will be captured 
        
        logger.setLevel(self.log_level)

        return logger