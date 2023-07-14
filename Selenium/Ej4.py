"""
crear 10 elementos dándole a "add" en esta web
https://the-internet.herokuapp.com/add_remove_elements/
y luego borrarlos dándole a "delete"
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def add(wdrv, t):
    addbtn = wdrv.find_element(By.XPATH, '//*[@id="content"]/div/button')
    for i in range(t):
        addbtn.click()
        time.sleep(0.25)
    return


def remove(wdrv, t):
    for i in range(t):
        rmbtn = wdrv.find_element(By.XPATH, f'//*[@id="elements"]/button[{t - i}]')
        rmbtn.click()
        time.sleep(0.25)
    return


url = "https://the-internet.herokuapp.com/add_remove_elements/"

driver = webdriver.Edge()

driver.get(url)
try:
    add(driver, 10)
finally:
    time.sleep(2)
try:
    remove(driver, 10)
finally:
    time.sleep(2)
    driver.quit()
