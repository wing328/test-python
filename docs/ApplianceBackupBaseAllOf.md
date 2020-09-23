# ApplianceBackupBaseAllOf

Definition of the list of properties defined in 'appliance.BackupBase', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Backup filename to backup or restore. | [optional] 
**protocol** | **str** | Communication protocol used by the file server (e.g. scp or sftp). | [optional]  if omitted the server will use the default value of "scp"
**remote_host** | **str** | Hostname of the remote file server. | [optional] 
**remote_path** | **str** | File server directory to copy the file. | [optional] 
**remote_port** | **int** | Remote TCP port on the file server (e.g. 22 for scp). | [optional] 
**username** | **str** | Username to authenticate the fileserver. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


