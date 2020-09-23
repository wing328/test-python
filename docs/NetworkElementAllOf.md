# NetworkElementAllOf

Definition of the list of properties defined in 'network.Element', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_evac_state** | **str** | Administratively configured state of Fabric Evacuation feature, for this switch. | [optional] [readonly] 
**admin_inband_interface_state** | **str** | The administrative state of the network Element inband management interface. | [optional] [readonly] 
**available_memory** | **str** | Available memory (un-used) on this switch platform. | [optional] [readonly] 
**ethernet_mode** | **str** | The user configured Ethernet operational mode for this switch (End-Host or Switching). | [optional] [readonly] 
**fault_summary** | **int** | The fault summary of the network Element out-of-band management interface. | [optional] 
**fc_mode** | **str** | The user configured FC operational mode for this switch (End-Host or Switching). | [optional] [readonly] 
**inband_ip_address** | **str** | The IP address of the network Element inband management interface. | [optional] [readonly] 
**inband_ip_gateway** | **str** | The default gateway of the network Element inband management interface. | [optional] [readonly] 
**inband_ip_mask** | **str** | The network mask of the network Element inband management interface. | [optional] [readonly] 
**inband_vlan** | **int** | The VLAN ID of the network Element inband management interface. | [optional] [readonly] 
**oper_evac_state** | **str** | Operational state of the Fabric Evacuation feature, for this switch. | [optional] [readonly] 
**operability** | **str** | The switch&#39;s current overall operational/health state. | [optional] [readonly] 
**out_of_band_ip_address** | **str** | The IP address of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ip_gateway** | **str** | The default gateway of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ip_mask** | **str** | The network mask of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv4_address** | **str** | The IPv4 address of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv4_gateway** | **str** | The default IPv4 gateway of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv4_mask** | **str** | The network mask of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv6_address** | **str** | The IPv6 address of the network Element out-of-band management interface. | [optional] 
**out_of_band_ipv6_gateway** | **str** | The default IPv6 gateway of the network Element out-of-band management interface. | [optional] 
**out_of_band_ipv6_prefix** | **str** | The network mask of the network Element out-of-band management interface. | [optional] 
**out_of_band_mac** | **str** | The MAC address of the network Element out-of-band management interface. | [optional] [readonly] 
**switch_id** | **str** | The Switch Id of the network Element. | [optional] [readonly] 
**total_memory** | **int** | Total available memory on this switch platform. | [optional] [readonly] 
**cards** | [**[EquipmentSwitchCardRelationship], none_type**](EquipmentSwitchCardRelationship.md) | An array of relationships to equipmentSwitchCard resources. | [optional] [readonly] 
**fanmodules** | [**[EquipmentFanModuleRelationship], none_type**](EquipmentFanModuleRelationship.md) | An array of relationships to equipmentFanModule resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**management_contoller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**management_entity** | [**ManagementEntityRelationship**](ManagementEntityRelationship.md) |  | [optional] 
**network_fc_zone_info** | [**NetworkFcZoneInfoRelationship**](NetworkFcZoneInfoRelationship.md) |  | [optional] 
**network_vlan_port_info** | [**NetworkVlanPortInfoRelationship**](NetworkVlanPortInfoRelationship.md) |  | [optional] 
**port_mac_bindings** | [**[PortMacBindingRelationship], none_type**](PortMacBindingRelationship.md) | An array of relationships to portMacBinding resources. | [optional] 
**psus** | [**[EquipmentPsuRelationship], none_type**](EquipmentPsuRelationship.md) | An array of relationships to equipmentPsu resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_items** | [**[StorageItemRelationship], none_type**](StorageItemRelationship.md) | An array of relationships to storageItem resources. | [optional] [readonly] 
**top_system** | [**TopSystemRelationship**](TopSystemRelationship.md) |  | [optional] 
**ucsm_running_firmware** | [**FirmwareRunningFirmwareRelationship**](FirmwareRunningFirmwareRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


