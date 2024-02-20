from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image
import time

class GreenKartTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.open_website()
        self.searchInput = self.driver.find_element(by=By.XPATH, value='//input[@type="search"]')       

    def open_website(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.implicitly_wait(0.5)

    def delete_text(self):
        self.searchInput.clear()

    def search_product(self, product):
        self.searchInput.send_keys(product)

    def add_unit(self, number):
        quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
        quantitySelected = int(quantityInput.get_attribute("value"))
        while quantitySelected < number - 1:
            quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
            quantitySelected = int(quantityInput.get_attribute("value"))
            increment = self.driver.find_element(by=By.CSS_SELECTOR, value="a.increment")
            increment.click()
            time.sleep(0.2)

    def subtract_unit(self, number):
        quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
        quantitySelected = int(quantityInput.get_attribute("value"))
        print(quantitySelected)
        while quantitySelected > number + 1:
            quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
            quantitySelected = int(quantityInput.get_attribute("value"))
            decrement = self.driver.find_element(by=By.CSS_SELECTOR, value="a.decrement")
            decrement.click()
            time.sleep(0.2)

    def add_cart(self):
        button_add_product = self.driver.find_element(by=By.CSS_SELECTOR, value=".product-action button")
        button_add_product.click()

    



green = GreenKartTest()
green.driver.implicitly_wait(0.5)

green.search_product("Potato")
green.add_unit(10)
quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
quantitySelected = quantityInput.get_attribute("value")
green.subtract_unit(5)
quantitySelected = quantityInput.get_attribute("value")
print(f"Potatos = {quantitySelected}")
green.add_cart()

time.sleep(2)
green.delete_text()

green.search_product("Broco")
time.sleep(2)
quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
quantitySelected = quantityInput.get_attribute("value")
print(quantitySelected)
green.add_unit(10)
quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
quantitySelected = quantityInput.get_attribute("value")
print(quantitySelected)
green.subtract_unit(5)
quantitySelected = quantityInput.get_attribute("value")
print(f"Brocoli = {quantitySelected}")
green.add_cart()


green.driver.quit()