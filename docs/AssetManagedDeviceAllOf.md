# AssetManagedDeviceAllOf

Definition of the list of properties defined in 'asset.ManagedDevice', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**CommCredential**](CommCredential.md) |  | [optional] 
**device_type** | **str** | Type of the Device such as VMware, Pure Storage supported by Intersight Assist. | [optional]  if omitted the server will use the default value of ""
**ignore_cert** | **bool** | Ignore Certificates with protocol https for connecting to the Managed Device. It is not used for other protocols. | [optional] 
**is_enabled** | **bool** | Device is Enabled/Disabled. | [optional] 
**management_address** | **str** | Management address of the device. It can be IPv4, IPv6 or FQDN. | [optional] 
**port** | **int** | Port to use for connecting to the Managed Device. Port is optional. If not specified, default port for protocol is used. | [optional] 
**protocol** | **str** | Protocol to use for connecting to the Managed Device. | [optional]  if omitted the server will use the default value of "https"
**status** | [**AssetManagedDeviceStatus**](AssetManagedDeviceStatus.md) |  | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**device_connector_manager** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**workflow_info** | [**WorkflowWorkflowInfoRelationship**](WorkflowWorkflowInfoRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


