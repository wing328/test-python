# FirmwareNetworkShare

Firmware upgrade where the image is located in remote shared machine.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**cifs_server** | [**FirmwareCifsServer**](FirmwareCifsServer.md) |  | [optional] 
**http_server** | [**FirmwareHttpServer**](FirmwareHttpServer.md) |  | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**map_type** | **str** | File server protocols such as CIFS, NFS, WWW for HTTP (S) that hosts the image. | [optional]  if omitted the server will use the default value of "nfs"
**nfs_server** | [**FirmwareNfsServer**](FirmwareNfsServer.md) |  | [optional] 
**password** | **str** | Password as configured on the file server. | [optional] 
**upgradeoption** | **str** | Option to control the upgrade operation. Some examples, 1) nw_upgrade_mount_only - mount the image from a file server and run the upgrade on the next server boot and 2) nw_upgrade_full - mount the image and immediately run the upgrade. | [optional]  if omitted the server will use the default value of "nw_upgrade_full"
**username** | **str** | Username as configured on the file server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


