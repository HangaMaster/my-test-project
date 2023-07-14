import time
from selenium.common import NoAlertPresentException
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""
Se puede usar la librería "velenium" para localizar elementos a partir de imágenes y pulsarlos
"""

driver = webdriver.Edge()

url = "https://the-internet.herokuapp.com/context_menu"
# Opción integrada en Selenium.
try:
    driver.get(url)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID, "hot-spot"))
    action.context_click().perform()
    driver.switch_to.alert.accept()
except NoAlertPresentException:
    print("ERROR: No hay alerta.")
finally:
    time.sleep(3)
#   driver.save_screenshot("1.png")  Para hacer capturas de pantalla.
    driver.quit()
# Opción con JS.
# try:
#     driver.get(url)
#     driver.find_element(By.ID, "hot-spot")
#     driver.execute_script('$("#myId").mousedown(function(ev){if (ev.which == 3){alert("Right mouse button clicked on element with id myId");}});')
#     driver.switch_to.alert.accept()
# except NoAlertPresentException:
#     print("ERROR: No hay alerta.")
# finally:
#     time.sleep(3)
#     driver.quit()
