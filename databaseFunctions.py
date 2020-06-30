import requests
import json
import pymongo
from pymongo import MongoClient
import dns

# Create new user account
def createUser(firstName, lastName, username, password, email):

    client = pymongo.MongoClient("mongodb+srv://AdiLaptop:asdAhagYHNUOzVmk@visanariesdb-942zb.mongodb.net/VisanariesDB?retryWrites=true&w=majority")
    db = client.main
    users = db.user

    x = users.insert_one({"name": {"first": firstName, "last": lastName}, "address": {"country": "", "county": "", "state": "", "zipCode": ""}, "userType": "Cardholder", "funds": 0, "accountNumber": "", "Username": username, "Password": password, "QRCode": "", "transactionHistory": []})

    # If user account is not created
    if (not x):
        return False

    return True

# Verify sign in credentials
def verifyCredentials(username, password):

    client = pymongo.MongoClient("mongodb+srv://AdiLaptop:asdAhagYHNUOzVmk@visanariesdb-942zb.mongodb.net/VisanariesDB?retryWrites=true&w=majority")
    db = client.main
    users = db.user

    specificUser = users.find_one({"Username": username, "Password": password})

    # If credentials do not match - return false
    if (not specificUser):
        return False

    return True
