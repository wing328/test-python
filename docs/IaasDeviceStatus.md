# IaasDeviceStatus

List of infra accounts managed by UCSD.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**account_name** | **str** | The UCSD infra account name. Account Name is created when UCSD admin adds any new infra account (Physical/Virtual/Compute/Network) to be managed by UCSD. | [optional] [readonly] 
**account_type** | **str** | The UCSD Infra Account type. | [optional] [readonly] 
**claim_status** | **str** | Describes if the device is claimed in Intersight or not. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**connection_status** | **str** | Describes about the connection status between the UCSD and the actual end device. | [optional] [readonly] 
**device_model** | **str** | Describes about the device model. | [optional] [readonly] 
**device_vendor** | **str** | Describes about the device vendor/manufacturer of the device. | [optional] [readonly] 
**device_version** | **str** | Describes about the current firmware version running on the device. | [optional] [readonly] 
**ip_address** | **str** | The IPAddress of the device. | [optional] [readonly] 
**pod** | **str** | Describes about the pod to which this device belongs to in UCSD. | [optional] [readonly] 
**pod_type** | **str** | Describes about the podType of Pod to which this device belongs to in UCSD. | [optional] [readonly] 
**guid** | [**IaasUcsdInfoRelationship**](IaasUcsdInfoRelationship.md) |  | [optional] 
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

