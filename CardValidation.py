import requests
import json

def getVisaCardValidation():

    url = "https://sandbox.api.visa.com/pav/v1/cardvalidation"
    certificate = "cert.pem"
    privateKey = "privateKey.pem"
    headers = {"Accept": "application/json"}
    user_id = "FJBIZAWDZAXKJ3X7B6GK21dL86tIkeBDG-Lppqraa6f07Scqg"
    password = "DZr64qXE3vdORl3m"
    body = {}
    payload = json.loads('''
    {
    "addressVerificationResults": {
    "postalCode": "T4B 3G5",
    "street": "2881 Main Street Sw"
    },
    "cardAcceptor": {
    "address": {
    "city": "Foster City",
    "country": "United States",
    "county": "CA",
    "state": "CA",
    "zipCode": "94404"
    },
    "idCode": "111111",
    "name": "Rohan",
    "terminalId": "123"
    },
    "cardCvv2Value": "672",
    "cardExpiryDate": "2020-07",
    "primaryAccountNumber": "4957030000313108",
    "retrievalReferenceNumber": "015221743720",
    "systemsTraceAuditNumber": "743720"
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
