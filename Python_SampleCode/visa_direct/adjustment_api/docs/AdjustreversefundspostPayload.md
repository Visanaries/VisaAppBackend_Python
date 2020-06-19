# AdjustreversefundspostPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_transaction_date_time** | **str** |  | 
**business_application_id** | **str** | Identifies the Visa Direct use case required for processing. This must match the value provided in the request of PullFundsTransactions. | 
**merchant_category_code** | **int** | Contains a code describing the merchant&#39;s type of business product or service, also known as the merchant category code (MCC). These codes are based on the Merchant Classification Code Guideline available from the Bank Card Division of the ABA. Clients should send the same merchantCategoryCode that was submitted in the PullFundsTransactions | 
**sender_card_expiry_date** | **str** | The expiration date for the sender&#39;s Visa account number in senderPrimaryAccountNumber. | [optional] 
**acquirer_country_code** | **int** | Use a 3-digit numeric country code for the country of the BIN under which your Visa Direct program is registered. | 
**transaction_identifier** | **int** | Clients should send the Visa transaction identifier returned in the response of PullFundsTransactions. | 
**amount** | **float** | The amount of the transaction, inclusive of all fees assessed for the transaction, including currency conversion fees. | 
**card_acceptor** | [**CardAcceptor**](CardAcceptor.md) |  | 
**acquiring_bin** | **int** | The Bank Identification Number (BIN) under which your Visa Direct is registered. This must match the information provided during enrollment. | 
**retrieval_reference_number** | **str** | This field contains a number that is used with other data elements as a key to identify and track all messages related to a given cardholder transaction; that is, to a given transaction set. Recommended format: ydddhhnnnnnn. The first four digits must be a valid yddd date in the Julian date format, where the first digit &#x3D; 0-9 (last digit of current year) and the next three digits &#x3D; 001-366 (number of the day in the year), hh can be the two digit hour in a 24 hour clock (00-23) during which the transaction is performed, nnnnnn can be the systemsTraceAuditNumber or any 6 digit number. A unique value should be used for each API invocation. | 
**systems_trace_audit_number** | **int** | This field contains a number assigned by the merchant, service provider or acquirer that uniquely identifies a cardholder transaction and all message types (also known as system transactions) that comprise it per individual program rules. A unique value should be used for each API invocation. | 
**sender_currency_code** | **str** | Use a 3-character alpha or numeric currency code for currency of the sender. This code identifies the currency of the transaction amount sent in the amount field. | 
**sender_primary_account_number** | **str** | This field contains a number identifying the customer account which could be a PAN or a token. | 

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