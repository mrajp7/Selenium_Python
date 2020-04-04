# web_element_dynamic_drop_down
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")

driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder=\"From\"]").send_keys("che")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p.blackText")

for city in cities:
    if city.text == "Chengdu, China":
        city.click()
        break

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()