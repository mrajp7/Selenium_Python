import os.path
import sys

sys.path.append(os.path.dirname(__file__) + "/..")

import logging
import pytest
from utilities.testbase import TestBase
from pageobjects.home_page import HomePage
from testdata.home_page_data import HomePageData


class TestHomePage(TestBase):
    """

    TestHomePage comprises of test cases that validates the Homepage of - 
        https://rahulshettyacademy.com/angularpractice/

    It Inherits - TestBase class 
    which in turn takes care of setup and teardown for the Test class

    """

    def test_home_page_happy_path(self, getdata):
        """
        Steps
        1. Load the home page - https://rahulshettyacademy.com/angularpractice/
        2. Enter a valid details on 'Name', 'Email', 'Password',  
            Yes to (check me out if you love Icecreams!) 'Checkbox',
            Select an option from 'Gender',
            choose the 'Employment Status' radio button - 'Employed',
            Enter a valid 'Date of Birth'
        3. Click on Submit
        4.  Verify the alert message - success
        """
        # create object for homepage Page Object.
        home_page = HomePage(self.driver)

        # set values to the fields Name,Email,Password,Checkbox
        home_page.get_name_input().send_keys(getdata["firstname"])
        home_page.get_email_input().send_keys(getdata["email"])
        home_page.get_password_input().send_keys(getdata["password"])
        if getdata["enable_check"]:
            home_page.get_ice_cream_checkbox().click()

        # select gender as Male
        # call the utility method in testbase to achieve the same
        self.select_option_by_text(home_page.get_gender_select(), getdata["gender"])

        # click on the Employed radio button to enable it
        home_page.get_employed_radio().click()

        # enter a valid date of birth on the DON field
        home_page.get_dob_date().send_keys(getdata["dob"])
        logging.info("The form is filled with the test data succesfully")
        logging.info(getdata)

        # click on submit
        home_page.get_submit_button().click()

        success_message = home_page.get_alert_message().text
        logging.info("The message received after form submittion," + success_message)
        assert "Success! The Form has been submitted" in success_message
        logging.info("Test completed")

    @pytest.fixture(params=HomePageData.home_page_happy_path_data)
    def getdata(self, request):
        self.driver.refresh()
        return request.param
