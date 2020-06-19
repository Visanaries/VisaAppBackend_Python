# Funds Transfer API
The Funds Transfer API can pull funds from the sender&apos;s Visa account (in preparation for pushing funds to a recipient&apos;s account) in an Account Funding Transaction (AFT).  Additionally, the Funds Transfer API also provides functionality to push funds to the recipient&apos;s Visa account in an Original Credit Transaction (OCT).  If a transaction is declined, the Funds Transfer API can also return the funds to the sender&apos;s funding source in an Account Funding Transaction Reversal (AFTR). The API has been enhanced to allow originators to send their PushFundsTransactions(OCTs) and PullFundsTransactions(AFTs) to Visa for routing to multiple U.S. debit networks.

All URIs are relative to *https://sandbox.api.visa.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getmultipullfundstransactions**](FundsTransferApi.md#getmultipullfundstransactions) | **GET** /visadirect/fundstransfer/v1/multipullfundstransactions/{statusIdentifier} | 
[**getmultipushfundstransactions**](FundsTransferApi.md#getmultipushfundstransactions) | **GET** /visadirect/fundstransfer/v1/multipushfundstransactions/{statusIdentifier} | 
[**getmultireversefundstransactions**](FundsTransferApi.md#getmultireversefundstransactions) | **GET** /visadirect/fundstransfer/v1/multireversefundstransactions/{statusIdentifier} | 
[**getpullfundstransactions**](FundsTransferApi.md#getpullfundstransactions) | **GET** /visadirect/fundstransfer/v1/pullfundstransactions/{statusIdentifier} | 
[**getpushfundstransactions**](FundsTransferApi.md#getpushfundstransactions) | **GET** /visadirect/fundstransfer/v1/pushfundstransactions/{statusIdentifier} | 
[**getreversefundstransactions**](FundsTransferApi.md#getreversefundstransactions) | **GET** /visadirect/fundstransfer/v1/reversefundstransactions/{statusIdentifier} | 
[**postmultipullfunds**](FundsTransferApi.md#postmultipullfunds) | **POST** /visadirect/fundstransfer/v1/multipullfundstransactions | 
[**postmultipushfunds**](FundsTransferApi.md#postmultipushfunds) | **POST** /visadirect/fundstransfer/v1/multipushfundstransactions | 
[**postmultireversefunds**](FundsTransferApi.md#postmultireversefunds) | **POST** /visadirect/fundstransfer/v1/multireversefundstransactions | 
[**postpullfunds**](FundsTransferApi.md#postpullfunds) | **POST** /visadirect/fundstransfer/v1/pullfundstransactions | 
[**postpushfunds**](FundsTransferApi.md#postpushfunds) | **POST** /visadirect/fundstransfer/v1/pushfundstransactions | 
[**postreversefunds**](FundsTransferApi.md#postreversefunds) | **POST** /visadirect/fundstransfer/v1/reversefundstransactions | 


# **getmultipullfundstransactions**
> MultipullfundstransactionsgetResponse getmultipullfundstransactions(status_identifier)



Read Multi Pull Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the getmultipullfundstransactions. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getmultipullfundstransactions(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->getmultipullfundstransactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**MultipullfundstransactionsgetResponse**](MultipullfundstransactionsgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **getmultipushfundstransactions**
> MultipushfundstransactionsgetResponse getmultipushfundstransactions(status_identifier)



Read Multi Push Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the getmultipushfundstransactions. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getmultipushfundstransactions(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->getmultipushfundstransactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**MultipushfundstransactionsgetResponse**](MultipushfundstransactionsgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **getmultireversefundstransactions**
> MultireversefundstransactionsgetResponse getmultireversefundstransactions(status_identifier)



Read Multi Reverse Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the getmultireversefundstransactions. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getmultireversefundstransactions(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->getmultireversefundstransactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**MultireversefundstransactionsgetResponse**](MultireversefundstransactionsgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **getpullfundstransactions**
> PullfundstransactionsgetResponse getpullfundstransactions(status_identifier)



Read Pull Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the getpullfundstransactions. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getpullfundstransactions(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->getpullfundstransactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**PullfundstransactionsgetResponse**](PullfundstransactionsgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **getpushfundstransactions**
> PushfundstransactionsgetResponse getpushfundstransactions(status_identifier)



Read Push Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the getpushfundstransactions. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getpushfundstransactions(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->getpushfundstransactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**PushfundstransactionsgetResponse**](PushfundstransactionsgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **getreversefundstransactions**
> ReversefundstransactionsgetResponse getreversefundstransactions(status_identifier)



Read Reverse Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the getreversefundstransactions. Look at the documentation for further clarification.
status_identifier = 'status_identifier_example' # str | Status Identifier

try: 
    api_response = api_instance.getreversefundstransactions(status_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->getreversefundstransactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_identifier** | **str**| Status Identifier | 

### Return type

[**ReversefundstransactionsgetResponse**](ReversefundstransactionsgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postmultipullfunds**
> MultipullfundspostResponse postmultipullfunds(x_client_transaction_id, multipullfundspost_payload)



Create Multi Pull Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the postmultipullfunds. Look at the documentation for further clarification.
x_client_transaction_id = 'x_client_transaction_id_example' # str | A unique value for a transaction (unique at the level of the individual service invoker and can be recycled every 24 hours). This identifies the transaction uniquely and can help reference the results of the original transaction.
multipullfundspost_payload = src.MultipullfundspostPayload() # MultipullfundspostPayload | Request body for creating in multi pull funds transfer

try: 
    api_response = api_instance.postmultipullfunds(x_client_transaction_id, multipullfundspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->postmultipullfunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client_transaction_id** | **str**| A unique value for a transaction (unique at the level of the individual service invoker and can be recycled every 24 hours). This identifies the transaction uniquely and can help reference the results of the original transaction. | 
 **multipullfundspost_payload** | [**MultipullfundspostPayload**](MultipullfundspostPayload.md)| Request body for creating in multi pull funds transfer | 

### Return type

[**MultipullfundspostResponse**](MultipullfundspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postmultipushfunds**
> MultipushfundspostResponse postmultipushfunds(x_client_transaction_id, multipushfundspost_payload)



Create Multi Push Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the postmultipushfunds. Look at the documentation for further clarification.
x_client_transaction_id = 'x_client_transaction_id_example' # str | A unique value for a transaction (unique at the level of the individual service invoker and can be recycled every 24 hours). This identifies the transaction uniquely and can help reference the results of the original transaction.
multipushfundspost_payload = src.MultipushfundspostPayload() # MultipushfundspostPayload | Request body for creating in multi push funds transfer

try: 
    api_response = api_instance.postmultipushfunds(x_client_transaction_id, multipushfundspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->postmultipushfunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client_transaction_id** | **str**| A unique value for a transaction (unique at the level of the individual service invoker and can be recycled every 24 hours). This identifies the transaction uniquely and can help reference the results of the original transaction. | 
 **multipushfundspost_payload** | [**MultipushfundspostPayload**](MultipushfundspostPayload.md)| Request body for creating in multi push funds transfer | 

### Return type

[**MultipushfundspostResponse**](MultipushfundspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postmultireversefunds**
> MultireversefundspostResponse postmultireversefunds(multireversefundspost_payload)



Create Multi Reverse Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the postmultireversefunds. Look at the documentation for further clarification.
multireversefundspost_payload = src.MultireversefundspostPayload() # MultireversefundspostPayload | Request body for creating in multi reverse funds transfer

try: 
    api_response = api_instance.postmultireversefunds(multireversefundspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->postmultireversefunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multireversefundspost_payload** | [**MultireversefundspostPayload**](MultireversefundspostPayload.md)| Request body for creating in multi reverse funds transfer | 

### Return type

[**MultireversefundspostResponse**](MultireversefundspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postpullfunds**
> PullfundspostResponse postpullfunds(pullfundspost_payload)



Create Pull Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the postpullfunds. Look at the documentation for further clarification.
pullfundspost_payload = src.PullfundspostPayload() # PullfundspostPayload | Request body for creating in pull funds transfer

try: 
    api_response = api_instance.postpullfunds(pullfundspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->postpullfunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pullfundspost_payload** | [**PullfundspostPayload**](PullfundspostPayload.md)| Request body for creating in pull funds transfer | 

### Return type

[**PullfundspostResponse**](PullfundspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postpushfunds**
> PushfundspostResponse postpushfunds(pushfundspost_payload)



Create Push Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the postpushfunds. Look at the documentation for further clarification.
pushfundspost_payload = src.PushfundspostPayload() # PushfundspostPayload | Request body for creating in push funds transfer

try: 
    api_response = api_instance.postpushfunds(pushfundspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->postpushfunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pushfundspost_payload** | [**PushfundspostPayload**](PushfundspostPayload.md)| Request body for creating in push funds transfer | 

### Return type

[**PushfundspostResponse**](PushfundspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postreversefunds**
> ReversefundspostResponse postreversefunds(reversefundspost_payload)



Create Reverse Funds Transaction

### Example 
```python
from __future__ import print_statement
import time
from src.apis.funds_transfer_api import FundsTransferApi
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
api_instance = FundsTransferApi()

# Set all the required parameters in the postreversefunds. Look at the documentation for further clarification.
reversefundspost_payload = src.ReversefundspostPayload() # ReversefundspostPayload | Request body for creating in reverse funds transfer

try: 
    api_response = api_instance.postreversefunds(reversefundspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsTransferApi->postreversefunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reversefundspost_payload** | [**ReversefundspostPayload**](ReversefundspostPayload.md)| Request body for creating in reverse funds transfer | 

### Return type

[**ReversefundspostResponse**](ReversefundspostResponse.md)

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