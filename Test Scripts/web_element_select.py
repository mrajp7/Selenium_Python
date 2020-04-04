# This test file emphasizes on element/tag type - Select
# The tag name should be <select>
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
gender_drop_down = Select(chrome_driver.find_element_by_id("exampleFormControlSelect1"))
gender_drop_down.select_by_visible_text("Female")

time.sleep(5)
chrome_driver.close()