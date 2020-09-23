# StorageVirtualDrive

A Virtual Disk Drive or Logical Unit Number.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**access_policy** | **str** | The access policy of the virtual drive. | [optional] [readonly] 
**actual_write_cache_policy** | **str** | The current write cache policy of the virtual drive. | [optional] [readonly] 
**available_size** | **str** | Available storage capacity of the virtual drive. | [optional] [readonly] 
**block_size** | **str** | Block size of the virtual drive. | [optional] [readonly] 
**bootable** | **str** | The virtual drive bootable state. | [optional] [readonly] 
**config_state** | **str** | The configuration state of the virtual drive. | [optional] [readonly] 
**configured_write_cache_policy** | **str** | The requested write cache policy of the virtual drive. | [optional] [readonly] 
**connection_protocol** | **str** | The connection protocol of the virtual drive. | [optional] [readonly] 
**drive_cache** | **str** | The state of the drive cache of the virtual drive. | [optional] [readonly] 
**drive_security** | **str** | The driveSecurity state of the Virtual drive. | [optional] [readonly] 
**drive_state** | **str** | The state of the Virtual drive. | [optional] [readonly] 
**io_policy** | **str** | The Input/Output Policy defined on the Virtual drive. | [optional] [readonly] 
**name** | **str** | The name of the Virtual drive. | [optional] [readonly] 
**num_blocks** | **str** | Number of Blocks on the Physical Disk. | [optional] [readonly] 
**oper_state** | **str** | The current operational state of Virtual drive. | [optional] [readonly] 
**operability** | **str** | The current operability state of Virtual drive. | [optional] [readonly] 
**physical_block_size** | **str** | The block size of the the virtual drive. | [optional] [readonly] 
**presence** | **str** | The presence status of the virtual drive. | [optional] [readonly] 
**read_policy** | **str** | The read-ahead cache mode of the virtual drive. | [optional] [readonly] 
**security_flags** | **str** | The security flags set for this virtual drive. | [optional] [readonly] 
**size** | **str** | The size of the virtual drive in MB. | [optional] [readonly] 
**strip_size** | **str** | The strip size is the portion of a stripe that resides on a single drive in the drive group, this is measured in KB. | [optional] [readonly] 
**type** | **str** | The raid type of the virtual drive. | [optional] [readonly] 
**uuid** | **str** | The uuid of the virtual drive. | [optional] [readonly] 
**vendor_uuid** | **str** | The UUID value of the vendor. | [optional] [readonly] 
**virtual_drive_id** | **str** | The identifier for this Virtual drive. | [optional] [readonly] 
**disk_group** | [**StorageDiskGroupRelationship**](StorageDiskGroupRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**physical_disk_usages** | [**[StoragePhysicalDiskUsageRelationship], none_type**](StoragePhysicalDiskUsageRelationship.md) | An array of relationships to storagePhysicalDiskUsage resources. | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_controller** | [**StorageControllerRelationship**](StorageControllerRelationship.md) |  | [optional] 
**vd_member_eps** | [**[StorageVdMemberEpRelationship], none_type**](StorageVdMemberEpRelationship.md) | An array of relationships to storageVdMemberEp resources. | [optional] [readonly] 
**virtual_drive_extension** | [**StorageVirtualDriveExtensionRelationship**](StorageVirtualDriveExtensionRelationship.md) |  | [optional] 
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
**device_mo_id** | **str** | The database identifier of the registered device of an object. | [optional] [readonly] 
**dn** | **str** | The Distinguished Name unambiguously identifies an object in the system. | [optional] [readonly] 
**rn** | **str** | The Relative Name uniquely identifies an object within a given context. | [optional] [readonly] 
**model** | **str** | This field identifies the model of the given component. | [optional] [readonly] 
**revision** | **str** | This field identifies the revision of the given component. | [optional] [readonly] 
**serial** | **str** | This field identifies the serial of the given component. | [optional] [readonly] 
**vendor** | **str** | This field identifies the vendor of the given component. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

