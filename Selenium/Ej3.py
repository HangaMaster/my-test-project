"""
Dada la primera tabla de la URL: https://the-internet.herokuapp.com/tables
Imprimir por pantalla las filas con más de valor 50 en el campo Due.
"""
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/tables"


# Con la función a continuación lo que hemos hecho es reutilizar la misma sentencia en diferentes puntos, economizando
# código.
def get_values(wdrv, row):
    cell = wdrv.find_element(By.CSS_SELECTOR, f"#table1 > tbody > tr:nth-child({row}) > td:nth-child(4)")
    cell_text = cell.text
    return int(cell_text.split(".")[0].lstrip("$"))


def get_persons(wdrv, row):
    cell = wdrv.find_element(By.CSS_SELECTOR, f"#table1 > tbody > tr:nth-child({row}) > td:nth-child(4)")
    cell_text = cell.text
    return cell_text
# En la función de arriba, podemos utilizar variables dentro de una frase literal, indicando una "f" al principio fuera
# de las comillas y luego dentro con unos corchetes la variable que queremos utilizar.


driver = webdriver.Edge()

try:
    driver.get(url)
    table = [
        get_values(driver, 1),
        get_values(driver, 2),
        get_values(driver, 3),
        get_values(driver, 4),
    ]

    rows = []
    for i in enumerate(table):
        if table[i] > 50:
            rows.append(1)

    persons = [
        get_persons(driver, 1),
        get_persons(driver, 2),
        get_persons(driver, 3),
        get_persons(driver, 4),
    ]

finally:
    driver.quit()

for table in rows:
    print()
