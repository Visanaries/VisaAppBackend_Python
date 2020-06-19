# Payment Account Validation API
The Payment Account Validation API allows applications to run validations of the payment account before processing a transaction ensuring greater probability of success and allowing for a more seamless transaction flow.

All URIs are relative to *https://sandbox.api.visa.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postcardvalidation**](PavApi.md#postcardvalidation) | **POST** /pav/v1/cardvalidation | 


# **postcardvalidation**
> CardvalidationpostResponse postcardvalidation(cardvalidationpost_payload, cardvalidationpost_payload2, cardvalidationpost_payload3, cardvalidationpost_payload4, cardvalidationpost_payload5, cardvalidationpost_payload6, cardvalidationpost_payload7, cardvalidationpost_payload8, cardvalidationpost_payload9)



Perform validations of the payment account

### Example 
```python
from __future__ import print_statement
import time
from src.apis.pav_api import PavApi
from src.configuration import Configuration
from pprint import pprint

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'
config.cert_file = 'ABSOLUTE_PATH_TO_CERT_FILE'
config.key_file = 'ABSOLUTE_PATH_TO_KEY_FILE'
config.ssl_ca_cert = 'ABSOLUTE_PATH_TO_CA_CERT_FILE'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'


# create an instance of the API class
api_instance = PavApi()

# Set all the required parameters in the postcardvalidation. Look at the documentation for further clarification.
cardvalidationpost_payload = src.CardvalidationpostPayload() # CardvalidationpostPayload | The primary account number for which account validations are being performed
cardvalidationpost_payload2 = src.CardvalidationpostPayload() # CardvalidationpostPayload | The expiration date for the primaryAccountNumber in the request. The date should not be a past date.</br>Required when the cvv2Value is present.
cardvalidationpost_payload3 = src.CardvalidationpostPayload() # CardvalidationpostPayload | 
cardvalidationpost_payload4 = src.CardvalidationpostPayload() # CardvalidationpostPayload | The cardCvv2Value value provided by the account holder for the primaryAccountNumber in the request.</br>Required when addressVerificationResults is not present.
cardvalidationpost_payload5 = src.CardvalidationpostPayload() # CardvalidationpostPayload | This is an optional field.  The clients of Funds Transfer APIs can choose to provide acquiringBin for reporting purpose.  The Bank Identification Number (BIN) under which your Funds Transfer is registered. This must match the information provided during enrollment.
cardvalidationpost_payload6 = src.CardvalidationpostPayload() # CardvalidationpostPayload | This is an optional field. If acquiringBin is provided, it is highly recommended that acquirerCountryCode is also provided.</br>The clients of Funds Transfer APIs can choose to provide acquirerCountryCode for reporting purpose.</br>Use a 3-digit numeric country code for the country where the Funds Transfer solution is registered. This must match the information provided during program enrollment.<br>Refer to <a href=\"/request_response_codes#iso_country_and_currency_codes\">ISO Codes</a>
cardvalidationpost_payload7 = src.CardvalidationpostPayload() # CardvalidationpostPayload | This is an optional field. The clients of Funds Transfer APIs can choose to provide card acceptor information for reporting purposes.
cardvalidationpost_payload8 = src.CardvalidationpostPayload() # CardvalidationpostPayload | This is an optional field. It is recommended that the clients of Funds Transfer APIs provide systemsTraceAuditNumber for tie the calls with a single funds transfer transaction.
cardvalidationpost_payload9 = src.CardvalidationpostPayload() # CardvalidationpostPayload | This is an optional field. It is recommended that the clients of Funds Transfer APIs provide retrievalReferenceNumber for tie the calls with a single funds transfer transaction.</br>Recommended Format: ydddhhnnnnnn</br>The first fours digits must be a valid yddd date in the Julian date format, where the first digit = 0-9 (last digit of current year) and the next three digits = 001-366 (number of the day in the year).</br>hh can be the two digit hour in a 24 hour clock (00-23) during which the transaction is performed.</br>nnnnnn can be the systemsTraceAuditNumber or any 6 digit number.

try: 
    api_response = api_instance.postcardvalidation(cardvalidationpost_payload, cardvalidationpost_payload2, cardvalidationpost_payload3, cardvalidationpost_payload4, cardvalidationpost_payload5, cardvalidationpost_payload6, cardvalidationpost_payload7, cardvalidationpost_payload8, cardvalidationpost_payload9)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PavApi->postcardvalidation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cardvalidationpost_payload** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)| The primary account number for which account validations are being performed | 
 **cardvalidationpost_payload2** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)| The expiration date for the primaryAccountNumber in the request. The date should not be a past date.&lt;/br&gt;Required when the cvv2Value is present. | 
 **cardvalidationpost_payload3** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)|  | 
 **cardvalidationpost_payload4** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)| The cardCvv2Value value provided by the account holder for the primaryAccountNumber in the request.&lt;/br&gt;Required when addressVerificationResults is not present. | 
 **cardvalidationpost_payload5** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)| This is an optional field.  The clients of Funds Transfer APIs can choose to provide acquiringBin for reporting purpose.  The Bank Identification Number (BIN) under which your Funds Transfer is registered. This must match the information provided during enrollment. | 
 **cardvalidationpost_payload6** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)| This is an optional field. If acquiringBin is provided, it is highly recommended that acquirerCountryCode is also provided.&lt;/br&gt;The clients of Funds Transfer APIs can choose to provide acquirerCountryCode for reporting purpose.&lt;/br&gt;Use a 3-digit numeric country code for the country where the Funds Transfer solution is registered. This must match the information provided during program enrollment.&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#iso_country_and_currency_codes\&quot;&gt;ISO Codes&lt;/a&gt; | 
 **cardvalidationpost_payload7** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)| This is an optional field. The clients of Funds Transfer APIs can choose to provide card acceptor information for reporting purposes. | 
 **cardvalidationpost_payload8** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)| This is an optional field. It is recommended that the clients of Funds Transfer APIs provide systemsTraceAuditNumber for tie the calls with a single funds transfer transaction. | 
 **cardvalidationpost_payload9** | [**CardvalidationpostPayload**](CardvalidationpostPayload.md)| This is an optional field. It is recommended that the clients of Funds Transfer APIs provide retrievalReferenceNumber for tie the calls with a single funds transfer transaction.&lt;/br&gt;Recommended Format: ydddhhnnnnnn&lt;/br&gt;The first fours digits must be a valid yddd date in the Julian date format, where the first digit &#x3D; 0-9 (last digit of current year) and the next three digits &#x3D; 001-366 (number of the day in the year).&lt;/br&gt;hh can be the two digit hour in a 24 hour clock (00-23) during which the transaction is performed.&lt;/br&gt;nnnnnn can be the systemsTraceAuditNumber or any 6 digit number. | 

### Return type

[**CardvalidationpostResponse**](CardvalidationpostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)


##Authors
**Visa Developer Platform**
See also the list of [contributors](https://github.com/visa/java-sample-code/graphs/contributors) who participated in this project.

##License
**© Copyright 2018 Visa. All Rights Reserved.**

*NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of
and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property
rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*

*By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).
In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided
through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED
INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR
CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply
product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally
do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims
all liability for any such components, including continued availability and functionality. Benefits depend on implementation
details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the
described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,
implementation and resources by you based on your business and operational details. Please refer to the specific
API documentation for details on the requirements, eligibility and geographic availability.*

*This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,
functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.
The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,
including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*