import time

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

use_step_matcher('re')

url = "https://the-internet.herokuapp.com/javascript_alerts"

driver = webdriver.Edge()


@Given("navegar a la url")
def step_impl(context):
    driver.get(url)


@When("pulsar en el primer boton")
def step_impl(context):
    driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button").click()


@When("pulsar en aceptar")
def step_impl(context):
    try:
        time.sleep(1)
        popup = driver.switch_to.alert
        popup.accept()

    except TimeoutException:
        print("No hay alerta.")


@Then("comprobar que se ha aceptado")
def step_impl(context):
    try:
        context.result = driver.find_element(By.CSS_SELECTOR, "#result").text
        assert context.result == "You successfully clicked an alert"
    except:
        raise AssertionError("Mensaje no esperado.")


@When("pulsar en el segundo boton")
def step_impl(context):
    driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button").click()


@When("comprobar que se ha confirmado")
def step_impl(context):
    try:
        context.result = driver.find_element(By.CSS_SELECTOR, "#result").text
        assert context.result == "You clicked: Ok"
    except:
        raise AssertionError("Mensaje no esperado.")


@When("pulsar en cancelar")
def step_impl(context):
    try:
        time.sleep(0.5)
        context.popup = driver.switch_to.alert
        context.popup.dismiss()

    except TimeoutException:
        print("No hay alerta.")


@Then("comprobar que se ha cancelado")
def step_impl(context):
    try:
        context.result = driver.find_element(By.CSS_SELECTOR, "#result").text
        assert context.result == "You clicked: Cancel"
    except:
        raise AssertionError("Mensaje no esperado.")


@When("pulsar en el tercer boton")
def step_impl(context):
    driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(3) > button").click()


@When('Introducir el texto "(?P<texto>.+)"')
def step_impl(context, texto):
    try:
        time.sleep(1)
        popup = driver.switch_to.alert
        popup.send_keys(texto)
        popup.accept()
    except:
        raise AssertionError("No hay alerta.")


@Then("comprobar que el texto pone '(?P<texto>.+)'")
def step_impl(context, texto):
    try:
        context.result = driver.find_element(By.CSS_SELECTOR, "#result").text
        assert context.result == "You entered: " + texto
    except:
        raise AssertionError("Mensaje no esperado.")
