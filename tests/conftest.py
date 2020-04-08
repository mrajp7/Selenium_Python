# A generic place to define Fixtures, pytest hooks etc
import pytest

# to add a new command line flag
def pytest_addoption(parser):
    # to have browser_name as cli input, so we can choose which browser to execute at run time
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox or edge"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getOption("browser_name")
    print(browser)