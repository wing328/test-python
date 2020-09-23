# TelemetryDruidDefaultLimitSpec

The default limit spec takes a limit and the list of columns to do an orderBy operation over.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | How many rows to return. If not specified, all rows will be returned. | 
**columns** | [**[TelemetryDruidOrderByColumnSpec]**](TelemetryDruidOrderByColumnSpec.md) | null | 
**type** | **str** | The limit spec type. | defaults to "default"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


