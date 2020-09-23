# TelemetryDruidArithmeticPostAggregator

The arithmetic post-aggregator applies the provided function to the given fields from left to right. The fields can be aggregators or other post aggregators. Supported functions are +, -, *, /, and quotient. / division always returns 0 if dividing by 0, regardless of the numerator. quotient division behaves like regular floating point division.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The post-aggregator type. | 
**name** | **str** | Output name for the minimum/maximum timestamp value. | [optional] 
**fn** | **str** | null | [optional] 
**fields** | **[str]** | null | [optional] 
**ordering** | **str** | Arithmetic post-aggregators may specify an ordering, which defines the order of resulting values when sorting results. This can be useful for topN queries for instance. If no ordering (or null) is specified, the default floating point ordering is used. numericFirst ordering always returns finite values first, followed by NaN, and infinite values last. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


