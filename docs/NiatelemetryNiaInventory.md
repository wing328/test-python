# NiatelemetryNiaInventory

Inventory object available per device scope. This common object holds a device level information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**cpu** | **float** | CPU usage of device being inventoried. This determines the percentage of CPU resources used. | [optional] 
**crash_reset_logs** | **str** | Last crash reset reason of device being inventoried. This determines the last reason for a device&#39;s restart due to crash of the system. | [optional] 
**device_name** | **str** | Name of device being inventoried. The name the user assigns to the device is inventoried here. | [optional] 
**device_type** | **str** | Type of device being inventoried. This determines whether the device is a controller, leaf or spine. | [optional] 
**disk** | [**NiatelemetryDiskinfo**](NiatelemetryDiskinfo.md) |  | [optional] 
**log_in_time** | **str** | Last log in time device being inventoried. This determines the last login time on the device. | [optional] 
**log_out_time** | **str** | Last log out time of device being inventoried. This determines the last logout time on the device. | [optional] 
**memory** | **int** | Memory usage of device being inventoried. This determines the percentage of memory resources used. | [optional] 
**record_type** | **str** | Type of record DCNM / APIC / SE. This determines the type of platform where inventory was collected. | [optional] 
**record_version** | **str** | Version of record being pushed. This determines what was the API version for data available from the device. | [optional] 
**serial** | **str** | Serial number of device being invetoried. The serial number is unique per device and will be used as the key. | [optional] 
**software_download** | **str** | Last software downloaded of device being inventoried. This determines if software download API was used. | [optional] 
**version** | **str** | Software version of device being inventoried. The various software version values for each device are available on cisco.com. | [optional] 
**license_state** | [**NiatelemetryNiaLicenseStateRelationship**](NiatelemetryNiaLicenseStateRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
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


