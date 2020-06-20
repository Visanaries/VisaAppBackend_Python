import requests
import json

def getFundsTransferVisaCardDetails():

    url = "https://sandbox.api.visa.com/paai/fundstransferattinq/v5/cardattributes/fundstransferinquiry"
    certificate = "cert.pem"
    privateKey = "privateKey.pem"
    headers = {"Accept": "application/json"}
    user_id = "FJBIZAWDZAXKJ3X7B6GK21dL86tIkeBDG-Lppqraa6f07Scqg"
    password = "DZr64qXE3vdORl3m"
    body = {}
    payload = json.loads('''
    {
    "primaryAccountNumber": "4957030420210512",
    "retrievalReferenceNumber": "330000550000",
    "systemsTraceAuditNumber": "451006"
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
