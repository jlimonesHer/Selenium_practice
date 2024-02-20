# Primer Proyecto Selenium
--------------

[//]: # (version: 1.0)
[//]: # (author: Jose Carlos Limones)
[//]: # (date: 2020-10-10)



# Tabla de contenidos
- [Primer Proyecto Selenium](#primer-proyecto-selenium)
- [Tabla de contenidos](#tabla-de-contenidos)
  - [Introducción](#introducción)
  - [Empiezo el proyecto creando un entorno virtual de python:](#empiezo-el-proyecto-creando-un-entorno-virtual-de-python)
    - [Importe la libreria](#importe-la-libreria)
    - [Inicie la sesion:](#inicie-la-sesion)
    - [URL a la que queremos ir](#url-a-la-que-queremos-ir)
    - [Solicita informacion al navegador](#solicita-informacion-al-navegador)
    - [Imprima resultado](#imprima-resultado)
    - [Cerrar el navegador y finalizar la sesión de WebDriver.](#cerrar-el-navegador-y-finalizar-la-sesión-de-webdriver)
    - [Establecer estrategia de espera](#establecer-estrategia-de-espera)
    - [Encuentra el elemento](#encuentra-el-elemento)
    - [Realice acciones sobre el elemento](#realice-acciones-sobre-el-elemento)
    - [Solicitar infomacion de un elemento](#solicitar-infomacion-de-un-elemento)
    - [Ejemplo](#ejemplo)
    - [Capturas de Pantalla](#capturas-de-pantalla)

## Introducción
[Tabla de contenidos](#tabla-de-contenidos)

> [!NOTE]
> En este ejercicio vamos a practicar con selenium y  la página de practica [GreenKart](https://rahulshettyacademy.com/seleniumPractise/#/). Simularemos la compra de un producto utilizando esta libreria.

## Empiezo el proyecto creando un entorno virtual de python:
[Tabla de contenidos](#tabla-de-contenidos)

```bash
# Crea un entorno virtual
python3 -m venv venv

# Activa el entorno virtual (Linux/macOS)
source venv/bin/activate
```

- Creamos nuestro primer script:
```python
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
print(title)
driver.quit()
```
### Importe la libreria
```python
from selenium import webdriver
```

### Inicie la sesion:
```python
driver = webdriver.Chrome()
```
### URL a la que queremos ir
```python
driver.get("https://github.com/jlimonesHer")
```
### Solicita informacion al navegador
  - Hay muchos tipos de información sobre el navegador que puede solicitar, incluidos identificadores de ventanas, tamaño/posición del navegador, cookies, alertas, etc
```python
title = driver.title
```
### Imprima resultado
```python
print(title)
```
### Cerrar el navegador y finalizar la sesión de WebDriver.
```python
driver.quit()
```

### Establecer estrategia de espera
- La función driver.implicitly_wait(t) en Selenium establece un tiempo de espera implícito para la búsqueda de elementos. Este tiempo de espera se aplica de manera global a todas las búsquedas de elementos realizadas por el WebDriver.

- La función toma un argumento t, que es el tiempo de espera en segundos. En tu ejemplo, driver.implicitly_wait(0.5) significa que Selenium esperará hasta 0.5 segundos antes de lanzar una excepción si no puede encontrar un elemento inmediatamente. Esto es útil para manejar situaciones en las que los elementos tardan un poco en cargarse después de que la página se ha cargado.

```python
driver.implicitly_wait(0.5)
```

### Encuentra el elemento
- La mayoria de las sesiones de Selenium estan relacionados con elementos y debes encontrarlo para ello:
```python
from selenium.webdriver.common.by import By 

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
```
- ID:
```python
By.ID
```
- Name:

```python
By.NAME
```
- Class name:

```python
By.CLASS_NAME
```
- Tag name:

```python
By.TAG_NAME
```
- Link text:

```python
By.LINK_TEXT
```
- Partial link text:

```python
By.PARTIAL_LINK_TEXT
```
- CSS selector:

```python
By.CSS_SELECTOR
```
- XPath:

```python
By.XPATH
```
- Estas estrategias se utilizan con el método find_element de la clase WebDriver para localizar elementos en la página web. Por ejemplo, para encontrar un elemento por su ID, puedes usar:

```python
element = driver.find_element(By.ID, "mi_id")
```
- O para encontrar un elemento por su nombre, puedes usar:

```python
element = driver.find_element(By.NAME, "mi_nombre")
```
- 

### Realice acciones sobre el elemento

```python
text_box.send_keys("Selenium")
submit_button.click()
```

### Solicitar infomacion de un elemento
```python
text = message.text
```

### Ejemplo
[Tabla de contenidos](#tabla-de-contenidos)

- Importamos dependencias:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
```

- Probamos que es la pagina deseada:
```python
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
title = driver.title
assert title == "GreenKart - veg and fruits kart"
```
- Asignamos el tiempo de espera
```python
driver.implicitly_wait(0.5)
```
- Guardamos cada elemento encontrandolos por sus atributos:
```python
searchInput = driver.find_element(by=By.XPATH, value='//input[@type="search"]')
increment = driver.find_element(by=By.CSS_SELECTOR, value="a.increment")
quantityInput = driver.find_element(by=By.XPATH, value="//input[@type='number']")
```
- En el buscador insertamos la palabra deseada:
```python
searchInput.send_keys("Broco")
```
- Hacemos click en el boton de incrementar:
```python
increment.click()
```
- Recogemos el valor del contador y lo comprobamos:
```python
quantitySelected = quantityInput.get_attribute("value")

assert quantitySelected == '2'
```
- Guardamos y hacemos click ne el desplegable del carrito
```python
button_add_product = driver.find_element(by=By.CSS_SELECTOR, value=".product-action button")
button_add_product.click()
```
- Guardamos y hacemos click en el boton de proceed
```python
button_proceed = driver.find_element(by=By.XPATH, value='//button[contains(text(), "PROCEED TO CHECKOUT")]')
button_proceed.click()
```
- Comprobamos que el total de la compra es el correcto
```python
totalAmount = driver.find_element(by=By.CLASS_NAME, value='amount').text

assert totalAmount == "240"
```
- Aceptamos la orden:
```python
checkAgree = driver.find_element(by=By.CSS_SELECTOR, value='.chkAgree')

checkAgree.click()
```
- Con la clase Select modificamos el campo select, hay que importar la clase:
```python
from selenium.webdriver.support.ui import Select

selectCountry = driver.find_element(by=By.CSS_SELECTOR, value='#root > div > div > div > div > div > select')
select = Select(selectCountry)
select.select_by_value("Spain")
```
- Mostrar la opcion seleccionada
```python
select_option = select.first_selected_option
select_text = select_option.text
print(select_text)
```
- Pulsamos el boton de realizar compra:
```python
btnProceed = driver.find_element(by=By.XPATH, value='//button[contains(text(), "Proceed")]')
btnProceed.click()
```
### Capturas de Pantalla
[Tabla de contenidos](#tabla-de-contenidos)

- Debemos intalar Pillow para selenium
```python
pip install selenium Pillow
```

- Despues importamos la libreria
```python
from PIL import Image
```
- Ejecutamos la funcion save_screenshot("nombre_captura"):
```python
driver.save_screenshot("pantalla_despues_proceed.png")
```

