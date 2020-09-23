# BiosSystemBootOrderAllOf

Definition of the list of properties defined in 'bios.SystemBootOrder', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_mode** | **str** | The BIOS boot mode. UEFI uses the GUID Partition Table (GPT) whereas Legacy mode uses the Master Boot Record (MBR) partitioning scheme. | [optional] [readonly]  if omitted the server will use the default value of "Legacy"
**dn** | **str** | The Distinguished Name for this object, used to uniquely identify this object. | [optional] [readonly] 
**secure_boot** | **str** | Secure boot if set to enabled, enforces that device boots using only software that is trusted by the Original Equipment Manufacturer (OEM). | [optional] [readonly]  if omitted the server will use the default value of "Disabled"
**bios_unit** | [**BiosUnitRelationship**](BiosUnitRelationship.md) |  | [optional] 
**boot_devices** | [**[BiosBootDeviceRelationship], none_type**](BiosBootDeviceRelationship.md) | An array of relationships to biosBootDevice resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


