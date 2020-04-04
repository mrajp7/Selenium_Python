from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#options = webdriver.ChromeOptions()
options = webdriver.FirefoxOptions()
options.add_argument("start--maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
# options.addArguments("--window-size=1920,1080");
options.add_argument("--enable-precise-memory-info")
options.add_argument("--disable-popup-blocking")
options.add_argument("test-type=browser")

#driver = webdriver.Chrome(options=options)
driver = webdriver.Firefox(options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()

# find all the list items and search for 'Blackberry'
items = driver.find_elements_by_css_selector('h4.card-title')

for item in items:
    if item.find_element_by_xpath('a').text == 'Blackberry':
        item.find_element_by_xpath('parent::div/parent::div/div/button').click()

# click on checkout screen
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

# wait for the checkout screen to load and click on Checkout
wait = WebDriverWait(driver,10)

wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@class='btn btn-success']")))

# Assert 'Blackberry' is added in the cart
assert 'Blackberry' == driver.find_element_by_xpath("//h4[@class='media-heading']/a").text

driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

# wait until the delivery location selection screen appears
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@class='btn btn-success btn-lg']")))

# enter 'india' and wait for the suggestion control to appear
driver.find_element_by_id('country').send_keys('india')

wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']//a[text()='India']")))

# click on the suggestion location - India
driver.find_element_by_xpath("//div[@class='suggestions']//a[text()='India']").click()

# click on the Terms and conditions check box
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

# click on Purchase
driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()

# wait until the text is shown
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='alert alert-success alert-dismissible']")))

alert_message = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you! Your order will be delivered in next few weeks" in alert_message

driver.get_screenshot_as_file("success_screen.png")

driver.quit()