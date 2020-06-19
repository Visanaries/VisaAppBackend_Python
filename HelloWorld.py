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

r = requests.get(url, 
                cert = (certificate, privateKey),
                headers = headers,
                auth = (user_id, password),
                #data = body,
                json = payload,
                timeout = timeout)

print(r.text)
