"""
Imprimir por pantalla la temperatura en Madrid y añadir un mensaje indicando en cual de estas franjas está
franja 1:  < 25ºC
franja 2:  25ºC < x < 30ºC
franja 3:  > 30ºC
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

htemp = 30
ltemp = 25

try:
    driver.get("https://www.google.es/search?q=temperatura+en+madrid&sxsrf=AB5stBgjxoAHmcey-LNL34PGjQOEdRC0dQ%3A16885724"
               "47303&source=hp&ei=H5KlZMHqD_6qkdUP6Pq42A8&iflsig=AD69kcEAAAAAZKWgL1ELqUKq-CEfNjA9pBoCY01ap516&ved=0ahUK"
               "EwiB9pXH9vf_AhV-VaQEHWg9DvsQ4dUDCAs&uact=5&oq=temperatura+en+madrid&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDE"
               "IMBEEYQgAIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCE"
               "Cc6BAgjECc6BwgjEIoFECc6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoICAAQgAQQsQM6DgguEIAEELEDEMcBEK8BOgsILhCK"
               "BRCxAxCDAToLCAAQigUQsQMQgwE6BAgAEANQ_AFYsBFglBJoAXAAeACAAdIBiAGtFZIBBjUuMTMuM5gBAKABAbABCg&sclient=gws-wiz")
    temp = float(driver.find_element(By.ID, "wob_tm").text)
    if temp < ltemp:
        print("Hace frío.")
    elif temp > htemp:
        print("Hace calor.")
    else:
        print("Buena temperatura.")

finally:
    time.sleep(3)
    driver.close()



