import requests
url = "https://mtp.alejmans.dev/maas/proxy/test/suma"

headers = {'User-Agent': 'PostmanRuntime/7.28.4',
           'Content-Type': 'application/json'}

data = '{"a": 1, "b": 2}'

response = requests.post(url, headers=headers, data=data)
try:
    assert int(response.json()["result"]) == 3, "El resultado no es 3."
    print("Estado:", response.status_code)
    print("Resultado: " + str(int(response.json()["result"])))
except AssertionError as e:
    print(e)
