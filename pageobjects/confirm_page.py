# Page objects of Confirm Page [Purchase page]
from selenium import webdriver
from selenium.webdriver.common.by import By

class ConfirmPage:
    
    #constructor
    def __init__(self,driver):
        self.driver = driver

    #region page locators

    checkout_btn = (By.XPATH,"//button[@class='btn btn-success']")
    product_listed = (By.XPATH,"//h4[@class='media-heading']/a")
    purchase_btn = (By.XPATH,"//input[@class='btn btn-success btn-lg']")
    delivery_input = (By.ID,"country")
    auto_suggestion_india = (By.XPATH,"//div[@class='suggestions']//a[text()='India']")
    tnc_checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    success_alert = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")

    #endregion

    def get_product_in_cart(self):
        return self.driver.find_element(*ConfirmPage.product_listed)

    def get_checkout_button(self):
        return self.driver.find_element(*ConfirmPage.checkout_btn)

    def get_delivery_input(self):
        return self.driver.find_element(*ConfirmPage.delivery_input)

    def get_auto_suggestion_india(self):
        return self.driver.find_element(*ConfirmPage.auto_suggestion_india)

    def get_tnc_checkbox(self):
        return self.driver.find_element(*ConfirmPage.tnc_checkbox)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def get_success_alert(self):
        return self.driver.find_element(*ConfirmPage.success_alert)

    