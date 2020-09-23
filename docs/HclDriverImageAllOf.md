# HclDriverImageAllOf

Definition of the list of properties defined in 'hcl.DriverImage', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_iso_url** | **str** | URL of the driver ISO images. | [optional] 
**management_type** | **str** | Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release. | [optional]  if omitted the server will use the default value of "UCSM"
**server_pid** | **str** | Three part ID representing the server model as returned by UCSM/CIMC XML APIs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


