# coding: utf-8

"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations. The Intersight OpenAPI document defines the complete set of properties that are returned in the HTTP response. From that perspective, a client can expect that no additional properties are returned, unless these properties are explicitly defined in the OpenAPI document. However, when a client uses an older version of the Intersight OpenAPI document, the server may send additional properties because the software is more recent than the client. In that case, the client may receive properties that it does not know about. Some generated SDKs perform a strict validation of the HTTP response body against the OpenAPI document. This document was created on 2020-06-30T07:31:54Z.  # noqa: E501

    The version of the OpenAPI document: 1.0.9-1950
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.display_names import DisplayNames
from openapi_client.model.equipment_base import EquipmentBase
from openapi_client.model.equipment_fex import EquipmentFex
from openapi_client.model.equipment_io_card import EquipmentIoCard
from openapi_client.model.equipment_io_card_base_all_of import EquipmentIoCardBaseAllOf
from openapi_client.model.ether_host_port_relationship import EtherHostPortRelationship
from openapi_client.model.ether_network_port_relationship import EtherNetworkPortRelationship
from openapi_client.model.management_controller_relationship import ManagementControllerRelationship
from openapi_client.model.mo_base_mo_relationship import MoBaseMoRelationship
from openapi_client.model.mo_tag import MoTag
from openapi_client.model.mo_version_context import MoVersionContext
globals()['DisplayNames'] = DisplayNames
globals()['EquipmentBase'] = EquipmentBase
globals()['EquipmentFex'] = EquipmentFex
globals()['EquipmentIoCard'] = EquipmentIoCard
globals()['EquipmentIoCardBaseAllOf'] = EquipmentIoCardBaseAllOf
globals()['EtherHostPortRelationship'] = EtherHostPortRelationship
globals()['EtherNetworkPortRelationship'] = EtherNetworkPortRelationship
globals()['ManagementControllerRelationship'] = ManagementControllerRelationship
globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
globals()['MoTag'] = MoTag
globals()['MoVersionContext'] = MoVersionContext
from openapi_client.model.equipment_io_card_base import EquipmentIoCardBase


class TestEquipmentIoCardBase(unittest.TestCase):
    """EquipmentIoCardBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEquipmentIoCardBase(self):
        """Test EquipmentIoCardBase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EquipmentIoCardBase()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()