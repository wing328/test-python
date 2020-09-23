# AssetConnectionControlMessage

Control message used to update the context of a devices connection. When a device registration is modified (e.g. by a user modifying the claim status) the process managing the connection must be notified of the change. On changes aurora will attempt to send the change to the current owner of the connection.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**account** | **str** | The account id to which the device belongs. | [optional] 
**connector_version** | **str** | The version of the device connector currently running on the platform. Deprecated by newer connectors that will report this directly to the device connector gateway in a websocket header, but included to continue to support older versions which report any version change after connect. | [optional] 
**device_id** | **str** | The Moid of the device under change. Used to route the message to a devices connection. | [optional] 
**domain_group** | **str** | The domain group id to which the device belongs. | [optional] 
**evict** | **bool** | Flag to force any open connections to be evicted. Used in case device has been deleted or blacklisted. | [optional] 
**leadership** | **str** | The current leadership of a device cluster member. | [optional]  if omitted the server will use the default value of "Unknown"
**new_identity** | **str** | The new identity assigned to a device on ownership change (claim/unclaim). | [optional] 
**partition** | **int** | The partition the device was last connected to, used to address the control message to the device connector gateway instance holding the devices connection. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


