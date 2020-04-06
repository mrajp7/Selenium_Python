# this file explains the usage of fixture in pytest
# to run - pytest sample_pytest_tests/test_fixture_demo.py -v -s
import pytest

@pytest.fixture
def setup():
    print("I run before the test method that has included me!")
    yield # teardown included!
    print("Setup cleared!")

def test_fix_demo1(setup):
    print("I will run after the fixture - setup has run")

def test_fix_demo2():
    print("I will not include the fixture - setup")

# test using a global fixture from 'conftest.py'
def test_conftest_fix_demo3(global_setup):
    print("test from file - test_fixture_demo.py")

@pytest.mark.usefixtures("global_setup")
# for every test method in this class, the global_setup method will be called
class TestGroup1:

    def test_testgroup_demo1(self):
        print('demo1 test comment')
    

    def test_testgroup_demo2(self):
        print('demo2 test comment')

    
    def test_testgroup_demo3(self):
        print('demo3 test comment')

@pytest.mark.usefixtures("global_class_setup")
class TestGroup2:

    def test_testgroup2_demo1(self):
        print('TestGroup2 - demo1 test comment')

    def test_testgroup2_demo2(self):
        print('TestGroup2 - demo2 test comment')
    
    def test_testgroup2_demo3(self):
        print('TestGroup2 - demo3 test comment')

