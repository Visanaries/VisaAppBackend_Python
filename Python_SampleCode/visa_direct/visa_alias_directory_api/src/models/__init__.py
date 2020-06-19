# coding: utf-8

"""
    Visa Alias Directory API

    Visa Alias Directory Services provide an ability to resolve an identifier (i.e. an alias) such as mobile phone number, email address, short name, or nickname, to a Visa card account (non-Visa soon) through APIs.  A Visa client can use these APIs to allow consumers provide an alias instead of inputting a card number (PAN) to use Visa Direct push payment services such as person-to-person (P2P) money transfers, mVisa merchant payments and mVisa agent deposits and withdrawals.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .account_look_up_info import AccountLookUpInfo
from .content import Content
from .create_aliaspost_payload import CreateAliaspostPayload
from .create_aliaspost_response import CreateAliaspostResponse
from .create_merchant_aliaspost_payload import CreateMerchantAliaspostPayload
from .create_merchant_aliaspost_response import CreateMerchantAliaspostResponse
from .delete_aliaspost_payload import DeleteAliaspostPayload
from .delete_aliaspost_response import DeleteAliaspostResponse
from .delete_merchant_aliaspost_payload import DeleteMerchantAliaspostPayload
from .delete_merchant_aliaspost_response import DeleteMerchantAliaspostResponse
from .generate_report_response import GenerateReportResponse
from .generate_reportpost_payload import GenerateReportpostPayload
from .generate_reportpost_response import GenerateReportpostResponse
from .get_aliasget_response import GetAliasgetResponse
from .get_merchant_aliasget_response import GetMerchantAliasgetResponse
from .get_report_response import GetReportResponse
from .get_reportget_response import GetReportgetResponse
from .links import Links
from .resolvepost_payload import ResolvepostPayload
from .resolvepost_response import ResolvepostResponse
from .update_aliaspost_payload import UpdateAliaspostPayload
from .update_aliaspost_response import UpdateAliaspostResponse
from .update_merchant_aliaspost_payload import UpdateMerchantAliaspostPayload
from .update_merchant_aliaspost_response import UpdateMerchantAliaspostResponse

# ----------------------------------------------------------------------------------------------------------------------
# © Copyright 2018 Visa. All Rights Reserved.
#
# NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of
# and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property
# rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.
#
# By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy
# (developer.visa.com/privacy). In addition, all permissible uses of the Software must be in support of Visa products,
# programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com).
# THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL
# FAULTS” BASIS WITHOUT WARRANTY OR CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.
# ----------------------------------------------------------------------------------------------------------------------