# TelemetryDruidAggregateRequest

Exposes a REST endpoint for performing queries against Druid time series data. View Telemetry allows [POST of a Druid query](http://druid.io/docs/latest/querying/querying). Manage Telemetry allows [READ of broker status](http://druid.io/docs/latest/operations/api-reference.html#broker).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_type** | **str** | null | 
**data_source** | [**TelemetryDruidDataSource**](TelemetryDruidDataSource.md) |  | defaults to nulltype.Null
**intervals** | **[str]** | A JSON Object representing ISO-8601 Intervals. This defines the time ranges to run the query over. If an interval is not specified, the query will use a default interval that spans a configurable period before the end time of the most recent segment. | defaults to nulltype.Null
**granularity** | [**TelemetryDruidGranularity**](TelemetryDruidGranularity.md) |  | defaults to nulltype.Null
**dimension** | [**TelemetryDruidDimensionSpec**](TelemetryDruidDimensionSpec.md) |  | defaults to nulltype.Null
**threshold** | **int** | An integer defining the N in the topN (i.e. how many results you want in the top list). | defaults to nulltype.Null
**metric** | [**TelemetryDruidTopNMetricSpec**](TelemetryDruidTopNMetricSpec.md) |  | defaults to nulltype.Null
**dimensions** | [**[TelemetryDruidDimensionSpec]**](TelemetryDruidDimensionSpec.md) | A JSON list of dimensions to do the groupBy over; or see DimensionSpec for ways to extract dimensions.. | defaults to nulltype.Null
**descending** | **bool** | Whether to make descending ordered result. Default is false(ascending). | [optional] 
**filter** | [**TelemetryDruidFilter**](TelemetryDruidFilter.md) |  | [optional] 
**aggregations** | [**[TelemetryDruidAggregator]**](TelemetryDruidAggregator.md) | Aggregation functions are used to summarize data in buckets. Summarization functions include counting rows, calculating the min/max/sum of metrics and retrieving the first/last value of metrics for each bucket. Additional summarization functions are available with extensions. If no aggregator is provided, the results will be empty for each bucket. | [optional] 
**post_aggregations** | [**[TelemetryDruidPostAggregator]**](TelemetryDruidPostAggregator.md) | Post-aggregations are specifications of processing that should happen on aggregated values as they come out of Apache Druid. If you include a post aggregation as part of a query, make sure to include all aggregators the post-aggregator requires. | [optional] 
**limit** | **int** | How many rows to return. If not specified, all rows will be returned. | [optional] 
**context** | [**TelemetryDruidQueryContext**](TelemetryDruidQueryContext.md) |  | [optional] 
**limit_spec** | [**TelemetryDruidDefaultLimitSpec**](TelemetryDruidDefaultLimitSpec.md) |  | [optional] 
**having** | [**TelemetryDruidHavingFilter**](TelemetryDruidHavingFilter.md) |  | [optional] 
**subtotals_spec** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A JSON array of arrays to return additional result sets for groupings of subsets of top level dimensions. The subtotals feature allows computation of multiple sub-groupings in a single query. To use this feature, add a \&quot;subtotalsSpec\&quot; to your query, which should be a list of subgroup dimension sets. It should contain the \&quot;outputName\&quot; from dimensions in your \&quot;dimensions\&quot; attribute, in the same order as they appear in the \&quot;dimensions\&quot; attribute. | [optional] 
**result_format** | **str** | How the results are represented, list, compactedList or valueVector. Currently only list and compactedList are supported. | [optional]  if omitted the server will use the default value of "list"
**columns** | **[str]** | A String array of dimensions and metrics to scan. If left empty, all dimensions and metrics are returned. | [optional] 
**batch_size** | **int** | The maximum number of rows buffered before being returned to the client. | [optional]  if omitted the server will use the default value of 20480
**order** | **str** | The ordering of returned rows based on timestamp. \&quot;ascending\&quot;, \&quot;descending\&quot;, and \&quot;none\&quot; (default) are supported. Currently, \&quot;ascending\&quot; and \&quot;descending\&quot; are only supported for queries where the __time column is included in the columns field and the requirements outlined in the time ordering section are met. | [optional]  if omitted the server will use the default value of "none"
**legacy** | **bool** | Return results consistent with the legacy \&quot;scan-query\&quot; contrib extension. Defaults to the value set by druid.query.scan.legacy, which in turn defaults to false. | [optional]  if omitted the server will use the default value of False
**bound** | **str** | Optional, set to maxTime or minTime to return only the latest or earliest timestamp. Default to returning both if not set. | [optional] 
**to_include** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A JSON Object representing what columns should be included in the result. Defaults to \&quot;all\&quot;. | [optional] 
**merge** | **bool** | Merge all individual segment metadata results into a single result. | [optional] 
**analysis_types** | **[str]** | A list of Strings specifying what column properties (e.g. cardinality, size) should be calculated and returned in the result. Defaults to [\&quot;cardinality\&quot;, \&quot;interval\&quot;, \&quot;minmax\&quot;], but can be overridden with using the segment metadata query config. * cardinality - in the result will return the estimated floor of cardinality for each column. Only relevant for dimension columns. * minmax - Estimated min/max values for each column. Only relevant for dimension columns. * size - in the result will contain the estimated total segment byte size as if the data were stored in text format. * intervals - in the result will contain the list of intervals associated with the queried segments. * timestampSpec - in the result will contain timestampSpec of data stored in segments. This can be null if timestampSpec of segments was unknown or unmergeable (if merging is enabled). * queryGranularity - in the result will contain query granularity of data stored in segments. This can be null if query granularity of segments was unknown or unmergeable (if merging is enabled). * aggregators - in the result will contain the list of aggregators usable for querying metric columns. This may be null if the aggregators are unknown or unmergeable (if merging is enabled). Merging can be strict or lenient. The form of the result is a map of column name to aggregator. * rollup - in the result is true/false/null. When merging is enabled, if some are rollup, others are not, result is null. | [optional] 
**lenient_aggregator_merge** | **bool** | If true, and if the \&quot;aggregators\&quot; analysisType is enabled, aggregators will be merged leniently. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


