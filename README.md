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

# Pytest conventions:
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
  - https://docs.pytest.org/en/latest/usage.html
  
## Run a specific test file:
  `pytest sample_pytest_tests/test_another_demo.py -v -s`

## Run tests matching test name:
  - To run a set of tests with a test case name pattern (which is persent in multiple files)
    `pytest -k testdemo -v -s`
    -k : flag to match the regular expression/pattern

## Run tests suites [group] :
  - To run a group of test (Smoke|Regression etc.,) pytest 'mark' is used.
    it is decorated on a test method as `@pytest.mark.smoke`
    _Note: 'suites or mark' has to be registered in pytest.ini file in order to decorate on a test._
    [LETS COVER THIS IN LATER PART OF THE FRAMEWORK CONFIGURATIONS]
    `pytest -m smoke -v -s`
    -m : flag to choose a marked suite in a test

## Skip tests:
  - To skip tests while running tests, there are two ways,
    1. to decorate your test method with default mark
      `@pytest.mark.skip`
    2. using `pytest.skip("skipping this test")` as first step inside the method

## Fixtures:
  ###### Basic usage:
    - When we want any method to be run as pre-requiste or common setup fixtures can be used
    - Just like Setup | Teardown in Testng or any harness tool, fixtures can be used for the same purpose.
    - Fixture method need not have 'test_' method conventions, hence it will not be considered as a test case/method.
    - Decorate the method with `@pytest.fixture`
    - Once a fixture is available we can pass the method name as paramater to test methods.
    `ex:
    @pytest.fixrure
    def setup():
      pass
    
    def test_login(setup):
      pass
    `
    - refer file - sample_pytest_tests\test_fixture_demo.py
    - When we need to use a teardown, we can include the steps in the same fixture (setup) created with `yield` infront of the teardown steps.

  ###### Module level fixtures:
    - In order to use a fixture method through out all files in a folder we need to create a file with name `conftest.py`
    - The fixture method has to be defined in this file and other files now can access this fixture.

  ###### Class level fixtures:
    - When we need to include fixture for many tests in a file, instead of passing it as argument on every step, we can create a class level decorations
    - create a class and add all the tests as methods to the class
    - Add decoration `@pytest.mark.usefixtures("<fixture_method_name>") on the class level.
    - When we need a fixture to run only once before all test methods starts execution,
      define the fixture scope as class
      `@pytest.fixture(scope="class")`
    - refer file - sample_pytest_tests\test_fixture_demo.py
  
  ###### Fixtures as data input
    - A fixture can also be used as data provider for a test method
    - A fixture can return any object type from the method (string, tuple, list etc.,)
    - for class level usage, even though the data fixture (which returns value) is decorated at class level, a test method should again use it in the paramter for the using the value that is being returned.
    - refer file - sample_pytest_tests\test_data_fixtures_demo.py

  ###### Fixtures run tests with different data
    - A fixture can be configured to return multiple params.
    - When consumed by a test method it runs for n times depending on the n params
    - refer file - sample_pytest_tests\test_params_fixtures_demo.py

# Pytest html reporting:
  - to install - pip3 install pytest-html
  - while running test over CLI run the following command to generate html report
    `pytest --html=report.html`
  
# Logging:
  - We use the package 'logging' which is by default included in Python
  - Genrally Logs gives more information on how the test has run and it even support or provide more information to a non technical person as well.
  - Logs helps in understanding the test code, steps and test failures wihtout debugging the tests
  - the format of logging each step is,
    `<timestamp> : <log_type> : <testcase_name> : <log_message>`
  - log_types - info, debug, warning, error, critical
  - refer file - sample_pytest_tests\test_logging_demo.py

# Run Test Final command to incorporate all required flag and inputs
`pytest tests -v -s --browser_name=chrome --log_level=info --html=reports/report.html --junitxml=reports/results.xml`
 - A shell script is created as test_run.sh
 - change the mode of the file as `chmod +x test_run.sh`
 - run in the terminal as `.\test_run.sh`

 # To read data from excel
  - `pip3 install openpyxl`