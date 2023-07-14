from behave import *
import requests

url = "https://mtp.alejmans.dev/maas/proxy/test/suma"
params = {
    "a": 2,
    "b": 1,
}


@given("Launch GET method")
def step_impl(context):
    context.response = float(requests.get(url, params=params).text)


@when("Check if data is received")
def step_impl(context):
    try:
        assert context.response is not ""
    except:
        raise AssertionError("No se han recibido datos.")


@then("Check if sum is correct")
def step_impl(context):
    try:
        assert float(context.response.json()) == 3
    except:
        raise AssertionError("El resultado no es 3.")
