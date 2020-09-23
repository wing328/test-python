# coding: utf-8

"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations. The Intersight OpenAPI document defines the complete set of properties that are returned in the HTTP response. From that perspective, a client can expect that no additional properties are returned, unless these properties are explicitly defined in the OpenAPI document. However, when a client uses an older version of the Intersight OpenAPI document, the server may send additional properties because the software is more recent than the client. In that case, the client may receive properties that it does not know about. Some generated SDKs perform a strict validation of the HTTP response body against the OpenAPI document. This document was created on 2020-06-30T07:31:54Z.  # noqa: E501

    The version of the OpenAPI document: 1.0.9-1950
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.license_api import LicenseApi  # noqa: E501


class TestLicenseApi(unittest.TestCase):
    """LicenseApi unit test stubs"""

    def setUp(self):
        self.api = LicenseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_license_license_info(self):
        """Test case for create_license_license_info

        Create a 'license.LicenseInfo' resource.  # noqa: E501
        """
        pass

    def test_create_license_license_reservation_op(self):
        """Test case for create_license_license_reservation_op

        Create a 'license.LicenseReservationOp' resource.  # noqa: E501
        """
        pass

    def test_get_license_account_license_data_by_moid(self):
        """Test case for get_license_account_license_data_by_moid

        Read a 'license.AccountLicenseData' resource.  # noqa: E501
        """
        pass

    def test_get_license_account_license_data_list(self):
        """Test case for get_license_account_license_data_list

        Read a 'license.AccountLicenseData' resource.  # noqa: E501
        """
        pass

    def test_get_license_customer_op_by_moid(self):
        """Test case for get_license_customer_op_by_moid

        Read a 'license.CustomerOp' resource.  # noqa: E501
        """
        pass

    def test_get_license_customer_op_list(self):
        """Test case for get_license_customer_op_list

        Read a 'license.CustomerOp' resource.  # noqa: E501
        """
        pass

    def test_get_license_license_info_by_moid(self):
        """Test case for get_license_license_info_by_moid

        Read a 'license.LicenseInfo' resource.  # noqa: E501
        """
        pass

    def test_get_license_license_info_list(self):
        """Test case for get_license_license_info_list

        Read a 'license.LicenseInfo' resource.  # noqa: E501
        """
        pass

    def test_get_license_license_reservation_op_by_moid(self):
        """Test case for get_license_license_reservation_op_by_moid

        Read a 'license.LicenseReservationOp' resource.  # noqa: E501
        """
        pass

    def test_get_license_license_reservation_op_list(self):
        """Test case for get_license_license_reservation_op_list

        Read a 'license.LicenseReservationOp' resource.  # noqa: E501
        """
        pass

    def test_get_license_smartlicense_token_by_moid(self):
        """Test case for get_license_smartlicense_token_by_moid

        Read a 'license.SmartlicenseToken' resource.  # noqa: E501
        """
        pass

    def test_get_license_smartlicense_token_list(self):
        """Test case for get_license_smartlicense_token_list

        Read a 'license.SmartlicenseToken' resource.  # noqa: E501
        """
        pass

    def test_patch_license_account_license_data(self):
        """Test case for patch_license_account_license_data

        Update a 'license.AccountLicenseData' resource.  # noqa: E501
        """
        pass

    def test_patch_license_customer_op(self):
        """Test case for patch_license_customer_op

        Update a 'license.CustomerOp' resource.  # noqa: E501
        """
        pass

    def test_patch_license_license_info(self):
        """Test case for patch_license_license_info

        Update a 'license.LicenseInfo' resource.  # noqa: E501
        """
        pass

    def test_patch_license_license_reservation_op(self):
        """Test case for patch_license_license_reservation_op

        Update a 'license.LicenseReservationOp' resource.  # noqa: E501
        """
        pass

    def test_patch_license_smartlicense_token(self):
        """Test case for patch_license_smartlicense_token

        Update a 'license.SmartlicenseToken' resource.  # noqa: E501
        """
        pass

    def test_update_license_account_license_data(self):
        """Test case for update_license_account_license_data

        Update a 'license.AccountLicenseData' resource.  # noqa: E501
        """
        pass

    def test_update_license_customer_op(self):
        """Test case for update_license_customer_op

        Update a 'license.CustomerOp' resource.  # noqa: E501
        """
        pass

    def test_update_license_license_info(self):
        """Test case for update_license_license_info

        Update a 'license.LicenseInfo' resource.  # noqa: E501
        """
        pass

    def test_update_license_license_reservation_op(self):
        """Test case for update_license_license_reservation_op

        Update a 'license.LicenseReservationOp' resource.  # noqa: E501
        """
        pass

    def test_update_license_smartlicense_token(self):
        """Test case for update_license_smartlicense_token

        Update a 'license.SmartlicenseToken' resource.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
