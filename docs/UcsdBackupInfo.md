# UcsdBackupInfo

List of backup images available for target end device for restore operation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**backup_file_name** | **str** | Auto generated backup File Name with combination of file prefix given an user input and the timestamp. | [optional] [readonly] 
**backup_location** | **str** | Backup location that contains the backup images for end device which can be used for restore operation. | [optional] [readonly] 
**backup_server_ip** | **str** | Backup server where backup images are maintained. | [optional] [readonly] 
**backup_size** | **int** | Size of the backup image in bytes. | [optional] [readonly] 
**connectors** | [**[UcsdConnectorPack]**](UcsdConnectorPack.md) |  | [optional] 
**duration** | **int** | Time taken for the backup to be completed. | [optional] [readonly] 
**encryption_key** | **str** | The key used for encrypting the backup file. | [optional] 
**failure_reason** | **str** | Reason for backup failure. | [optional] [readonly] 
**is_purged** | **bool** | Backup image got purged or not. The backup images get purged based on the retention count set by the user in the backup config policy. | [optional] [readonly] 
**last_modified** | **datetime** | Last modified time when this backup record got updated. | [optional] [readonly] 
**percentage_completion** | **int** | Backup current precentage completion status information. | [optional] [readonly] 
**product_version** | **str** | The end device product version when the backup image was taken. | [optional] 
**protocol** | **str** | Protocol used for the remote backup. possible values are FTP, SCP and SFTP. Not applicable for the localhost (127.0.0.1). | [optional] [readonly] 
**stage_completion** | **str** | Backup current status stage information. | [optional] [readonly] 
**start_time** | **datetime** | Start time of backup when it got initiated. | [optional] [readonly] 
**status** | **str** | Current status of Backup current. | [optional] [readonly] 
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
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


