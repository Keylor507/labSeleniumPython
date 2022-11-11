from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Establecer el navegador y sitio web
driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

# Seleccionar barra de busqueda e introducir texto
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("HP Pavilion azul")
driver.find_element(By.ID, "nav-search-submit-button").click()
# Tambien podemos agregar '+ Keys.ENTER' al final de la entrada de texto para hacer submit

# Seleccionar el primer resultado mediante la imagen, Selenium selecciona la primera instancia por defecto
driver.find_element(By.CLASS_NAME, "s-image").click()

# Cambiar la cantidad a 2, donde "1" es indice 0 y "2" es indice 1
miSeleccion = Select(driver.find_element(By.ID, "quantity"))
miSeleccion.select_by_index(1)

# Agregar al carrito y verificar su contenido
driver.find_element(By.ID, "add-to-cart-button").click()
driver.find_element(By.CLASS_NAME, "a-button-text").click()

# Finalizar la secuencia
time.sleep(100)
driver.close()