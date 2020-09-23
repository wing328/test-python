# NiatelemetryNiaInventoryAllOf

Definition of the list of properties defined in 'niatelemetry.NiaInventory', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


