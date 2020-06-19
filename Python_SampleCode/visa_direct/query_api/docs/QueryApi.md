# Query API
The Transaction Query API can be used to determine the processing status of a transaction or to retreive the lifecycle of a transaction. This API can be used to check whether a PullFunds, PushFunds or ReverseFunds transaction processed successfully if received by Visa. This API could also be used to retrieve the detailed lifecycle or history of a transaction (e.g. original transaction, chargeback, chargeback reversal etc).

All URIs are relative to *https://sandbox.api.visa.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gettransaction_query**](QueryApi.md#gettransaction_query) | **GET** /visadirect/v1/transactionquery | 


# **gettransaction_query**
> TransactionQuerygetResponse gettransaction_query(acquiring_bin, stan=stan, rrn=rrn, transaction_identifier=transaction_identifier, caid=caid, transaction_start_date=transaction_start_date, transaction_end_date=transaction_end_date, fields=fields, limit=limit, offset=offset)



The Transaction Query API can be used to determine the processing status of a transaction or to retreive the lifecycle of a transaction. This API can be used to check whether a PullFunds, PushFunds or ReverseFunds transaction processed successfully if received by Visa. This API could also be used to retrieve the detailed lifecycle or history of a transaction (e.g. original transaction, chargeback, chargeback reversal etc).

