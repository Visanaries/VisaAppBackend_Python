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


class DeleteMerchantAliaspostPayload(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alias_id=None, is_agent_alias=None, merchant_id=None):
        """
        DeleteMerchantAliaspostPayload - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alias_id': 'str',
            'is_agent_alias': 'str',
            'merchant_id': 'str'
        }

        self.attribute_map = {
            'alias_id': 'aliasId',
            'is_agent_alias': 'isAgentAlias',
            'merchant_id': 'merchantId'
        }

        self._alias_id = alias_id
        self._is_agent_alias = is_agent_alias
        self._merchant_id = merchant_id

    @property
    def alias_id(self):
        """
        Gets the alias_id of this DeleteMerchantAliaspostPayload.
        This attribute is uniquely used by acquirer to identify their merchant or agent.

        :return: The alias_id of this DeleteMerchantAliaspostPayload.
        :rtype: str
        """
        return self._alias_id

    @alias_id.setter
    def alias_id(self, alias_id):
        """
        Sets the alias_id of this DeleteMerchantAliaspostPayload.
        This attribute is uniquely used by acquirer to identify their merchant or agent.

        :param alias_id: The alias_id of this DeleteMerchantAliaspostPayload.
        :type: str
        """
        if alias_id is None:
            raise ValueError("Invalid value for `alias_id`, must not be `None`")

        self._alias_id = alias_id

    @property
    def is_agent_alias(self):
        """
        Gets the is_agent_alias of this DeleteMerchantAliaspostPayload.
        Optional and applicable for agent alias use only. If set as 'Y', agent alias to be created.

        :return: The is_agent_alias of this DeleteMerchantAliaspostPayload.
        :rtype: str
        """
        return self._is_agent_alias

    @is_agent_alias.setter
    def is_agent_alias(self, is_agent_alias):
        """
        Sets the is_agent_alias of this DeleteMerchantAliaspostPayload.
        Optional and applicable for agent alias use only. If set as 'Y', agent alias to be created.

        :param is_agent_alias: The is_agent_alias of this DeleteMerchantAliaspostPayload.
        :type: str
        """

        self._is_agent_alias = is_agent_alias

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this DeleteMerchantAliaspostPayload.
        A 16 digit-number as per Mobile Push Payment Program Implementation Guide to receive payment by merchant or agent.

        :return: The merchant_id of this DeleteMerchantAliaspostPayload.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this DeleteMerchantAliaspostPayload.
        A 16 digit-number as per Mobile Push Payment Program Implementation Guide to receive payment by merchant or agent.

        :param merchant_id: The merchant_id of this DeleteMerchantAliaspostPayload.
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")

        self._merchant_id = merchant_id

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
        if not isinstance(other, DeleteMerchantAliaspostPayload):
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