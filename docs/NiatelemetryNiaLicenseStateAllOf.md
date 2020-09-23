# NiatelemetryNiaLicenseStateAllOf

Definition of the list of properties defined in 'niatelemetry.NiaLicenseState', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_activated** | **str** | Features activated on device being inventoried. This determines which features are currently enabled on the device that the license API can check. | [optional] 
**license_activated** | **str** | Licenses activated on device being inventoried. This determines which lienceses are currently enabled on the device. | [optional] 
**pid_type** | **str** | PID of device being inventoried. This determines the hardware model type of the device. | [optional] 
**serial** | **str** | Serial number of device being inventoried. The serial number is unique per device. | [optional] 
**device** | [**NiatelemetryNiaInventoryRelationship**](NiatelemetryNiaInventoryRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