### Example 
```python
from __future__ import print_statement
import time
from src.apis.query_api import QueryApi
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
api_instance = QueryApi()

# Set all the required parameters in the gettransaction_query. Look at the documentation for further clarification.
acquiring_bin = 'acquiring_bin_example' # str | The Bank Identification Number (BIN) under which the Visa Direct solution is registered. This must match the information provided during enrollment.
stan = 'stan_example' # str | A number assigned by the message initiator that uniquely identifies a transaction. This is the same as systemsTraceAuditNumber previously sent in the request for the PullFunds, PushFunds or ReverseFunds transaction API calls. <br/> <b>Note: When <i>transactionIdentifier</i> is  not used as a query parameter, this parameter must be included along with <i>rrn</i> as query parameters.</b><br/>e.g.:/transactionquery?acquiringBIN=408999&stan=351480&rrn=221917871070 (optional)
rrn = 'rrn_example' # str | A value used to tie together service calls related to a single financial transaction. This is the same as retrievalReferenceNumber previously sent in the request for PullFunds, PushFunds or ReverseFunds transaction API calls. <br/> <b>Note: When <i>transactionIdentifier</i> is  not used as a query parameter, this parameter must be included along with <i>stan</i> as query parameters.</b><br/>e.g.:/transactionquery?acquiringBIN=408999&stan=351480&rrn=221917871070 (optional)
transaction_identifier = 'transaction_identifier_example' # str | The VisaNet reference number for the transaction. This is the same transactionIdentifier previously received in the response for PullFunds, PushFunds or ReverseFunds transaction API calls. <br/> <b>Note: When <i>stan</i> and <i>rrn</i> parameters combination is not used as query parameters, this parameter must be included as a query parameter.</b><br/>e.g.:/transactionquery?acquiringBIN=408999&transactionIdentifier=234234322342343 (optional)
caid = 'caid_example' # str | An identifier for the card acceptor. This is the same as cardAcceptor.idCode previously sent in the request for PullFunds, PushFunds or ReverseFunds transaction API calls. (optional)
transaction_start_date = 'transaction_start_date_example' # str | The start date for querying the transaction. Can be in previous 120 day range including today's date. Start date cannot be later than End date. (optional)
transaction_end_date = 'transaction_end_date_example' # str | The end date for querying the transacton. Can be in previous 120 day range including today's date. (optional)
fields = 'fields_example' # str | Comma separated list of additional fields requestor would like in response e.g. amount, responseCode <br/> Note: <br/> If no fields parameter is specified, then following fields are returned by default in the response <br/> 1) statusCode <br/> 2) acquiringBin <br/> 3) actionCode <br/> 4) approvalCode <br/> 5) responseCode <br/> 6) transactionIdentifier <br/> 7) transactionType <br/> 8) retrievalReferenceNumber <br/> 9) systemsTraceAuditNumber <br/> 10) transactionDate <br/> 11) transactionTime (optional)
limit = 'limit_example' # str | Number of records to return, if there are multiple records. Useful for pagination. e.g. if there are 29 records, limit=10 returns 10 records at a time <br/> Note: <br/> 1) If no limit parameter is specified, then max of 10 records will be returned by default. <br/> 2) A header value x-pagination=true will be returned if there are more than 10 records, so that you can query with offset and limit parameters to get the next set of records. (optional)
offset = 'offset_example' # str | Starting record number, from where to return records. Useful for pagination. e.g. if offset =11 and limit =10, then records 11 thru 20 will be returned. (optional)

try: 
    api_response = api_instance.gettransaction_query(acquiring_bin, stan=stan, rrn=rrn, transaction_identifier=transaction_identifier, caid=caid, transaction_start_date=transaction_start_date, transaction_end_date=transaction_end_date, fields=fields, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->gettransaction_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acquiring_bin** | **str**| The Bank Identification Number (BIN) under which the Visa Direct solution is registered. This must match the information provided during enrollment. | 
 **stan** | **str**| A number assigned by the message initiator that uniquely identifies a transaction. This is the same as systemsTraceAuditNumber previously sent in the request for the PullFunds, PushFunds or ReverseFunds transaction API calls. &lt;br/&gt; &lt;b&gt;Note: When &lt;i&gt;transactionIdentifier&lt;/i&gt; is  not used as a query parameter, this parameter must be included along with &lt;i&gt;rrn&lt;/i&gt; as query parameters.&lt;/b&gt;&lt;br/&gt;e.g.:/transactionquery?acquiringBIN&#x3D;408999&amp;stan&#x3D;351480&amp;rrn&#x3D;221917871070 | [optional] 
 **rrn** | **str**| A value used to tie together service calls related to a single financial transaction. This is the same as retrievalReferenceNumber previously sent in the request for PullFunds, PushFunds or ReverseFunds transaction API calls. &lt;br/&gt; &lt;b&gt;Note: When &lt;i&gt;transactionIdentifier&lt;/i&gt; is  not used as a query parameter, this parameter must be included along with &lt;i&gt;stan&lt;/i&gt; as query parameters.&lt;/b&gt;&lt;br/&gt;e.g.:/transactionquery?acquiringBIN&#x3D;408999&amp;stan&#x3D;351480&amp;rrn&#x3D;221917871070 | [optional] 
 **transaction_identifier** | **str**| The VisaNet reference number for the transaction. This is the same transactionIdentifier previously received in the response for PullFunds, PushFunds or ReverseFunds transaction API calls. &lt;br/&gt; &lt;b&gt;Note: When &lt;i&gt;stan&lt;/i&gt; and &lt;i&gt;rrn&lt;/i&gt; parameters combination is not used as query parameters, this parameter must be included as a query parameter.&lt;/b&gt;&lt;br/&gt;e.g.:/transactionquery?acquiringBIN&#x3D;408999&amp;transactionIdentifier&#x3D;234234322342343 | [optional] 
 **caid** | **str**| An identifier for the card acceptor. This is the same as cardAcceptor.idCode previously sent in the request for PullFunds, PushFunds or ReverseFunds transaction API calls. | [optional] 
 **transaction_start_date** | **str**| The start date for querying the transaction. Can be in previous 120 day range including today&#39;s date. Start date cannot be later than End date. | [optional] 
 **transaction_end_date** | **str**| The end date for querying the transacton. Can be in previous 120 day range including today&#39;s date. | [optional] 
 **fields** | **str**| Comma separated list of additional fields requestor would like in response e.g. amount, responseCode &lt;br/&gt; Note: &lt;br/&gt; If no fields parameter is specified, then following fields are returned by default in the response &lt;br/&gt; 1) statusCode &lt;br/&gt; 2) acquiringBin &lt;br/&gt; 3) actionCode &lt;br/&gt; 4) approvalCode &lt;br/&gt; 5) responseCode &lt;br/&gt; 6) transactionIdentifier &lt;br/&gt; 7) transactionType &lt;br/&gt; 8) retrievalReferenceNumber &lt;br/&gt; 9) systemsTraceAuditNumber &lt;br/&gt; 10) transactionDate &lt;br/&gt; 11) transactionTime | [optional] 
 **limit** | **str**| Number of records to return, if there are multiple records. Useful for pagination. e.g. if there are 29 records, limit&#x3D;10 returns 10 records at a time &lt;br/&gt; Note: &lt;br/&gt; 1) If no limit parameter is specified, then max of 10 records will be returned by default. &lt;br/&gt; 2) A header value x-pagination&#x3D;true will be returned if there are more than 10 records, so that you can query with offset and limit parameters to get the next set of records. | [optional] 
 **offset** | **str**| Starting record number, from where to return records. Useful for pagination. e.g. if offset &#x3D;11 and limit &#x3D;10, then records 11 thru 20 will be returned. | [optional] 

### Return type

[**TransactionQuerygetResponse**](TransactionQuerygetResponse.md)

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