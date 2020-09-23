# SoftwarerepositoryNfsServerAllOf

Definition of the list of properties defined in 'softwarerepository.NfsServer', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_location** | **str** | The location to the image file. The accepted format is IP-or-hostname/folder1/folder2/.../imageFile. | [optional] 
**mount_options** | **str** | For NFS, leave the field blank or enter one or more comma seperated options from the following.For Example, \&quot; \&quot; , \&quot; ro \&quot; , \&quot; ro , rw \&quot; . * ro. * rw. * nolock. * noexec. * soft. * PORT&#x3D;VALUE. * timeo&#x3D;VALUE. * retry&#x3D;VALUE. | [optional] [readonly] 
**remote_file** | **str** | Filename of the image in the NFS server. For example:ucs-c220m5-huu-3.1.2c.iso. | [optional] [readonly] 
**remote_ip** | **str** | Hostname or IP Address of the NFS server. | [optional] [readonly] 
**remote_share** | **str** | Remote directory where the image is present. For example:/share/subfolder. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


