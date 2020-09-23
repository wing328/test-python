# TelemetryDruidFieldAccessorPostAggregator

These post-aggregators return the value produced by the specified aggregator. 'fieldName' refers to the output name of the aggregator given in the aggregations portion of the query. For complex aggregators, like \"cardinality\" and \"hyperUnique\", the type of the post-aggregator determines what the post-aggregator will return. Use type \"fieldAccess\" to return the raw aggregation object, or use type \"finalizingFieldAccess\" to return a finalized value, such as an estimated cardinality.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The post-aggregator type. | 
**name** | **str** | Output name for the post-aggregator. | [optional] 
**field_name** | **str** | Name of the metric column. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


