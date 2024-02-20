from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

title = driver.title
assert title == "GreenKart - veg and fruits kart"

driver.implicitly_wait(0.5)

searchInput = driver.find_element(by=By.XPATH, value='//input[@type="search"]')
increment = driver.find_element(by=By.CSS_SELECTOR, value="a.increment")
quantityInput = driver.find_element(by=By.XPATH, value="//input[@type='number']")

searchInput.send_keys("Broco")

increment.click()

quantitySelected = quantityInput.get_attribute("value")

assert quantitySelected == '2'

button_add_product = driver.find_element(by=By.CSS_SELECTOR, value=".product-action button")
button_add_product.click()

button_cart = driver.find_element(by=By.CSS_SELECTOR, value='[alt="Cart"]')
button_cart.click()

button_proceed = driver.find_element(by=By.XPATH, value='//button[contains(text(), "PROCEED TO CHECKOUT")]')
button_proceed.click()

totalAmount = driver.find_element(by=By.CLASS_NAME, value='amount').text

assert totalAmount == "240"

driver.find_element(by=By.XPATH, value='//button[contains(text(),"Place Order")]').click()

checkAgree = driver.find_element(by=By.CSS_SELECTOR, value='.chkAgree')

checkAgree.click()

selectBox = driver.find_element(by=By.CSS_SELECTOR, value='#root > div > div > div > div > div > select')
select = Select(selectBox)
select.select_by_value("Spain")

# select_option = select.first_selected_option
# select_text = select_option.text
# print(select_text)

btnProceed = driver.find_element(by=By.XPATH, value='//button[contains(text(), "Proceed")]')
btnProceed.click()

driver.save_screenshot("pantalla_despues_proceed.png")
driver.quit()