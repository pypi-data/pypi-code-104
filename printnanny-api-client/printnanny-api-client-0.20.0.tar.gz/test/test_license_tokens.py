# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.license_tokens import LicenseTokens  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestLicenseTokens(unittest.TestCase):
    """LicenseTokens unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LicenseTokens
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.license_tokens.LicenseTokens()  # noqa: E501
        if include_optional :
            return LicenseTokens(
                printnanny_api_token = '', 
                printnanny_api_url = '', 
                honeycomb_dataset = '', 
                honeycomb_api_key = ''
            )
        else :
            return LicenseTokens(
        )

    def testLicenseTokens(self):
        """Test LicenseTokens"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
