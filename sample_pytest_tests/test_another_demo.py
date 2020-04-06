import pytest

# this test is marked as group - smoke
# syntax - pytest.mark.<suite_name>
@pytest.mark.smoke
def test_with_print_stmts():
    print("Hello Test")

def test_with_assert():
    assert "" == "d", "Test failed due to message not matched!"

def test_testdemo_tc02():
    pass