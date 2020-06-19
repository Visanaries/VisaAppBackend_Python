# GetMerchantAliasgetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | Merchant or agent city. | 
**merchant_category_code** | **str** | Merchant Category Code. Numeric only. | 
**payload_format_indicator** | **str** | Defines the format of the merchant data payload. Payload Format Indicator must be set to &#39;01&#39; as per EMVCo Merchant Presented QR specifications. | 
**transaction_currency_code** | **str** | As defined by ISO 4217. This is the transaction currency code that a merchant can accept for payment. 3-digit numeric presentation of the currency is recommended to be used if alias may be used for QR. | 
**recipient_name** | **str** | Merchant or agent name. | 
**email** | **str** | Merchant or agent email address. | [optional] 
**country** | **str** | Merchant or agent country code as defined by ISO 3166. ISO 3166 alpha-2 is recommended to be used if alias may be used for QR. | 
**phone** | **str** | Merchant or agent phone number. | [optional] 
**convenience_fee_amount** | **str** | The convenience fee of a fixed amount. Applicable only for merchant alias. | [optional] 
**point_of_initiation_method** | **str** | In this two-digit field, the first character indicates the method by which the data is presented by the merchant. The second character indicates whether the data is static or dynamic. Static data refers to a situation wherein same data is presented for every transaction unlike a dynamic data wherein the information is specific to a transaction.&lt;br&gt;&lt;b&gt;1st character&lt;/b&gt;&lt;br&gt;&#39;1&#39; &#x3D; QR&lt;br&gt;&#39;2&#39; &#x3D; BLE&lt;br&gt;&#39;3&#39; &#x3D; NFC&lt;br&gt;&#39;4&#39; - &#39;9&#39; &#x3D; Reserved for Future Use&lt;br&gt;&lt;b&gt;2nd character&lt;/b&gt;&lt;br&gt;&#39;1&#39; &#x3D; Static&lt;br&gt;&#39;2&#39; &#x3D; Dynamic&lt;br&gt;&#39;3&#39; - &#39;9&#39; &#x3D; Reserved for Future Use.&lt;br&gt;Example: &#39;11&#39; indicates QR static code, &#39;12&#39; indicates QR dynamic code. | [optional] 
**postal_code** | **str** | Merchant or agent postal code. | [optional] 
**tip_convenience_fee_indicator** | **str** | Tip or Convenience Fee Indicator. This shall contains a value of &#39;01&#39;, &#39;02&#39; or &#39;03&#39; as per EMVCo Merchant Presented QR specifications. Applicable only for merchant alias. | [optional] 
**convenience_fee_percentage** | **str** | Applicable only for merchant alias. The percentage convenience fee, specified as numeric value from “00.01” (for 00.01%) to “99.99” (for 99.99%). | [optional] 
**alias_id** | **str** | This attribute is uniquely used by Acquirer to identify their merchant or agent . | 
**merchant_id** | **str** | A 16 digit-number as per Mobile Push Payment Program Implementation Guide to receive payment by merchant or agent. | 

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