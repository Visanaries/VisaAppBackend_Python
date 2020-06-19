# coding: utf-8

"""
    mVisa API

    mVisa is a simple, secure and fast way to pay and be paid using mobile phones. mVisa enables a range of payment use cases and is technology agnostic-leveraging evolving POS environment such as QR codes and works on both smart or feature phones.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest
import datetime
import pytz
import random
import string
import re
import json

from src.apis.mvisa_api import MvisaApi
from src.configuration import Configuration
from globalConfig import GlobalConfig


class TestMvisaApi(unittest.TestCase):
    """ MvisaApi unit test stubs """

    @classmethod
    def setUpClass(self):
        print("---------------------------------------Tests---------------------------------------\nProduct Name: Visa Direct\nApi Name: mVisa API")
        globalConfig = GlobalConfig()
        config = Configuration()
        config.username = globalConfig.userName
        config.password = globalConfig.password
        config.cert_file = globalConfig.certificatePath
        config.key_file = globalConfig.privateKeyPath
        config.shared_secret = globalConfig.sharedSecret
        config.api_key['apikey'] = globalConfig.apiKey
        config.ssl_ca_cert = globalConfig.caCertPath
        config.proxy_url = globalConfig.proxyUrl
        self.api = MvisaApi(None)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def transformPayload(self, payload):
        payload = self.editLocalTime(payload)
        payload = self.addRandom(payload)
        payload = json.loads(payload)
        return payload

    def editLocalTime(self, payload):
        timezone = pytz.timezone("America/Los_Angeles")
        timestamp = timezone.localize(datetime.datetime.now()).strftime('%Y-%m-%dT%H:%M:%S')
        pattern = re.compile('"localTransactionDateTime":".{19}"', re.IGNORECASE)
        replacement = '"localTransactionDateTime": "'+timestamp+'"'
        payload = re.sub(pattern, replacement, payload)

        timestamp = timezone.localize(datetime.datetime.now()).strftime('%m%d%H%M%S')
        pattern = re.compile('"dateTimeLocal":".{10}"', re.IGNORECASE)
        replacement = '"dateTimeLocal": "'+timestamp+'"'
        payload = re.sub(pattern, replacement, payload)
        return payload

    def addRandom(self, payload):
        if payload == 'mle_keyId':
            return self.mleKeyId
        payload = re.sub(r'random_string', ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)), payload)
        payload = re.sub(r'random_integer', ''.join(random.choice(string.digits) for _ in range(8)), payload)
        payload= re.sub(r'random', ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)), payload)
        return payload

    """
    Test case for getcash_in_push_payments_get

    .
    """
    def testgetcash_in_push_payments_get(self):
        print("\ngetcash_in_push_payments_get")
        result = self.api.getcash_in_push_payments_get(self.addRandom('random'))
        pass

    """
    Test case for getcash_out_payments_get

    .
    """
    def testgetcash_out_payments_get(self):
        print("\ngetcash_out_payments_get")
        result = self.api.getcash_out_payments_get(self.addRandom('random'))
        pass

    """
    Test case for getmerchant_push_payment_get

    .
    """
    def testgetmerchant_push_payment_get(self):
        print("\ngetmerchant_push_payment_get")
        result = self.api.getmerchant_push_payment_get(self.addRandom('random'))
        pass

    """
    Test case for postcash_in_push_payments

    .
    """
    def testpostcash_in_push_payments(self):
        print("\npostcash_in_push_payments")
        result = self.api.postcash_in_push_payments(self.transformPayload('{"senderAccountNumber":"4541237895236","localTransactionDateTime":"2018-05-30T09:29:29","businessApplicationId":"CI","merchantCategoryCode":"6012","transactionCurrencyCode":"840","acquiringBin":"400171","acquirerCountryCode":"643","retrievalReferenceNumber":"430000367618","senderReference":"1234","cardAcceptor":{"idCode":"ID-Code123","name":"Test Merchant","address":{"country":"IN","city":"Bangalore"}},"recipientPrimaryAccountNumber":"4123640062698797","systemsTraceAuditNumber":"313042","amount":"124.05","senderName":"Mohammed Qasim"}'))
        pass

    """
    Test case for postcash_out_push_payments_post

    .
    """
    def testpostcash_out_push_payments_post(self):
        print("\npostcash_out_push_payments_post")
        result = self.api.postcash_out_push_payments_post(self.transformPayload('{"senderAccountNumber":"456789123456","localTransactionDateTime":"2018-05-30T09:51:18","businessApplicationId":"CO","merchantCategoryCode":"6012","transactionCurrencyCode":"356","acquiringBin":"400171","acquirerCountryCode":"643","retrievalReferenceNumber":"412123412878","senderReference":"REFNUM123","cardAcceptor":{"idCode":"CA-IDCode-77765","name":"Test merchant","address":{"country":"IN","city":"merchant city"}},"recipientPrimaryAccountNumber":"4123640062698797","systemsTraceAuditNumber":"567889","amount":"124.05","senderName":"Mohammed Qasim"}'))
        pass

    """
    Test case for postmerchant_push_payments_post

    .
    """
    def testpostmerchant_push_payments_post(self):
        print("\npostmerchant_push_payments_post")
        result = self.api.postmerchant_push_payments_post(self.transformPayload('{"senderAccountNumber":"4027290077881587","localTransactionDateTime":"2018-05-30T05:36:14","purchaseIdentifier":{"type":"0","referenceNumber":"REF_123456789123456789123"},"merchantCategoryCode":"5812","feeProgramIndicator":"123","transactionCurrencyCode":"356","acquiringBin":"408972","acquirerCountryCode":"356","retrievalReferenceNumber":"412770451035","senderReference":"","secondaryId":"123TEST","cardAcceptor":{"idCode":"CA-IDCode-77765","name":"Visa Inc. USA-Foster City","address":{"country":"IN","city":"KOLKATA"}},"recipientPrimaryAccountNumber":"4123640062698797","systemsTraceAuditNumber":"451035","businessApplicationId":"MP","amount":"124.05","senderName":"Jasper"}'))
        pass


if __name__ == '__main__':
    unittest.main()


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