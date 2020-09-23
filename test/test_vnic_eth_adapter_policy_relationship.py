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
from openapi_client.model.mo_base_mo_relationship import MoBaseMoRelationship
from openapi_client.model.mo_mo_ref import MoMoRef
from openapi_client.model.mo_tag import MoTag
from openapi_client.model.mo_version_context import MoVersionContext
from openapi_client.model.organization_organization_relationship import OrganizationOrganizationRelationship
from openapi_client.model.vnic_arfs_settings import VnicArfsSettings
from openapi_client.model.vnic_completion_queue_settings import VnicCompletionQueueSettings
from openapi_client.model.vnic_eth_adapter_policy import VnicEthAdapterPolicy
from openapi_client.model.vnic_eth_interrupt_settings import VnicEthInterruptSettings
from openapi_client.model.vnic_eth_rx_queue_settings import VnicEthRxQueueSettings
from openapi_client.model.vnic_eth_tx_queue_settings import VnicEthTxQueueSettings
from openapi_client.model.vnic_nvgre_settings import VnicNvgreSettings
from openapi_client.model.vnic_roce_settings import VnicRoceSettings
from openapi_client.model.vnic_rss_hash_settings import VnicRssHashSettings
from openapi_client.model.vnic_tcp_offload_settings import VnicTcpOffloadSettings
from openapi_client.model.vnic_vxlan_settings import VnicVxlanSettings
globals()['DisplayNames'] = DisplayNames
globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
globals()['MoMoRef'] = MoMoRef
globals()['MoTag'] = MoTag
globals()['MoVersionContext'] = MoVersionContext
globals()['OrganizationOrganizationRelationship'] = OrganizationOrganizationRelationship
globals()['VnicArfsSettings'] = VnicArfsSettings
globals()['VnicCompletionQueueSettings'] = VnicCompletionQueueSettings
globals()['VnicEthAdapterPolicy'] = VnicEthAdapterPolicy
globals()['VnicEthInterruptSettings'] = VnicEthInterruptSettings
globals()['VnicEthRxQueueSettings'] = VnicEthRxQueueSettings
globals()['VnicEthTxQueueSettings'] = VnicEthTxQueueSettings
globals()['VnicNvgreSettings'] = VnicNvgreSettings
globals()['VnicRoceSettings'] = VnicRoceSettings
globals()['VnicRssHashSettings'] = VnicRssHashSettings
globals()['VnicTcpOffloadSettings'] = VnicTcpOffloadSettings
globals()['VnicVxlanSettings'] = VnicVxlanSettings
from openapi_client.model.vnic_eth_adapter_policy_relationship import VnicEthAdapterPolicyRelationship


class TestVnicEthAdapterPolicyRelationship(unittest.TestCase):
    """VnicEthAdapterPolicyRelationship unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVnicEthAdapterPolicyRelationship(self):
        """Test VnicEthAdapterPolicyRelationship"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VnicEthAdapterPolicyRelationship()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
