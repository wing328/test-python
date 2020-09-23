# TelemetryDruidGranularity

The granularity field determines how data gets bucketed across the time dimension, or how it gets aggregated by hour, day, minute, etc. It can be specified either as a string for simple granularities or as an object for arbitrary granularities. See [Granularities](https://druid.apache.org/docs/latest/querying/granularities.html).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of granularity. | 
**duration** | **int** | The duration in milliseconds. | defaults to nulltype.Null
**period** | **str** | The period in ISO 8601 format. Examples are P2W, P3M, PT1H30M, PT0.750S. | defaults to nulltype.Null
**origin** | **datetime** | An optional value specifying when to start counting time buckets from. The default value is 1970-01-01T00:00:00Z. | [optional] 
**time_zone** | **str** | An optional value specifying the time zone. Standard [IANA time zones](http://joda-time.sourceforge.net/timezones.html) are supported. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


