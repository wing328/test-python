# ApplianceUpgrade

Upgrade tracks the Intersight Appliance's software upgrades. Intersight Appliance's upgrade service automatically creates an Upgrade managed object when there is a pending software upgrade. User may modify an active Upgrade managed object to reset the software upgrade start time. However, user may not be able to postpone an upgrade beyond the limit enforced by the upgrade grace period set in the software manifest.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**active** | **bool** | Indicates if the software upgrade is active or not. | [optional] [readonly] 
**auto_created** | **bool** | Indicates that the request was automatically created by the system. | [optional] [readonly] 
**completed_phases** | [**[OnpremUpgradePhase]**](OnpremUpgradePhase.md) |  | [optional] 
**current_phase** | [**OnpremUpgradePhase**](OnpremUpgradePhase.md) |  | [optional] 
**description** | **str** | Description of the software upgrade. | [optional] [readonly] 
**elapsed_time** | **int** | Elapsed time in seconds during the software upgrade. | [optional] [readonly] 
**end_time** | **datetime** | End date of the software upgrade. | [optional] [readonly] 
**error_code** | **int** | Error code for Intersight Appliance&#39;s software upgrade. In case of failure - this code will help decide if software upgrade can be retried. | [optional] [readonly] 
**fingerprint** | **str** | Software upgrade manifest&#39;s fingerprint. | [optional] [readonly] 
**is_rolling_back** | **bool** | Track if software upgrade is upgrading or rolling back. | [optional] [readonly] 
**messages** | **[str]** |  | [optional] 
**rollback_needed** | **bool** | Track if rollback is needed. | [optional] 
**rollback_phases** | [**[OnpremUpgradePhase]**](OnpremUpgradePhase.md) |  | [optional] 
**rollback_status** | **str** | Status of the Intersight Appliance&#39;s software rollback status. | [optional] [readonly] 
**services** | **[str]** |  | [optional] 
**start_time** | **datetime** | Start date of the software upgrade. UI can modify startTime to re-schedule an upgrade. | [optional] 
**status** | **str** | Status of the Intersight Appliance&#39;s software upgrade. | [optional] [readonly] 
**total_phases** | **int** | TotalPhase represents the total number of the upgradePhases for one upgrade. | [optional] [readonly] 
**ui_packages** | **[str]** |  | [optional] 
**version** | **str** | Software upgrade manifest&#39;s version. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**image_bundle** | [**ApplianceImageBundleRelationship**](ApplianceImageBundleRelationship.md) |  | [optional] 
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


