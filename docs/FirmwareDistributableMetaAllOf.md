# FirmwareDistributableMetaAllOf

Definition of the list of properties defined in 'firmware.DistributableMeta', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | The S3 bucket name where the images are present, if source is external cloud store. | [optional] 
**file_type** | **str** | The type of distributable image, example huu, scu, driver, os. | [optional]  if omitted the server will use the default value of "Distributable"
**from_version** | **str** | The version from which user can download images from amazon store, if source is external cloud store. | [optional] 
**mdfid** | **str** | The mdfid of the image provided by cisco.com. | [optional] 
**software_type_id** | **str** | The software type id provided by cisco.com. | [optional] 
**source** | **str** | The image can be downloaded from cisco.com or external cloud store. | [optional]  if omitted the server will use the default value of "Cisco"
**supported_models** | **[str]** |  | [optional] 
**to_version** | **str** | The version till which user can download images from amazon store, if source is external cloud store. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


