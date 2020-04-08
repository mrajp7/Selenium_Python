from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com/windows")
# click on 'clikc here' to create a new window
chrome.find_element_by_css_selector("div.example a[href='/windows/new']").click()
# this also possible
# chrome.find_element_by_link_text("Click Here")

# handle the new window here
# Note: New tab or New window both are same in selenium webdriver
# since we expect a new window is being opened on the above step
assert len(chrome.window_handles) > 1
chrome.switch_to.window(chrome.window_handles[1])

assert "New Window" == chrome.find_element_by_tag_name("h3").text
# close the child window
chrome.close()
#switching back to parent window/tab
chrome.switch_to.window(chrome.window_handles[0]) #[0] is always the parent window that the script has opened

assert "Opening a new window" == chrome.find_element_by_tag_name("h3").text

