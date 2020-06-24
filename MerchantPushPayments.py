import requests
import json

def getPayMerchant():

    url = "https://sandbox.api.visa.com/visadirect/mvisa/v1/merchantpushpayments"
    certificate = "cert.pem"
    privateKey = "privateKey.pem"
    headers = {"Accept": "application/json"}
    user_id = "FJBIZAWDZAXKJ3X7B6GK21dL86tIkeBDG-Lppqraa6f07Scqg"
    password = "DZr64qXE3vdORl3m"
    body = {}
    payload = json.loads('''   
    {
    "acquirerCountryCode": "356",
    "acquiringBin": "408972",
    "amount": "124.05",
    "businessApplicationId": "MP",
    "cardAcceptor": {
    "address": {
    "city": "KOLKATA",
    "country": "IN"
    },
    "idCode": "CA-IDCode-77765",
    "name": "Visa Inc. USA-Foster City"
    },
    "localTransactionDateTime": "2020-06-24T07:01:55",
    "purchaseIdentifier": {
    "type": "0",
    "referenceNumber": "REF_123456789123456789123"
    },
    "recipientPrimaryAccountNumber": "4123640062698797",
    "retrievalReferenceNumber": "412770451035",
    "secondaryId": "123TEST",
    "senderAccountNumber": "4027290077881587",
    "senderName": "Jasper",
    "senderReference": "",
    "systemsTraceAuditNumber": "451035",
    "transactionCurrencyCode": "356",
    "merchantCategoryCode": "5812",
    "settlementServiceIndicator": "9"
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
