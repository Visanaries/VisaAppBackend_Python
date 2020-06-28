import requests
from flask import Flask, jsonify, request
import json
import datetime
from QueueInsightsService import getVisaWaitTimes
from GeneralAttributesInquiry import getGeneralVisaCardDetails
from FundsTransferInquiry import getFundsTransferVisaCardDetails
from CardValidation import getVisaCardValidation
from MerchantPushPayments import getPayMerchant

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if (request.method == "GET"):
        return jsonify({"default message": "Hello World!"})
    elif (request.method == "POST"):
        json_received = request.get_json()
        return jsonify({"your message": json_received}), 201

@app.route("/multiply/<int:num1>/<int:num2>", methods = ["GET"])
def multiply(num1, num2):
    return jsonify({"Product": num1 * num2})

# Find merchants and their wait times
@app.route("/merchantWaitTimes", methods = ["GET"])
def getWaitTimes():
    data = getVisaWaitTimes()
    return data

# Find general card details (must provide Account Number)
# ToDo: Send specific card numbers for each person
@app.route("/generalCardDetails/<string:firstName>/<string:lastName>", methods = ["GET"])
def getGeneralCardDetails(firstName, lastName):
    data = getGeneralVisaCardDetails(firstName, lastName)
    if (data == None):
        return jsonify({"Error": "No such object exists in the database"}), 404
    else:
        return data

# Find card details pertaining to funds transfers (must provide Account Number, reference number, system trace audit number)
# ToDo: Send specific info for each person
@app.route("/fundsTransferCardDetails/<string:firstName>/<string:lastName>", methods = ["GET"])
def getFundsTransferCardDetails(firstName, lastName):
    data = getFundsTransferVisaCardDetails(firstName, lastName)
    if (data == None):
        return jsonify({"Error": "No such object exists in the database"}), 404
    else:
        return data

# Find out if a card is valid before payments/transactions
# ToDo: Populate information in body before HTTP request is sent 
@app.route("/cardValidation/<string:firstName>/<string:lastName>", methods = ["GET"])
def getCardValidation(firstName, lastName):
    data = getVisaCardValidation(firstName, lastName)
    if (data == None):
        return jsonify({"Error": "No such object exists in the database"}), 404
    else:
        return data

@app.route("/payMerchant", methods = ["GET", "POST"])
def payMerchant():
    data = getPayMerchant()
    return data

if (__name__ == "__main__"):
    app.run(debug = True)
