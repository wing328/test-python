# VnicRoceSettings

Settings for RDMA over Converged Ethernet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**class_of_service** | **int** | The Class of Service for RoCE on this virtual interface. | [optional]  if omitted the server will use the default value of 5
**enabled** | **bool** | If enabled sets RDMA over Converged Ethernet (RoCE) on this virtual interface. | [optional] 
**memory_regions** | **int** | The number of memory regions per adapter. Recommended value &#x3D; integer power of 2. | [optional] 
**queue_pairs** | **int** | The number of queue pairs per adapter. Recommended value &#x3D; integer power of 2. | [optional] 
**resource_groups** | **int** | The number of resource groups per adapter. Recommended value &#x3D; be an integer power of 2 greater than or equal to the number of CPU cores on the system for optimum performance. | [optional] 
**version** | **int** | Configures RDMA over Converged Ethernet (RoCE) version on the virtual interface. Only RoceV1 is supported onn Cisco VIC models 13xx and only RoceV2 is supported on models 14xx. | [optional]  if omitted the server will use the default value of 1
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


