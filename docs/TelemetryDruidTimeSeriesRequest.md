# TelemetryDruidTimeSeriesRequest

These types of queries take a timeseries query object and return an array of JSON objects where each object represents a value asked for by the timeseries query.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_type** | **str** | null | 
**data_source** | [**TelemetryDruidDataSource**](TelemetryDruidDataSource.md) |  | 
**intervals** | **[str]** | A JSON Object representing ISO-8601 Intervals. This defines the time ranges to run the query over. | 
**granularity** | [**TelemetryDruidGranularity**](TelemetryDruidGranularity.md) |  | 
**descending** | **bool** | Whether to make descending ordered result. Default is false(ascending). | [optional] 
**filter** | [**TelemetryDruidFilter**](TelemetryDruidFilter.md) |  | [optional] 
**aggregations** | [**[TelemetryDruidAggregator]**](TelemetryDruidAggregator.md) | Aggregation functions are used to summarize data in buckets. Summarization functions include counting rows, calculating the min/max/sum of metrics and retrieving the first/last value of metrics for each bucket. Additional summarization functions are available with extensions. If no aggregator is provided, the results will be empty for each bucket. | [optional] 
**post_aggregations** | [**[TelemetryDruidPostAggregator]**](TelemetryDruidPostAggregator.md) | Post-aggregations are specifications of processing that should happen on aggregated values as they come out of Apache Druid. If you include a post aggregation as part of a query, make sure to include all aggregators the post-aggregator requires. | [optional] 
**limit** | **int** | An integer that limits the number of results. The default is unlimited. | [optional] 
**context** | [**TelemetryDruidQueryContext**](TelemetryDruidQueryContext.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


