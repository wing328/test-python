# AssetDeviceRegistrationAllOf

Definition of the list of properties defined in 'asset.DeviceRegistration', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | An identifier for the credential used by the device connector to authenticate with the Intersight web socket gateway. | [optional] 
**claimed_by_user_name** | **str** | The name of the user who claimed the device for the account. | [optional] [readonly] 
**claimed_time** | **datetime** | The date and time at which the device was claimed to this account. | [optional] [readonly] 
**device_hostname** | **[str]** |  | [optional] 
**device_ip_address** | **[str]** |  | [optional] 
**execution_mode** | **str** | Indicates if the platform is an actual device or an emulated device for testing, demos, etc. Permitted values are [Normal, Emulator, ContainerEmulator]. | [optional]  if omitted the server will use the default value of ""
**parent_signature** | [**AssetParentConnectionSignature**](AssetParentConnectionSignature.md) |  | [optional] 
**pid** | **[str]** |  | [optional] 
**platform_type** | **str** | The platform type on which device connector is executing. | [optional]  if omitted the server will use the default value of ""
**public_access_key** | **str** | The device connector&#39;s public key used by Intersight to authenticate a connection from the device connector. The public key is used to verify that the signature a device connector sends on connect has been signed by the connector&#39;s private key stored on the device&#39;s filesystem. Must be a PEM encoded RSA public key string. | [optional] [readonly] 
**read_only** | **bool** | Flag reported by devices to indicate an administrator of the device has disabled management operations of the device connector and only monitoring is permitted. | [optional] [readonly] 
**serial** | **[str]** |  | [optional] 
**vendor** | **str** | The vendor of the managed device. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**claimed_by_user** | [**IamUserRelationship**](IamUserRelationship.md) |  | [optional] 
**cluster_members** | [**[AssetClusterMemberRelationship], none_type**](AssetClusterMemberRelationship.md) | An array of relationships to assetClusterMember resources. | [optional] [readonly] 
**device_claim** | [**AssetDeviceClaimRelationship**](AssetDeviceClaimRelationship.md) |  | [optional] 
**device_configuration** | [**AssetDeviceConfigurationRelationship**](AssetDeviceConfigurationRelationship.md) |  | [optional] 
**domain_group** | [**IamDomainGroupRelationship**](IamDomainGroupRelationship.md) |  | [optional] 
**parent_connection** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


