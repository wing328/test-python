# PolicyConfigResultContext

The context for a validation/config result such as the related entity's name, type, MOID etc.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**entity_data** | **bool, date, datetime, dict, float, int, list, str, none_type** | The data of the object present in config result context. | [optional] 
**entity_moid** | **str** | The Moid of the object present in config result context. | [optional] 
**entity_name** | **str** | The name of the object present in config result context. | [optional] 
**entity_type** | **str** | The type of the object present in config result context. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


