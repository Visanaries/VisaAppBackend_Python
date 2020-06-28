import requests
import json
import pymongo
from pymongo import MongoClient
import dns
import datetime

def getPayMerchant(amount, firstName, lastName, merchant):

    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    client = pymongo.MongoClient("mongodb+srv://AdiLaptop:asdAhagYHNUOzVmk@visanariesdb-942zb.mongodb.net/VisanariesDB?retryWrites=true&w=majority")
    db = client.main
    users = db.user
    merchants = db.merchant

    specificUser = users.find_one({"name": {"first": firstName, "last": lastName}})
    specificMerchant = merchants.find_one({"name": {"organizationName": merchant}})

    # If user does not exist - send string response
    if (not specificUser):
        return ("NO USER")
    # If user does not exist - send string response
    if (not specificMerchant):
        return ("NO MERCHANT")

    #coll.update_one({"_id":"102"},{"$set":{"city":"Visakhapatnam"}})

    # Handle Insufficient Funds
    if (int(amount) > specificUser["funds"]):
        return ("INSUFFICIENT FUNDS")

    # Update Accounts to Reflect Change in Funds
    newUserAmount = specificUser["funds"] - int(amount)
    users.update_one({"name": {"first": firstName, "last": lastName}}, {"$set": {"funds": newUserAmount}})
    newMerchantAmount = specificMerchant["funds"] + int(amount)
    merchants.update_one({"name": {"organizationName": merchant}}, {"$set": {"funds": newMerchantAmount}})

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
    "amount": "''' + amount + '''",
    "businessApplicationId": "MP",
    "cardAcceptor": {
    "address": {
    "city": "KOLKATA",
    "country": "IN"
    },
    "idCode": "CA-IDCode-77765",
    "name": "Visa Inc. USA-Foster City"
    },
    "localTransactionDateTime": "''' + date + '''",
    "purchaseIdentifier": {
    "type": "0",
    "referenceNumber": "REF_123456789123456789123"
    },
    "recipientPrimaryAccountNumber": "''' + specificMerchant["accountNumber"] + '''",
    "retrievalReferenceNumber": "412770451035",
    "secondaryId": "123TEST",
    "senderAccountNumber": "''' + specificUser["accountNumber"] + '''",
    "senderName": "''' + specificUser["name"]["first"] + specificUser["name"]["last"] + '''",
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
