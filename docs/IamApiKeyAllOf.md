# IamApiKeyAllOf

Definition of the list of properties defined in 'iam.ApiKey', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_algorithm** | **str** | The cryptographic hash algorithm to calculate the message digest. | [optional]  if omitted the server will use the default value of "SHA256"
**key_spec** | [**PkixKeyGenerationSpec**](PkixKeyGenerationSpec.md) |  | [optional] 
**private_key** | **str** | Holds the private key for the API key. | [optional] 
**purpose** | **str** | The purpose of the API Key. | [optional] 
**signing_algorithm** | **str** | The signing algorithm used by the client to authenticate API requests to Intersight. The signing algorithm must be compatible with the key generation specification. | [optional]  if omitted the server will use the default value of "RSASSA-PKCS1-v1_5"
**permission** | [**IamPermissionRelationship**](IamPermissionRelationship.md) |  | [optional] 
**user** | [**IamUserRelationship**](IamUserRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


