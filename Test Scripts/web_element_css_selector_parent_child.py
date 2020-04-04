# This test file describes css selector on traversing through parent, child 
# (ancestors) and usages of :nth-child()
from selenium import webdriver
import time

firefox_driver = webdriver.Chrome()
firefox_driver.maximize_window()
firefox_driver.get("https://rahulshettyacademy.com/angularpractice/")

# tag.class .class:nth-child(3)
# tag.#id tag:nth-child(3)
employed_radio_btn = firefox_driver.find_element_by_css_selector(".form-group .form-check-inline:nth-child(3) label")
print(employed_radio_btn.text)
employed_radio_btn.click()

time.sleep(5)

firefox_driver.close()