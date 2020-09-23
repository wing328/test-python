# NetworkElementSummaryAllOf

Definition of the list of properties defined in 'network.ElementSummary', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_evac_state** | **str** | Administratively configured state of Fabric Evacuation feature, for this switch. | [optional] [readonly] 
**admin_inband_interface_state** | **str** | The administrative state of the network Element inband management interface. | [optional] [readonly] 
**available_memory** | **str** | Available memory (un-used) on this switch platform. | [optional] [readonly] 
**device_mo_id** | **str** | The database identifier of the registered device of an object. | [optional] [readonly] 
**dn** | **str** | The Distinguished Name unambiguously identifies an object in the system. | [optional] [readonly] 
**ethernet_mode** | **str** | The user configured Ethernet operational mode for this switch (End-Host or Switching). | [optional] [readonly] 
**fault_summary** | **int** | The fault summary of the network Element out-of-band management interface. | [optional] [readonly] 
**fc_mode** | **str** | The user configured FC operational mode for this switch (End-Host or Switching). | [optional] [readonly] 
**firmware** | **str** | Running firmware information. | [optional] [readonly] 
**inband_ip_address** | **str** | The IP address of the network Element inband management interface. | [optional] [readonly] 
**inband_ip_gateway** | **str** | The default gateway of the network Element inband management interface. | [optional] [readonly] 
**inband_ip_mask** | **str** | The network mask of the network Element inband management interface. | [optional] [readonly] 
**inband_vlan** | **int** | The VLAN ID of the network Element inband management interface. | [optional] [readonly] 
**ipv4_address** | **str** | IP version 4 address is saved in this property. | [optional] [readonly] 
**model** | **str** | This field identifies the model of the given component. | [optional] [readonly] 
**name** | **str** | Name of the ElementSummary object is saved in this property. | [optional] [readonly] 
**num_ether_ports** | **int** | Total number of Ethernet ports. | [optional] [readonly] 
**num_ether_ports_configured** | **int** | Total number of configured Ethernet ports. | [optional] [readonly] 
**num_ether_ports_link_up** | **int** | Total number of Ethernet ports which are UP. | [optional] [readonly] 
**num_expansion_modules** | **int** | Total number of expansion modules. | [optional] [readonly] 
**num_fc_ports** | **int** | Total number of FC ports. | [optional] [readonly] 
**num_fc_ports_configured** | **int** | Total number of configured FC ports. | [optional] [readonly] 
**num_fc_ports_link_up** | **int** | Total number of FC ports which are UP. | [optional] [readonly] 
**oper_evac_state** | **str** | Operational state of the Fabric Evacuation feature, for this switch. | [optional] [readonly] 
**operability** | **str** | The switch&#39;s current overall operational/health state. | [optional] [readonly] 
**out_of_band_ip_address** | **str** | The IP address of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ip_gateway** | **str** | The default gateway of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ip_mask** | **str** | The network mask of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv4_address** | **str** | The IPv4 address of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv4_gateway** | **str** | The default IPv4 gateway of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv4_mask** | **str** | The network mask of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv6_address** | **str** | The IPv6 address of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv6_gateway** | **str** | The default IPv6 gateway of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_ipv6_prefix** | **str** | The network mask of the network Element out-of-band management interface. | [optional] [readonly] 
**out_of_band_mac** | **str** | The MAC address of the network Element out-of-band management interface. | [optional] [readonly] 
**revision** | **str** | This field identifies the revision of the given component. | [optional] [readonly] 
**rn** | **str** | The Relative Name uniquely identifies an object within a given context. | [optional] [readonly] 
**serial** | **str** | This field identifies the serial of the given component. | [optional] [readonly] 
**source_object_type** | **str** | The source object type of this view MO. | [optional] [readonly] 
**switch_id** | **str** | The Switch Id of the network Element. | [optional] [readonly] 
**total_memory** | **int** | Total available memory on this switch platform. | [optional] [readonly] 
**vendor** | **str** | This field identifies the vendor of the given component. | [optional] [readonly] 
**version** | **str** | Version holds the firmware version related information. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


