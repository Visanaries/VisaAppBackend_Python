# ResolvepostResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City of the recipient.  Recipient can be a consumer, merchant or agent. | [optional] 
**merchant_category_code** | **str** | &lt;b&gt;Conditional.&lt;/b&gt;  Merchant Category Code. This attribute will only be returned if businessApplicationId&#x3D;MP, CO | [optional] 
**url** | **str** | &lt;b&gt;Optional.&lt;/b&gt;  An URL of a landing page that contains participating issuers will be returned to originator if an alias cannot be found in Visa Alias Directory and &lt;b&gt;HTTP status code &#x3D; 404&lt;/b&gt;.  Originator can notify unregistered recipient with this URL so that he/she can select preferred issuer for alias registration.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;This attribute is only applicable to selective markets, originator will receive this URL instead of error JSON response for processing if HTTP status code &#x3D; 404.  Contact Visa&#39;s representative for details. | [optional] 
**country** | **str** | Country code of the recipient. As defined by ISO 3166. | 
**transaction_currency_code** | **str** | &lt;b&gt;Conditional.&lt;/b&gt;  This is the transaction currency code that a merchant can accept for payment. This attribute will only be returned if businessApplicationId&#x3D;MP, CO. As defined by ISO 4217. | [optional] 
**recipient_primary_account_number** | **str** | Depending on the businessApplicationId of the request, this attribute can contain the consumer card number, mVisa merchant ID (16-digit) or mVisa agent ID (16-digit). | 
**tip_convenience_fee_indicator** | **str** | &lt;b&gt;Conditional.&lt;/b&gt; Tip or Convenience Fee Indicator. This attribute will only be returned if businessApplicationId&#x3D;MP. | [optional] 
**card_type** | **str** | &lt;b&gt;Conditional.&lt;/b&gt;  Card type description. Reference to Field 62.23 — Product ID of available card products. e.g. Visa Platinum. Only applicable if businessApplicationId &#x3D; “PP” or “CI” | [optional] 
**convenience_fee_amount** | **str** | &lt;b&gt;Conditional.&lt;/b&gt;  The convenience fee of a fixed amount. The format of the amount is the same as defined in tag 54. Convenience amount as provided by merchant shall be passed in Field 28 of ISO or transactionFeeAmt of API message, in the Visa specifications. This attribute will only be returned if businessApplicationId&#x3D;MP. | [optional] 
**point_of_initiation_method** | **str** | &lt;b&gt;Conditional.&lt;/b&gt; In this two-digit field, the first character indicates the method by which the data is presented by the merchant. The second character indicates whether the data is static or dynamic. Static data refers to a situation wherein same data is presented for every transaction unlike a dynamic data wherein the information is specific to a transaction. &lt;br&gt;1st Character: &lt;br&gt;“1” &#x3D; QR &lt;br&gt;“2” &#x3D; BLE &lt;br&gt;“3” &#x3D; NFC &lt;br&gt;“4”-“9” &#x3D; Reserved for future use &lt;br&gt;&lt;br&gt;2nd Character: &lt;br&gt;“1” &#x3D; Static &lt;br&gt;“2” &#x3D; Dynamic &lt;br&gt;“3”-“9” &#x3D; Reserved for future use &lt;br&gt;&lt;br&gt;Example: “11” indicates QR static code, “12” indicates QR dynamic code &lt;br&gt;This attribute will only be returned if businessApplicationId&#x3D;MP, CO | [optional] 
**postal_code** | **str** | Postal Code of the recipient. Recipient can be a consumer, merchant or agent. | [optional] 
**recipient_name** | **str** | Depending on the businessApplicationId of the request, this attribute can contain the consumer name, merchant name or agent name. Regarding consumer name, this is composed of consumer’s first, middle and last name | 
**issuer_name** | **str** | &lt;b&gt;Conditional.&lt;/b&gt;  This is the issuer name of recipient’s card. Only applicable if businessApplicationId &#x3D; “PP” or “CI” | [optional] 
**convenience_fee_percentage** | **str** | &lt;b&gt;Conditional.&lt;/b&gt; The percentage convenience fee, specified as numeric value from “00.01” (for 00.01%) to “99.99” (for 99.99%). Originators are required to derive the convenience fee amount and shall pass it in Field 28 of ISO or transactionFeeAmt of API message, in the Visa specifications. This attribute will only be returned if businessApplicationId&#x3D;MP. | [optional] 
**account_look_up_info** | [**AccountLookUpInfo**](AccountLookUpInfo.md) |  | [optional] 

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