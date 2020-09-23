# IaasUcsdManagedInfra

Describes about UCSD Managed infrastructure statistics.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**advanced_catalog_count** | **int** | Total advanced catalogs in UCSD. | [optional] [readonly] 
**bm_catalog_count** | **int** | Total bare metal catalogs in UCSD. | [optional] [readonly] 
**container_catalog_count** | **int** | Total service container catalogs in UCSD. | [optional] [readonly] 
**esxi_host_count** | **int** | Total ESXi hosts in UCSD. | [optional] [readonly] 
**external_group_count** | **int** | Total external (Ldap) groups in UCSD. | [optional] [readonly] 
**hyperv_host_count** | **int** | Total HyperV hosts in UCSD. | [optional] [readonly] 
**local_group_count** | **int** | Total local groups in UCSD. | [optional] [readonly] 
**standard_catalog_count** | **int** | Total standard catalogs in UCSD. | [optional] [readonly] 
**user_count** | **int** | Total user accounts in UCSD. | [optional] [readonly] 
**vdc_count** | **int** | Total virtual datacenters in UCSD. | [optional] [readonly] 
**vm_count** | **int** | Total Virtual machines in UCSD. | [optional] [readonly] 
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


