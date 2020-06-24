import requests
import json
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

url = "https://sandbox.api.visa.com/visadirect/fundstransfer/v1/pushfundstransactions"
certificate = "cert.pem"
privateKey = "privateKey.pem"
headers = {"Accept": "application/json"}
user_id = "FJBIZAWDZAXKJ3X7B6GK21dL86tIkeBDG-Lppqraa6f07Scqg"
password = "DZr64qXE3vdORl3m"
body = {}
payload = json.loads('''
{
"acquirerCountryCode": "840",
"acquiringBin": "408999",
"amount": "124.05",
"businessApplicationId": "AA",
"cardAcceptor": {
"address": {
"country": "USA",
"county": "San Mateo",
"state": "CA",
"zipCode": "94404"
},
"idCode": "CA-IDCode-77765",
"name": "Visa Inc. USA-Foster City",
"terminalId": "TID-9999"
},
"localTransactionDateTime": "''' + date + '''",
"merchantCategoryCode": "6012",
"pointOfServiceData": {
"motoECIIndicator": "0",
"panEntryMode": "90",
"posConditionCode": "00"
},
"recipientName": "rohan",
"recipientPrimaryAccountNumber": "4957030420210496",
"retrievalReferenceNumber": "412770451018",
"senderAccountNumber": "4653459515756154",
"senderAddress": "901 Metro Center Blvd",
"senderCity": "Foster City",
"senderCountryCode": "124",
"senderName": "Mohammed Qasim",
"senderReference": "",
"senderStateCode": "CA",
"sourceOfFundsCode": "05",
"systemsTraceAuditNumber": "451018",
"transactionCurrencyCode": "USD",
"transactionIdentifier": "381228649430015",
"settlementServiceIndicator": "9",
"colombiaNationalServiceData": {
"countryCodeNationalService": "170",
"nationalReimbursementFee": "20.00",
"nationalNetMiscAmountType": "A",
"nationalNetReimbursementFeeBaseAmount": "20.00",
"nationalNetMiscAmount": "10.00",
"addValueTaxReturn": "10.00",
"taxAmountConsumption": "10.00",
"addValueTaxAmount": "10.00",
"costTransactionIndicator": "0",
"emvTransactionIndicator": "1",
"nationalChargebackReason": "11"
}
}
''')
timeout = 10

r = requests.post(url, 
                cert = (certificate, privateKey),
                headers = headers,
                auth = (user_id, password),
                #data = body,
                json = payload,
                timeout = timeout)

print(r.text)

