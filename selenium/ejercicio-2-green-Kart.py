from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image
import time

class GreenKartTest:
    """Es una clase que testea  como realizar una compra en la web de parctica.
    """
    def __init__(self):
        """
        Constructor de la clase.\n
        self.driver = webdriver.Chrome() -> inicializa un objeto d la clase webdriver.\n
        self.open_website() -> Abre el navegador.\n
        self.searchInput -> Guarda el input del buscador de la web.\n
        """
        self.driver = webdriver.Chrome()
        self.open_website()
        self.searchInput = self.driver.find_element(by=By.XPATH, value='//input[@type="search"]')       

    def open_website(self):
        """Abre el sitio web para las pruebas.\n
        Establece el tiempo de espera para la carga de la página.
        """
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.implicitly_wait(0.5)

    def delete_text(self):
        """Elimina el texto del input del buscador de productos\n
        """
        self.searchInput.clear()

    def search_product(self, product):
        """Inserta el nombre del producto deseado en el buscador de productos.\n

        Args:
            product (string): Recibe el nombre del producto.\n
        """
        self.searchInput.send_keys(product)

    def add_unit(self, number):
        """Añade una cantidad del producto seleccionado.

        Args:
            number (int): Recibe un entero que determina el numero de unidades del producto
        """
        quantitySelected = 1
        while quantitySelected != number:
            quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
            increment = self.driver.find_element(by=By.CSS_SELECTOR, value="a.increment")
            increment.click()
            quantitySelected = int(quantityInput.get_attribute("value"))
        time.sleep(0.2)
        self.add_cart()
       

    def subtract_unit(self):
        """Resta una unidad del producto al total antyes de añadirlo a la cesta.\n
        """
        quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
        quantitySelected = int(quantityInput.get_attribute("value"))

        while quantitySelected != 1:
            quantityInput = green.driver.find_element(by=By.XPATH, value="//input[@type='number']")
            quantitySelected = int(quantityInput.get_attribute("value"))
            decrement = self.driver.find_element(by=By.CSS_SELECTOR, value="a.decrement")
            decrement.click()
        time.sleep(0.2)

    def add_cart(self):
        """Añade el total de unidades de un producto a la cesta.\n
        """
        button_add_product = self.driver.find_element(by=By.CSS_SELECTOR, value=".product-action button")
        button_add_product.click()

    def complet_buy(self):
        """Completa la compra aceptando la lista final de productos.\n
        Selecciona el pais y acepta terminos y condiciones.\n
        """
        button_cart = self.driver.find_element(by=By.CSS_SELECTOR, value='[alt="Cart"]')
        button_cart.click()

        button_proceed = self.driver.find_element(by=By.XPATH, value='//button[contains(text(), "PROCEED TO CHECKOUT")]')
        button_proceed.click()

        totalAmount = self.driver.find_element(by=By.CLASS_NAME, value='amount').text

        assert totalAmount != 0
        self.driver.save_screenshot("resumen_cuenta.png")
        placeOrder = self.driver.find_element(by=By.XPATH, value='//button[contains(text(),"Place Order")]')
        placeOrder.click()
        checkAgree = self.driver.find_element(by=By.CSS_SELECTOR, value='.chkAgree')

        checkAgree.click()

        selectBox = self.driver.find_element(by=By.CSS_SELECTOR, value='#root > div > div > div > div > div > select')
        select = Select(selectBox)
        select.select_by_value("Spain")
        btnProceed = self.driver.find_element(by=By.XPATH, value='//button[contains(text(), "Proceed")]')
        btnProceed.click()

        self.driver.save_screenshot("pantalla_despues_proceed.png")

    def complete_process(self, products):
        """Hace el proceso completo de compra.\n

        Args:
            products (dictionary): recibe un diccionario en el que la clave es el numero del producto y el valor la cantidad deseada.\n
        """
        for product, amount in products.items():
            self.driver.implicitly_wait(0.5)
            self.search_product(product)
            time.sleep(1)
            self.add_unit(amount)
           
            time.sleep(1)
            self.delete_text()
            time.sleep(1)
        self.complet_buy()


green = GreenKartTest()
green.driver.implicitly_wait(0.5)

products = {
    "Brocolli": 3,
    "Potato": 4, 
    "Tomato": 5, 
    }

green.complete_process(products)

green.driver.quit()