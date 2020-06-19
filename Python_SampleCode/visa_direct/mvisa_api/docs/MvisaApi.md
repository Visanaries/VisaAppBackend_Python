# mVisa API
mVisa is a simple, secure and fast way to pay and be paid using mobile phones. mVisa enables a range of payment use cases and is technology agnostic-leveraging evolving POS environment such as QR codes and works on both smart or feature phones.

All URIs are relative to *https://sandbox.api.visa.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcash_in_push_payments_get**](MvisaApi.md#getcash_in_push_payments_get) | **GET** /visadirect/mvisa/v1/cashinpushpayments/{statusIdentifier} | 
[**getcash_out_payments_get**](MvisaApi.md#getcash_out_payments_get) | **GET** /visadirect/mvisa/v1/cashoutpushpayments/{statusIdentifier} | 
[**getmerchant_push_payment_get**](MvisaApi.md#getmerchant_push_payment_get) | **GET** /visadirect/mvisa/v1/merchantpushpayments/{statusIdentifier} | 
[**postcash_in_push_payments**](MvisaApi.md#postcash_in_push_payments) | **POST** /visadirect/mvisa/v1/cashinpushpayments | 
[**postcash_out_push_payments_post**](MvisaApi.md#postcash_out_push_payments_post) | **POST** /visadirect/mvisa/v1/cashoutpushpayments | 
[**postmerchant_push_payments_post**](MvisaApi.md#postmerchant_push_payments_post) | **POST** /visadirect/mvisa/v1/merchantpushpayments | 


# **getcash_in_push_payments_get**
> CashInPushPaymentsGetgetResponse getcash_in_push_payments_get(status_identifier)



Get Cash In Push Payment

### Example 
```python
from __future__ import print_statement
import time
from src.apis.mvisa_api import MvisaApi
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
api_instance = MvisaApi()

# Set all the required parameters in the getcash_in_push_payments_get. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getcash_in_push_payments_get(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MvisaApi->getcash_in_push_payments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**CashInPushPaymentsGetgetResponse**](CashInPushPaymentsGetgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **getcash_out_payments_get**
> CashOutPaymentsGetgetResponse getcash_out_payments_get(status_identifier)



Get Cash Out Push Payment

### Example 
```python
from __future__ import print_statement
import time
from src.apis.mvisa_api import MvisaApi
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
api_instance = MvisaApi()

# Set all the required parameters in the getcash_out_payments_get. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getcash_out_payments_get(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MvisaApi->getcash_out_payments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**CashOutPaymentsGetgetResponse**](CashOutPaymentsGetgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **getmerchant_push_payment_get**
> MerchantPushPaymentGetgetResponse getmerchant_push_payment_get(status_identifier)



Get Merchant Push Payment

### Example 
```python
from __future__ import print_statement
import time
from src.apis.mvisa_api import MvisaApi
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
api_instance = MvisaApi()

# Set all the required parameters in the getmerchant_push_payment_get. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getmerchant_push_payment_get(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MvisaApi->getmerchant_push_payment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**MerchantPushPaymentGetgetResponse**](MerchantPushPaymentGetgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postcash_in_push_payments**
> CashInPushPaymentspostResponse postcash_in_push_payments(cash_in_push_paymentspost_payload)



Create Cash In Push Payment

### Example 
```python
from __future__ import print_statement
import time
from src.apis.mvisa_api import MvisaApi
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
api_instance = MvisaApi()

# Set all the required parameters in the postcash_in_push_payments. Look at the documentation for further clarification.
cash_in_push_paymentspost_payload = src.CashInPushPaymentspostPayload() # CashInPushPaymentspostPayload | Request body for creating in cash in push payment

try: 
    api_response = api_instance.postcash_in_push_payments(cash_in_push_paymentspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MvisaApi->postcash_in_push_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_in_push_paymentspost_payload** | [**CashInPushPaymentspostPayload**](CashInPushPaymentspostPayload.md)| Request body for creating in cash in push payment | 

### Return type

[**CashInPushPaymentspostResponse**](CashInPushPaymentspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postcash_out_push_payments_post**
> CashOutPushPaymentsPostpostResponse postcash_out_push_payments_post(cash_out_push_payments_postpost_payload)



Create Cash Out Push Payment

### Example 
```python
from __future__ import print_statement
import time
from src.apis.mvisa_api import MvisaApi
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
api_instance = MvisaApi()

# Set all the required parameters in the postcash_out_push_payments_post. Look at the documentation for further clarification.
cash_out_push_payments_postpost_payload = src.CashOutPushPaymentsPostpostPayload() # CashOutPushPaymentsPostpostPayload | Request body for creating in cash out push payment

try: 
    api_response = api_instance.postcash_out_push_payments_post(cash_out_push_payments_postpost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MvisaApi->postcash_out_push_payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_out_push_payments_postpost_payload** | [**CashOutPushPaymentsPostpostPayload**](CashOutPushPaymentsPostpostPayload.md)| Request body for creating in cash out push payment | 

### Return type

[**CashOutPushPaymentsPostpostResponse**](CashOutPushPaymentsPostpostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postmerchant_push_payments_post**
> MerchantPushPaymentsPostpostResponse postmerchant_push_payments_post(merchant_push_payments_postpost_payload)



Create Merchant Push Payment

### Example 
```python
from __future__ import print_statement
import time
from src.apis.mvisa_api import MvisaApi
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
api_instance = MvisaApi()

# Set all the required parameters in the postmerchant_push_payments_post. Look at the documentation for further clarification.
merchant_push_payments_postpost_payload = src.MerchantPushPaymentsPostpostPayload() # MerchantPushPaymentsPostpostPayload | Request body for creating in merchant push payment

try: 
    api_response = api_instance.postmerchant_push_payments_post(merchant_push_payments_postpost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MvisaApi->postmerchant_push_payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_push_payments_postpost_payload** | [**MerchantPushPaymentsPostpostPayload**](MerchantPushPaymentsPostpostPayload.md)| Request body for creating in merchant push payment | 

### Return type

[**MerchantPushPaymentsPostpostResponse**](MerchantPushPaymentsPostpostResponse.md)

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