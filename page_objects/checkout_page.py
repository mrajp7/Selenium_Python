# Page objects for Checkout Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.confirm_page import  ConfirmPage

class CheckoutPage:

    # Constructor to initiate webdriver object
    def __init__(self,driver):
        self.driver = driver
    
    #region page locators

    card_titles = (By.CSS_SELECTOR,"h4.card-title")
    checkout_btn = (By.XPATH,"//a[@class='nav-link btn btn-primary']")

    #endregion
    
    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_titles)

    def click_checkout_get_confirm_page(self):
        self.driver.find_element(*CheckoutPage.checkout_btn).click()
        return ConfirmPage(self.driver)
