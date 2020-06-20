import requests
import json

url = "https://sandbox.api.visa.com/vdp/helloworld"
certificate = "cert.pem"
privateKey = "privateKey.pem"
headers = {}
user_id = "FJBIZAWDZAXKJ3X7B6GK21dL86tIkeBDG-Lppqraa6f07Scqg"
password = "DZr64qXE3vdORl3m"
body = {}
payload = json.loads('''{}''')
timeout = 10

# How to get response from HelloWorld API from Visa
r = requests.get(url, 
                cert = (certificate, privateKey),
                headers = headers,
                auth = (user_id, password),
                #data = body,
                json = payload,
                timeout = timeout)

# Print text of response from Visa API
print(r.text)

# Example - How to get response from Pokemon API
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
# How to turn response into JSON
data = response.json()
# Print specific value from a specified key from JSON in data
print(data["name"])
# Print entire JSON
print(data)
