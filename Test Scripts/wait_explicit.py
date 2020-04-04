from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

# ##############################
# chrome.implicitly_wait(10) #################
# ##############################

chrome.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Select and type 'ber' on the search input box
search = chrome.find_element_by_css_selector("input.search-keyword")
search.send_keys("ber")

# Click on Search button
search_button = chrome.find_element_by_css_selector("button.search-button")
search_button.click()

# wait for the results to get loaded
wait = WebDriverWait(chrome,8)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='products']/div[@class='product']")))

# verify the count of all products that are returned
products = chrome.find_elements_by_xpath("//div[@class='products']/div[@class='product']")
results_count = len(products)
assert results_count == 3

# Add each of the 3 products to the cart
product_names = []
product_buttons = chrome.find_elements_by_xpath("//div[@class='product-action']/button")
for button in product_buttons:
    product_names.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

# click on cart icon and click 'Proceed to checkout'
chrome.find_element_by_xpath("//a[@class='cart-icon']/img").click()
# time.sleep(1)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']")))

chrome.find_element_by_xpath("//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']").click()

# wait for checkout page
# time.sleep(2)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

# verify the added products are present in the checkout-form
checkout_products = []
checkout_list = chrome.find_elements_by_css_selector("p.product-name")
for each in checkout_list:
    checkout_products.append(each.text)

assert product_names == checkout_products
# enter promo code
chrome.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
chrome.find_element_by_class_name("promoBtn").click()

# Assert code applied!..
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
assert chrome.find_element_by_css_selector("span.promoInfo").text == "Code applied ..!"

