# ReportingApigetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date_time** | **str** | The date &amp; time of a transaction’s SMS settlement between the acquirer and issuer.  Example 2016-05-01:091234 | [optional] 
**approval_code** | **str** | The authorization code from the issuer. A code provided by the issuer (or VIP STIP) when a transaction is approved, or a \&quot;no reason to decline\&quot; code is provided. Used to tie subsequent messages to the original transaction. | [optional] 
**card_acceptor_id_code** | **str** | An acquirer-assigned (15 byte) code identifying the card acceptor for the transaction. The code can represent a merchant, a specific merchant location, or a specific merchant terminal. | [optional] 
**fee_program_indicator** | **str** | This field contains an interchange reimbursement fee program indicator (FPI), which is used in assessing the fee amount applied to financial transactions. | [optional] 
**fee_program_desc** | **str** | Short text description of the Acquirer IRF (Interchange Reimbursement Fee) indicator. (Interchange fees are paid by issuers and acquirers to each other for transactions entered into interchange and their reversals). | [optional] 
**card_acceptor_name** | **str** | The name of the merchant or ATM (id/location) where the transaction occurred. In VIP this is the first 25 bytes of ISO F43 Card Acceptor Name. | [optional] 
**transaction_currency_code** | **str** | Set internally during VisaNet processing, the ISO currency code which identifies the transaction currency code. | [optional] 
**transaction_identifier** | **str** | An identifier assigned by Visa to help uniquely identify a transaction and to link subsequent transactions, such as a reversal, to an original. The transaction identifier is returned to the acquirer in the authorization response and should be provided in subsequent clearing transactions. The components of the identifier include the transaction date, a sequence number for that date, a system identifier, and the time expressed in relative seconds. | [optional] 
**amount** | **float** | This is the transaction amount expressed in U.S. Dollars. Derived internally. | [optional] 
**acquiring_bin** | **int** | The Bank Identification Number (BIN) under which your Visa Direct is registered. This must match the information provided during enrollment. | [optional] 
**retrieval_reference_number** | **str** | A value used to tie together service calls related to a single financial transaction. Contains a number used with other key data elements to identify and track all messages related to a given cardholder transaction (referred to as a transaction set). | [optional] 
**systems_trace_audit_number** | **int** | An audit number assigned by the message originator - unique to the originator.  Also known as the Interface Trace Number in Base II and the System Trace Audit Number in VIP (ISO F11).  The trace number remains unchanged for all messages throughout the life of the transaction.  It is a key data element used to match a response to its request or to match a message to others for a given cardholder transaction set. | [optional] 
**processing_date** | **str** | The date on which VisaNet created the log (record). | [optional] 
**account_number_masked** | **str** | Contains a masked number identifying an account or customer relationship at a financial institution. Populated from the primary account number (PAN) contained in the original authorization request.  The account number is typically 16 digits, but can vary depending on the source.  The six digits after the initial 6 digit BIN number of a 16 digit PAN number are replaced by &#39;xxxxxx&#39; for security reasons.  This field is left justified with trailing blanks.  (Note: Trailing zeros indicate the Account Number Extension was appended, which is zero-filled if not used.  Insignificant trailing zeros are not part of the account number.) | [optional] 
**reason_code** | **str** | The reason code description is derived from, Field 63.3 of VIP/SMS transactions. Several different kinds of codes may appear in this field, including Fee Collection Reason Codes, Advice Reason Codes, Adjustment Reason Codes, Service Confirmation/Change Notification Reason Codes, Chargeback Reason Codes, etc.&lt;br&gt;Valid values include*:&lt;br&gt;(*Not a complete list)&lt;br&gt;0053 - Chargeback - not as described / defective&lt;br&gt;0083 - Fraud - card not present&lt;br&gt;2105 - Acquirer advice - Clearing of an authorized transaction&lt;br&gt;2121 - VSDC transaction - Offline approval&lt;br&gt;2501 - Reversal - Transaction voided by customer | [optional] 
**transaction_date_time** | **str** | The date &amp; time the transaction was submitted to VisaNet. Example 2016-04-30:162345 | [optional] 
**transaction_state** | **str** | The transaction code (TC) description identifies the type of transaction being processed by BASE II. &lt;br&gt;Valid Values include*:&lt;br&gt;04 - Reclassification Advice&lt;br&gt;05 - Original Sales Draft or Representment&lt;br&gt;06 - Original Credit Voucher or Representment&lt;br&gt;07 - Original Cash Disbursement or Representment&lt;br&gt;10 - Clearing Fee Collection&lt;br&gt;15 - Sales Draft Chargeback&lt;br&gt;25 - Sales Draft Reversal&lt;br&gt;40 - Fraud Advice&lt;br&gt;*Examples provided to clarify definition. May not be a complete list. | [optional] 

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