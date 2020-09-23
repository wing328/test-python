# TelemetryDruidDataSource

A data source is the Apache Druid equivalent of a database table. However, a query can also masquerade as a data source, providing subquery-like functionality. Query data sources are currently supported only by GroupBy queries.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of data source. | 
**name** | **str** | The name of a data source. | defaults to nulltype.Null
**data_sources** | **[str]** | A list of data sources. | defaults to nulltype.Null
**query** | [**TelemetryDruidGroupByRequest**](TelemetryDruidGroupByRequest.md) |  | defaults to nulltype.Null
**lookup** | **str** | the name of the lookup object. | defaults to nulltype.Null
**left** | **str** | Left-hand datasource. Must be of type table, join, lookup, query, or inline. Placing another join as the left datasource allows you to join arbitrarily many datasources. | defaults to nulltype.Null
**right** | **str** | Right-hand datasource. Must be of type lookup, query, or inline. | defaults to nulltype.Null
**right_prefix** | **str** | String prefix that will be applied to all columns from the right-hand datasource, to prevent them from colliding with columns from the left-hand datasource. Can be any string, so long as it is nonempty and is not be a prefix of the string __time. Any columns from the left-hand side that start with your rightPrefix will be shadowed. It is up to you to provide a prefix that will not shadow any important columns from the left side. | defaults to nulltype.Null
**condition** | **str** | Expression that must be an equality where one side is an expression of the left-hand side, and the other side is a simple column reference to the right-hand side. The right-hand reference must be a simple column reference. | defaults to nulltype.Null
**join_type** | **str** |  | defaults to nulltype.Null
**column_names** | **[str]** | the column names. | defaults to nulltype.Null
**rows** | **[[str]]** | an array of rows. | defaults to nulltype.Null
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


