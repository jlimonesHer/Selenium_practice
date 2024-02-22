from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
import time

class InputModel:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.open_website()
        self.driver.implicitly_wait(0.5)

    def open_website(self):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    
    def radio_button(self, option):
        """Este metodo elige un radio_button dependiendo de la opcin pasada

        Args:
            option (int): opcion que va a elegir si existe
        """
        if option == 1:
            radio_button = self.driver.find_element(By.XPATH, '//input[@value="radio1"]')
        elif option == 2:
            radio_button = self.driver.find_element(By.XPATH, '//input[@value="radio2"]')
        elif option == 3:
            radio_button = self.driver.find_element(By.XPATH, '//input[@value="radio3"]')
        else:
            return
        radio_button.click()

    def suggessionClass(self, country):
        inputSugesstion = self.driver.find_element(by=By.ID, value='autocomplete')
        inputSugesstion.send_keys(country)

    def selectExample(self, option):
        inputSelect = self.driver.find_element(by=By.ID, value='dropdown-class-example')
        select = Select(inputSelect)
        if option == 1:
            optionString = "option1"
        elif option == 2:
            optionString = "option2"
        elif option == 3:
            optionString = "option3"
        else:
            return
        select.select_by_value(optionString)

    def checkbox(self, options):
        """Marcara las casillas pasadas por parametros

        Args:
            options (array): Recibe un array de boolenaos.
        """
        checkbox_option1 = self.driver.find_element(By.ID, "checkBoxOption1")
        checkbox_option2 = self.driver.find_element(By.ID, "checkBoxOption2")
        checkbox_option3 = self.driver.find_element(By.ID, "checkBoxOption3")
        checks = (checkbox_option1, checkbox_option2, checkbox_option3)
        for index in range(len(checks)):
            if options[index]:
                checks[index].click()

    def open_window(self):
        """Este método simplemente hace click en el boton, abre la nueva ventana y cambia el foco de una ventana a otra.
        los tiempos de espera los dejamos para ver su funcionamiento.
        """
        button = self.driver.find_element(by=By.ID, value="openwindow")
        button.click()
        time.sleep(1)
        handles = self.driver.window_handles
        time.sleep(1)
        new_window = handles[-1]
        time.sleep(1)
        self.driver.switch_to.window(new_window)
        time.sleep(1)

        # Realizar acciones en la nueva ventana (si es necesario)
        # ...

        # Cerrar ventana actual
        self.driver.close()
        # Regresar a la ventana principal
        self.driver.switch_to.window(handles[0])

    def open_tab(self):
        """Este método simplemente hace click en el boton, abre la nueva pestaña y cambia el foco de una pestaña a otra.
        los tiempos de espera los dejamos para ver su funcionamiento.
        """
        button = self.driver.find_element(by=By.ID, value="opentab")
        button.click()
        time.sleep(1)
        handles = self.driver.window_handles
        time.sleep(1)
        new_tab = handles[-1]
        time.sleep(1)
        self.driver.switch_to.window(new_tab)
        time.sleep(1)

        # Realizar acciones en la nueva pestaña (si es necesario)
        # ...

        # Cerrar pestaña actual
        self.driver.close()

        # Regresar a la pestaña principal
        self.driver.switch_to.window(handles[0])
         
    def read_table(self):
        """Esta función Lee y muestra todos los datos de la primera tabla.
        """
        table = self.driver.find_element(by=By.NAME, value='courses')
        rows = self.driver.find_elements(by=By.XPATH, value='//*[@name="courses"]/tbody/tr')
        for row in rows:
            print(row.text)

            
form = InputModel()

options = (True, False, True)

form.radio_button(3)

form.suggessionClass("España")

form.selectExample(2)

form.checkbox(options)

form.open_window()

form.open_tab()

form.read_table()

time.sleep(2)
form.driver.quit()

    