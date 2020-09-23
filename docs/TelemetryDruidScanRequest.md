# TelemetryDruidScanRequest

The Scan query returns raw Apache Druid rows in streaming mode. In addition to straightforward usage where a Scan query is issued to the Broker, the Scan query can also be issued directly to Historical processes or streaming ingestion tasks. This can be useful if you want to retrieve large amounts of data in parallel.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_type** | **str** | null | 
**data_source** | [**TelemetryDruidDataSource**](TelemetryDruidDataSource.md) |  | 
**intervals** | **[str]** | A JSON Object representing ISO-8601 Intervals. This defines the time ranges to run the query over. | 
**result_format** | **str** | How the results are represented, list, compactedList or valueVector. Currently only list and compactedList are supported. | [optional]  if omitted the server will use the default value of "list"
**filter** | [**TelemetryDruidFilter**](TelemetryDruidFilter.md) |  | [optional] 
**columns** | **[str]** | A String array of dimensions and metrics to scan. If left empty, all dimensions and metrics are returned. | [optional] 
**batch_size** | **int** | The maximum number of rows buffered before being returned to the client. | [optional]  if omitted the server will use the default value of 20480
**limit** | **int** | How many rows to return. If not specified, all rows will be returned. | [optional] 
**order** | **str** | The ordering of returned rows based on timestamp. \&quot;ascending\&quot;, \&quot;descending\&quot;, and \&quot;none\&quot; (default) are supported. Currently, \&quot;ascending\&quot; and \&quot;descending\&quot; are only supported for queries where the __time column is included in the columns field and the requirements outlined in the time ordering section are met. | [optional]  if omitted the server will use the default value of "none"
**legacy** | **bool** | Return results consistent with the legacy \&quot;scan-query\&quot; contrib extension. Defaults to the value set by druid.query.scan.legacy, which in turn defaults to false. | [optional]  if omitted the server will use the default value of False
**context** | [**TelemetryDruidQueryContext**](TelemetryDruidQueryContext.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


