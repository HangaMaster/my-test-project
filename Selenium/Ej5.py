"""
Hacer hover en un usuario y entrar en su perfil.
"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
url = "https://the-internet.herokuapp.com/hovers"

driver.get(url)

action = ActionChains(driver)

hover = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(4) > img")
action.move_to_element(hover).perform()
menu = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(4) > div > a")
action.move_to_element(menu).perform()

menu.click()

time.sleep(10)
driver.quit()
