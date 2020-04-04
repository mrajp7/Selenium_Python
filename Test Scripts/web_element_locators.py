from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")

name_element = driver.find_element_by_name("name")

name_element.clear()
name_element.send_keys("Check Box By id")
check_box = driver.find_element_by_id("exampleCheck1")
check_box.click()

name_element.clear()
name_element.send_keys("Check Box By xpath")
check_box_by_xpath = driver.find_elements_by_xpath("//input[@class='form-check-input' and @type='checkbox']")
print(*check_box_by_xpath)
check_box_by_xpath[0].click()

name_element.clear()
name_element.send_keys("Check Box By css selector - id")
check_box_by_css_selector = driver.find_element_by_css_selector("input#exampleCheck1")
check_box_by_css_selector.click()
name_element.clear()
name_element.send_keys("Check Box By css selector - class")
check_box_by_css_selector = driver.find_element_by_css_selector("input.form-check-input#exampleCheck1")
check_box_by_css_selector.click()
name_element.clear()
name_element.send_keys("Check Box By css selector - tag[attribute:value]")
check_box_by_css_selector = driver.find_element_by_css_selector("input[id=exampleCheck1][type=checkbox]")
check_box_by_css_selector.click()



time.sleep(5)
driver.close()