# TechsupportmanagementNiaParam

NIA parameter object for Tech Support requests.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**collection_level** | **int** | CollectionLevel controls the size / depth of the tech support files collected. | [optional]  if omitted the server will use the default value of 1
**filename** | **str** | Filename specifies an individual filename to collect from the endpoint. | [optional] 
**force_fresh** | **bool** | ForceFresh controls whether to return pre-collected files or force the collection of new files. | [optional] 
**pids** | **[str]** |  | [optional] 
**serial_numbers** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


