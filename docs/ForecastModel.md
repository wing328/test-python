# ForecastModel

Model encapsulated model type and the model generated based on the type for computing forecast. For example if linear regression predictive modeling is used then the model data contains slope, coefficient and RMSE.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**accuracy** | **float** | The standard error of the estimate is a measure of the accuracy of predictions from predective modeling. | [optional] 
**model_data** | **[float]** |  | [optional] 
**model_type** | **str** | Model type indicating type of predictive model used for computing forecast. | [optional]  if omitted the server will use the default value of "Linear"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


