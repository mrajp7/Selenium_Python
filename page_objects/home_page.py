# Page objects for Checkout Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.checkout_page import CheckoutPage

class HomePage:

    # Constructor to initiate webdriver object
    def __init__(self,driver):
        self.driver = driver
    
    #region page locators

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "div.form-group input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    icecream_checkbox = (By.ID, "exampleCheck1")
    gender_select = (By.ID, "exampleFormControlSelect1")
    employed_radio = (By.ID,"inlineRadio2")
    dob_date = (By.CSS_SELECTOR,"input[name='bday']")
    submit = (By.CSS_SELECTOR,"input[value='Submit']")
    alert_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    #endregion

    def navigate_shop_to_checkout(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)

    def get_name_input(self):
        return self.driver.find_element(*HomePage.name)

    def get_email_input(self):
        return self.driver.find_element(*HomePage.email)

    def get_password_input(self):
        return self.driver.find_element(*HomePage.password)

    def get_ice_cream_checkbox(self):
        return self.driver.find_element(*HomePage.icecream_checkbox)

    def get_gender_select(self):
        return self.driver.find_element(*HomePage.gender_select)

    def get_employed_radio(self):
        return self.driver.find_element(*HomePage.employed_radio)

    def get_dob_date(self):
        return self.driver.find_element(*HomePage.dob_date)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit)

    def get_alert_message(self):
        return self.driver.find_element(*HomePage.alert_msg)
    