# TelemetryDruidInlineDataSource

Inline datasources allow you to query a small amount of data that is embedded in the query itself. They are useful when you want to write a query on a small amount of data without loading it first. They are also useful as inputs into a join. Druid also uses them internally to handle subqueries that need to be inlined on the Broker. There are two fields in an inline datasource, an array of columnNames and an array of rows. Each row is an array that must be exactly as long as the list of columnNames. The first element in each row corresponds to the first column in columnNames, and so on.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of data source. | 
**column_names** | **[str]** | the column names. | 
**rows** | **[[str]]** | an array of rows. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


