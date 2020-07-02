import json

import pymongo
import requests


def getFundsTransferVisaCardDetails(firstName, lastName):
    client = pymongo.MongoClient(
        "mongodb+srv://AdiLaptop:asdAhagYHNUOzVmk@visanariesdb-942zb.mongodb.net/VisanariesDB?retryWrites=true&w=majority")
    db = client.main
    users = db.user

    specificUser = users.find_one({"name": {"first": firstName, "last": lastName}})

    # If user does not exist - send None as response
    if (not specificUser):
        return None

    url = "https://sandbox.api.visa.com/paai/fundstransferattinq/v5/cardattributes/fundstransferinquiry"
    certificate = "cert.pem"
    privateKey = "privateKey.pem"
    headers = {"Accept": "application/json"}
    user_id = "FJBIZAWDZAXKJ3X7B6GK21dL86tIkeBDG-Lppqraa6f07Scqg"
    password = "DZr64qXE3vdORl3m"
    body = {}
    payload = json.loads('''
    {
    "primaryAccountNumber": "''' + specificUser["accountNumber"] + '''",
    "retrievalReferenceNumber": "330000550000",
    "systemsTraceAuditNumber": "451006"
    }
    ''')
    timeout = 10

    response = requests.post(url,
                             cert=(certificate, privateKey),
                             headers=headers,
                             auth=(user_id, password),
                             # data = body,
                             json=payload,
                             timeout=timeout)

    data = response.json()
    return data
