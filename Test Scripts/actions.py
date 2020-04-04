# actions
from selenium import webdriver
from selenium.webdriver import ActionChains

chrome = webdriver.Chrome()
chrome.get("https://www.adidas.co.in/")

actions = ActionChains(chrome)

# move to the mega menu 'Select'
actions.move_to_element(chrome.find_element_by_xpath("//div[@class='flyout online-shop']")).perform()

# click on kids
actions.move_to_element(chrome.find_element_by_xpath("//a[contains(text(),'Kids')]")).click().perform()
