# VnicEthAdapterPolicyAllOf

Definition of the list of properties defined in 'vnic.EthAdapterPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_filter** | **bool** | Enables advanced filtering on the interface. | [optional] 
**arfs_settings** | [**VnicArfsSettings**](VnicArfsSettings.md) |  | [optional] 
**completion_queue_settings** | [**VnicCompletionQueueSettings**](VnicCompletionQueueSettings.md) |  | [optional] 
**interrupt_scaling** | **bool** | Enables Interrupt Scaling on the interface. | [optional] 
**interrupt_settings** | [**VnicEthInterruptSettings**](VnicEthInterruptSettings.md) |  | [optional] 
**nvgre_settings** | [**VnicNvgreSettings**](VnicNvgreSettings.md) |  | [optional] 
**roce_settings** | [**VnicRoceSettings**](VnicRoceSettings.md) |  | [optional] 
**rss_hash_settings** | [**VnicRssHashSettings**](VnicRssHashSettings.md) |  | [optional] 
**rss_settings** | **bool** | Receive Side Scaling allows the incoming traffic to be spread across multiple CPU cores. | [optional] 
**rx_queue_settings** | [**VnicEthRxQueueSettings**](VnicEthRxQueueSettings.md) |  | [optional] 
**tcp_offload_settings** | [**VnicTcpOffloadSettings**](VnicTcpOffloadSettings.md) |  | [optional] 
**tx_queue_settings** | [**VnicEthTxQueueSettings**](VnicEthTxQueueSettings.md) |  | [optional] 
**uplink_failback_timeout** | **int** | Uplink Failback Timeout in seconds when uplink failover is enabled for a vNIC. After a vNIC has started using its secondary interface, this setting controls how long the primary interface must be available before the system resumes using the primary interface for the vNIC. | [optional] 
**vxlan_settings** | [**VnicVxlanSettings**](VnicVxlanSettings.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


