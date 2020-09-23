# FirmwareUpgradeBase

Firmware upgrade operation that downloads the image from Cisco/appliance/user provided HTTP repository or use the image from a network share and upgrade. The direct download is used for upgrade to use the image from Cisco repository or appliance repository. The network share is used for upgrade to use the image from a network share in user data center.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**direct_download** | [**FirmwareDirectDownload**](FirmwareDirectDownload.md) |  | [optional] 
**file_server** | [**SoftwarerepositoryFileServer**](SoftwarerepositoryFileServer.md) |  | [optional] 
**network_share** | [**FirmwareNetworkShare**](FirmwareNetworkShare.md) |  | [optional] 
**skip_estimate_impact** | **bool** | User has the option to skip the estimate impact calculation. | [optional] 
**status** | **str** | Status of the upgrade operation. | [optional]  if omitted the server will use the default value of "NONE"
**upgrade_type** | **str** | Desired upgrade mode to choose either direct download based upgrade or network share upgrade. | [optional]  if omitted the server will use the default value of "direct_upgrade"
**distributable** | [**FirmwareDistributableRelationship**](FirmwareDistributableRelationship.md) |  | [optional] 
**release** | [**SoftwarerepositoryReleaseRelationship**](SoftwarerepositoryReleaseRelationship.md) |  | [optional] 
**upgrade_impact** | [**FirmwareUpgradeImpactStatusRelationship**](FirmwareUpgradeImpactStatusRelationship.md) |  | [optional] 
**upgrade_status** | [**FirmwareUpgradeStatusRelationship**](FirmwareUpgradeStatusRelationship.md) |  | [optional] 
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

