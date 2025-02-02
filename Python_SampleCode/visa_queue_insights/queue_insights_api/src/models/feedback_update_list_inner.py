# coding: utf-8

"""
    Queue Insights API

    Visa Queue Insights - Deliver Predicted Waiting Time for select merchants to our clients through the Visa Developer Platform

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FeedbackUpdateListInner(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status=None, feedback_correlation_id=None):
        """
        FeedbackUpdateListInner - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'feedback_correlation_id': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'feedback_correlation_id': 'feedbackCorrelationID'
        }

        self._status = status
        self._feedback_correlation_id = feedback_correlation_id

    @property
    def status(self):
        """
        Gets the status of this FeedbackUpdateListInner.
        Status of this feedback by the client

        :return: The status of this FeedbackUpdateListInner.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FeedbackUpdateListInner.
        Status of this feedback by the client

        :param status: The status of this FeedbackUpdateListInner.
        :type: str
        """

        self._status = status

    @property
    def feedback_correlation_id(self):
        """
        Gets the feedback_correlation_id of this FeedbackUpdateListInner.
        feedbackCorrelationID for which the feedback was provided by the client

        :return: The feedback_correlation_id of this FeedbackUpdateListInner.
        :rtype: str
        """
        return self._feedback_correlation_id

    @feedback_correlation_id.setter
    def feedback_correlation_id(self, feedback_correlation_id):
        """
        Sets the feedback_correlation_id of this FeedbackUpdateListInner.
        feedbackCorrelationID for which the feedback was provided by the client

        :param feedback_correlation_id: The feedback_correlation_id of this FeedbackUpdateListInner.
        :type: str
        """

        self._feedback_correlation_id = feedback_correlation_id

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
        if not isinstance(other, FeedbackUpdateListInner):
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