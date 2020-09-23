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
from openapi_client.model.firmware_base_distributable import FirmwareBaseDistributable
from openapi_client.model.firmware_component_meta import FirmwareComponentMeta
from openapi_client.model.firmware_distributable_meta_relationship import FirmwareDistributableMetaRelationship
from openapi_client.model.firmware_server_configuration_utility_distributable_all_of import FirmwareServerConfigurationUtilityDistributableAllOf
from openapi_client.model.mo_base_mo_relationship import MoBaseMoRelationship
from openapi_client.model.mo_tag import MoTag
from openapi_client.model.mo_version_context import MoVersionContext
from openapi_client.model.softwarerepository_catalog_relationship import SoftwarerepositoryCatalogRelationship
from openapi_client.model.softwarerepository_file_server import SoftwarerepositoryFileServer
from openapi_client.model.softwarerepository_release_relationship import SoftwarerepositoryReleaseRelationship
globals()['DisplayNames'] = DisplayNames
globals()['FirmwareBaseDistributable'] = FirmwareBaseDistributable
globals()['FirmwareComponentMeta'] = FirmwareComponentMeta
globals()['FirmwareDistributableMetaRelationship'] = FirmwareDistributableMetaRelationship
globals()['FirmwareServerConfigurationUtilityDistributableAllOf'] = FirmwareServerConfigurationUtilityDistributableAllOf
globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
globals()['MoTag'] = MoTag
globals()['MoVersionContext'] = MoVersionContext
globals()['SoftwarerepositoryCatalogRelationship'] = SoftwarerepositoryCatalogRelationship
globals()['SoftwarerepositoryFileServer'] = SoftwarerepositoryFileServer
globals()['SoftwarerepositoryReleaseRelationship'] = SoftwarerepositoryReleaseRelationship
from openapi_client.model.firmware_server_configuration_utility_distributable import FirmwareServerConfigurationUtilityDistributable


class TestFirmwareServerConfigurationUtilityDistributable(unittest.TestCase):
    """FirmwareServerConfigurationUtilityDistributable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFirmwareServerConfigurationUtilityDistributable(self):
        """Test FirmwareServerConfigurationUtilityDistributable"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FirmwareServerConfigurationUtilityDistributable()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
