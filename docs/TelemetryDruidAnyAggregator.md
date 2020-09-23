# TelemetryDruidAnyAggregator

Returns any value including null. This aggregator can simplify and optimize the performance by returning the first encountered value (including null).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The aggregator type. | 
**name** | **str** | Output name for the &#39;any&#39; value. | 
**field_name** | **str** | Name of the metric column. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


