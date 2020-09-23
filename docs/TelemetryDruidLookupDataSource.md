# TelemetryDruidLookupDataSource

Lookup datasources correspond to Druid's key-value lookup objects. In Druid SQL, they reside in the the lookup schema. They are preloaded in memory on all servers, so they can be accessed rapidly. They can be joined onto regular tables using the join operator. Lookup datasources are key-value oriented and always have exactly two columns, k (the key) and v (the value), and both are always strings. Lookups can be joined with a base table either using an explicit join, or by using the SQL LOOKUP function. However, the join operator must evaluate the condition on each row, whereas the LOOKUP function can defer evaluation until after an aggregation phase. This means that the LOOKUP function is usually faster than joining to a lookup datasource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of data source. | 
**lookup** | **str** | the name of the lookup object. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


