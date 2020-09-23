# TelemetryDruidDurationGranularity

Duration granularities are specified as an exact duration in milliseconds and timestamps are returned as UTC. Duration granularity values are in milliseconds. They also support specifying an optional origin, which defines where to start counting time buckets from (defaults to 1970-01-01T00:00:00Z).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of granularity. | 
**duration** | **int** | The duration in milliseconds. | 
**origin** | **datetime** | An optional value specifying when to start counting time buckets from. The default value is 1970-01-01T00:00:00Z. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


