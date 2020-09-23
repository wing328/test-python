# SoftwarerepositoryNfsServer

An external file repository accessible through the NFS protocol.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**file_location** | **str** | The location to the image file. The accepted format is IP-or-hostname/folder1/folder2/.../imageFile. | [optional] 
**mount_options** | **str** | For NFS, leave the field blank or enter one or more comma seperated options from the following.For Example, \&quot; \&quot; , \&quot; ro \&quot; , \&quot; ro , rw \&quot; . * ro. * rw. * nolock. * noexec. * soft. * PORT&#x3D;VALUE. * timeo&#x3D;VALUE. * retry&#x3D;VALUE. | [optional] [readonly] 
**remote_file** | **str** | Filename of the image in the NFS server. For example:ucs-c220m5-huu-3.1.2c.iso. | [optional] [readonly] 
**remote_ip** | **str** | Hostname or IP Address of the NFS server. | [optional] [readonly] 
**remote_share** | **str** | Remote directory where the image is present. For example:/share/subfolder. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


