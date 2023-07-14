from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver


url = "https://the-internet.herokuapp.com/login"


@given('el usuario está registrado')  # Aquí se puede hacer una búsqueda en bd y comprobar que está registrado.
def step_impl(context):
    pass


@when('cuando introduce un nombre de usuario')
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.get(url)
    context.driver.find_element(By.ID, "username").send_keys("tomsmith")


@when('cuando introduce su password')
def step_impl(context):
    context.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")


@when('el usuario pulsa el botón de "Login"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#login > button").click()


@then('el usuario accede al portal')  # Aquí se localiza algo que esté en la web como resultado OK.
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "#flash").is_displayed()
    context.driver.quit()
    