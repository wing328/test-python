# PciCoprocessorCardList

This resource list is returned as a response to a HTTP GET request that does not include a specific resource identifier.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | A discriminator value to disambiguate the schema of a HTTP GET response body. | 
**count** | **int** | The total number of &#39;pci.CoprocessorCard&#39; resources matching the request, accross all pages. The &#39;Count&#39; attribute is included when the HTTP GET request includes the &#39;$inlinecount&#39; parameter. | [optional] 
**results** | [**[PciCoprocessorCard], none_type**](PciCoprocessorCard.md) | The array of &#39;pci.CoprocessorCard&#39; resources matching the request. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


