# FirmwareNfsServerAllOf

Definition of the list of properties defined in 'firmware.NfsServer', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_location** | **str** | The location to the image file. The accepted format is IP-or-hostname/folder1/folder2/.../imageFile. | [optional] 
**mount_options** | **str** | Mount option as configured on the NFS Server. For example:nolock. | [optional] 
**remote_file** | **str** | Filename of the image in the remote share location. For example:ucs-c220m5-huu-3.1.2c.iso. | [optional] [readonly] 
**remote_ip** | **str** | NFS Server Hostname or IP Address. For example:NFS-server-hostname or 10.10.8.7. The remote share server should have network connectivity with the CIMC of the selected devices for a successful upgrade. | [optional] [readonly] 
**remote_share** | **str** | Directory where the image is stored. For example:/share/subfolder. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


