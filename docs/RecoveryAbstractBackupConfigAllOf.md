# RecoveryAbstractBackupConfigAllOf

Definition of the list of properties defined in 'recovery.AbstractBackupConfig', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name_prefix** | **str** | The file name for the backup image. This name is added as a prefix in the name for the backup image. A unique file name for the backup image is created along with a timestamp. For example: prefix-1572431305418. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**location_type** | **str** | Specifies whether the backup will be stored locally or remotely. | [optional]  if omitted the server will use the default value of "Network Share"
**password** | **str** | Password of Backup server. | [optional] 
**path** | **str** | The file system path where the backup images must be stored. Include the IP address/hostname of the network share location and the complete file system path. For example: 172.29.109.234/var/backups/. | [optional] 
**protocol** | **str** | Protocol for transferring the backup image to the network share location. | [optional]  if omitted the server will use the default value of "SCP"
**retention_count** | **int** | Number of backup copies maintained on the local or remote server. When the created backup files exceed this number, the initial backup files are overwritten in a sequential manner. | [optional] 
**user_name** | **str** | Backup server user name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


