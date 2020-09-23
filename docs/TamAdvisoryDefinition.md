# TamAdvisoryDefinition

An Intersight Advisory. An advisory represents an identification of a potential issue and may also include  a recommendation for resolving the said issue. Advisories may be of different kind and severity. for e.g. It could be a security vulnerability or a performance issue or a hardware issue with different recommendations for resolving them.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**actions** | [**[TamAction]**](TamAction.md) |  | [optional] 
**advisory_details** | [**TamBaseAdvisoryDetails**](TamBaseAdvisoryDetails.md) |  | [optional] 
**advisory_id** | **str** | Cisco generated identifier for the published security advisory. | [optional] 
**api_data_sources** | [**[TamApiDataSource]**](TamApiDataSource.md) |  | [optional] 
**date_published** | **datetime** | Date when the security advisory was first published by Cisco. | [optional] 
**date_updated** | **datetime** | Date when the security advisory was last updated by Cisco. | [optional] 
**external_url** | **str** | A link to an external URL describing security Advisory in more details. | [optional] 
**recommendation** | **str** | Recommended action to resolve the security advisory. | [optional] 
**type** | **str** | The type (field notice, security advisory etc.) of Intersight advisory. | [optional]  if omitted the server will use the default value of "securityAdvisory"
**version** | **str** | Cisco assigned advisory version after latest revision. | [optional] 
**workaround** | **str** | Workarounds available for the advisory. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**account_moid** | **str** | The Account ID for this managed object. | [optional] [readonly] 
**create_time** | **datetime** | The time when this managed object was created. | [optional] [readonly] 
**domain_group_moid** | **str** | The DomainGroup ID for this managed object. | [optional] [readonly] 
**mod_time** | **datetime** | The time when this managed object was last modified. | [optional] [readonly] 
**moid** | **str** | The unique identifier of this Managed Object instance. | [optional] 
**owners** | **[str]** |  | [optional] 
**shared_scope** | **str** | Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a &#39;shared&#39; ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs. | [optional] [readonly] 
**tags** | [**[MoTag]**](MoTag.md) |  | [optional] 
**version_context** | [**MoVersionContext**](MoVersionContext.md) |  | [optional] 
**ancestors** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**parent** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**permission_resources** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**display_names** | [**DisplayNames**](DisplayNames.md) |  | [optional] 
**description** | **str** | Brief description of the advisory details. | [optional] 
**name** | **str** | A user defined name for the Intersight Advisory. | [optional] 
**severity** | [**TamSeverity**](TamSeverity.md) |  | [optional] 
**state** | **str** | Current state of the advisory. | [optional]  if omitted the server will use the default value of "ready"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


