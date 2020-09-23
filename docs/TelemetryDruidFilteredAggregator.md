# TelemetryDruidFilteredAggregator

A filtered aggregator wraps any given aggregator, but only aggregates the values for which the given dimension filter matches. This makes it possible to compute the results of a filtered and an unfiltered aggregation simultaneously, without having to issue multiple queries, and use both results as part of post-aggregations. If only the filtered results are required, consider putting the filter on the query itself, which will be much faster since it does not require scanning all the data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The aggregator type. | 
**filter** | [**TelemetryDruidFilter**](TelemetryDruidFilter.md) |  | 
**aggregator** | [**TelemetryDruidAggregator**](TelemetryDruidAggregator.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


