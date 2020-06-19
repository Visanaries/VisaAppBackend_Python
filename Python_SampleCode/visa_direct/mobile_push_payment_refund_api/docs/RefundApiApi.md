# Mobile Push Payment Refund API
Mobile Push Payment is a simple, secure and fast way to pay and be paid using mobile phones. Mobile Push Payment enables a range of payment use cases and is technology agnostic-leveraging evolving POS environment such as QR codes and works on both smart or feature phones.

All URIs are relative to *https://sandbox.api.visa.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getmerchandise_return_get**](RefundApiApi.md#getmerchandise_return_get) | **GET** /visadirect/mvisa/v1/mr/{statusIdentifier} | 
[**getmerchandise_return_reversal_get**](RefundApiApi.md#getmerchandise_return_reversal_get) | **GET** /visadirect/mvisa/v1/mrr/{statusIdentifier} | 
[**postmerchandise_return_post**](RefundApiApi.md#postmerchandise_return_post) | **POST** /visadirect/mvisa/v1/mr | 
[**postmerchandise_return_reversal_post**](RefundApiApi.md#postmerchandise_return_reversal_post) | **POST** /visadirect/mvisa/v1/mrr | 


# **getmerchandise_return_get**
> MerchandiseReturnGetgetResponse getmerchandise_return_get(status_identifier)



Read Merchandise Return Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.refund_api_api import RefundApiApi
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
api_instance = RefundApiApi()

# Set all the required parameters in the getmerchandise_return_get. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getmerchandise_return_get(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundApiApi->getmerchandise_return_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**MerchandiseReturnGetgetResponse**](MerchandiseReturnGetgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **getmerchandise_return_reversal_get**
> MerchandiseReturnReversalGetgetResponse getmerchandise_return_reversal_get(status_identifier)



Read Merchandise Return Reversal Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.refund_api_api import RefundApiApi
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
api_instance = RefundApiApi()

# Set all the required parameters in the getmerchandise_return_reversal_get. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getmerchandise_return_reversal_get(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundApiApi->getmerchandise_return_reversal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**MerchandiseReturnReversalGetgetResponse**](MerchandiseReturnReversalGetgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postmerchandise_return_post**
> MerchandiseReturnPostpostResponse postmerchandise_return_post(merchandise_return_postpost_payload)



Merchandise Return Transaction is used to refund (full or partial) sale amount back to consumer.  A merchant may, at its discretion, process a credit into consumer account when a valid transaction was previously processed. This situation can arise when the consumer cancels the purchase, or returns the goods in part or in full, or the merchant agrees to return a part of the payment.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.refund_api_api import RefundApiApi
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
api_instance = RefundApiApi()

# Set all the required parameters in the postmerchandise_return_post. Look at the documentation for further clarification.
merchandise_return_postpost_payload = src.MerchandiseReturnPostpostPayload() # MerchandiseReturnPostpostPayload | Request body for creating in merchandise return

try: 
    api_response = api_instance.postmerchandise_return_post(merchandise_return_postpost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundApiApi->postmerchandise_return_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchandise_return_postpost_payload** | [**MerchandiseReturnPostpostPayload**](MerchandiseReturnPostpostPayload.md)| Request body for creating in merchandise return | 

### Return type

[**MerchandiseReturnPostpostResponse**](MerchandiseReturnPostpostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postmerchandise_return_reversal_post**
> MerchandiseReturnReversalPostpostResponse postmerchandise_return_reversal_post(merchandise_return_reversal_postpost_payload)



Merchandise Return Reversal Transaction is used to reverse the refund amount that sent to the consumer. 

### Example 
```python
from __future__ import print_statement
import time
from src.apis.refund_api_api import RefundApiApi
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
api_instance = RefundApiApi()

# Set all the required parameters in the postmerchandise_return_reversal_post. Look at the documentation for further clarification.
merchandise_return_reversal_postpost_payload = src.MerchandiseReturnReversalPostpostPayload() # MerchandiseReturnReversalPostpostPayload | Request body for creating in merchandise return reversal

try: 
    api_response = api_instance.postmerchandise_return_reversal_post(merchandise_return_reversal_postpost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundApiApi->postmerchandise_return_reversal_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchandise_return_reversal_postpost_payload** | [**MerchandiseReturnReversalPostpostPayload**](MerchandiseReturnReversalPostpostPayload.md)| Request body for creating in merchandise return reversal | 

### Return type

[**MerchandiseReturnReversalPostpostResponse**](MerchandiseReturnReversalPostpostResponse.md)

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