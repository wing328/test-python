# AssetWorkloadOptimizerService

WorkloadOptimizerService provides the necessary configuration details to enable Intersight Workflow Optimizer on the selected managed target. Subject to licensing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**options** | [**AssetServiceOptions**](AssetServiceOptions.md) |  | [optional] 
**status** | **str** | Status indicates if the respective Service can establish a connection and authenticate with the managed target. Status does not include information about the functional health of the target. | [optional]  if omitted the server will use the default value of ""
**status_error_reason** | **str** | When &#39;Status&#39; is not Connected, statusErrorReason provides further details about why the device is not connected with Intersight. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


