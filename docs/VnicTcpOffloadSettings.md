# VnicTcpOffloadSettings

The TCP offload settings decide whether to offload the TCP related network functions from the CPU to the network hardware or not. These options help reduce the CPU overhead and increase the network throughput.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**large_receive** | **bool** | Enables the reassembly of segmented packets in hardware before sending them to the CPU. | [optional] 
**large_send** | **bool** | Enables the CPU to send large packets to the hardware for segmentation. | [optional] 
**rx_checksum** | **bool** | When enabled, the CPU sends all packet checksums to the hardware for validation. | [optional] 
**tx_checksum** | **bool** | When enabled, the CPU sends all packets to the hardware so that the checksum can be calculated. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


