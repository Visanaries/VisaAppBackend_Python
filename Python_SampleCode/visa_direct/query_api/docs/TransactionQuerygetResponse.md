# TransactionQuerygetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_application_id** | **str** | Business Application ID indicates to the type of Transaction that has taken place. &lt;br/&gt; Valid Values include* &lt;br/&gt; &lt;ul&gt; &lt;li&gt; AA - Account to Account &lt;/li&gt; &lt;li&gt; BB - Business to Business &lt;/li&gt; &lt;li&gt; BI - Money Transfer (bank-initiated) &lt;/li&gt; &lt;li&gt; CP - Card Bill Payment &lt;/li&gt; &lt;/ul&gt; &lt;br/&gt; For more information visit &lt;a href&#x3D;\&quot;/request_response_codes#businessApplicationId\&quot;&gt;Visa Developer Platform Documentation &lt;/a&gt; | [optional] 
**settlement_date** | **str** | This field contains the settlement date for the transaction processed by VisaNet. | [optional] 
**transaction_date** | **str** | The date the transaction was submitted to VisaNet. | 
**retrieval_reference_number** | **str** | A value used to tie together service calls related to a single financial transaction. This is the same as retrievalReferenceNumber previously sent in the request for PullFunds, PushFunds or ReverseFunds transaction API calls. | 
**currency_conversion_rate** | **str** | Currency conversion rate taken place at Acquirer&#39;s end. | [optional] 
**processing_date** | **str** | The date on which VisaNet created the log (record). | [optional] 
**transaction_time** | **str** | The time the transaction was submitted to VisaNet. | 
**reason_code** | **str** | The reason code description contains the reason explaining:&lt;ul&gt;&lt;li&gt; An acquirer-generated advice, reversal, cancellation, adjustment, chargeback (validation request or advice).&lt;/li&gt;&lt;li&gt; A chargeback reversal, representment (validation request or advice). &lt;/li&gt; etc. | [optional] 
**transaction_identifier** | **str** | The VisaNet reference number for the transaction. This is the same transactionIdentifier previously received in the response for PullFunds, PushFunds or ReverseFunds transaction API calls. | 
**network_id** | **str** | Network ID on which the transaction was performed. &lt;br/&gt; Takes the format of 000x where x is a number. &lt;br/&gt; Valid Values include* &lt;br/&gt; 0002 - Visa/PLUS &lt;br/&gt; 0016 - Maestro &lt;br/&gt; 0003 - Interlink &lt;br/&gt; 0008,0010,0011,0012,0015 - Star | [optional] 
**amount** | **str** | This is the transaction amount expressed in U.S. Dollars. Derived internally. | [optional] 
**account_number_masked** | **str** | Contains the masked PAN number. Populated from the primary account number (PAN) contained in the original authorization request. | [optional] 
**amount_in_transaction_currency** | **str** | This is the transaction amount in original transaction currency. | [optional] 
**product_identifier_platform_code** | **str** | Product Identifier Platform Code. &lt;br/&gt; Valid Values include* &lt;br/&gt; BZ - Business &lt;br/&gt; CN - Consumer &lt;br/&gt; CO - Commercial &lt;br/&gt; GV - Government | [optional] 
**settlement_time** | **str** | This field contains the settlement time for the transaction processed by VisaNet. &lt;br/&gt; Note: The exact time of settlement may vary and is indicative only. | [optional] 
**fee_program_indicator** | **str** | This field contains an interchange reimbursement fee program indicator (FPI), which is used in assessing the fee amount applied to financial transactions that were originally sent. | [optional] 
**transaction_currency_code** | **str** | 3-character numeric currency code of the transaction. | [optional] 
**reason_code_value** | **str** | While reasonCode property explains the reason in details, reasonCodeValue property is a four digit number that corelates to reasonCode. &lt;br/&gt; Valid Values include* &lt;br/&gt; 0000 - NOT APPLICABLE &lt;br/&gt; 0083 - FRAUD; CARD ABSENT ENVIRONMENT | [optional] 
**card_acceptor** | [**CardAcceptor**](CardAcceptor.md) |  | [optional] 
**transaction_state_code** | **str** | Code explaining the state of the transaction. | [optional] 
**card_type** | **str** | Product type of the card on which the transaction is performed. &lt;br/&gt; Valid Values include* &lt;br/&gt; Credit  &lt;br/&gt; Debit &lt;br/&gt; Prepaid | [optional] 
**action_code** | **str** | The results of the transaction request &lt;br/&gt; Refer to &lt;a href&#x3D;&#39;/request_response_codes#action_code&#39;&gt;actionCode&lt;/a&gt;&lt;br/&gt; Note: The VisaNet Response Code for the transaction | 
**acquiring_bin** | **int** | The Bank Identification Number (BIN) under which the Visa Direct solution is registered. This must match the information provided during enrollment. | 
**approval_code** | **str** | The authorization code from the issuer. A code provided by the issuer (or VIP STIP) when a transaction is approved, or a no reason to decline code is provided. | 
**reject_reason_code** | **int** | This field contains reject reason code if the the transaction was rejected by VisaNet. &lt;br/&gt; A positive number not greater than 9999. | [optional] 
**reject_reason_text** | **str** | This field contains reject reason text if the transaction was rejected by VisaNet. | [optional] 
**fee_program_desc** | **str** | Short text description of the Acquirer IRF (Interchange Reimbursement Fee) indicator. (Interchange fees are paid by issuers and acquirers to each other for transactions entered into interchange and their reversals). | [optional] 
**systems_trace_audit_number** | **str** | A number assigned by the message initiator that uniquely identifies a transaction. This is the same as systemsTraceAuditNumber previously sent in the request for the PullFunds, PushFunds or ReverseFunds transaction API calls. | 
**response_code** | **str** | The source for the response; typically, either the recipient issuer or a Visa system. &lt;br/&gt; Refer to &lt;a href&#x3D;&#39;/request_response_codes#response_code&#39;&gt;responseCode&lt;/a&gt;&lt;br/&gt; Note: The VisaNet Response Source for the transaction | 
**transaction_type** | **str** | Identifies the type of transaction originally sent &lt;br/&gt; Valid Values include*: &lt;br/&gt;  CRED VOUCHER &lt;br/&gt; CRED REVERSAL &lt;br/&gt; CRED CHGBK &lt;br/&gt; CRED CHGBK REVERSAL &lt;br/&gt; SALES DRAFT &lt;br/&gt; SALES CHGBK &lt;br/&gt; SALES REVERSAL &lt;br/&gt; CASH DISBURSEMT &lt;br/&gt; CASH CHGBK | 
**status_code** | **str** | Specifies status of the transaction processing. &lt;br/&gt; Valid values are &lt;ul&gt; &lt;li&gt;COMPLETED - Transaction was processed by Visa &lt;/li&gt; &lt;li&gt; IN_PROGRESS - Transaction is in progress, being processed by Visa &lt;/li&gt; &lt;li&gt; FAILED - Transaction was received &amp; rejected by Visa&lt;/li&gt;&lt;/ul&gt; | 

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