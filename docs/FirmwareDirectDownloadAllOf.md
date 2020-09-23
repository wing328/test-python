# FirmwareDirectDownloadAllOf

Definition of the list of properties defined in 'firmware.DirectDownload', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_server** | [**FirmwareHttpServer**](FirmwareHttpServer.md) |  | [optional] 
**image_source** | **str** | Source type referring the image to be downloaded from CCO or from a local HTTPS server. | [optional]  if omitted the server will use the default value of "cisco"
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**password** | **str** | Password as configured on the local https server. | [optional] 
**upgradeoption** | **str** | Option to control the upgrade, e.g., sd_upgrade_mount_only - download the image into sd and upgrade wait for the server on-next boot. | [optional]  if omitted the server will use the default value of "sd_upgrade_mount_only"
**username** | **str** | Username as configured on the local https server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


