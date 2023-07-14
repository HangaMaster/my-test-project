"""
Marcar los checks de esta url https://the-internet.herokuapp.com/checkboxes con el resultado de hacer una petición GET a
esta otra url: https://mtp.alejmans.dev/maas/proxy/test/checkbox . true => debe estar marcado,
false ≥ debe estar desmarcado.
"""
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()

url1 = "https://mtp.alejmans.dev/maas/proxy/test/checkbox"
url2 = "https://the-internet.herokuapp.com/checkboxes"
response = requests.get(url1)

c1 = (response.json()["checkbox 1"])
c2 = (response.json()["checkbox 2"])

print("La casilla 1 estará en:", c1, "\nLa casilla 2 estará en:", c2)

try:
    driver.get(url2)
    cb1 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
    cb2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")
    if c1 != cb1.is_selected():
        cb1.click()
    if c2 != cb2.is_selected():
        cb2.click()
finally:
    time.sleep(5)
    driver.quit()

