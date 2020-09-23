# ApplianceImageBundle

ImageBundle keeps track of all the software bundles installed in the Intersight Appliances. Each ImageBundle managed object is derived from a software upgrade manifest. ImageBundle has additional properties computed during the manifest processing. Additional properties are the dynamic attributes of the software packages declared in the software manifest. For example, SHA256 values of the software packages are computed during the software manifest processing. An ImageBundle managed object named 'current' is always present in the Intersight Appliance. The software upgrade service creates another ImageBundle managed object named 'pending' when there is a pending software upgrade. The upgrade service renames the 'pending' bundle to the 'current' bundle after the software upgrade is successful.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**ansible_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**auto_upgrade** | **bool** | Indicates that the software upgrade was automatically initiated by the Intersight Appliance. | [optional] [readonly] 
**dc_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**debug_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**description** | **str** | Short description of the software upgrade bundle. | [optional] [readonly] 
**endpoint_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**fingerprint** | **str** | Fingerprint of the software manifest from which this bundle is created. Fingerprint is calculated using the SHA256 algorithm. | [optional] [readonly] 
**has_error** | **bool** | Indicates that the ImageBundle has errors. The upgrade service sets this field when it encounters errors during the manifest processing. | [optional] [readonly] 
**infra_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**init_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**name** | **str** | Name of the software upgrade bundle. | [optional] [readonly] 
**notes** | **str** | Detailed description of the software upgrade bundle. | [optional] [readonly] 
**priority** | **str** | Software upgrade manifest&#39;s upgrade priority. The upgrade service supports two priorities, Normal and Critical. Normal priority is used for regular software upgrades, and the upgrade service uses the Upgrade Policy to compute upgrade start time. Critical priority is used for the critical software security patches, and the upgrade service ignores the Upgrade Policy when it computes the upgrade start time. | [optional] [readonly]  if omitted the server will use the default value of "Normal"
**release_time** | **datetime** | Software upgrade manifest&#39;s release date and time. | [optional] [readonly] 
**service_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**status_message** | **str** | Status message set during the manifest processing. | [optional] [readonly] 
**system_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**ui_packages** | [**[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**upgrade_end_time** | **datetime** | End date of the software upgrade process. | [optional] [readonly] 
**upgrade_grace_period** | **int** | Grace period in seconds before the automatic upgrade is initiated. The upgrade service uses the grace period to compute the upgrade start time when it receives an upgrade notfication from the Intersight. If there is an Upgrade Policy configured for the Intersight Appliance, then the upgrade service uses the policy to compute the upgrade start time. However, the upgrade start time cannot not exceed the limit enforced by the grace period. | [optional] [readonly] 
**upgrade_impact_duration** | **int** | Duration (in minutes) for which services will be disrupted. | [optional] [readonly] 
**upgrade_impact_enum** | **str** | UpgradeImpactEnum is used to indicate the kind of impact the upgrade has on currently running services on the appliance. | [optional] [readonly]  if omitted the server will use the default value of "None"
**upgrade_start_time** | **datetime** | Start date of the software upgrade process. | [optional] [readonly] 
**version** | **str** | Software upgrade manifest&#39;s version. | [optional] [readonly] 
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

