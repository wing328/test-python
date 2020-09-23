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
from openapi_client.model.adapter_ext_eth_interface import AdapterExtEthInterface
from openapi_client.model.adapter_host_eth_interface import AdapterHostEthInterface
from openapi_client.model.adapter_host_fc_interface import AdapterHostFcInterface
from openapi_client.model.adapter_host_iscsi_interface import AdapterHostIscsiInterface
from openapi_client.model.adapter_unit import AdapterUnit
from openapi_client.model.bios_boot_mode import BiosBootMode
from openapi_client.model.bios_unit import BiosUnit
from openapi_client.model.boot_device_boot_mode import BootDeviceBootMode
from openapi_client.model.compute_blade import ComputeBlade
from openapi_client.model.compute_board import ComputeBoard
from openapi_client.model.compute_physical import ComputePhysical
from openapi_client.model.compute_rack_unit import ComputeRackUnit
from openapi_client.model.compute_server_setting import ComputeServerSetting
from openapi_client.model.display_names import DisplayNames
from openapi_client.model.equipment_abstract_device import EquipmentAbstractDevice
from openapi_client.model.equipment_base import EquipmentBase
from openapi_client.model.equipment_chassis import EquipmentChassis
from openapi_client.model.equipment_fan import EquipmentFan
from openapi_client.model.equipment_fan_module import EquipmentFanModule
from openapi_client.model.equipment_fex import EquipmentFex
from openapi_client.model.equipment_io_card import EquipmentIoCard
from openapi_client.model.equipment_io_card_base import EquipmentIoCardBase
from openapi_client.model.equipment_io_expander import EquipmentIoExpander
from openapi_client.model.equipment_locator_led import EquipmentLocatorLed
from openapi_client.model.equipment_psu import EquipmentPsu
from openapi_client.model.equipment_psu_control import EquipmentPsuControl
from openapi_client.model.equipment_rack_enclosure import EquipmentRackEnclosure
from openapi_client.model.equipment_rack_enclosure_slot import EquipmentRackEnclosureSlot
from openapi_client.model.equipment_shared_io_module import EquipmentSharedIoModule
from openapi_client.model.equipment_switch_card import EquipmentSwitchCard
from openapi_client.model.equipment_system_io_controller import EquipmentSystemIoController
from openapi_client.model.equipment_tpm import EquipmentTpm
from openapi_client.model.equipment_transceiver import EquipmentTransceiver
from openapi_client.model.ether_host_port import EtherHostPort
from openapi_client.model.ether_network_port import EtherNetworkPort
from openapi_client.model.ether_physical_port import EtherPhysicalPort
from openapi_client.model.ether_physical_port_base import EtherPhysicalPortBase
from openapi_client.model.ether_port_channel import EtherPortChannel
from openapi_client.model.fault_instance import FaultInstance
from openapi_client.model.fc_physical_port import FcPhysicalPort
from openapi_client.model.fc_port_channel import FcPortChannel
from openapi_client.model.firmware_running_firmware import FirmwareRunningFirmware
from openapi_client.model.graphics_card import GraphicsCard
from openapi_client.model.graphics_controller import GraphicsController
from openapi_client.model.inventory_base_all_of import InventoryBaseAllOf
from openapi_client.model.inventory_generic_inventory import InventoryGenericInventory
from openapi_client.model.inventory_generic_inventory_holder import InventoryGenericInventoryHolder
from openapi_client.model.ls_service_profile import LsServiceProfile
from openapi_client.model.management_controller import ManagementController
from openapi_client.model.management_entity import ManagementEntity
from openapi_client.model.management_interface import ManagementInterface
from openapi_client.model.memory_abstract_unit import MemoryAbstractUnit
from openapi_client.model.memory_array import MemoryArray
from openapi_client.model.memory_persistent_memory_config_result import MemoryPersistentMemoryConfigResult
from openapi_client.model.memory_persistent_memory_configuration import MemoryPersistentMemoryConfiguration
from openapi_client.model.memory_persistent_memory_namespace import MemoryPersistentMemoryNamespace
from openapi_client.model.memory_persistent_memory_namespace_config_result import MemoryPersistentMemoryNamespaceConfigResult
from openapi_client.model.memory_persistent_memory_region import MemoryPersistentMemoryRegion
from openapi_client.model.memory_persistent_memory_unit import MemoryPersistentMemoryUnit
from openapi_client.model.memory_unit import MemoryUnit
from openapi_client.model.mo_base_mo import MoBaseMo
from openapi_client.model.mo_base_mo_relationship import MoBaseMoRelationship
from openapi_client.model.mo_tag import MoTag
from openapi_client.model.mo_version_context import MoVersionContext
from openapi_client.model.network_element import NetworkElement
from openapi_client.model.network_fc_zone_info import NetworkFcZoneInfo
from openapi_client.model.network_vlan_port_info import NetworkVlanPortInfo
from openapi_client.model.pci_coprocessor_card import PciCoprocessorCard
from openapi_client.model.pci_device import PciDevice
from openapi_client.model.pci_link import PciLink
from openapi_client.model.pci_switch import PciSwitch
from openapi_client.model.port_group import PortGroup
from openapi_client.model.port_interface_base import PortInterfaceBase
from openapi_client.model.port_mac_binding import PortMacBinding
from openapi_client.model.port_physical import PortPhysical
from openapi_client.model.port_sub_group import PortSubGroup
from openapi_client.model.processor_unit import ProcessorUnit
from openapi_client.model.security_unit import SecurityUnit
from openapi_client.model.storage_base_array import StorageBaseArray
from openapi_client.model.storage_base_array_controller import StorageBaseArrayController
from openapi_client.model.storage_base_array_disk import StorageBaseArrayDisk
from openapi_client.model.storage_controller import StorageController
from openapi_client.model.storage_disk_group import StorageDiskGroup
from openapi_client.model.storage_enclosure import StorageEnclosure
from openapi_client.model.storage_enclosure_disk import StorageEnclosureDisk
from openapi_client.model.storage_enclosure_disk_slot_ep import StorageEnclosureDiskSlotEp
from openapi_client.model.storage_flex_flash_controller import StorageFlexFlashController
from openapi_client.model.storage_flex_flash_controller_props import StorageFlexFlashControllerProps
from openapi_client.model.storage_flex_flash_physical_drive import StorageFlexFlashPhysicalDrive
from openapi_client.model.storage_flex_flash_virtual_drive import StorageFlexFlashVirtualDrive
from openapi_client.model.storage_flex_util_controller import StorageFlexUtilController
from openapi_client.model.storage_flex_util_physical_drive import StorageFlexUtilPhysicalDrive
from openapi_client.model.storage_flex_util_virtual_drive import StorageFlexUtilVirtualDrive
from openapi_client.model.storage_item import StorageItem
from openapi_client.model.storage_physical_disk import StoragePhysicalDisk
from openapi_client.model.storage_physical_disk_extension import StoragePhysicalDiskExtension
from openapi_client.model.storage_physical_disk_usage import StoragePhysicalDiskUsage
from openapi_client.model.storage_pure_array import StoragePureArray
from openapi_client.model.storage_pure_controller import StoragePureController
from openapi_client.model.storage_pure_disk import StoragePureDisk
from openapi_client.model.storage_sas_expander import StorageSasExpander
from openapi_client.model.storage_sas_port import StorageSasPort
from openapi_client.model.storage_span import StorageSpan
from openapi_client.model.storage_vd_member_ep import StorageVdMemberEp
from openapi_client.model.storage_virtual_drive import StorageVirtualDrive
from openapi_client.model.storage_virtual_drive_extension import StorageVirtualDriveExtension
from openapi_client.model.top_system import TopSystem
globals()['AdapterExtEthInterface'] = AdapterExtEthInterface
globals()['AdapterHostEthInterface'] = AdapterHostEthInterface
globals()['AdapterHostFcInterface'] = AdapterHostFcInterface
globals()['AdapterHostIscsiInterface'] = AdapterHostIscsiInterface
globals()['AdapterUnit'] = AdapterUnit
globals()['BiosBootMode'] = BiosBootMode
globals()['BiosUnit'] = BiosUnit
globals()['BootDeviceBootMode'] = BootDeviceBootMode
globals()['ComputeBlade'] = ComputeBlade
globals()['ComputeBoard'] = ComputeBoard
globals()['ComputePhysical'] = ComputePhysical
globals()['ComputeRackUnit'] = ComputeRackUnit
globals()['ComputeServerSetting'] = ComputeServerSetting
globals()['DisplayNames'] = DisplayNames
globals()['EquipmentAbstractDevice'] = EquipmentAbstractDevice
globals()['EquipmentBase'] = EquipmentBase
globals()['EquipmentChassis'] = EquipmentChassis
globals()['EquipmentFan'] = EquipmentFan
globals()['EquipmentFanModule'] = EquipmentFanModule
globals()['EquipmentFex'] = EquipmentFex
globals()['EquipmentIoCard'] = EquipmentIoCard
globals()['EquipmentIoCardBase'] = EquipmentIoCardBase
globals()['EquipmentIoExpander'] = EquipmentIoExpander
globals()['EquipmentLocatorLed'] = EquipmentLocatorLed
globals()['EquipmentPsu'] = EquipmentPsu
globals()['EquipmentPsuControl'] = EquipmentPsuControl
globals()['EquipmentRackEnclosure'] = EquipmentRackEnclosure
globals()['EquipmentRackEnclosureSlot'] = EquipmentRackEnclosureSlot
globals()['EquipmentSharedIoModule'] = EquipmentSharedIoModule
globals()['EquipmentSwitchCard'] = EquipmentSwitchCard
globals()['EquipmentSystemIoController'] = EquipmentSystemIoController
globals()['EquipmentTpm'] = EquipmentTpm
globals()['EquipmentTransceiver'] = EquipmentTransceiver
globals()['EtherHostPort'] = EtherHostPort
globals()['EtherNetworkPort'] = EtherNetworkPort
globals()['EtherPhysicalPort'] = EtherPhysicalPort
globals()['EtherPhysicalPortBase'] = EtherPhysicalPortBase
globals()['EtherPortChannel'] = EtherPortChannel
globals()['FaultInstance'] = FaultInstance
globals()['FcPhysicalPort'] = FcPhysicalPort
globals()['FcPortChannel'] = FcPortChannel
globals()['FirmwareRunningFirmware'] = FirmwareRunningFirmware
globals()['GraphicsCard'] = GraphicsCard
globals()['GraphicsController'] = GraphicsController
globals()['InventoryBaseAllOf'] = InventoryBaseAllOf
globals()['InventoryGenericInventory'] = InventoryGenericInventory
globals()['InventoryGenericInventoryHolder'] = InventoryGenericInventoryHolder
globals()['LsServiceProfile'] = LsServiceProfile
globals()['ManagementController'] = ManagementController
globals()['ManagementEntity'] = ManagementEntity
globals()['ManagementInterface'] = ManagementInterface
globals()['MemoryAbstractUnit'] = MemoryAbstractUnit
globals()['MemoryArray'] = MemoryArray
globals()['MemoryPersistentMemoryConfigResult'] = MemoryPersistentMemoryConfigResult
globals()['MemoryPersistentMemoryConfiguration'] = MemoryPersistentMemoryConfiguration
globals()['MemoryPersistentMemoryNamespace'] = MemoryPersistentMemoryNamespace
globals()['MemoryPersistentMemoryNamespaceConfigResult'] = MemoryPersistentMemoryNamespaceConfigResult
globals()['MemoryPersistentMemoryRegion'] = MemoryPersistentMemoryRegion
globals()['MemoryPersistentMemoryUnit'] = MemoryPersistentMemoryUnit
globals()['MemoryUnit'] = MemoryUnit
globals()['MoBaseMo'] = MoBaseMo
globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
globals()['MoTag'] = MoTag
globals()['MoVersionContext'] = MoVersionContext
globals()['NetworkElement'] = NetworkElement
globals()['NetworkFcZoneInfo'] = NetworkFcZoneInfo
globals()['NetworkVlanPortInfo'] = NetworkVlanPortInfo
globals()['PciCoprocessorCard'] = PciCoprocessorCard
globals()['PciDevice'] = PciDevice
globals()['PciLink'] = PciLink
globals()['PciSwitch'] = PciSwitch
globals()['PortGroup'] = PortGroup
globals()['PortInterfaceBase'] = PortInterfaceBase
globals()['PortMacBinding'] = PortMacBinding
globals()['PortPhysical'] = PortPhysical
globals()['PortSubGroup'] = PortSubGroup
globals()['ProcessorUnit'] = ProcessorUnit
globals()['SecurityUnit'] = SecurityUnit
globals()['StorageBaseArray'] = StorageBaseArray
globals()['StorageBaseArrayController'] = StorageBaseArrayController
globals()['StorageBaseArrayDisk'] = StorageBaseArrayDisk
globals()['StorageController'] = StorageController
globals()['StorageDiskGroup'] = StorageDiskGroup
globals()['StorageEnclosure'] = StorageEnclosure
globals()['StorageEnclosureDisk'] = StorageEnclosureDisk
globals()['StorageEnclosureDiskSlotEp'] = StorageEnclosureDiskSlotEp
globals()['StorageFlexFlashController'] = StorageFlexFlashController
globals()['StorageFlexFlashControllerProps'] = StorageFlexFlashControllerProps
globals()['StorageFlexFlashPhysicalDrive'] = StorageFlexFlashPhysicalDrive
globals()['StorageFlexFlashVirtualDrive'] = StorageFlexFlashVirtualDrive
globals()['StorageFlexUtilController'] = StorageFlexUtilController
globals()['StorageFlexUtilPhysicalDrive'] = StorageFlexUtilPhysicalDrive
globals()['StorageFlexUtilVirtualDrive'] = StorageFlexUtilVirtualDrive
globals()['StorageItem'] = StorageItem
globals()['StoragePhysicalDisk'] = StoragePhysicalDisk
globals()['StoragePhysicalDiskExtension'] = StoragePhysicalDiskExtension
globals()['StoragePhysicalDiskUsage'] = StoragePhysicalDiskUsage
globals()['StoragePureArray'] = StoragePureArray
globals()['StoragePureController'] = StoragePureController
globals()['StoragePureDisk'] = StoragePureDisk
globals()['StorageSasExpander'] = StorageSasExpander
globals()['StorageSasPort'] = StorageSasPort
globals()['StorageSpan'] = StorageSpan
globals()['StorageVdMemberEp'] = StorageVdMemberEp
globals()['StorageVirtualDrive'] = StorageVirtualDrive
globals()['StorageVirtualDriveExtension'] = StorageVirtualDriveExtension
globals()['TopSystem'] = TopSystem
from openapi_client.model.inventory_base import InventoryBase


class TestInventoryBase(unittest.TestCase):
    """InventoryBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInventoryBase(self):
        """Test InventoryBase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InventoryBase()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()