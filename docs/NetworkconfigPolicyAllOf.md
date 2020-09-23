# NetworkconfigPolicyAllOf

Definition of the list of properties defined in 'networkconfig.Policy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_ipv4dns_server** | **str** | IP address of the secondary DNS server. | [optional] 
**alternate_ipv6dns_server** | **str** | IP address of the secondary DNS server. | [optional] 
**dynamic_dns_domain** | **str** | The domain name appended to a hostname for a Dynamic DNS (DDNS) update. If left blank, only a hostname is sent to the DDNS update request. | [optional] 
**enable_dynamic_dns** | **bool** | If enabled, updates the resource records to the DNS from Cisco IMC. | [optional] 
**enable_ipv4dns_from_dhcp** | **bool** | If enabled, Cisco IMC retrieves the DNS server addresses from DHCP. Use DHCP field must be enabled for IPv4 in Cisco IMC to enable it. | [optional] 
**enable_ipv6** | **bool** | If enabled, allows to configure IPv6 properties. | [optional] 
**enable_ipv6dns_from_dhcp** | **bool** | If enabled, Cisco IMC retrieves the DNS server addresses from DHCP. Use DHCP field must be enabled for IPv6 in Cisco IMC to enable it. | [optional] 
**preferred_ipv4dns_server** | **str** | IP address of the primary DNS server. | [optional] 
**preferred_ipv6dns_server** | **str** | IP address of the primary DNS server. | [optional] 
**appliance_account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


