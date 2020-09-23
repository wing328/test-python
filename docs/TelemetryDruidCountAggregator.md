# TelemetryDruidCountAggregator

Computes the count of Druid rows that match the filters. The count aggregator counts the number of Druid rows, which does not always reflect the number of raw events ingested. This is because Druid can be configured to roll up data at ingestion time To count the number of ingested rows of data, include a count aggregator at ingestion time, and a longSum aggregator at query time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The aggregator type. | 
**name** | **str** | the output name | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


