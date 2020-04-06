# this test files talks about skipping tests in pytest
import pytest

# to skip a test
def test_skip():
    pytest.skip("skipping this test")

# this test is skipped using default mark.skip
@pytest.mark.skip
def test_skip_by_mark():
    assert 0