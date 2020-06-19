# Visa Alias Directory API
Visa Alias Directory Services provide an ability to resolve an identifier (i.e. an alias) such as mobile phone number, email address, short name, or nickname, to a Visa card account (non-Visa soon) through APIs.  A Visa client can use these APIs to allow consumers provide an alias instead of inputting a card number (PAN) to use Visa Direct push payment services such as person-to-person (P2P) money transfers, mVisa merchant payments and mVisa agent deposits and withdrawals.

All URIs are relative to *https://sandbox.api.visa.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_alias**](AliasApiApi.md#get_get_alias) | **GET** /visaaliasdirectory/v1/manage/{guid} | 
[**get_get_merchant_alias**](AliasApiApi.md#get_get_merchant_alias) | **GET** /visaaliasdirectory/v1/managemerchant | 
[**get_get_report**](AliasApiApi.md#get_get_report) | **GET** /visaaliasdirectory/v1/managereport | 
[**post_create_alias**](AliasApiApi.md#post_create_alias) | **POST** /visaaliasdirectory/v1/manage/createalias | 
[**post_create_merchant_alias**](AliasApiApi.md#post_create_merchant_alias) | **POST** /visaaliasdirectory/v1/managemerchant/createalias | 
[**post_delete_alias**](AliasApiApi.md#post_delete_alias) | **POST** /visaaliasdirectory/v1/manage/deletealias | 
[**post_delete_merchant_alias**](AliasApiApi.md#post_delete_merchant_alias) | **POST** /visaaliasdirectory/v1/managemerchant/deletealias | 
[**post_generate_report**](AliasApiApi.md#post_generate_report) | **POST** /visaaliasdirectory/v1/managereport/generate | 
[**post_resolve**](AliasApiApi.md#post_resolve) | **POST** /visaaliasdirectory/v1/resolve | 
[**post_update_alias**](AliasApiApi.md#post_update_alias) | **POST** /visaaliasdirectory/v1/manage/updatealias | 
[**post_update_merchant_alias**](AliasApiApi.md#post_update_merchant_alias) | **POST** /visaaliasdirectory/v1/managemerchant/updatealias | 


# **get_get_alias**
> GetAliasgetResponse get_get_alias(guid)



Get alias and recipient's related data.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the get_get_alias. Look at the documentation for further clarification.
guid = 'guid_example' # str | This attribute is uniquely used by Issuer to identify their customer (i.e. consumer cardholder).

try: 
    api_response = api_instance.get_get_alias(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->get_get_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| This attribute is uniquely used by Issuer to identify their customer (i.e. consumer cardholder). | 

### Return type

[**GetAliasgetResponse**](GetAliasgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **get_get_merchant_alias**
> GetMerchantAliasgetResponse get_get_merchant_alias(merchantaliasid, type=type)



Get alias and merchant or agent related data.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the get_get_merchant_alias. Look at the documentation for further clarification.
merchantaliasid = 'merchantaliasid_example' # str | This attribute is uniquely used by acquirer to identify their merchant or agent.
type = 'type_example' # str | Valid type value is 'agent'. If type is not provided, default search for merchant alias records only. (optional)

try: 
    api_response = api_instance.get_get_merchant_alias(merchantaliasid, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->get_get_merchant_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantaliasid** | **str**| This attribute is uniquely used by acquirer to identify their merchant or agent. | 
 **type** | **str**| Valid type value is &#39;agent&#39;. If type is not provided, default search for merchant alias records only. | [optional] 

### Return type

[**GetMerchantAliasgetResponse**](GetMerchantAliasgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **get_get_report**
> GetReportgetResponse get_get_report(reportid, pageid)



Get Report data.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the get_get_report. Look at the documentation for further clarification.
reportid = 'reportid_example' # str | This attribute is uniquely generated by Visa Alias directory to identify the report generation request.  This is used to retrieve the alias report together with the page ID.<br>The format is {BID}-{TYPE}-{NUMERIC STRING}, where <b>BID</b> is the Business Identifier of the client used by Visa, <b>TYPE</b> can be 'CONSUMER', 'MERCHANT' or 'AGENT' alias report. 
pageid = 'pageid_example' # str | Numeric only. This attribute is used to specify the page number of the report.

try: 
    api_response = api_instance.get_get_report(reportid, pageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->get_get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reportid** | **str**| This attribute is uniquely generated by Visa Alias directory to identify the report generation request.  This is used to retrieve the alias report together with the page ID.&lt;br&gt;The format is {BID}-{TYPE}-{NUMERIC STRING}, where &lt;b&gt;BID&lt;/b&gt; is the Business Identifier of the client used by Visa, &lt;b&gt;TYPE&lt;/b&gt; can be &#39;CONSUMER&#39;, &#39;MERCHANT&#39; or &#39;AGENT&#39; alias report.  | 
 **pageid** | **str**| Numeric only. This attribute is used to specify the page number of the report. | 

### Return type

[**GetReportgetResponse**](GetReportgetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **post_create_alias**
> CreateAliaspostResponse post_create_alias(create_aliaspost_payload)



Create an alias in the Alias Directory.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the post_create_alias. Look at the documentation for further clarification.
create_aliaspost_payload = src.CreateAliaspostPayload() # CreateAliaspostPayload | Request body for creating alias API

try: 
    api_response = api_instance.post_create_alias(create_aliaspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->post_create_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_aliaspost_payload** | [**CreateAliaspostPayload**](CreateAliaspostPayload.md)| Request body for creating alias API | 

### Return type

[**CreateAliaspostResponse**](CreateAliaspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **post_create_merchant_alias**
> CreateMerchantAliaspostResponse post_create_merchant_alias(create_merchant_aliaspost_payload)



Creates a merchant or agent alias in the Alias Directory.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the post_create_merchant_alias. Look at the documentation for further clarification.
create_merchant_aliaspost_payload = src.CreateMerchantAliaspostPayload() # CreateMerchantAliaspostPayload | Request body for creating merchant or agent alias

try: 
    api_response = api_instance.post_create_merchant_alias(create_merchant_aliaspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->post_create_merchant_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_merchant_aliaspost_payload** | [**CreateMerchantAliaspostPayload**](CreateMerchantAliaspostPayload.md)| Request body for creating merchant or agent alias | 

### Return type

[**CreateMerchantAliaspostResponse**](CreateMerchantAliaspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **post_delete_alias**
> DeleteAliaspostResponse post_delete_alias(delete_aliaspost_payload)



Delete alias of a recipient from the Alias Directory.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the post_delete_alias. Look at the documentation for further clarification.
delete_aliaspost_payload = src.DeleteAliaspostPayload() # DeleteAliaspostPayload | Request body for deleting an alias

try: 
    api_response = api_instance.post_delete_alias(delete_aliaspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->post_delete_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_aliaspost_payload** | [**DeleteAliaspostPayload**](DeleteAliaspostPayload.md)| Request body for deleting an alias | 

### Return type

[**DeleteAliaspostResponse**](DeleteAliaspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **post_delete_merchant_alias**
> DeleteMerchantAliaspostResponse post_delete_merchant_alias(delete_merchant_aliaspost_payload)



Delete alias of a merchant or agent from the Alias Directory.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the post_delete_merchant_alias. Look at the documentation for further clarification.
delete_merchant_aliaspost_payload = src.DeleteMerchantAliaspostPayload() # DeleteMerchantAliaspostPayload | Request body for deleting a merchant or agent alias

try: 
    api_response = api_instance.post_delete_merchant_alias(delete_merchant_aliaspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->post_delete_merchant_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_merchant_aliaspost_payload** | [**DeleteMerchantAliaspostPayload**](DeleteMerchantAliaspostPayload.md)| Request body for deleting a merchant or agent alias | 

### Return type

[**DeleteMerchantAliaspostResponse**](DeleteMerchantAliaspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **post_generate_report**
> GenerateReportpostResponse post_generate_report(generate_reportpost_payload)



To submit a request to generate report and return a URL as response for retrieving report.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the post_generate_report. Look at the documentation for further clarification.
generate_reportpost_payload = src.GenerateReportpostPayload() # GenerateReportpostPayload | Request body for generating a report

try: 
    api_response = api_instance.post_generate_report(generate_reportpost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->post_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_reportpost_payload** | [**GenerateReportpostPayload**](GenerateReportpostPayload.md)| Request body for generating a report | 

### Return type

[**GenerateReportpostResponse**](GenerateReportpostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **post_resolve**
> ResolvepostResponse post_resolve(resolvepost_payload)



Resolve an alias for recipient's primary account number (PAN) and related data.

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the post_resolve. Look at the documentation for further clarification.
resolvepost_payload = src.ResolvepostPayload() # ResolvepostPayload | Request body for resolve alias API

try: 
    api_response = api_instance.post_resolve(resolvepost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->post_resolve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolvepost_payload** | [**ResolvepostPayload**](ResolvepostPayload.md)| Request body for resolve alias API | 

### Return type

[**ResolvepostResponse**](ResolvepostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **post_update_alias**
> UpdateAliaspostResponse post_update_alias(update_aliaspost_payload)



Update alias and recipient data in the Alias Directory

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the post_update_alias. Look at the documentation for further clarification.
update_aliaspost_payload = src.UpdateAliaspostPayload() # UpdateAliaspostPayload | Request body for updating alias API

try: 
    api_response = api_instance.post_update_alias(update_aliaspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->post_update_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_aliaspost_payload** | [**UpdateAliaspostPayload**](UpdateAliaspostPayload.md)| Request body for updating alias API | 

### Return type

[**UpdateAliaspostResponse**](UpdateAliaspostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **post_update_merchant_alias**
> UpdateMerchantAliaspostResponse post_update_merchant_alias(update_merchant_aliaspost_payload)



Update merchant alias or agent alias info in the Alias Directory

### Example 
```python
from __future__ import print_statement
import time
from src.apis.alias_api_api import AliasApiApi
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
api_instance = AliasApiApi()

# Set all the required parameters in the post_update_merchant_alias. Look at the documentation for further clarification.
update_merchant_aliaspost_payload = src.UpdateMerchantAliaspostPayload() # UpdateMerchantAliaspostPayload | Request body for updating merchant or agent alias API

try: 
    api_response = api_instance.post_update_merchant_alias(update_merchant_aliaspost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApiApi->post_update_merchant_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_merchant_aliaspost_payload** | [**UpdateMerchantAliaspostPayload**](UpdateMerchantAliaspostPayload.md)| Request body for updating merchant or agent alias API | 

### Return type

[**UpdateMerchantAliaspostResponse**](UpdateMerchantAliaspostResponse.md)

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