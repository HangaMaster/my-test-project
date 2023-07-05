import requests

url = "https://mtp.alejmans.dev/maas/proxy/test/suma"
params = {
    "a": 1,
    "b": 2,
}

response = requests.get(url, params=params)
try:
    assert int(response.json()) == 3, "El resultado no es 3."
    #print("Estado:", response.status_code)
    print("Resultado:", int(response.json()))
except AssertionError as e:
    print(e)
