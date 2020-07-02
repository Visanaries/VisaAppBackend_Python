import requests
import json
import pymongo
from pymongo import MongoClient
import dns
import datetime

def getPayMerchant(amount, username, password, merchant):

    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    client = pymongo.MongoClient("mongodb+srv://AdiLaptop:asdAhagYHNUOzVmk@visanariesdb-942zb.mongodb.net/VisanariesDB?retryWrites=true&w=majority")
    db = client.main
    users = db.user
    merchants = db.merchant

    specificUser = users.find_one({"Username": username, "Password": password})
    specificMerchant = merchants.find_one({"name": {"organizationName": merchant}})

    # If user does not exist - send string response
    if (not specificUser):
        return ("NO USER")
    # If user does not exist - send string response
    if (not specificMerchant):
        return ("NO MERCHANT")

    # Handle Insufficient Funds
    if (float(amount) > specificUser["funds"]):
        return ("INSUFFICIENT FUNDS")

    firstName = specificUser["name"]["first"]
    lastName = specificUser["name"]["last"]

    # Update Accounts to Reflect Change in Funds
    newUserAmount = specificUser["funds"] - float(amount)
    users.update_one({"name": {"first": firstName, "last": lastName}}, {"$set": {"funds": newUserAmount}})
    newMerchantAmount = specificMerchant["funds"] + float(amount)
    merchants.update_one({"name": {"organizationName": merchant}}, {"$set": {"funds": newMerchantAmount}})

    # Update Transaction History
    users.update_one({"name": {"first": firstName, "last": lastName}}, {"$push": {"transactionHistory": {"name": merchant, "amount": float(amount)}}})

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

def getPayCardholder(amount, username, password, recipient):

    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    client = pymongo.MongoClient("mongodb+srv://AdiLaptop:asdAhagYHNUOzVmk@visanariesdb-942zb.mongodb.net/VisanariesDB?retryWrites=true&w=majority")
    db = client.main
    users = db.user

    specificUser = users.find_one({"Username": username, "Password": password})
    specificRecipient = users.find_one({"Username": recipient})

    # If user does not exist - send string response
    if (not specificUser):
        return ("NO USER")
    # If recipient cardholder does not exist - send string response
    if (not specificRecipient):
        return ("NO RECIPIENT")

    # Handle Insufficient Funds
    if (float(amount) > specificUser["funds"]):
        return ("INSUFFICIENT FUNDS")

    firstName = specificUser["name"]["first"]
    lastName = specificUser["name"]["last"]

    # Update Accounts to Reflect Change in Funds
    newUserAmount = specificUser["funds"] - float(amount)
    users.update_one({"name": {"first": firstName, "last": lastName}}, {"$set": {"funds": newUserAmount}})
    newRecipientAmount = specificRecipient["funds"] + float(amount)
    users.update_one({"Username": recipient}, {"$set": {"funds": newRecipientAmount}})

    # Update Transaction History
    users.update_one({"name": {"first": firstName, "last": lastName}}, {"$push": {"transactionHistory": {"name": recipient, "amount": float(amount)}}})

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
    "recipientPrimaryAccountNumber": "''' + specificRecipient["accountNumber"] + '''",
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
