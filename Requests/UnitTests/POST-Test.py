import requests
url = "https://mtp.alejmans.dev/maas/proxy/test/suma"

data = '{"a": 1, "b": 2}'

response = requests.post(url, data=data)
try:
    assert int(response.json()["result"]) == 3, "ERROR: El resultado no es 3."
#print("Estado:", response.status_code)
    print("Resultado: " + str(int(response.json()["result"])))
except AssertionError as e:
    print(e)
