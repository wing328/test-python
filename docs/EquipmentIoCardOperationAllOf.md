# EquipmentIoCardOperationAllOf

Definition of the list of properties defined in 'equipment.IoCardOperation', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_power_state** | **str** | User configured power state of the iomodule. | [optional]  if omitted the server will use the default value of "None"
**config_state** | **str** | The configured state of these settings in the target chassis. The value is any one of Applied, Applying, Failed. Applied - This state denotes that the settings are applied successfully in the target chassis iomodule. Applying - This state denotes that the settings are being applied in the target chassis iomodule. Failed - This state denotes that the settings could not be applied in the target chassis iomodule. | [optional] [readonly]  if omitted the server will use the default value of "None"
**device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**io_card** | [**EquipmentIoCardRelationship**](EquipmentIoCardRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


