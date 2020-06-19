# CardvalidationpostResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_code** | **str** | The authorization code from the issuer. | [optional] 
**card_verification_results** | **str** | A Visa-defined code indicating Card Verification Value (CVV), iCVV (Integrated Chip Card CVV) or dCVV (dynamic CVV) verification results. &lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#cvv_icvv_results_codes\&quot;&gt; CVV/iCVV Results Codes.&lt;/a&gt;&lt;br&gt;&lt;b&gt;Note: &lt;/b&gt;Reserved for future use | [optional] 
**card_authentication_results** | **str** | A Visa-defined code indicating Online Card Authentication Method results. &lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#card_authentication_results\&quot;&gt;cardAuthenticationResults.&lt;/a&gt;&lt;br&gt;&lt;b&gt;Note: &lt;/b&gt;Reserved for future use | [optional] 
**transaction_identifier** | **int** | The VisaNet reference number for the transaction. | 
**cardholder_authentication_verification_results** | **str** | Results of the Cardholder Authentication Verification Value (CAVV) validation. &lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#cardholder_authentication_verification_value\&quot;&gt;CAVV Results Codes.&lt;/a&gt;&lt;br&gt;&lt;b&gt;Note: &lt;/b&gt;Reserved for future use | [optional] 
**cvv2_result_code** | **str** | Results of the CVV2 validation for the primaryAccountNumber in the request.&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#card_verification2_results\&quot;&gt;cvv2ResultsCode&lt;/a&gt; | [optional] 
**response_code** | **str** | The source for the response; typically, either the recipient issuer or a Visa system. &lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#response_code\&quot;&gt;Response Code&lt;/a&gt; | 
**action_code** | **str** | The results of the transaction request.&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#action_code\&quot;&gt;Action Code&lt;/a&gt; &lt;br&gt;&lt;b&gt;Note: &lt;/b&gt;The VisaNet Response Code for the transaction | 
**address_verification_results** | **str** | Results of the Address Verification Service (AVS) validation for the PrimaryAccountNumber in the request. &lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#address_verification_results\&quot;&gt;Address Verification Results&lt;/a&gt; | [optional] 

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