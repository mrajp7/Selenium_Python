# This file is to demeonstrate the pytest conventions and features.
import pytest

# `Filename rules`
#  ---------------
# the file name should start with `test*.py` for pytest to identify when the tests are run.

# `Function/Method rules`
# -----------------------
# Each function in this file will be considered as a test case.
# the function also should start with `def test_*`` or end with `*_test`

# reference - https://docs.pytest.org/en/latest/usage.html

# this test is marked as group - smoke
# syntax - pytest.mark.<suite_name>
@pytest.mark.smoke
def test_to_pass():
    pass

# to learn more about fixtures - 
# https://pythontesting.net/framework/pytest/pytest-fixtures/
@pytest.fixture
def error_fixture():
    assert 0

def test_to_fail():
    assert False

def test_error(error_fixture):
    pass


# to mark a test failure for any reason, such as not implemented etc.,
def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass

def test_testdemo_tc01():
    pass