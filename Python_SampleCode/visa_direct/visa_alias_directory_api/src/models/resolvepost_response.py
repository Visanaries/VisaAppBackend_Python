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


class ResolvepostResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, city=None, merchant_category_code=None, url=None, country=None, transaction_currency_code=None, recipient_primary_account_number=None, tip_convenience_fee_indicator=None, card_type=None, convenience_fee_amount=None, point_of_initiation_method=None, postal_code=None, recipient_name=None, issuer_name=None, convenience_fee_percentage=None, account_look_up_info=None):
        """
        ResolvepostResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'city': 'str',
            'merchant_category_code': 'str',
            'url': 'str',
            'country': 'str',
            'transaction_currency_code': 'str',
            'recipient_primary_account_number': 'str',
            'tip_convenience_fee_indicator': 'str',
            'card_type': 'str',
            'convenience_fee_amount': 'str',
            'point_of_initiation_method': 'str',
            'postal_code': 'str',
            'recipient_name': 'str',
            'issuer_name': 'str',
            'convenience_fee_percentage': 'str',
            'account_look_up_info': 'AccountLookUpInfo'
        }

        self.attribute_map = {
            'city': 'city',
            'merchant_category_code': 'merchantCategoryCode',
            'url': 'url',
            'country': 'country',
            'transaction_currency_code': 'transactionCurrencyCode',
            'recipient_primary_account_number': 'recipientPrimaryAccountNumber',
            'tip_convenience_fee_indicator': 'tipConvenienceFeeIndicator',
            'card_type': 'cardType',
            'convenience_fee_amount': 'convenienceFeeAmount',
            'point_of_initiation_method': 'pointOfInitiationMethod',
            'postal_code': 'postalCode',
            'recipient_name': 'recipientName',
            'issuer_name': 'issuerName',
            'convenience_fee_percentage': 'convenienceFeePercentage',
            'account_look_up_info': 'accountLookUpInfo'
        }

        self._city = city
        self._merchant_category_code = merchant_category_code
        self._url = url
        self._country = country
        self._transaction_currency_code = transaction_currency_code
        self._recipient_primary_account_number = recipient_primary_account_number
        self._tip_convenience_fee_indicator = tip_convenience_fee_indicator
        self._card_type = card_type
        self._convenience_fee_amount = convenience_fee_amount
        self._point_of_initiation_method = point_of_initiation_method
        self._postal_code = postal_code
        self._recipient_name = recipient_name
        self._issuer_name = issuer_name
        self._convenience_fee_percentage = convenience_fee_percentage
        self._account_look_up_info = account_look_up_info

    @property
    def city(self):
        """
        Gets the city of this ResolvepostResponse.
        City of the recipient.  Recipient can be a consumer, merchant or agent.

        :return: The city of this ResolvepostResponse.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this ResolvepostResponse.
        City of the recipient.  Recipient can be a consumer, merchant or agent.

        :param city: The city of this ResolvepostResponse.
        :type: str
        """

        self._city = city

    @property
    def merchant_category_code(self):
        """
        Gets the merchant_category_code of this ResolvepostResponse.
        <b>Conditional.</b>  Merchant Category Code. This attribute will only be returned if businessApplicationId=MP, CO

        :return: The merchant_category_code of this ResolvepostResponse.
        :rtype: str
        """
        return self._merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, merchant_category_code):
        """
        Sets the merchant_category_code of this ResolvepostResponse.
        <b>Conditional.</b>  Merchant Category Code. This attribute will only be returned if businessApplicationId=MP, CO

        :param merchant_category_code: The merchant_category_code of this ResolvepostResponse.
        :type: str
        """

        self._merchant_category_code = merchant_category_code

    @property
    def url(self):
        """
        Gets the url of this ResolvepostResponse.
        <b>Optional.</b>  An URL of a landing page that contains participating issuers will be returned to originator if an alias cannot be found in Visa Alias Directory and <b>HTTP status code = 404</b>.  Originator can notify unregistered recipient with this URL so that he/she can select preferred issuer for alias registration.<br><b>Note:</b>This attribute is only applicable to selective markets, originator will receive this URL instead of error JSON response for processing if HTTP status code = 404.  Contact Visa's representative for details.

        :return: The url of this ResolvepostResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ResolvepostResponse.
        <b>Optional.</b>  An URL of a landing page that contains participating issuers will be returned to originator if an alias cannot be found in Visa Alias Directory and <b>HTTP status code = 404</b>.  Originator can notify unregistered recipient with this URL so that he/she can select preferred issuer for alias registration.<br><b>Note:</b>This attribute is only applicable to selective markets, originator will receive this URL instead of error JSON response for processing if HTTP status code = 404.  Contact Visa's representative for details.

        :param url: The url of this ResolvepostResponse.
        :type: str
        """

        self._url = url

    @property
    def country(self):
        """
        Gets the country of this ResolvepostResponse.
        Country code of the recipient. As defined by ISO 3166.

        :return: The country of this ResolvepostResponse.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this ResolvepostResponse.
        Country code of the recipient. As defined by ISO 3166.

        :param country: The country of this ResolvepostResponse.
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")

        self._country = country

    @property
    def transaction_currency_code(self):
        """
        Gets the transaction_currency_code of this ResolvepostResponse.
        <b>Conditional.</b>  This is the transaction currency code that a merchant can accept for payment. This attribute will only be returned if businessApplicationId=MP, CO. As defined by ISO 4217.

        :return: The transaction_currency_code of this ResolvepostResponse.
        :rtype: str
        """
        return self._transaction_currency_code

    @transaction_currency_code.setter
    def transaction_currency_code(self, transaction_currency_code):
        """
        Sets the transaction_currency_code of this ResolvepostResponse.
        <b>Conditional.</b>  This is the transaction currency code that a merchant can accept for payment. This attribute will only be returned if businessApplicationId=MP, CO. As defined by ISO 4217.

        :param transaction_currency_code: The transaction_currency_code of this ResolvepostResponse.
        :type: str
        """

        self._transaction_currency_code = transaction_currency_code

    @property
    def recipient_primary_account_number(self):
        """
        Gets the recipient_primary_account_number of this ResolvepostResponse.
        Depending on the businessApplicationId of the request, this attribute can contain the consumer card number, mVisa merchant ID (16-digit) or mVisa agent ID (16-digit).

        :return: The recipient_primary_account_number of this ResolvepostResponse.
        :rtype: str
        """
        return self._recipient_primary_account_number

    @recipient_primary_account_number.setter
    def recipient_primary_account_number(self, recipient_primary_account_number):
        """
        Sets the recipient_primary_account_number of this ResolvepostResponse.
        Depending on the businessApplicationId of the request, this attribute can contain the consumer card number, mVisa merchant ID (16-digit) or mVisa agent ID (16-digit).

        :param recipient_primary_account_number: The recipient_primary_account_number of this ResolvepostResponse.
        :type: str
        """
        if recipient_primary_account_number is None:
            raise ValueError("Invalid value for `recipient_primary_account_number`, must not be `None`")

        self._recipient_primary_account_number = recipient_primary_account_number

    @property
    def tip_convenience_fee_indicator(self):
        """
        Gets the tip_convenience_fee_indicator of this ResolvepostResponse.
        <b>Conditional.</b> Tip or Convenience Fee Indicator. This attribute will only be returned if businessApplicationId=MP.

        :return: The tip_convenience_fee_indicator of this ResolvepostResponse.
        :rtype: str
        """
        return self._tip_convenience_fee_indicator

    @tip_convenience_fee_indicator.setter
    def tip_convenience_fee_indicator(self, tip_convenience_fee_indicator):
        """
        Sets the tip_convenience_fee_indicator of this ResolvepostResponse.
        <b>Conditional.</b> Tip or Convenience Fee Indicator. This attribute will only be returned if businessApplicationId=MP.

        :param tip_convenience_fee_indicator: The tip_convenience_fee_indicator of this ResolvepostResponse.
        :type: str
        """

        self._tip_convenience_fee_indicator = tip_convenience_fee_indicator

    @property
    def card_type(self):
        """
        Gets the card_type of this ResolvepostResponse.
        <b>Conditional.</b>  Card type description. Reference to Field 62.23 — Product ID of available card products. e.g. Visa Platinum. Only applicable if businessApplicationId = “PP” or “CI”

        :return: The card_type of this ResolvepostResponse.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this ResolvepostResponse.
        <b>Conditional.</b>  Card type description. Reference to Field 62.23 — Product ID of available card products. e.g. Visa Platinum. Only applicable if businessApplicationId = “PP” or “CI”

        :param card_type: The card_type of this ResolvepostResponse.
        :type: str
        """

        self._card_type = card_type

    @property
    def convenience_fee_amount(self):
        """
        Gets the convenience_fee_amount of this ResolvepostResponse.
        <b>Conditional.</b>  The convenience fee of a fixed amount. The format of the amount is the same as defined in tag 54. Convenience amount as provided by merchant shall be passed in Field 28 of ISO or transactionFeeAmt of API message, in the Visa specifications. This attribute will only be returned if businessApplicationId=MP.

        :return: The convenience_fee_amount of this ResolvepostResponse.
        :rtype: str
        """
        return self._convenience_fee_amount

    @convenience_fee_amount.setter
    def convenience_fee_amount(self, convenience_fee_amount):
        """
        Sets the convenience_fee_amount of this ResolvepostResponse.
        <b>Conditional.</b>  The convenience fee of a fixed amount. The format of the amount is the same as defined in tag 54. Convenience amount as provided by merchant shall be passed in Field 28 of ISO or transactionFeeAmt of API message, in the Visa specifications. This attribute will only be returned if businessApplicationId=MP.

        :param convenience_fee_amount: The convenience_fee_amount of this ResolvepostResponse.
        :type: str
        """

        self._convenience_fee_amount = convenience_fee_amount

    @property
    def point_of_initiation_method(self):
        """
        Gets the point_of_initiation_method of this ResolvepostResponse.
        <b>Conditional.</b> In this two-digit field, the first character indicates the method by which the data is presented by the merchant. The second character indicates whether the data is static or dynamic. Static data refers to a situation wherein same data is presented for every transaction unlike a dynamic data wherein the information is specific to a transaction. <br>1st Character: <br>“1” = QR <br>“2” = BLE <br>“3” = NFC <br>“4”-“9” = Reserved for future use <br><br>2nd Character: <br>“1” = Static <br>“2” = Dynamic <br>“3”-“9” = Reserved for future use <br><br>Example: “11” indicates QR static code, “12” indicates QR dynamic code <br>This attribute will only be returned if businessApplicationId=MP, CO

        :return: The point_of_initiation_method of this ResolvepostResponse.
        :rtype: str
        """
        return self._point_of_initiation_method

    @point_of_initiation_method.setter
    def point_of_initiation_method(self, point_of_initiation_method):
        """
        Sets the point_of_initiation_method of this ResolvepostResponse.
        <b>Conditional.</b> In this two-digit field, the first character indicates the method by which the data is presented by the merchant. The second character indicates whether the data is static or dynamic. Static data refers to a situation wherein same data is presented for every transaction unlike a dynamic data wherein the information is specific to a transaction. <br>1st Character: <br>“1” = QR <br>“2” = BLE <br>“3” = NFC <br>“4”-“9” = Reserved for future use <br><br>2nd Character: <br>“1” = Static <br>“2” = Dynamic <br>“3”-“9” = Reserved for future use <br><br>Example: “11” indicates QR static code, “12” indicates QR dynamic code <br>This attribute will only be returned if businessApplicationId=MP, CO

        :param point_of_initiation_method: The point_of_initiation_method of this ResolvepostResponse.
        :type: str
        """

        self._point_of_initiation_method = point_of_initiation_method

    @property
    def postal_code(self):
        """
        Gets the postal_code of this ResolvepostResponse.
        Postal Code of the recipient. Recipient can be a consumer, merchant or agent.

        :return: The postal_code of this ResolvepostResponse.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this ResolvepostResponse.
        Postal Code of the recipient. Recipient can be a consumer, merchant or agent.

        :param postal_code: The postal_code of this ResolvepostResponse.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def recipient_name(self):
        """
        Gets the recipient_name of this ResolvepostResponse.
        Depending on the businessApplicationId of the request, this attribute can contain the consumer name, merchant name or agent name. Regarding consumer name, this is composed of consumer’s first, middle and last name

        :return: The recipient_name of this ResolvepostResponse.
        :rtype: str
        """
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, recipient_name):
        """
        Sets the recipient_name of this ResolvepostResponse.
        Depending on the businessApplicationId of the request, this attribute can contain the consumer name, merchant name or agent name. Regarding consumer name, this is composed of consumer’s first, middle and last name

        :param recipient_name: The recipient_name of this ResolvepostResponse.
        :type: str
        """
        if recipient_name is None:
            raise ValueError("Invalid value for `recipient_name`, must not be `None`")

        self._recipient_name = recipient_name

    @property
    def issuer_name(self):
        """
        Gets the issuer_name of this ResolvepostResponse.
        <b>Conditional.</b>  This is the issuer name of recipient’s card. Only applicable if businessApplicationId = “PP” or “CI”

        :return: The issuer_name of this ResolvepostResponse.
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """
        Sets the issuer_name of this ResolvepostResponse.
        <b>Conditional.</b>  This is the issuer name of recipient’s card. Only applicable if businessApplicationId = “PP” or “CI”

        :param issuer_name: The issuer_name of this ResolvepostResponse.
        :type: str
        """

        self._issuer_name = issuer_name

    @property
    def convenience_fee_percentage(self):
        """
        Gets the convenience_fee_percentage of this ResolvepostResponse.
        <b>Conditional.</b> The percentage convenience fee, specified as numeric value from “00.01” (for 00.01%) to “99.99” (for 99.99%). Originators are required to derive the convenience fee amount and shall pass it in Field 28 of ISO or transactionFeeAmt of API message, in the Visa specifications. This attribute will only be returned if businessApplicationId=MP.

        :return: The convenience_fee_percentage of this ResolvepostResponse.
        :rtype: str
        """
        return self._convenience_fee_percentage

    @convenience_fee_percentage.setter
    def convenience_fee_percentage(self, convenience_fee_percentage):
        """
        Sets the convenience_fee_percentage of this ResolvepostResponse.
        <b>Conditional.</b> The percentage convenience fee, specified as numeric value from “00.01” (for 00.01%) to “99.99” (for 99.99%). Originators are required to derive the convenience fee amount and shall pass it in Field 28 of ISO or transactionFeeAmt of API message, in the Visa specifications. This attribute will only be returned if businessApplicationId=MP.

        :param convenience_fee_percentage: The convenience_fee_percentage of this ResolvepostResponse.
        :type: str
        """

        self._convenience_fee_percentage = convenience_fee_percentage

    @property
    def account_look_up_info(self):
        """
        Gets the account_look_up_info of this ResolvepostResponse.

        :return: The account_look_up_info of this ResolvepostResponse.
        :rtype: AccountLookUpInfo
        """
        return self._account_look_up_info

    @account_look_up_info.setter
    def account_look_up_info(self, account_look_up_info):
        """
        Sets the account_look_up_info of this ResolvepostResponse.

        :param account_look_up_info: The account_look_up_info of this ResolvepostResponse.
        :type: AccountLookUpInfo
        """

        self._account_look_up_info = account_look_up_info

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
        if not isinstance(other, ResolvepostResponse):
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