# VirtualizationVmwareVmMemoryShareInfo

Information about the virtual machine's memory sharing and limits. For more information, see VMware documentation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**mem_limit** | **int** | Limit on the memory sharing imposed (in Mbytes). | [optional] 
**mem_overhead_limit** | **int** | Limit on memory overhead imposed (in Mbytes). | [optional] 
**mem_reservation** | **int** | Similar to CPU reservations (Mbytes). | [optional] 
**mem_shares** | **int** | Similar to CPU Shares but applicable to memory. There is no unit for this value. It is a relative measure based on the settings for other resource pools. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


