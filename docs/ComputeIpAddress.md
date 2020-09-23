# ComputeIpAddress

Complex type representing an IP address in UCSM.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
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
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


