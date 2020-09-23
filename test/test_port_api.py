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
from openapi_client.api.port_api import PortApi  # noqa: E501


class TestPortApi(unittest.TestCase):
    """PortApi unit test stubs"""

    def setUp(self):
        self.api = PortApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_port_group_by_moid(self):
        """Test case for get_port_group_by_moid

        Read a 'port.Group' resource.  # noqa: E501
        """
        pass

    def test_get_port_group_list(self):
        """Test case for get_port_group_list

        Read a 'port.Group' resource.  # noqa: E501
        """
        pass

    def test_get_port_mac_binding_by_moid(self):
        """Test case for get_port_mac_binding_by_moid

        Read a 'port.MacBinding' resource.  # noqa: E501
        """
        pass

    def test_get_port_mac_binding_list(self):
        """Test case for get_port_mac_binding_list

        Read a 'port.MacBinding' resource.  # noqa: E501
        """
        pass

    def test_get_port_sub_group_by_moid(self):
        """Test case for get_port_sub_group_by_moid

        Read a 'port.SubGroup' resource.  # noqa: E501
        """
        pass

    def test_get_port_sub_group_list(self):
        """Test case for get_port_sub_group_list

        Read a 'port.SubGroup' resource.  # noqa: E501
        """
        pass

    def test_patch_port_group(self):
        """Test case for patch_port_group

        Update a 'port.Group' resource.  # noqa: E501
        """
        pass

    def test_patch_port_mac_binding(self):
        """Test case for patch_port_mac_binding

        Update a 'port.MacBinding' resource.  # noqa: E501
        """
        pass

    def test_patch_port_sub_group(self):
        """Test case for patch_port_sub_group

        Update a 'port.SubGroup' resource.  # noqa: E501
        """
        pass

    def test_update_port_group(self):
        """Test case for update_port_group

        Update a 'port.Group' resource.  # noqa: E501
        """
        pass

    def test_update_port_mac_binding(self):
        """Test case for update_port_mac_binding

        Update a 'port.MacBinding' resource.  # noqa: E501
        """
        pass

    def test_update_port_sub_group(self):
        """Test case for update_port_sub_group

        Update a 'port.SubGroup' resource.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
