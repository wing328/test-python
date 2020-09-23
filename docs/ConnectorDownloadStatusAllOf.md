# ConnectorDownloadStatusAllOf

Definition of the list of properties defined in 'connector.DownloadStatus', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | [**ConnectorFileChecksum**](ConnectorFileChecksum.md) |  | [optional] 
**download_error** | **bool, date, datetime, dict, float, int, list, str, none_type** | Any error encountered. Set to empty when download is in progress or completed.} type: string | [optional] 
**download_progress** | **int** | The download progress of the file represented as a percentage between 0% and 100%. If progress reporting is not possible a value of -1 is sent. | [optional] 
**download_retries** | **int** | The number of retries the plugin attempted before succeeding or failing the download. | [optional] 
**sha256checksum** | **str** | The sha256checksum of the downloaded file as calculated by the download plugin after successfully downloading a file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


