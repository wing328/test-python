# ComputeIpAddressAllOf

Definition of the list of properties defined in 'compute.IpAddress', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP Address to be used for KVM. | [optional] [readonly] 
**category** | **str** | Category of the Kvm IP Address. | [optional] [readonly]  if omitted the server will use the default value of "Equipment"
**default_gateway** | **str** | Default gateway property of KVM IP Address. | [optional] [readonly] 
**dn** | **str** | The distinguished name for this managed object. | [optional] [readonly] 
**http_port** | **int** | HTTP port of an IP Address. | [optional] [readonly] 
**https_port** | **int** | Secured HTTP port of an IP Address. | [optional] [readonly] 
**kvm_port** | **int** | Port number on which the KVM is running and used for connecting to KVM console. | [optional] [readonly] 
**kvm_vlan** | **int** | VLAN Identifier of Inband IP Address. | [optional] [readonly] 
**name** | **str** | Name to identify the KVM IP Address. | [optional] [readonly]  if omitted the server will use the default value of "Outband"
**subnet** | **str** | Subnet detail of a KVM IP Address. | [optional] [readonly] 
**type** | **str** | Type of the KVM IP Address. | [optional] [readonly]  if omitted the server will use the default value of "MgmtInterface"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


