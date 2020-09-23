# TelemetryDruidTimeBoundaryRequest

Time boundary queries return the earliest and latest data points of a data set.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_type** | **str** | null | 
**data_source** | [**TelemetryDruidDataSource**](TelemetryDruidDataSource.md) |  | 
**bound** | **str** | Optional, set to maxTime or minTime to return only the latest or earliest timestamp. Default to returning both if not set. | [optional] 
**filter** | [**TelemetryDruidFilter**](TelemetryDruidFilter.md) |  | [optional] 
**context** | [**TelemetryDruidQueryContext**](TelemetryDruidQueryContext.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


