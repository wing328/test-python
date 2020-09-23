# StorageVirtualDriveConfig

The type models a single virtual drive that needs to be created through this policy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**access_policy** | **str** | Access policy that host has on this virtual drive. | [optional]  if omitted the server will use the default value of "Default"
**boot_drive** | **bool** | The flag enables the use of this virtual drive as a boot drive. | [optional] 
**disk_group_name** | **str** | Disk group policy that has the disk group in which this virtual drive needs to be created. | [optional] [readonly] 
**disk_group_policy** | **str** | Disk group policy that has the disk group in which this virtual drive needs to be created. | [optional] 
**drive_cache** | **str** | The property expect disk cache policy. | [optional]  if omitted the server will use the default value of "Default"
**expand_to_available** | **bool** | The flag enables this virtual drive to use all the available space in the disk group. When this flag is configured, the size property is ignored. | [optional] 
**io_policy** | **str** | Desired IO mode - direct IO or cached IO. | [optional]  if omitted the server will use the default value of "Default"
**name** | **str** | The name of the virtual drive. The name can be between 1 and 15 alphanumeric characters. Spaces or any special characters other than - (hyphen), _ (underscore), : (colon), and . (period) are not allowed. | [optional] 
**read_policy** | **str** | Read ahead mode to be used to read data from this virtual drive. | [optional]  if omitted the server will use the default value of "Default"
**size** | **int** | Virtual drive size in MB. Size is mandatory field unless the &#39;Expand to Available&#39; option is enabled. | [optional] 
**write_policy** | **str** | Write mode to be used to write data to this virtual drive. | [optional]  if omitted the server will use the default value of "Default"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


