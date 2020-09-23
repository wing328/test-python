# FirmwareNetworkShareAllOf

Definition of the list of properties defined in 'firmware.NetworkShare', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cifs_server** | [**FirmwareCifsServer**](FirmwareCifsServer.md) |  | [optional] 
**http_server** | [**FirmwareHttpServer**](FirmwareHttpServer.md) |  | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**map_type** | **str** | File server protocols such as CIFS, NFS, WWW for HTTP (S) that hosts the image. | [optional]  if omitted the server will use the default value of "nfs"
**nfs_server** | [**FirmwareNfsServer**](FirmwareNfsServer.md) |  | [optional] 
**password** | **str** | Password as configured on the file server. | [optional] 
**upgradeoption** | **str** | Option to control the upgrade operation. Some examples, 1) nw_upgrade_mount_only - mount the image from a file server and run the upgrade on the next server boot and 2) nw_upgrade_full - mount the image and immediately run the upgrade. | [optional]  if omitted the server will use the default value of "nw_upgrade_full"
**username** | **str** | Username as configured on the file server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


