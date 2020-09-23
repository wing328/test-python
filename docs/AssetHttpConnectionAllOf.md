# AssetHttpConnectionAllOf

Definition of the list of properties defined in 'asset.HttpConnection', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**AssetCredential**](AssetCredential.md) |  | [optional] 
**is_secure** | **bool** | Indicates whether a connection to the target should be established using HTTPS. | [optional] 
**management_address** | **str** | The DNS hostname or IP Address, either IPv4 or IPv6, to be used to connect to the managed target. | [optional] 
**port** | **int** | The port number to be used to to connect to the managed target. Values 1-65535 indicate a port number to be used. A value of 0 is not a valid port number and instead indicates that the default management port, as defined by the documentation of the managed target, should be used to establish a connection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


