# TelemetryDruidGreatestLeastPostAggregator

doubleGreatest and longGreatest computes the maximum of all fields and Double.NEGATIVE_INFINITY. doubleLeast and longLeast computes the minimum of all fields and Double.POSITIVE_INFINITY. The difference between the doubleMax aggregator and the doubleGreatest post-aggregator is that doubleMax returns the highest value of all rows for one specific column while doubleGreatest returns the highest value of multiple columns in one row. These are similar to the SQL MAX and GREATEST functions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The post-aggregator type. | 
**name** | **str** | Output name for the post-aggregator. | [optional] 
**fields** | **str** | the fields that are used to compute the greatest or least value. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


