# handling frames

from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com/iframe")

# switching to frame to handle the body/editor of the frames
chrome.switch_to.frame("mce_0_ifr")

chrome.find_element_by_id("tinymce").send_keys("I am able to automate")

# switching back to main dom
chrome.switch_to.default_content()

print(chrome.find_element_by_tag_name("h3").text)