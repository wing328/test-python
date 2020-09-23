# TelemetryDruidFirstLastAggregator

(Double/Float/Long) First and Last aggregator cannot be used in ingestion spec, and should only be specified as part of queries. Note that queries with first/last aggregators on a segment created with rollup enabled will return the rolled up value, and not the last value within the raw ingested data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The aggregator type. | 
**name** | **str** | Output name for the first/last value. | 
**field_name** | **str** | Name of the metric column. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


