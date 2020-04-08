# Test site - https://rahulshettyacademy.com/AutomationPractice/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector('input.inputs[id="name"][placeholder="Enter Your Name"]').send_keys("Test")
driver.find_element_by_css_selector('input.btn-style[id="alertbtn"][value="Alert"]').click()

# change the driver context to handle alerts
pop_up = driver.switch_to.alert
print(pop_up.text)
# accept to click on 'ok'
pop_up.accept()

driver.find_element_by_id('confirmbtn').click()
# dismiss() to click on 'cancel'
pop_up.dismiss()
#pop_up.send_keys(Keys.SPACE)