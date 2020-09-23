# CapabilitySwitchCapabilityAllOf

Definition of the list of properties defined in 'capability.SwitchCapability', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_vifs_supported** | **bool** | Dynamic VIFs support on this switch. | [optional] 
**fan_modules_supported** | **bool** | Fan Modules support on this switch. | [optional] 
**fc_end_host_mode_reserved_vsans** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**fc_uplink_ports_auto_negotiation_supported** | **bool** | Fc Uplink ports auto negotiation speed support on this switch. | [optional] 
**locator_beacon_supported** | **bool** | Locator Beacon LED support on this switch. | [optional] 
**max_active_span_sessions** | **int** | Maximum allowed Traffic Monitoring (SPAN) sessions on this switch. | [optional] 
**max_ethernet_port_channel_members** | **int** | Maximum allowed Ethernet Uplink Port-channel members for each Uplink Port-channel on this switch. | [optional] 
**max_ethernet_port_channels** | **int** | Maximum allowed Ethernet Uplink Port-channels on this switch. | [optional] 
**max_ethernet_uplink_ports** | **int** | Maximum allowed Ethernet Uplink Ports on this switch. | [optional] 
**max_fc_fcoe_port_channels** | **int** | Total maximum Fc and Fcoe Port-channels allowed on this switch. | [optional] 
**max_fc_port_channel_members** | **int** | Maximum allowed FC Uplink Port-channel members for each FCoE Port-channel on this switch. | [optional] 
**max_fcoe_port_channel_members** | **int** | Maximum allowed FCoE Uplink Port-channel members for each FCoE Port-channel on this switch. | [optional] 
**max_ports** | **int** | Maximum allowed physical ports on this switch. | [optional] 
**max_slots** | **int** | Maximum allowed physical slots on this switch. | [optional] 
**max_vsans_supported** | **int** | Maximum number of Vsans supported on this switch. | [optional] 
**min_active_fans** | **int** | Minimum number of fans needed to be active/running on this switch. | [optional] 
**ports_supporting100g_speed** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**ports_supporting10g_speed** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**ports_supporting1g_speed** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**ports_supporting25g_speed** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**ports_supporting40g_speed** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**ports_supporting_breakout** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**ports_supporting_fcoe** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**ports_supporting_server_role** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**reserved_vsans** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**sereno_netflow_supported** | **bool** | Sereno Adaptor with Netflow support on this switch. | [optional] 
**unified_ports** | [**[CapabilityPortRange]**](CapabilityPortRange.md) |  | [optional] 
**unified_rule** | **str** | The Slider rule for Unified ports on this switch. | [optional] 
**vp_compression_supported** | **bool** | VP Compression support on this switch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


