"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.outer_enum import OuterEnum
from openapi_client.model.outer_enum_default_value import OuterEnumDefaultValue
from openapi_client.model.outer_enum_integer import OuterEnumInteger
from openapi_client.model.outer_enum_integer_default_value import OuterEnumIntegerDefaultValue
globals()['OuterEnum'] = OuterEnum
globals()['OuterEnumDefaultValue'] = OuterEnumDefaultValue
globals()['OuterEnumInteger'] = OuterEnumInteger
globals()['OuterEnumIntegerDefaultValue'] = OuterEnumIntegerDefaultValue
from openapi_client.model.enum_test import EnumTest


class TestEnumTest(unittest.TestCase):
    """EnumTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnumTest(self):
        """Test EnumTest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnumTest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
