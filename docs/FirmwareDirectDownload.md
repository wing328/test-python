# FirmwareDirectDownload

A specification for downloading the image from Cisco or appliance repository or user provided HTTP file server that hosts the image for firmware upgrade.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**http_server** | [**FirmwareHttpServer**](FirmwareHttpServer.md) |  | [optional] 
**image_source** | **str** | Source type referring the image to be downloaded from CCO or from a local HTTPS server. | [optional]  if omitted the server will use the default value of "cisco"
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**password** | **str** | Password as configured on the local https server. | [optional] 
**upgradeoption** | **str** | Option to control the upgrade, e.g., sd_upgrade_mount_only - download the image into sd and upgrade wait for the server on-next boot. | [optional]  if omitted the server will use the default value of "sd_upgrade_mount_only"
**username** | **str** | Username as configured on the local https server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


