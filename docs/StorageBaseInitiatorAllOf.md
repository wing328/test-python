# StorageBaseInitiatorAllOf

Definition of the list of properties defined in 'storage.BaseInitiator', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iqn** | **str** | IQN (iSCSI qualified name). Can be up to 255 characters long and has the format iqn.yyyy-mm.naming-authority:unique name. | [optional] [readonly] 
**name** | **str** | Name of the initiator represented in the storage array. | [optional] [readonly] 
**type** | **str** | Initiator type, it can be FC or iSCSI. | [optional] [readonly]  if omitted the server will use the default value of "FC"
**wwn** | **str** | World wide name, 128 bit address represented in hexadecimal notation. For example, 51:4f:0c:50:14:1f:af:01:51:4f:0c:51:14:1f:af:01. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


