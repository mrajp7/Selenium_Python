from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://google.com")
print(driver.current_url)
driver.close()

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://google.com")
print(driver.title)
driver.back()
driver.refresh()
driver.minimize_window()
time.sleep(5)
driver.close()