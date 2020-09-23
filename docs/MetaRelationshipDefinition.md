# MetaRelationshipDefinition

Definitions for the relationship in a meta.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**api_access** | **str** | API access definition for this relationship. | [optional] [readonly]  if omitted the server will use the default value of "NoAccess"
**collection** | **bool** | Specifies whether the relationship is a collection. | [optional] [readonly] 
**export** | **bool** | When turned off, the peer MO is not exported when the local MO is exported. | [optional] [readonly] 
**export_with_peer** | **bool** | When turned on, the local MO is exported when the peer is exported. | [optional] [readonly] 
**name** | **str** | The name of the relationship. | [optional] [readonly] 
**type** | **str** | Fully qualified type of the foreign managed object. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


