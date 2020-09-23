# CmrfCmRf

A reference to a REST resource from a complex type, uniquely identified by object type and Moid. CMRF is a short term workaround until MoRef properties of complex types can be supported. CMRF means complex type managed object reference and is unique enough that it can be removed easily later. The long term solution is to support for relationships stanza under complextypes. Deprecated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The Object Type of the referenced REST resource. | [readonly] 
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**moid** | **str** | The Moid of the referenced REST resource. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


