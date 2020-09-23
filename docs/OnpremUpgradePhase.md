# OnpremUpgradePhase

UpgradePhase represents a phase of the Intersight Appliance software upgrade process. This data structure is shared by both the Intersight upgrade service and the Intersight Appliance's upgrade service.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**elapsed_time** | **int** | Elapsed time in seconds to complete the current upgrade phase. | [optional] [readonly] 
**end_time** | **datetime** | End date of the software upgrade phase. | [optional] [readonly] 
**failed** | **bool** | Indicates if the upgrade phase has failed or not. | [optional] [readonly] 
**message** | **str** | Status message set during the upgrade phase. | [optional] [readonly] 
**name** | **str** | Name of the upgrade phase. | [optional] [readonly]  if omitted the server will use the default value of "init"
**start_time** | **datetime** | Start date of the software upgrade phase. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


