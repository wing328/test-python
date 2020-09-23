# MoTagSummary

A document returned in a response body when the HTTP GET request specifies the 'tag' query parameter.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | A discriminator value to disambiguate the schema of a HTTP GET response body. | 
**object_type** | **str** | A discriminator value to disambiguate the schema of a HTTP GET response body. | [optional] 
**results** | [**[MoTagKeySummary], none_type**](MoTagKeySummary.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


