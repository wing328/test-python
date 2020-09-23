# HclHardwareCompatibilityProfileAllOf

Definition of the list of properties defined in 'hcl.HardwareCompatibilityProfile', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_iso_url** | **str** | Url for the ISO with the drivers supported for the server. | [optional] 
**error_code** | **str** | Error code indicating the compatibility status. | [optional] [readonly]  if omitted the server will use the default value of "Success"
**id** | **str** | Identifier of the hardware compatibility profile. | [optional] 
**os_vendor** | **str** | Vendor of the Operating System running on the server. | [optional] 
**os_version** | **str** | Version of the Operating System running on the server. | [optional] 
**processor_model** | **str** | Model of the processor present in the server. | [optional] 
**products** | [**[HclProduct]**](HclProduct.md) |  | [optional] 
**server_model** | **str** | Model of the server as returned by UCSM/CIMC XML API. | [optional] 
**server_revision** | **str** | Revision of the server model. | [optional] 
**ucs_version** | **str** | Version of the UCS software. | [optional] 
**version_type** | **str** | Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release. | [optional]  if omitted the server will use the default value of "UCSM"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

