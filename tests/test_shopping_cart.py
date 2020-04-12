import os.path
import sys

sys.path.append(os.path.dirname(__file__) + "/..")

import logging
import pytest
from utilities.testbase import TestBase
from pageobjects.home_page import HomePage

class TestShoppingCart(TestBase):
    """
    TestShoppingCart comprises of test cases that validates the shopping cart website

    It Inherits - TestBase class 
    which in turn takes care of setup and teardown for the Test class

    """

    def test_shopping_cart_happy_path(self):
        """
        Shopping cart End to End test

        Steps:
        1. Load the shopping website - https://rahulshettyacademy.com/angularpractice/shop
        2. Add blackberry mobile to the cart
        3. Navigtate to checkout
        4. Add delivery details
        5. Complete the checkout
        
        """
        # create page objects
        log = logging.getLogger("test_shopping_cart_happy_path")
        home_page = HomePage(self.driver)
        checkout_page = home_page.navigate_shop_to_checkout()
        log.info("Navigated to shop")

        # find all the list items and search for 'Blackberry'
        items = checkout_page.get_card_titles()

        for item in items:
            if item.find_element_by_xpath("a").text == "Blackberry":
                item.find_element_by_xpath("parent::div/parent::div/div/button").click()

        # click on checkout screen
        confirm_page = checkout_page.click_checkout_get_confirm_page()

        # wait for the checkout screen to load and click on Checkout
        self.wait_for_element(confirm_page.checkout_btn, 4)

        # Assert 'Blackberry' is added in the cart
        assert "Blackberry" == confirm_page.get_product_in_cart().text
        log.info("Succesfully added 'Blackberry' to the cart")

        confirm_page.get_checkout_button().click()

        # wait until the delivery location selection screen appears
        self.wait_for_element(confirm_page.purchase_btn, 3)

        # enter 'india' and wait for the suggestion control to appear
        confirm_page.get_delivery_input().send_keys("india")

        self.wait_for_element(confirm_page.auto_suggestion_india, 8)

        # click on the suggestion location - India
        confirm_page.get_auto_suggestion_india().click()
        log.info("'India' has been selected as delivery location")

        # click on the Terms and conditions check box
        confirm_page.get_tnc_checkbox().click()

        # click on Purchase
        confirm_page.get_purchase_button().click()

        # wait until the text is shown
        log.info("Waiting for the order confirmation message")
        self.wait_for_element(confirm_page.success_alert, 4)

        assert "Success! Thank you!" in confirm_page.get_success_alert().text
        log.info("Test completed")
