# coding: utf-8

"""
    Visa Alias Directory API

    Visa Alias Directory Services provide an ability to resolve an identifier (i.e. an alias) such as mobile phone number, email address, short name, or nickname, to a Visa card account (non-Visa soon) through APIs.  A Visa client can use these APIs to allow consumers provide an alias instead of inputting a card number (PAN) to use Visa Direct push payment services such as person-to-person (P2P) money transfers, mVisa merchant payments and mVisa agent deposits and withdrawals.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import io
import json
import ssl
import certifi
import logging
import re

import time
from jwcrypto import jwk, jwe

# python 2 and python 3 compatibility library
from six import PY3
from six.moves.urllib.parse import urlencode

from .configuration import Configuration

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')


logger = logging.getLogger(__name__)

class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """
        Returns a dictionary of the response headers.
        """
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """
        Returns a given response header.
        """
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, pools_size=4, maxsize=4):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680
        # maxsize is the number of requests to host that are allowed in parallel
        # ca_certs vs cert_file vs key_file
        # http://stackoverflow.com/a/23957365/2985775

        # cert_reqs
        if Configuration().verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if Configuration().ssl_ca_cert:
            ca_certs = Configuration().ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        # cert_file
        cert_file = Configuration().cert_file

        # key file
        key_file = Configuration().key_file

        # https pool manager
        if Configuration().proxy_url != '' and Configuration().proxy_url != None:
            self.pool_manager = urllib3.ProxyManager(
                Configuration().proxy_url,
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=cert_file,
                key_file=key_file
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=cert_file,
                key_file=key_file
            )
    def encrypt(self, payload):
        config = Configuration()
        payload = json.dumps(payload)
        protected_header = {
            "alg": "RSA-OAEP-256",
            "enc": "A128GCM",
            "kid": config.api_key['keyId'],
            "iat": int(round(time.time() * 1000))
        }
        jwetoken = jwe.JWE(payload.encode('utf-8'),
                            recipient=self.loadPem(config.encryption_public_key_path),
                            protected=protected_header)
        encryptedPayload = jwetoken.serialize(compact=True)
        return {"encData": encryptedPayload}

    def decrypt(self, encPayload):
        if type(encPayload) is str:
            payload = json.loads(encPayload)
        if payload.get('encData', False):
            config = Configuration()
            jwetoken = jwe.JWE()
            jwetoken.deserialize(payload["encData"], key=self.loadPem(config.decryption_private_key_path))
            return jwetoken.payload
        return encPayload

    def loadPem(self, filePath):
        with open(filePath, "rb") as pemfile:
            return jwk.JWK.from_pem(pemfile.read())

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True, _request_timeout=None):
        """
        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will be returned without
                                 reading/decoding response data. Default is True.
        :param _request_timeout: timeout setting for this request. If one number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']
        config = Configuration()
        if 'keyId' in config.api_key and body :
            body = self.encrypt(body)
        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, ) if PY3 else (int, long)):
                timeout = urllib3.Timeout(total=_request_timeout)
            elif isinstance(_request_timeout, tuple) and len(_request_timeout) == 2:
                timeout = urllib3.Timeout(connect=_request_timeout[0], read=_request_timeout[1])

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = None
                    if body:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(method, url,
                                                  body=request_body,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':
                    r = self.pool_manager.request(method, url,
                                                  fields=post_params,
                                                  encode_multipart=False,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct Content-Type
                    # which generated by urllib3 will be overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(method, url,
                                                  fields=post_params,
                                                  encode_multipart=True,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is provided
                # in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(method, url,
                                                  body=request_body,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided arguments.
                             Please check that your arguments match declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)
        print (r.status)
        if _preload_content:
            r = RESTResponse(r)

            # In the python 3, the response.data is bytes.
            # we need to decode it to string.
            if PY3:
                r.data = r.data.decode('utf8')
            if 'keyId' in config.api_key:
                r.data = self.decrypt(r.data)
            # log response body
            logger.debug("response body: %s", r.data)

        if r.status not in range(200, 206):
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None, _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
             _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
            _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
              _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """
        Custom error messages for exception
        """
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message

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