import os.path
import sys
sys.path.append(os.path.dirname(__file__) + '/..')

import pytest
from utilities.testbase import TestBase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestSample(TestBase):

    def test_sample(self):
        # find all the list items and search for 'Blackberry'
        items = self.driver.find_elements_by_css_selector('h4.card-title')

        for item in items:
            if item.find_element_by_xpath('a').text == 'Blackberry':
                item.find_element_by_xpath('parent::div/parent::div/div/button').click()

        # click on checkout screen
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

        # wait for the checkout screen to load and click on Checkout
        wait = WebDriverWait(self.driver,10)

        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@class='btn btn-success']")))

        # Assert 'Blackberry' is added in the cart
        assert 'Blackberry' == self.driver.find_element_by_xpath("//h4[@class='media-heading']/a").text

        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

        # wait until the delivery location selection screen appears
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@class='btn btn-success btn-lg']")))

        # enter 'india' and wait for the suggestion control to appear
        self.driver.find_element_by_id('country').send_keys('india')

        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']//a[text()='India']")))

        # click on the suggestion location - India
        self.driver.find_element_by_xpath("//div[@class='suggestions']//a[text()='India']").click()

        # click on the Terms and conditions check box
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

        # click on Purchase
        self.driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()

        # wait until the text is shown
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='alert alert-success alert-dismissible']")))

        alert_message = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

        assert "Success! Thank you! Your order will be delivered in next few weeks" in alert_message