# MetaRelationshipDefinitionAllOf

Definition of the list of properties defined in 'meta.RelationshipDefinition', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_access** | **str** | API access definition for this relationship. | [optional] [readonly]  if omitted the server will use the default value of "NoAccess"
**collection** | **bool** | Specifies whether the relationship is a collection. | [optional] [readonly] 
**export** | **bool** | When turned off, the peer MO is not exported when the local MO is exported. | [optional] [readonly] 
**export_with_peer** | **bool** | When turned on, the local MO is exported when the peer is exported. | [optional] [readonly] 
**name** | **str** | The name of the relationship. | [optional] [readonly] 
**type** | **str** | Fully qualified type of the foreign managed object. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


