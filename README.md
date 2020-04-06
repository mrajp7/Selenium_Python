# Selenium_Python
Test Automation project with Python and Selenium web driver

# Project Details:
- python 3.6.9 64-bit
- pip3 
  [for ubuntu pip3 is not installed along with Python as default: 
  `sudo apt-get install python3-pip`]

# Required packages:
- pip3 install selenium
- install webdriver executables
  chromedriver - https://chromedriver.chromium.org/downloads
  firefox/geckodriver - https://github.com/mozilla/geckodriver/releases
  [Ubuntu|Linux] - download the `chromedriver` and place it in `usr\bin\chromedriver`
  [Windos] - Download and place it in any desired path. Remember to append
  the path variable or directly mention the path details in the scripts
  note: similar steps for geckodriver. Ensure to download the latest version depending upon your      OS and browser
- pip3 install pytest

# Pytest conventions
## Test Filename rules:
  any pytest file should start with 'test*.py'
  ex: `test_login_valid_tc_01.py`

## Function | Method rules:
  any method is considered as testcase (defined in the pytest files) if
  it starts with test_ 'def test_*()' or ends with _test 'def *_test()'
  ex: `def test_login_demo()` `def login_demo_test()`
  Methods should always have a unique and meaningful names

## Run Test options:
  ###### GUI [VS Code]:
    Configure using command palette [Menu:View->Comman Palette or CTRL + SHIFT + P]
    run command -> `Python: Configure Tests -> [Pytest]`
  ###### CLI:
    Go to specific path where tests are available
    `pytest -v -s` to run all the tests under the folder.
    -v : verbose details
    -s : displays the console log in the test
    _Note: Here on we will focus on CLI test run mode._

## pytest reference:
  https://docs.pytest.org/en/latest/usage.html
  
## Run a specific test file:
  `pytest sample_pytest_tests/test_another_demo.py -v -s`

## Run tests matching test name pattern
  To run a set of tests with a test case name pattern (which is persent in multiple files)
  `pytest -k testdemo -v -s`
  -k : flag to match the regular expression/pattern

## Run tests suites [group] :
  To run a group of test (Smoke|Regression etc.,) pytest 'mark' is used.
  it is decorated on a test method as `@pytest.mark.smoke`
  _Note: 'suites or mark' has to be registered in pytest.ini file in order to decorate on a test._
  [LETS COVER THIS IN LATER PART OF THE FRAMEWORK CONFIGURATIONS]
  `pytest -m smoke -v -s`
  -m : flag to choose a marked suite in a test

- To skip
