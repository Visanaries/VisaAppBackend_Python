# AccountLookUpInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**push_funds_block_indicator** | **str** | Indicates whether the PAN submitted in the request can receive Push Funds(OCTs).&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#pushFundsIndicator\&quot;&gt;pushFundsBlockIndicator&lt;/a&gt; | 
**billing_currency_code** | **int** | Use a 3-digit numeric currency code for the card billing currency of the PAN.&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#currency_codes\&quot;&gt;ISO Codes&lt;/a&gt; | 
**billing_currency_code_minor_digits** | **str** | Identifies the number of decimal positions that should be present in any amounts for the requested card&#39;s billing currency. | [optional] 
**fast_funds_indicator** | **str** | Indicates the funds delivery speed of the PAN submitted in the request. If the value is &#39;B&#39;, &#39;C&#39;, or &#39;D&#39;, funds will be available to the recipient within 30 minutes of successful transfer. If the value is &#39;N&#39;, the funds will be available within 2 business days of successful transfer.&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#fastFundsIndicator\&quot;&gt;fastFundsIndicator&lt;/a&gt; | 
**card_issuer_country_code** | **str** | Refer to &lt;a href&#x3D;\&quot;/request_response_codes#iso_country_codes\&quot;&gt;ISO Codes&lt;/a&gt; | 
**online_gambing_block_indicator** | **str** | Indicates whether the PAN submitted in the request can receive Push Funds(OCTs) for gambling-type transactions. If the value is &#39;Y&#39;, then the account cannot receive gambling Push Funds (OCTs). If the value is &#39;N&#39;, the account can receive gambling Push Funds (OCTs). | 
**issuer_name** | **str** | Issuer name of the consumer card. | 
**geo_restriction_ind** | **str** | This field will determine if the recipient issuer can accept transactions from the Originator country. If the value is &#39;Y&#39;, transactions cannot be accepted from the sender country. If the value is &#39;N&#39;, transactions are allowed. | 
**card_type_code** | **str** | The code of account funding source for the card, e.g. Credit, Debit, Prepaid, Charge, Deferred Debit.&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#cardTypeCode\&quot;&gt;cardTypeCode&lt;/a&gt; | [optional] 

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