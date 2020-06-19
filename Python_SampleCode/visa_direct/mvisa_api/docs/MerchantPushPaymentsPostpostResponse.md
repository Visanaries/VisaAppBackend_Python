# MerchantPushPaymentsPostpostResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_verification_value** | **str** | Recipient are expected to populate the Merchant Verification Value used to identify merchants that participate in a variety of programs in this field The valid values are 0-9 and A-F. These values are hexadecimal. | [optional] 
**approval_code** | **str** | &lt;b&gt;Conditional.&lt;/b&gt; Contains the authorization code provided by the recipient when a transaction is approved. Visa recommends that recipients maintain uniqueness of this code for a given merchant PAN, however Visa would not maintain any checks for uniqueness. | [optional] 
**merchant_category_code** | **str** | Numeric only. Recipient should populate the MCC of the merchant in the response message. | 
**fee_program_indicator** | **str** | Optional field which may be populated by recipient where applicable. | [optional] 
**transaction_identifier** | **str** | It is added by VisaNet. It contains a right-justified, VisaNet generated Transaction Identifier (TID) that is unique for each request. The identifier links original messages to subsequent messages, such as those for exception item processing and clearing record. | 
**status_identifier** | **str** | Required when API response times out. | 
**retrieval_reference_number** | **str** | Numeric only. Key data element for matching a message to others within a given transaction set. Value will be the same as what has been provided in the request. | 
**card_acceptor** | [**CardAcceptor**](CardAcceptor.md) |  | 
**response_code** | **str** | It is added by VisaNet and contains the response source/reason code that identifies the source of the actionCode response decision. | 
**action_code** | **str** | Contains a code that defines the response to a request. Refer to &lt;a href&#x3D;\&quot;/request_response_codes#action_code\&quot;&gt;ActionCode&lt;/a&gt; | 
**purchase_identifier** | [**PurchaseIdentifier**](PurchaseIdentifier.md) |  | [optional] 
**transmission_date_time** | **str** | The value in response must match the value in the request. | 

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