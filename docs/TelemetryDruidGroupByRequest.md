# TelemetryDruidGroupByRequest

These types of Apache Druid queries take a groupBy query object and return an array of JSON objects where each object represents a grouping asked for by the query.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_type** | **str** | null | 
**data_source** | [**TelemetryDruidDataSource**](TelemetryDruidDataSource.md) |  | 
**dimensions** | [**[TelemetryDruidDimensionSpec]**](TelemetryDruidDimensionSpec.md) | A JSON list of dimensions to do the groupBy over; or see DimensionSpec for ways to extract dimensions.. | 
**granularity** | [**TelemetryDruidGranularity**](TelemetryDruidGranularity.md) |  | 
**intervals** | **[str]** | A JSON Object representing ISO-8601 Intervals. This defines the time ranges to run the query over. | 
**limit_spec** | [**TelemetryDruidDefaultLimitSpec**](TelemetryDruidDefaultLimitSpec.md) |  | [optional] 
**having** | [**TelemetryDruidHavingFilter**](TelemetryDruidHavingFilter.md) |  | [optional] 
**filter** | [**TelemetryDruidFilter**](TelemetryDruidFilter.md) |  | [optional] 
**aggregations** | [**[TelemetryDruidAggregator]**](TelemetryDruidAggregator.md) | Aggregation functions are used to summarize data in buckets. Summarization functions include counting rows, calculating the min/max/sum of metrics and retrieving the first/last value of metrics for each bucket. Additional summarization functions are available with extensions. If no aggregator is provided, the results will be empty for each bucket. | [optional] 
**post_aggregations** | [**[TelemetryDruidPostAggregator]**](TelemetryDruidPostAggregator.md) | Post-aggregations are specifications of processing that should happen on aggregated values as they come out of Apache Druid. If you include a post aggregation as part of a query, make sure to include all aggregators the post-aggregator requires. | [optional] 
**subtotals_spec** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A JSON array of arrays to return additional result sets for groupings of subsets of top level dimensions. The subtotals feature allows computation of multiple sub-groupings in a single query. To use this feature, add a \&quot;subtotalsSpec\&quot; to your query, which should be a list of subgroup dimension sets. It should contain the \&quot;outputName\&quot; from dimensions in your \&quot;dimensions\&quot; attribute, in the same order as they appear in the \&quot;dimensions\&quot; attribute. | [optional] 
**context** | [**TelemetryDruidQueryContext**](TelemetryDruidQueryContext.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


