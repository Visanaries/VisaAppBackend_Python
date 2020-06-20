import requests
import json
import datetime

def getVisaWaitTimes():
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    url = "https://sandbox.api.visa.com/visaqueueinsights/v1/queueinsights"
    certificate = "cert.pem"
    privateKey = "privateKey.pem"
    headers = {"Accept": "application/json"}
    user_id = "FJBIZAWDZAXKJ3X7B6GK21dL86tIkeBDG-Lppqraa6f07Scqg"
    password = "DZr64qXE3vdORl3m"
    body = {}
    payload = json.loads('''
    {
    "requestHeader": {
    "messageDateTime": "2020-06-20T19:45:22.327",
    "requestMessageId": "6da60e1b8b024532a2e0eacb1af58581"
    },
    "requestData": {
    "kind": "predict"
    }
    }
    ''')
    timeout = 10

    response = requests.post(url, 
                    cert = (certificate, privateKey),
                    headers = headers,
                    auth = (user_id, password),
                    #data = body,
                    json = payload,
                    timeout = timeout)
    
    data = response.json()
    return data
