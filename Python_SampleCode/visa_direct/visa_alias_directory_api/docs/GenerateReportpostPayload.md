# GenerateReportpostPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | If not provided, default report contains alias records with all valid status, i.e. &lt;br&gt;Consumer alias report will contain &#39;ACTIVE&#39;,&#39;INACTIVE&#39; and &#39;DISABLED&#39; records&lt;br&gt;Merchant alias report will contain &#39;ACTIVE&#39; and &#39;DISABLED&#39; records&lt;br&gt;Agent alias report will contain &#39;ACTIVE&#39; and &#39;DISABLED&#39; records. &lt;br&gt;Valid values for status are &#39;ACTIVE&#39;, &#39;INACTIVE&#39; and &#39;DISABLED&#39;. | [optional] 
**limit** | **str** | Maximum number of records to be contained in each page of the report. &lt;br&gt;Default is set to a maximum of 20,000 records per page of a report. &lt;br&gt;Minimum value is 1, Maximum value is 20,000. | [optional] 
**type** | **str** | Specify the type of alias records to be contained in the report. &lt;br&gt;Valid values are &lt;b&gt;CONSUMER&lt;/b&gt;, &lt;b&gt;MERCHANT&lt;/b&gt; and &lt;b&gt;AGENT&lt;/b&gt;. | 
**report_start_date** | **str** | The start date of a report. Follows ISO 8601, date format YYYY-MM-DD. Example: 2019-01-01. &lt;br&gt;If not set, it will be default to the previous date (T-1). | [optional] 

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