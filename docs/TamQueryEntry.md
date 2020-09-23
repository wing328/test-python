# TamQueryEntry

Contains a set of queries, each with an integer priority. the queries are executed in the order of specified priority. The result of each query is used as an input to the query next in priority order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**name** | **str** | Name is used to unique identify and result of the given query which can be used by subsequent queries as input data source. | [optional] 
**priority** | **int** | An integer value depicting the priority of the query among the queries that are part of the same QueryEntry collection. | [optional] 
**query** | **str** | A SparkSQL query to be used on a given data source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


