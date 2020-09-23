# WorkflowWorkflowMeta

Contains a workflow definition which is a sequence of tasks to execute.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**description** | **str** | The description for the workflow. | [optional] 
**input_parameters** | **[str]** |  | [optional] 
**name** | **str** | The name given to the workflow. | [optional] 
**output_parameters** | **bool, date, datetime, dict, float, int, list, str, none_type** | The workflow output parameters. | [optional] 
**retryable** | **bool** | When true, this workflow can be retried for 2 weeks since the last modification of the workflow. | [optional] 
**schema_version** | **int** | The Conductor schema version that decides what attribute can be supported. | [optional] 
**src** | **str** | The src is workflow owner service. | [optional] 
**tasks** | **bool, date, datetime, dict, float, int, list, str, none_type** | The tasks contained inside of the workflow. | [optional] 
**type** | **str** | The type of workflow definition. | [optional]  if omitted the server will use the default value of "SystemDefined"
**version** | **int** | The version for the workflow so we can support multiple versions for the same workflow name. | [optional] 
**wait_on_duplicate** | **bool** | Parameter decides if workflows will wait for a duplicate to finish before starting a new one. | [optional] 
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
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


