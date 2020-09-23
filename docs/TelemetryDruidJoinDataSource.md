# TelemetryDruidJoinDataSource

Join datasources allow you to do a SQL-style join of two datasources. Stacking joins on top of each other allows you to join arbitrarily many datasources. Joins are implemented with a broadcast hash-join algorithm. This means that all tables other than the leftmost \"base\" table must fit in memory. It also means that the join condition must be an equality. This feature is intended mainly to allow joining regular Druid tables with lookup, inline, and query datasources.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of data source. | 
**left** | **str** | Left-hand datasource. Must be of type table, join, lookup, query, or inline. Placing another join as the left datasource allows you to join arbitrarily many datasources. | 
**right** | **str** | Right-hand datasource. Must be of type lookup, query, or inline. | 
**right_prefix** | **str** | String prefix that will be applied to all columns from the right-hand datasource, to prevent them from colliding with columns from the left-hand datasource. Can be any string, so long as it is nonempty and is not be a prefix of the string __time. Any columns from the left-hand side that start with your rightPrefix will be shadowed. It is up to you to provide a prefix that will not shadow any important columns from the left side. | 
**condition** | **str** | Expression that must be an equality where one side is an expression of the left-hand side, and the other side is a simple column reference to the right-hand side. The right-hand reference must be a simple column reference. | 
**join_type** | **str** |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


