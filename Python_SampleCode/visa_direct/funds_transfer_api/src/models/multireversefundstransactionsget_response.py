# coding: utf-8

"""
    Funds Transfer API

    The Funds Transfer API can pull funds from the sender&apos;s Visa account (in preparation for pushing funds to a recipient&apos;s account) in an Account Funding Transaction (AFT).  Additionally, the Funds Transfer API also provides functionality to push funds to the recipient&apos;s Visa account in an Original Credit Transaction (OCT).  If a transaction is declined, the Funds Transfer API can also return the funds to the sender&apos;s funding source in an Account Funding Transaction Reversal (AFTR). The API has been enhanced to allow originators to send their PushFundsTransactions(OCTs) and PullFundsTransactions(AFTs) to Visa for routing to multiple U.S. debit networks.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MultireversefundstransactionsgetResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, approval_code=None, fee_program_indicator=None, last4of_pan=None, status_identifier=None, transaction_identifier=None, member_comments=None, response_code=None, action_code=None, transmission_date_time=None):
        """
        MultireversefundstransactionsgetResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'approval_code': 'str',
            'fee_program_indicator': 'str',
            'last4of_pan': 'int',
            'status_identifier': 'str',
            'transaction_identifier': 'int',
            'member_comments': 'str',
            'response_code': 'str',
            'action_code': 'str',
            'transmission_date_time': 'str'
        }

        self.attribute_map = {
            'approval_code': 'approvalCode',
            'fee_program_indicator': 'feeProgramIndicator',
            'last4of_pan': 'last4ofPAN',
            'status_identifier': 'statusIdentifier',
            'transaction_identifier': 'transactionIdentifier',
            'member_comments': 'memberComments',
            'response_code': 'responseCode',
            'action_code': 'actionCode',
            'transmission_date_time': 'transmissionDateTime'
        }

        self._approval_code = approval_code
        self._fee_program_indicator = fee_program_indicator
        self._last4of_pan = last4of_pan
        self._status_identifier = status_identifier
        self._transaction_identifier = transaction_identifier
        self._member_comments = member_comments
        self._response_code = response_code
        self._action_code = action_code
        self._transmission_date_time = transmission_date_time

    @property
    def approval_code(self):
        """
        Gets the approval_code of this MultireversefundstransactionsgetResponse.
        The authorization code from the issuer.

        :return: The approval_code of this MultireversefundstransactionsgetResponse.
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """
        Sets the approval_code of this MultireversefundstransactionsgetResponse.
        The authorization code from the issuer.

        :param approval_code: The approval_code of this MultireversefundstransactionsgetResponse.
        :type: str
        """

        self._approval_code = approval_code

    @property
    def fee_program_indicator(self):
        """
        Gets the fee_program_indicator of this MultireversefundstransactionsgetResponse.
        

        :return: The fee_program_indicator of this MultireversefundstransactionsgetResponse.
        :rtype: str
        """
        return self._fee_program_indicator

    @fee_program_indicator.setter
    def fee_program_indicator(self, fee_program_indicator):
        """
        Sets the fee_program_indicator of this MultireversefundstransactionsgetResponse.
        

        :param fee_program_indicator: The fee_program_indicator of this MultireversefundstransactionsgetResponse.
        :type: str
        """

        self._fee_program_indicator = fee_program_indicator

    @property
    def last4of_pan(self):
        """
        Gets the last4of_pan of this MultireversefundstransactionsgetResponse.
        This field contains the last four digits of the cardholder primary account number (PAN)

        :return: The last4of_pan of this MultireversefundstransactionsgetResponse.
        :rtype: int
        """
        return self._last4of_pan

    @last4of_pan.setter
    def last4of_pan(self, last4of_pan):
        """
        Sets the last4of_pan of this MultireversefundstransactionsgetResponse.
        This field contains the last four digits of the cardholder primary account number (PAN)

        :param last4of_pan: The last4of_pan of this MultireversefundstransactionsgetResponse.
        :type: int
        """

        self._last4of_pan = last4of_pan

    @property
    def status_identifier(self):
        """
        Gets the status_identifier of this MultireversefundstransactionsgetResponse.
        

        :return: The status_identifier of this MultireversefundstransactionsgetResponse.
        :rtype: str
        """
        return self._status_identifier

    @status_identifier.setter
    def status_identifier(self, status_identifier):
        """
        Sets the status_identifier of this MultireversefundstransactionsgetResponse.
        

        :param status_identifier: The status_identifier of this MultireversefundstransactionsgetResponse.
        :type: str
        """
        if status_identifier is None:
            raise ValueError("Invalid value for `status_identifier`, must not be `None`")

        self._status_identifier = status_identifier

    @property
    def transaction_identifier(self):
        """
        Gets the transaction_identifier of this MultireversefundstransactionsgetResponse.
        The VisaNet reference number for the transaction<br><br><b>Note: </b><br>transactionIdentifier is a Visa generated field that client recieves in the response message.<br><b>Note: </b>As an exception Visa allows clients to use the transactionIdentifier received in the AFT response into the subsequent OCT message - this is to simplify matching the pull and push transaction pair and reconciliation.

        :return: The transaction_identifier of this MultireversefundstransactionsgetResponse.
        :rtype: int
        """
        return self._transaction_identifier

    @transaction_identifier.setter
    def transaction_identifier(self, transaction_identifier):
        """
        Sets the transaction_identifier of this MultireversefundstransactionsgetResponse.
        The VisaNet reference number for the transaction<br><br><b>Note: </b><br>transactionIdentifier is a Visa generated field that client recieves in the response message.<br><b>Note: </b>As an exception Visa allows clients to use the transactionIdentifier received in the AFT response into the subsequent OCT message - this is to simplify matching the pull and push transaction pair and reconciliation.

        :param transaction_identifier: The transaction_identifier of this MultireversefundstransactionsgetResponse.
        :type: int
        """
        if transaction_identifier is None:
            raise ValueError("Invalid value for `transaction_identifier`, must not be `None`")

        self._transaction_identifier = transaction_identifier

    @property
    def member_comments(self):
        """
        Gets the member_comments of this MultireversefundstransactionsgetResponse.
        This field can be optionally used to send and receive comments by service providers. Issuers can optionally include new text in this field in the response. If the issuer does not include this field, Visa will inject the value from the request in the response and send it back to the service provider.

        :return: The member_comments of this MultireversefundstransactionsgetResponse.
        :rtype: str
        """
        return self._member_comments

    @member_comments.setter
    def member_comments(self, member_comments):
        """
        Sets the member_comments of this MultireversefundstransactionsgetResponse.
        This field can be optionally used to send and receive comments by service providers. Issuers can optionally include new text in this field in the response. If the issuer does not include this field, Visa will inject the value from the request in the response and send it back to the service provider.

        :param member_comments: The member_comments of this MultireversefundstransactionsgetResponse.
        :type: str
        """

        self._member_comments = member_comments

    @property
    def response_code(self):
        """
        Gets the response_code of this MultireversefundstransactionsgetResponse.
        The source for the response; typically, either the recipient issuer or a Visa system.<br><br>Refer to <a href=\"/request_response_codes#response_code\">responseCode</a><br><b>Note: </b>: The VisaNet Response Source for the transaction

        :return: The response_code of this MultireversefundstransactionsgetResponse.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this MultireversefundstransactionsgetResponse.
        The source for the response; typically, either the recipient issuer or a Visa system.<br><br>Refer to <a href=\"/request_response_codes#response_code\">responseCode</a><br><b>Note: </b>: The VisaNet Response Source for the transaction

        :param response_code: The response_code of this MultireversefundstransactionsgetResponse.
        :type: str
        """
        if response_code is None:
            raise ValueError("Invalid value for `response_code`, must not be `None`")

        self._response_code = response_code

    @property
    def action_code(self):
        """
        Gets the action_code of this MultireversefundstransactionsgetResponse.
        The results of the transaction request <br><br>Refer to <a href=\"/request_response_codes#action_code\">actionCode</a><br><b>Note: </b>: The VisaNet Response Code for the transaction

        :return: The action_code of this MultireversefundstransactionsgetResponse.
        :rtype: str
        """
        return self._action_code

    @action_code.setter
    def action_code(self, action_code):
        """
        Sets the action_code of this MultireversefundstransactionsgetResponse.
        The results of the transaction request <br><br>Refer to <a href=\"/request_response_codes#action_code\">actionCode</a><br><b>Note: </b>: The VisaNet Response Code for the transaction

        :param action_code: The action_code of this MultireversefundstransactionsgetResponse.
        :type: str
        """
        if action_code is None:
            raise ValueError("Invalid value for `action_code`, must not be `None`")

        self._action_code = action_code

    @property
    def transmission_date_time(self):
        """
        Gets the transmission_date_time of this MultireversefundstransactionsgetResponse.
        Example: 2016-01-15T07:03:52:000Z

        :return: The transmission_date_time of this MultireversefundstransactionsgetResponse.
        :rtype: str
        """
        return self._transmission_date_time

    @transmission_date_time.setter
    def transmission_date_time(self, transmission_date_time):
        """
        Sets the transmission_date_time of this MultireversefundstransactionsgetResponse.
        Example: 2016-01-15T07:03:52:000Z

        :param transmission_date_time: The transmission_date_time of this MultireversefundstransactionsgetResponse.
        :type: str
        """
        if transmission_date_time is None:
            raise ValueError("Invalid value for `transmission_date_time`, must not be `None`")

        self._transmission_date_time = transmission_date_time

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
        if not isinstance(other, MultireversefundstransactionsgetResponse):
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