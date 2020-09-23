# TelemetryDruidPeriodGranularity

Period granularities are specified as arbitrary period combinations of years, months, weeks, hours, minutes and seconds (e.g. P2W, P3M, PT1H30M, PT0.750S) in ISO8601 format. They support specifying a time zone which determines where period boundaries start as well as the timezone of the returned timestamps. By default, years start on the first of January, months start on the first of the month and weeks start on Mondays unless an origin is specified. Time zone is optional (defaults to UTC). Origin is optional (defaults to 1970-01-01T00:00:00 in the given time zone).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of granularity. | 
**period** | **str** | The period in ISO 8601 format. Examples are P2W, P3M, PT1H30M, PT0.750S. | 
**time_zone** | **str** | An optional value specifying the time zone. Standard [IANA time zones](http://joda-time.sourceforge.net/timezones.html) are supported. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


