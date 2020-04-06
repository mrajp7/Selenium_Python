import pytest
# This file explains the concepts of using a data driven fixture

# A normal fixture
@pytest.fixture
def pre_requisite():
    print('I have to prepare the environment')


# Returning a string fixture
@pytest.fixture
def info():
    print('Inside the info')
    return "demo tests"

# Returning a tuple fixture
@pytest.fixture
def personal_info():
    print('Inside personal info')
    return ['Mohan','Raj',30]

@pytest.mark.usefixtures("pre_requisite","info","personal_info")
class TestDataFixtures:

    def test_demo(self):
        print('this test doesnt use the data provided by the fixtures')

    def test_demo1(self,info,personal_info):
        print(info)
        print(personal_info[0])
        print(personal_info[1])
        print(personal_info[2])