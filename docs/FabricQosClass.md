# FabricQosClass

Type to represent the Best Effort QoS class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**admin_state** | **str** | Administrative state for this QoS class. | [optional]  if omitted the server will use the default value of "Disabled"
**bandwidth_percent** | **int** | Percentage of bandwidth received by the traffic tagged with this QoS. | [optional] 
**cos** | **int** | Class of service received by the traffic tagged with this QoS. | [optional] 
**mtu** | **int** | Maximum transmission unit (MTU) is the largest size packet or frame, that can be sent in a packet- or frame-based network such as the Internet. User can select from the following: 1. Any value between 1500 and 9216 2. &#39;Normal&#39; (default) mapping to a value of 1500. 3. &#39;FC&#39; mapping to a value of 2240. | [optional] 
**multicast_optimize** | **bool** | If enabled, this QoS class will be optimized to send multiple packets. | [optional] 
**name** | **str** | The &#39;name&#39; of this QoS Class. | [optional] 
**packet_drop** | **bool** | If enabled, this QoS class will allow packet drops within an acceptable limit. | [optional] 
**weight** | **int** | The weight of the QoS Class controls the distribution of bandwidth between QoS Classes, with the same priority after the Guarantees for the QoS Classes are reached. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


