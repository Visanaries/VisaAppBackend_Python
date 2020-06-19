# MerchandiseReturnPostpostPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_transaction_date_time** | **str** | This should be +/- 3 days from the current date.The date is in yyyy-mm-ddThh:mm:ss format. | 
**recipient_primary_account_number** | **str** | Populate with Consumer PAN. This is the same PAN the consumer used in merchant payment. | 
**merchant_category_code** | **str** | This is to be populated with the MCC of the merchant initiating the refund. | 
**fee_program_indicator** | **str** | Originators can leave this field blank. | [optional] 
**transaction_fee_amt** | **str** | Prefix ‘C’ Originators are required to populate convenience fee amount in this field to be returned, if presented in the original message | [optional] 
**retrieval_reference_number** | **str** | Numeric only. This is a key data element for matching a message to others within a given transaction set.Recommended Format : ydddhhnnnnnnThe first fours digits must be a valid yddd date in the Julian date format, where the first digit &#x3D; 0-9 (last digit of current year) and the next three digits &#x3D; 001-366 (number of the day in the year). hh can be the two digit hour in a 24 hour clock (00-23) during which the transaction is performed.&lt;br&gt;&lt;br&gt; nnnnnn can be the SystemsTraceAuditNumber or any 6 digit number. | 
**acquirer_country_code** | **str** | Use a 3-digit numeric country code for the country. This must match the information provided during program enrollment. | 
**amount** | **str** | Refunded amount in original transaction currency. | 
**card_acceptor** | [**CardAcceptor**](CardAcceptor.md) |  | 
**acquiring_bin** | **str** | This BIN number identifies the originator of refund transaction. This must match the information provided during enrollment. | 
**systems_trace_audit_number** | **str** | Numeric only. This must be the same value as in the original request. | 
**transaction_currency_code** | **str** | The code in this field must always reflect the currency associated to the amount | 
**merchant_verification_value** | [**MerchantVerificationValue**](MerchantVerificationValue.md) |  | [optional] 
**card_expiry_date** | **str** | The expiration date for the Consumer PAN in recipientPrimaryAccountNumber | [optional] 
**transaction_identifier** | **str** | &lt;b&gt;Conditional.&lt;/b&gt; If originator submits merchant payment transaction using MerchantPushPayments API, they should submit the same value of transactionIdentifier in API request. Otherwise, do not use this field in the API request. | [optional] 

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