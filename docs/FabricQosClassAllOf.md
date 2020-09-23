# FabricQosClassAllOf

Definition of the list of properties defined in 'fabric.QosClass', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_state** | **str** | Administrative state for this QoS class. | [optional]  if omitted the server will use the default value of "Disabled"
**bandwidth_percent** | **int** | Percentage of bandwidth received by the traffic tagged with this QoS. | [optional] 
**cos** | **int** | Class of service received by the traffic tagged with this QoS. | [optional] 
**mtu** | **int** | Maximum transmission unit (MTU) is the largest size packet or frame, that can be sent in a packet- or frame-based network such as the Internet. User can select from the following: 1. Any value between 1500 and 9216 2. &#39;Normal&#39; (default) mapping to a value of 1500. 3. &#39;FC&#39; mapping to a value of 2240. | [optional] 
**multicast_optimize** | **bool** | If enabled, this QoS class will be optimized to send multiple packets. | [optional] 
**name** | **str** | The &#39;name&#39; of this QoS Class. | [optional] 
**packet_drop** | **bool** | If enabled, this QoS class will allow packet drops within an acceptable limit. | [optional] 
**weight** | **int** | The weight of the QoS Class controls the distribution of bandwidth between QoS Classes, with the same priority after the Guarantees for the QoS Classes are reached. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


