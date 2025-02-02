# coding: utf-8

"""
    Visa Alias Directory API

    Visa Alias Directory Services provide an ability to resolve an identifier (i.e. an alias) such as mobile phone number, email address, short name, or nickname, to a Visa card account (non-Visa soon) through APIs.  A Visa client can use these APIs to allow consumers provide an alias instead of inputting a card number (PAN) to use Visa Direct push payment services such as person-to-person (P2P) money transfers, mVisa merchant payments and mVisa agent deposits and withdrawals.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccountLookUpInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, push_funds_block_indicator=None, billing_currency_code=None, billing_currency_code_minor_digits=None, fast_funds_indicator=None, card_issuer_country_code=None, online_gambing_block_indicator=None, issuer_name=None, geo_restriction_ind=None, card_type_code=None):
        """
        AccountLookUpInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'push_funds_block_indicator': 'str',
            'billing_currency_code': 'int',
            'billing_currency_code_minor_digits': 'str',
            'fast_funds_indicator': 'str',
            'card_issuer_country_code': 'str',
            'online_gambing_block_indicator': 'str',
            'issuer_name': 'str',
            'geo_restriction_ind': 'str',
            'card_type_code': 'str'
        }

        self.attribute_map = {
            'push_funds_block_indicator': 'pushFundsBlockIndicator',
            'billing_currency_code': 'billingCurrencyCode',
            'billing_currency_code_minor_digits': 'billingCurrencyCodeMinorDigits',
            'fast_funds_indicator': 'fastFundsIndicator',
            'card_issuer_country_code': 'cardIssuerCountryCode',
            'online_gambing_block_indicator': 'onlineGambingBlockIndicator',
            'issuer_name': 'issuerName',
            'geo_restriction_ind': 'geoRestrictionInd',
            'card_type_code': 'cardTypeCode'
        }

        self._push_funds_block_indicator = push_funds_block_indicator
        self._billing_currency_code = billing_currency_code
        self._billing_currency_code_minor_digits = billing_currency_code_minor_digits
        self._fast_funds_indicator = fast_funds_indicator
        self._card_issuer_country_code = card_issuer_country_code
        self._online_gambing_block_indicator = online_gambing_block_indicator
        self._issuer_name = issuer_name
        self._geo_restriction_ind = geo_restriction_ind
        self._card_type_code = card_type_code

    @property
    def push_funds_block_indicator(self):
        """
        Gets the push_funds_block_indicator of this AccountLookUpInfo.
        Indicates whether the PAN submitted in the request can receive Push Funds(OCTs).<br>Refer to <a href=\"/request_response_codes#pushFundsIndicator\">pushFundsBlockIndicator</a>

        :return: The push_funds_block_indicator of this AccountLookUpInfo.
        :rtype: str
        """
        return self._push_funds_block_indicator

    @push_funds_block_indicator.setter
    def push_funds_block_indicator(self, push_funds_block_indicator):
        """
        Sets the push_funds_block_indicator of this AccountLookUpInfo.
        Indicates whether the PAN submitted in the request can receive Push Funds(OCTs).<br>Refer to <a href=\"/request_response_codes#pushFundsIndicator\">pushFundsBlockIndicator</a>

        :param push_funds_block_indicator: The push_funds_block_indicator of this AccountLookUpInfo.
        :type: str
        """
        if push_funds_block_indicator is None:
            raise ValueError("Invalid value for `push_funds_block_indicator`, must not be `None`")

        self._push_funds_block_indicator = push_funds_block_indicator

    @property
    def billing_currency_code(self):
        """
        Gets the billing_currency_code of this AccountLookUpInfo.
        Use a 3-digit numeric currency code for the card billing currency of the PAN.<br>Refer to <a href=\"/request_response_codes#currency_codes\">ISO Codes</a>

        :return: The billing_currency_code of this AccountLookUpInfo.
        :rtype: int
        """
        return self._billing_currency_code

    @billing_currency_code.setter
    def billing_currency_code(self, billing_currency_code):
        """
        Sets the billing_currency_code of this AccountLookUpInfo.
        Use a 3-digit numeric currency code for the card billing currency of the PAN.<br>Refer to <a href=\"/request_response_codes#currency_codes\">ISO Codes</a>

        :param billing_currency_code: The billing_currency_code of this AccountLookUpInfo.
        :type: int
        """
        if billing_currency_code is None:
            raise ValueError("Invalid value for `billing_currency_code`, must not be `None`")

        self._billing_currency_code = billing_currency_code

    @property
    def billing_currency_code_minor_digits(self):
        """
        Gets the billing_currency_code_minor_digits of this AccountLookUpInfo.
        Identifies the number of decimal positions that should be present in any amounts for the requested card's billing currency.

        :return: The billing_currency_code_minor_digits of this AccountLookUpInfo.
        :rtype: str
        """
        return self._billing_currency_code_minor_digits

    @billing_currency_code_minor_digits.setter
    def billing_currency_code_minor_digits(self, billing_currency_code_minor_digits):
        """
        Sets the billing_currency_code_minor_digits of this AccountLookUpInfo.
        Identifies the number of decimal positions that should be present in any amounts for the requested card's billing currency.

        :param billing_currency_code_minor_digits: The billing_currency_code_minor_digits of this AccountLookUpInfo.
        :type: str
        """

        self._billing_currency_code_minor_digits = billing_currency_code_minor_digits

    @property
    def fast_funds_indicator(self):
        """
        Gets the fast_funds_indicator of this AccountLookUpInfo.
        Indicates the funds delivery speed of the PAN submitted in the request. If the value is 'B', 'C', or 'D', funds will be available to the recipient within 30 minutes of successful transfer. If the value is 'N', the funds will be available within 2 business days of successful transfer.<br>Refer to <a href=\"/request_response_codes#fastFundsIndicator\">fastFundsIndicator</a>

        :return: The fast_funds_indicator of this AccountLookUpInfo.
        :rtype: str
        """
        return self._fast_funds_indicator

    @fast_funds_indicator.setter
    def fast_funds_indicator(self, fast_funds_indicator):
        """
        Sets the fast_funds_indicator of this AccountLookUpInfo.
        Indicates the funds delivery speed of the PAN submitted in the request. If the value is 'B', 'C', or 'D', funds will be available to the recipient within 30 minutes of successful transfer. If the value is 'N', the funds will be available within 2 business days of successful transfer.<br>Refer to <a href=\"/request_response_codes#fastFundsIndicator\">fastFundsIndicator</a>

        :param fast_funds_indicator: The fast_funds_indicator of this AccountLookUpInfo.
        :type: str
        """
        if fast_funds_indicator is None:
            raise ValueError("Invalid value for `fast_funds_indicator`, must not be `None`")

        self._fast_funds_indicator = fast_funds_indicator

    @property
    def card_issuer_country_code(self):
        """
        Gets the card_issuer_country_code of this AccountLookUpInfo.
        Refer to <a href=\"/request_response_codes#iso_country_codes\">ISO Codes</a>

        :return: The card_issuer_country_code of this AccountLookUpInfo.
        :rtype: str
        """
        return self._card_issuer_country_code

    @card_issuer_country_code.setter
    def card_issuer_country_code(self, card_issuer_country_code):
        """
        Sets the card_issuer_country_code of this AccountLookUpInfo.
        Refer to <a href=\"/request_response_codes#iso_country_codes\">ISO Codes</a>

        :param card_issuer_country_code: The card_issuer_country_code of this AccountLookUpInfo.
        :type: str
        """
        if card_issuer_country_code is None:
            raise ValueError("Invalid value for `card_issuer_country_code`, must not be `None`")

        self._card_issuer_country_code = card_issuer_country_code

    @property
    def online_gambing_block_indicator(self):
        """
        Gets the online_gambing_block_indicator of this AccountLookUpInfo.
        Indicates whether the PAN submitted in the request can receive Push Funds(OCTs) for gambling-type transactions. If the value is 'Y', then the account cannot receive gambling Push Funds (OCTs). If the value is 'N', the account can receive gambling Push Funds (OCTs).

        :return: The online_gambing_block_indicator of this AccountLookUpInfo.
        :rtype: str
        """
        return self._online_gambing_block_indicator

    @online_gambing_block_indicator.setter
    def online_gambing_block_indicator(self, online_gambing_block_indicator):
        """
        Sets the online_gambing_block_indicator of this AccountLookUpInfo.
        Indicates whether the PAN submitted in the request can receive Push Funds(OCTs) for gambling-type transactions. If the value is 'Y', then the account cannot receive gambling Push Funds (OCTs). If the value is 'N', the account can receive gambling Push Funds (OCTs).

        :param online_gambing_block_indicator: The online_gambing_block_indicator of this AccountLookUpInfo.
        :type: str
        """
        if online_gambing_block_indicator is None:
            raise ValueError("Invalid value for `online_gambing_block_indicator`, must not be `None`")

        self._online_gambing_block_indicator = online_gambing_block_indicator

    @property
    def issuer_name(self):
        """
        Gets the issuer_name of this AccountLookUpInfo.
        Issuer name of the consumer card.

        :return: The issuer_name of this AccountLookUpInfo.
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """
        Sets the issuer_name of this AccountLookUpInfo.
        Issuer name of the consumer card.

        :param issuer_name: The issuer_name of this AccountLookUpInfo.
        :type: str
        """
        if issuer_name is None:
            raise ValueError("Invalid value for `issuer_name`, must not be `None`")

        self._issuer_name = issuer_name

    @property
    def geo_restriction_ind(self):
        """
        Gets the geo_restriction_ind of this AccountLookUpInfo.
        This field will determine if the recipient issuer can accept transactions from the Originator country. If the value is 'Y', transactions cannot be accepted from the sender country. If the value is 'N', transactions are allowed.

        :return: The geo_restriction_ind of this AccountLookUpInfo.
        :rtype: str
        """
        return self._geo_restriction_ind

    @geo_restriction_ind.setter
    def geo_restriction_ind(self, geo_restriction_ind):
        """
        Sets the geo_restriction_ind of this AccountLookUpInfo.
        This field will determine if the recipient issuer can accept transactions from the Originator country. If the value is 'Y', transactions cannot be accepted from the sender country. If the value is 'N', transactions are allowed.

        :param geo_restriction_ind: The geo_restriction_ind of this AccountLookUpInfo.
        :type: str
        """
        if geo_restriction_ind is None:
            raise ValueError("Invalid value for `geo_restriction_ind`, must not be `None`")

        self._geo_restriction_ind = geo_restriction_ind

    @property
    def card_type_code(self):
        """
        Gets the card_type_code of this AccountLookUpInfo.
        The code of account funding source for the card, e.g. Credit, Debit, Prepaid, Charge, Deferred Debit.<br>Refer to <a href=\"/request_response_codes#cardTypeCode\">cardTypeCode</a>

        :return: The card_type_code of this AccountLookUpInfo.
        :rtype: str
        """
        return self._card_type_code

    @card_type_code.setter
    def card_type_code(self, card_type_code):
        """
        Sets the card_type_code of this AccountLookUpInfo.
        The code of account funding source for the card, e.g. Credit, Debit, Prepaid, Charge, Deferred Debit.<br>Refer to <a href=\"/request_response_codes#cardTypeCode\">cardTypeCode</a>

        :param card_type_code: The card_type_code of this AccountLookUpInfo.
        :type: str
        """

        self._card_type_code = card_type_code

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AccountLookUpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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