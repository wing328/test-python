# VmediaMapping

Virtual Media mapping settings required to map images from remote server.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**authentication_protocol** | **str** | Type of Authentication protocol when CIFS is used for communication with the remote server. | [optional]  if omitted the server will use the default value of "none"
**device_type** | **str** | Type of remote Virtual Media device. | [optional]  if omitted the server will use the default value of "cdd"
**host_name** | **str** | IP address or hostname of the remote server. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**mount_options** | **str** | Mount options for the Virtual Media mapping. The field can be left blank or filled in a comma separated list with the following options.\\n For NFS, supported options are ro, rw, nolock, noexec, soft, port&#x3D;VALUE, timeo&#x3D;VALUE, retry&#x3D;VALUE.\\n For CIFS, supported options are soft, nounix, noserverino, guest.\\n For CIFS version &lt; 3.0, vers&#x3D;VALUE is mandatory. e.g. vers&#x3D;2.0\\n For HTTP/HTTPS, the only supported option is noauto. | [optional] 
**mount_protocol** | **str** | Protocol to use to communicate with the remote server. | [optional]  if omitted the server will use the default value of "nfs"
**password** | **str** | Password associated with the username. | [optional] 
**remote_file** | **str** | Name of the remote file. It should be of .img format for HDD Virtual Media mapping and .iso format for CDD Virtual Media mapping. | [optional] 
**remote_path** | **str** | URL path to the location of the image on the remote server. The preferred format is &#39;/path&#39;. | [optional] 
**username** | **str** | Username to log in to the remote server. | [optional] 
**volume_name** | **str** | Identity of the image for Virtual Media mapping. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


