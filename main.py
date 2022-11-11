from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("HP Pavilion azul")
driver.find_element(By.ID, "nav-search-submit-button").click()

driver.find_element(By.CLASS_NAME, "s-image").click()

seleccion = Select(driver.find_element(By.ID, "quantity"))
seleccion.select_by_index(1)

driver.find_element(By.ID, "add-to-cart-button").click()
driver.find_element(By.CLASS_NAME, "a-button-text").click()

time.sleep(100)
driver.close()
