# this file demostrates the Logging object creation and usage.
import logging

# we are creating a logger object directly inside a test.
# ( this will not be the same case in the test framework )
def test_logging_demo_tc():
    
    # create object for the logging

    # getLogger accepts a optional param name: and 
    # assigns the value to logging objects global variable 'name'
    
    # __name__ denotes the name of the runtine method thats currently in focus, 
    # i.e., in this context __name__ is 'test_logging_demo'
    logger = logging.getLogger(__name__) 

    # create a filehandler (file location)
    fileHandler = logging.FileHandler('logfile.txt',mode="w")

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
    logger.setLevel(logging.DEBUG)

    # logger usage in test steps
    logger.debug("this is a debug level message")
    logger.info("this is a info level message")
    logger.warning("this is a warning level message")
    logger.error("this is a error level message")
    logger.critical("this is a critical level message")

    # by default pytest-html will include the log messages in the html report as well
    # just run a test with html report and the logs will be included.
    # pytest -v -s --html=report.html