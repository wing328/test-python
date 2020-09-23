# BootSan

Device type used when booting from SAN Boot device.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**bootloader** | [**BootBootloader**](BootBootloader.md) |  | [optional] 
**lun** | **int** | The Logical Unit Number (LUN) of the device. | [optional] 
**slot** | **str** | Slot ID of the device. Supported values are ( 1 - 255, \&quot;MLOM\&quot;, \&quot;L1\&quot;, \&quot;L2\&quot; ). | [optional] 
**enabled** | **bool** | Specifies if the boot device is enabled or disabled. | [optional] 
**name** | **str** | A name that helps identify a boot device. It can be any string that adheres to the following constraints. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


