import os.path
import sys
sys.path.append(os.path.dirname(__file__) + '/..')

import pytest
from utilities.testbase import TestBase
from page_objects.home_page import HomePage

class TestHomePage(TestBase):
    """

    TestHomePage comprises of test cases that validates the Homepage of - 
        https://rahulshettyacademy.com/angularpractice/

    It Inherits - TestBase class 
    which in turn takes care of setup and teardown for the Test class

    """

    def test_home_page_happy_path(self):
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
        home_page.get_name_input().send_keys("Mohan raj")
        home_page.get_email_input().send_keys("mohan.raj888@gmail.com")
        home_page.get_password_input().send_keys("test1234")
        home_page.get_ice_cream_checkbox().click()

        # select gender as Male
        # call the utility method in testbase to achieve the same
        self.select_option_by_text(home_page.get_gender_select(),"Male")

        # click on the Employed radio button to enable it
        home_page.get_employed_radio().click()

        # enter a valid date of birth on the DON field
        home_page.get_dob_date().send_keys("01091989")

        # click on submit
        home_page.get_submit_button().click()

        success_message = home_page.get_alert_message().text

        assert "Success! The Form has been submitted" in success_message
