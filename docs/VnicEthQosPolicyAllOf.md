# VnicEthQosPolicyAllOf

Definition of the list of properties defined in 'vnic.EthQosPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cos** | **int** | Class of Service to be associated to the traffic on the virtual interface. | [optional] 
**mtu** | **int** | The Maximum Transmission Unit (MTU) or packet size that the virtual interface accepts. | [optional] 
**rate_limit** | **int** | The value in Mbps (0-10G/40G/100G depending on Adapter Model) to use for limiting the data rate on the virtual interface. Setting this to zero will turn rate limiting off. | [optional] 
**trust_host_cos** | **bool** | Enables usage of the Class of Service provided by the operating system. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


