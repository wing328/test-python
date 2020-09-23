# TamSecurityAdvisoryDetails

Details pertaining to a security advisory defined by a given advisory.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**base_score** | **float** | CVSS version 3 base score for the security Advisory. | [optional] 
**cve_ids** | **[str]** |  | [optional] 
**environmental_score** | **float** | CVSS version 3 environmental score for the security Advisory. | [optional] 
**status** | **str** | Cisco assigned status of the published advisory. Depends on whether the investigation is complete or on-going. | [optional]  if omitted the server will use the default value of "interim"
**temporal_score** | **float** | CVSS version 3 temporal score for the security Advisory. | [optional] 
**description** | **str** | Brief description of details specified for an advisory type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


