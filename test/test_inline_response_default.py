"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.foo import Foo
globals()['Foo'] = Foo
from openapi_client.model.inline_response_default import InlineResponseDefault


class TestInlineResponseDefault(unittest.TestCase):
    """InlineResponseDefault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponseDefault(self):
        """Test InlineResponseDefault"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineResponseDefault()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
