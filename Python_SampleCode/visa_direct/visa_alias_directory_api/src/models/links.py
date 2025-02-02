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


class Links(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, next=None, _self=None, previous=None, last=None, first=None):
        """
        Links - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'next': 'str',
            '_self': 'str',
            'previous': 'str',
            'last': 'str',
            'first': 'str'
        }

        self.attribute_map = {
            'next': 'next',
            '_self': 'self',
            'previous': 'previous',
            'last': 'last',
            'first': 'first'
        }

        self._next = next
        self.__self = _self
        self._previous = previous
        self._last = last
        self._first = first

    @property
    def next(self):
        """
        Gets the next of this Links.
        This attribute is the url to retrieve the content of previous page of the report if available.

        :return: The next of this Links.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this Links.
        This attribute is the url to retrieve the content of previous page of the report if available.

        :param next: The next of this Links.
        :type: str
        """

        self._next = next

    @property
    def _self(self):
        """
        Gets the _self of this Links.
        This attribute is the url to retrieve the content of current page of the report.

        :return: The _self of this Links.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this Links.
        This attribute is the url to retrieve the content of current page of the report.

        :param _self: The _self of this Links.
        :type: str
        """

        self.__self = _self

    @property
    def previous(self):
        """
        Gets the previous of this Links.
        This attribute is the url to retrieve the content of previous page of the report if available.

        :return: The previous of this Links.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """
        Sets the previous of this Links.
        This attribute is the url to retrieve the content of previous page of the report if available.

        :param previous: The previous of this Links.
        :type: str
        """

        self._previous = previous

    @property
    def last(self):
        """
        Gets the last of this Links.
        This attribute is the url to retrieve the content of last page of the report.

        :return: The last of this Links.
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this Links.
        This attribute is the url to retrieve the content of last page of the report.

        :param last: The last of this Links.
        :type: str
        """

        self._last = last

    @property
    def first(self):
        """
        Gets the first of this Links.
        This attribute is the url to retrieve the content of first page of the report.

        :return: The first of this Links.
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this Links.
        This attribute is the url to retrieve the content of first page of the report.

        :param first: The first of this Links.
        :type: str
        """

        self._first = first

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
        if not isinstance(other, Links):
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