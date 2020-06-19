# CreateAliaspostPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_middle_name** | **str** | Consumer’s middle name. | [optional] 
**city** | **str** | Consumer’s city | [optional] 
**recipient_first_name** | **str** | Consumer’s first name. | 
**contact_phone_number** | **str** | Consumer’s contact phone number for all communications | [optional] 
**address1** | **str** | Address line 1. | [optional] 
**address2** | **str** | Address line 2. | [optional] 
**recipient_primary_account_number** | **str** | Consumer&#39;s card number. | 
**consent_date_time** | **str** | Date &amp; time when consumer has provided their consent to Issuer about the use of their personal personal data for VAD service. Format: YYYY-MM-DD hh:mm:ss.  Local date and time should be converted to Coordinated Universal Time (UTC) before submitting this value in API request. | 
**contact_email** | **str** | Consumer’s contact email for all communications | [optional] 
**alias** | **str** | This attribute contains the alias data, e.g. phone number, email address, etc.&lt;br&gt;If phone number is used for alias, this should be provided in accordance with ITU-T E.164 (2010) number structure. &lt;br&gt;Below are some examples of phone numbers with different country codes:&lt;br&gt;&lt;table&gt;&lt;tr&gt;&lt;td&gt;Country&lt;/td&gt;&lt;td&gt;Country Code&lt;/td&gt;&lt;td&gt;Examples&lt;/td&gt;&lt;tr&gt;&lt;td&gt;United States&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;b&gt;1&lt;/b&gt;650xxxxxxx&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Russia&lt;/td&gt;&lt;td&gt;7&lt;/td&gt;&lt;td&gt;&lt;b&gt;7&lt;/b&gt;495xxxxxxx&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;United Kingdom&lt;/td&gt;&lt;td&gt;44&lt;/td&gt;&lt;td&gt;&lt;b&gt;44&lt;/b&gt;78xxxxxxxx&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Singapore&lt;/td&gt;&lt;td&gt;65&lt;/td&gt;&lt;td&gt;&lt;b&gt;65&lt;/b&gt;9xxxxxxx&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Hong Kong&lt;/td&gt;&lt;td&gt;852&lt;/td&gt;&lt;td&gt;8529xxxxxxx&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Kenya&lt;/td&gt;&lt;td&gt;254&lt;/td&gt;&lt;td&gt;&lt;b&gt;254&lt;/b&gt;701xxxxxx&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; | 
**card_type** | **str** | Card type description. Reference to Field 62.23—Product ID of available card products. e.g. Visa Platinum | 
**recipient_last_name** | **str** | Consumer’s last name. | 
**country** | **str** | Consumer’s country code as defined by ISO 3166, ISO 3166 alpha-2 is recommended to be used if alias may be used for QR. | 
**postal_code** | **str** | Postal/Zip code of the consumer. | [optional] 
**issuer_name** | **str** | This is the Issuer name of recipient’s card | 
**guid** | **str** | This attribute is uniquely used by Issuer to identify their customer (i.e. consumer cardholder).&lt;br&gt;Issuer may pass their existing unique identifier of a cardholder of their system to VAD as a guid.&lt;br&gt;For multiple aliases linked to the same PAN, different guids should be provided. | 
**alias_type** | **str** | “01” – Phone number &lt;br&gt;“02” – email address | 

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