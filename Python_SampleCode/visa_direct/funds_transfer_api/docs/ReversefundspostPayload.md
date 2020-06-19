# ReversefundspostPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_application_id** | **str** | Identifies the programs&#39; business application type for VisaNet transaction processing&lt;br&gt;&lt;br&gt;For Money Transfer, AA applies to transactions where the sender and recipient are the same person and PP applies to transactions where the sender and recipient are not the same person.&lt;br&gt;&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#business_application_identifier\&quot;&gt;businessApplicationId&lt;/a&gt; codes | 
**transaction_identifier** | **int** | The VisaNet reference number for the transaction. You must use the transactionIdentifier from the initial AFT in this field. | 
**card_acceptor** | [**CardAcceptor**](CardAcceptor.md) |  | 
**surcharge** | **str** | When present, this field contains the sender&#39;s surcharge as assessed by the originator. Values in this field must be in the same currency and format as defined in the amount field. | [optional] 
**network_id** | **int** | This contains a code that specifies the network to be used for transmission of the message and determines the program rules that apply to the transaction.&lt;br&gt;&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#network_id_and_sharing_group_code\&quot;&gt;Network ID&lt;/a&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;For ReverseFundsTransactions(AFTR) and MultiReverseFundsTransactions (MULTIAFTR) originators must populate the networkId returned in the original PullFundsTransactions(AFT) and  MultiPullFundsTransactions (MULTIAFT) response.&lt;br&gt; Supported only in US for domestic transactions. | [optional] 
**merchant_category_code** | **int** | If provided, then the value overrides the one present in onboarding data. If the merchantCategoryCode value is not populated in onboarding data then this field is mandatory.&lt;br&gt;&lt;br&gt;If not provided, then the value will default to the values provided during onboarding (when the services are provisioned)&lt;b&gt;Note:&lt;/b&gt; required if not provided during onboarding | 
**merchant_verification_value** | [**MerchantVerificationValue**](MerchantVerificationValue.md) |  | [optional] 
**sharing_group_code** | **str** | This field is optionally used by Push Payments Gateway participants (merchants and acquirers) to specify the network access priority.&lt;br&gt;&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#network_id_and_sharing_group_code\&quot;&gt;Sharing Group Code&lt;/a&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;Supported only in US for domestic transactions involving Push Payments Gateway Service. | [optional] 
**acquirer_country_code** | **int** | Use a 3-digit numeric country code for the country of the BIN under which your Visa Direct solution is registered. This must match the information provided during program enrollment. | 
**systems_trace_audit_number** | **int** | A unique value should be used for each API method. however, when passing the Account Funding Transaction Reversal (AFTR) method, this value must match the systemsTraceAuditNumber previously passed with the AFT method for the current transaction. | 
**original_data_elements** | [**OriginalDataElements**](OriginalDataElements.md) |  | 
**member_comments** | **str** | This field can be optionally used to send and receive comments by service providers. Issuers can optionally include new text in this field in the response. If the issuer does not include this field, Visa will inject the value from the request in the response and send it back to the service provider. | [optional] 
**national_reimbursement_fee** | **float** | When present, this field contains the IRF fees. | [optional] 
**fee_program_indicator** | **str** | If present, a valid value is required. Spaces or special characters are not allowed. | [optional] 
**retrieval_reference_number** | **str** | A value used to tie together service calls related to a single financial transaction. When passing Account Funding Transaction (AFT) and Original Credit Transaction (OCT) methods, this value must differ between the two methods. When passing the Account Funding Transaction Reversal (AFTR) method, this value must match the retrievalReferenceNumber previously passed with the AFT method for this transaction.&lt;br&gt;&lt;br&gt;Recommended Format: ydddhhnnnnnn&lt;br&gt;&lt;br&gt;The first fours digits must be a valid yddd date in the Julian date format, where the first digit &#x3D; 0-9 (last digit of current year) and the next three digits &#x3D; 001-366 (number of the day in the year).&lt;br&gt;&lt;br&gt;hh can be the two digit hour in a 24 hour clock (00-23) during which the transaction is performed.&lt;br&gt;&lt;br&gt;nnnnnn can be the systemsTraceAuditNumber or any 6 digit number. | 
**acquiring_bin** | **int** | The Bank Identification Number (BIN) under which your Visa Direct is registered. This must match the information provided during enrollment. | 
**account_type** | **str** | This is used to identify the account type of the senderPrimaryAccountNumber in the request. Below are the possible values.&lt;br&gt;&lt;br&gt; 00-Not applicable&lt;br&gt; 10-Saving account&lt;br&gt; 20-Checking account&lt;br&gt; 30-Credit card account&lt;br&gt; 40-Universal account&lt;br&gt;&lt;br&gt;Default is set to \&quot;00\&quot; if not provided. | [optional] 
**merchant_pseudo_aba_number** | **str** | This is a number that uniquely identifies the originator when they sign up to send Push Payment Gateway transactions. On enrollment, an originator will get a single pseudo-value that is assigned by Visa. The other networks will assign their own unique values for the originator.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;Supported only in US for domestic transactions involving Push Payments Gateway Service. | [optional] 
**foreign_exchange_fee_transaction** | **float** | When present, this field contains the sender&#39;s foreign exchange markup fee (markup above the wholesale or VisaNet exchange rate as assessed by the originator.Values in this field must be in the same currency and format as defined in the amount field(minimum value is 0). | [optional] 
**point_of_service_data** | [**PointOfServiceData**](PointOfServiceData.md) |  | [optional] 
**sender_primary_account_number** | **str** | The primary account number of the sender&#39;s account. | 
**local_transaction_date_time** | **str** |  | 
**sender_card_expiry_date** | **str** | The expiration date for the sender&#39;s Visa account number in senderPrimaryAccountNumber. | [optional] 
**amount** | **float** | The total amount to be sent to the recipient. | 
**sender_currency_code** | **str** | Use a 3-character alpha or numeric currency code for currency of the sender.&lt;br&gt;&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#iso_country_and_currency_codes\&quot;&gt;ISO Codes&lt;/a&gt; | 
**point_of_service_capability** | [**PointOfServiceCapability**](PointOfServiceCapability.md) |  | [optional] 

[Back to Model list](../README.md#documentation-for-models)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to README](../README.md)



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