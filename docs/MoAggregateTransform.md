# MoAggregateTransform

The output of a request that includes the $apply query parameter. The schema of an aggregation query is dynamically determined based on the request query parameters.  See https://intersight.com/apidocs/introduction/query/#apply-query-option for more details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | A discriminator value to disambiguate the schema of a HTTP GET response body. | 
**results** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type** | The results of the aggregation query. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


