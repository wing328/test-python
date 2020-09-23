# SoftwarerepositoryDownloadSpecAllOf

Definition of the list of properties defined in 'softwarerepository.DownloadSpec', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** | The OAuth2 token that will be used during image download by the endpoint to authenticate with file server. | [optional] 
**certificate** | **str** | The certificate of file server that will be used by the endpoint to validate the server before starting the file download. | [optional] 
**filename** | **str** | The name of the firmware image. | [optional] 
**md5sum** | **str** | MD5 sum of the firmware image that will be used by the endpoint to validate the integrity of the image, post download. | [optional] 
**size** | **int** | The size (in bytes) of the firmware image. | [optional] 
**url** | **str** | The URL of this file in file server. The endpoint uses this URL to download the file from the file server. | [optional] 
**file** | [**SoftwarerepositoryFileRelationship**](SoftwarerepositoryFileRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


