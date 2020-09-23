# TelemetryDruidAggregator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The aggregator type. | 
**name** | **str** | A String for the output (result) name of the calculation. | defaults to nulltype.Null
**field_name** | **str** | A String for the name of the aggregator used at ingestion time. | defaults to nulltype.Null
**filter** | [**TelemetryDruidFilter**](TelemetryDruidFilter.md) |  | defaults to nulltype.Null
**aggregator** | [**TelemetryDruidAggregator**](TelemetryDruidAggregator.md) |  | defaults to nulltype.Null
**max_string_bytes** | **int** | null | [optional]  if omitted the server will use the default value of 1024
**size** | **int** | Must be a power of 2. Internally, size refers to the maximum number of entries sketch object will retain. Higher size means higher accuracy but more space to store sketches. Note that after you index with a particular size, druid will persist sketch in segments and you will use size greater or equal to that at query time. In general, We recommend just sticking to default size. | [optional]  if omitted the server will use the default value of 16384
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


