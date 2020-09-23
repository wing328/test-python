# MoDocumentCount

A document returned in a response body when the HTTP GET request specifies the '$count' query parameter.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | A discriminator value to disambiguate the schema of a HTTP GET response body. | 
**count** | **int** | The total number of resources matching the query filter, accross all pages. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


