# TamApiDataSource

Data source using Intersight API to collect data regarding managed devices.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**mo_type** | **str** | Type of Intersight managed object used as data source. | [optional] 
**queries** | [**[TamQueryEntry]**](TamQueryEntry.md) |  | [optional] 
**name** | **str** | Name is used to unique identify and refer a given data source in an alert definition. | [optional] 
**type** | **str** | Type of data source (for e.g. TextFsmTempalate based, Intersight API based etc.). | [optional]  if omitted the server will use the default value of "nxos"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


