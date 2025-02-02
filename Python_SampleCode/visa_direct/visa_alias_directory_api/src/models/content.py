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


class Content(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status=None, guid=None, alias_id=None, merchant_id=None, status_change_date_time=None):
        """
        Content - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'guid': 'str',
            'alias_id': 'str',
            'merchant_id': 'str',
            'status_change_date_time': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'guid': 'guid',
            'alias_id': 'aliasId',
            'merchant_id': 'merchantId',
            'status_change_date_time': 'statusChangeDateTime'
        }

        self._status = status
        self._guid = guid
        self._alias_id = alias_id
        self._merchant_id = merchant_id
        self._status_change_date_time = status_change_date_time

    @property
    def status(self):
        """
        Gets the status of this Content.
        The status of an alias.<br>For consumer alias, this value can be 'ACTIVE', 'DISABLED' or 'INACTIVE'.<br>For merchant/agent alias, this value can be 'ACTIVE' or 'DISABLED'.

        :return: The status of this Content.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Content.
        The status of an alias.<br>For consumer alias, this value can be 'ACTIVE', 'DISABLED' or 'INACTIVE'.<br>For merchant/agent alias, this value can be 'ACTIVE' or 'DISABLED'.

        :param status: The status of this Content.
        :type: str
        """

        self._status = status

    @property
    def guid(self):
        """
        Gets the guid of this Content.
        <b>Conditional</b>.  Only applicable for consumer alias report.  This attribute is uniquely used by issuer to identify their cardholders (i.e. consumer).

        :return: The guid of this Content.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this Content.
        <b>Conditional</b>.  Only applicable for consumer alias report.  This attribute is uniquely used by issuer to identify their cardholders (i.e. consumer).

        :param guid: The guid of this Content.
        :type: str
        """

        self._guid = guid

    @property
    def alias_id(self):
        """
        Gets the alias_id of this Content.
        <b>Conditional</b>.  Only applicable for merchant/agent alias report.  This attribute is used by acquirer to uniquely identify their merchant or agent.

        :return: The alias_id of this Content.
        :rtype: str
        """
        return self._alias_id

    @alias_id.setter
    def alias_id(self, alias_id):
        """
        Sets the alias_id of this Content.
        <b>Conditional</b>.  Only applicable for merchant/agent alias report.  This attribute is used by acquirer to uniquely identify their merchant or agent.

        :param alias_id: The alias_id of this Content.
        :type: str
        """

        self._alias_id = alias_id

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this Content.
        A 16 digit-number as per Mobile Push Payment Program Implementation Guide to receive payment by merchant or agent.

        :return: The merchant_id of this Content.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this Content.
        A 16 digit-number as per Mobile Push Payment Program Implementation Guide to receive payment by merchant or agent.

        :param merchant_id: The merchant_id of this Content.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def status_change_date_time(self):
        """
        Gets the status_change_date_time of this Content.
        The date and time when the status of an alias is changed.  It is in Coordinated Universal Time (UTC).

        :return: The status_change_date_time of this Content.
        :rtype: str
        """
        return self._status_change_date_time

    @status_change_date_time.setter
    def status_change_date_time(self, status_change_date_time):
        """
        Sets the status_change_date_time of this Content.
        The date and time when the status of an alias is changed.  It is in Coordinated Universal Time (UTC).

        :param status_change_date_time: The status_change_date_time of this Content.
        :type: str
        """

        self._status_change_date_time = status_change_date_time

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
        if not isinstance(other, Content):
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