# PullfundspostResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_id** | **int** | This contains a code that identifies the network on which the transaction was processed.&lt;br&gt;&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#network_id_and_sharing_group_code\&quot;&gt;Network ID&lt;/a&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;This field is returned only if it is anything other than networkId value 2.&lt;br&gt;&lt;br&gt;Supported only in US for domestic transactions. | [optional] 
**approval_code** | **str** | The authorization code from the issuer. | [optional] 
**fee_program_indicator** | **str** |  | [optional] 
**last4of_pan** | **int** | This field contains the last four digits of the cardholder primary account number (PAN) | [optional] 
**merchant_verification_value** | **str** | The concatenated Merchant Verification Value of Visa assigned and Acquirer assigned value is returned. | [optional] 
**cavv_result_code** | **str** | The cavvResultCode identifies the outcome of the CAVV validation. &lt;br&gt;&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#cardholder_authentication_verification_value\&quot;&gt;cavvResultCode&lt;/a&gt; | [optional] 
**status_identifier** | **str** |  | 
**transaction_identifier** | **int** | The VisaNet reference number for the transaction&lt;br&gt;&lt;br&gt;&lt;b&gt;Note: &lt;/b&gt;&lt;br&gt;transactionIdentifier is a Visa generated field that client recieves in the response message.&lt;br&gt;&lt;b&gt;Note: &lt;/b&gt;As an exception Visa allows clients to use the transactionIdentifier received in the AFT response into the subsequent OCT message - this is to simplify matching the pull and push transaction pair and reconciliation. | 
**member_comments** | **str** | This field can be optionally used to send and receive comments by service providers. Issuers can optionally include new text in this field in the response. If the issuer does not include this field, Visa will inject the value from the request in the response and send it back to the service provider. | [optional] 
**response_code** | **str** | The source for the response; typically, either the recipient issuer or a Visa system.&lt;br&gt;&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#response_code\&quot;&gt;responseCode&lt;/a&gt;&lt;br&gt;&lt;b&gt;Note: &lt;/b&gt;: The VisaNet Response Source for the transaction | 
**action_code** | **str** | The results of the transaction request &lt;br&gt;&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#action_code\&quot;&gt;actionCode&lt;/a&gt; | 
**cps_authorization_characteristics_indicator** | **str** | Indicates whether AFT transaction has qualified for CPS. Possible values are : F (Meets CPS/Account Funding requirements) , N (Not Qualified), T (Not Qualified) | [optional] 
**reimbursement_attribute** | **str** | If AFT transaction has qualified for CPS then this field contains a code that identifies the applicable interchange reimbursement fee. Possible values are : A (Payment Service Interchange Reimbursement Fee (PSIRF)�U.S.) | [optional] 
**transmission_date_time** | **str** | Example: 2016-01-15T07:03:52.000Z&lt;br&gt;&lt;b&gt;Note: &lt;/b&gt; Remove �.000Z� if this field value is used for ReverseFundsTransactions POST request or MultiReverseFundsTransactions POST request. | 

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