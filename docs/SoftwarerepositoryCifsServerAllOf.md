# SoftwarerepositoryCifsServerAllOf

Definition of the list of properties defined in 'softwarerepository.CifsServer', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_location** | **str** | The location to the image file. The accepted format is IP-or-hostname/folder1/folder2/.../imageFile. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**mount_option** | **str** | For CIFS, leave the field blank or enter one or more comma seperated options from the following. For Example, \&quot; \&quot; , \&quot; soft \&quot; , \&quot; soft , nounix \&quot; . * soft. * nounix. * noserviceino. * guest. * USERNAME&#x3D;VALUE. * PASSWORD&#x3D;VALUE. * sec&#x3D;VALUE (VALUE could be None, Ntlm, Ntlmi, Ntlmssp, Ntlmsspi, Ntlmv2, Ntlmv2i). | [optional] 
**password** | **str** | Password configured on the CIFS server. | [optional] 
**remote_file** | **str** | Filename of the image in the CIFS server. For example:ucs-c220m5-huu-3.1.2c.iso. | [optional] [readonly] 
**remote_ip** | **str** | Hostname or IP Address of the CIFS server. | [optional] [readonly] 
**remote_share** | **str** | Remote directory where the image is present. For example:/share/subfolder. | [optional] [readonly] 
**username** | **str** | Username configured on the CIFS server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


