# global / module level file to define fixtures that can be consumed by any tests under test files
# in this folder.
import pytest

#default - method level scope
#i.e., runs before every test method when used
@pytest.fixture
def global_setup():
    print('Global - setup has run')
    yield
    print('Global - teardown has run')

# class level scope
# this will be called only once before all the tests in a class runs 
# and teardown after all the tests are completed if yield is added
@pytest.fixture(scope="class")
def global_class_setup():
    print('Scope - class setup')
    yield
    print('Scope - class teardown')