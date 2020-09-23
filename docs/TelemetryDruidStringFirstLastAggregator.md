# TelemetryDruidStringFirstLastAggregator

Computes the metric value with the minimum/maximum timestamp or null if no row exist.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The aggregator type. | 
**name** | **str** | Output name for the minimum/maximum timestamp value. | 
**field_name** | **str** | Name of the metric column. | 
**max_string_bytes** | **int** | null | [optional]  if omitted the server will use the default value of 1024
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


