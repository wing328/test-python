# TelemetryDruidHyperUniquePostAggregator

The hyperUniqueCardinality post aggregator is used to wrap a hyperUnique object such that it can be used in post aggregations. This post-aggregator will inherit the rounding behavior of the aggregator it references. Note that this inheritance is only effective if you directly reference an aggregator. Going through another post-aggregator, for example, will cause the user-specified rounding behavior to get lost and default to \"no rounding\".
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The post-aggregator type. | 
**name** | **str** | Output name for the post-aggregator. | [optional] 
**field_name** | **str** | The name field value of the hyperUnique aggregator. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


