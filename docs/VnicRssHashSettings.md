# VnicRssHashSettings

The RSS Hash parameters help the traffic distribution across the Receive Queues based on the IP address (IPv4 or IPv6) and TCP Port numbers. These options help ensure that a single flow is directed to the same receive queue ensuring in-order delivery.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**ipv4_hash** | **bool** | When enabled, the IPv4 address is used for traffic distribution. | [optional] 
**ipv6_ext_hash** | **bool** | When enabled, the IPv6 extensions are used for traffic distribution. | [optional] 
**ipv6_hash** | **bool** | When enabled, the IPv6 address is used for traffic distribution. | [optional] 
**tcp_ipv4_hash** | **bool** | When enabled, both the IPv4 address and TCP port number are used for traffic distribution. | [optional] 
**tcp_ipv6_ext_hash** | **bool** | When enabled, both the IPv6 extensions and TCP port number are used for traffic distribution. | [optional] 
**tcp_ipv6_hash** | **bool** | When enabled, both the IPv6 address and TCP port number are used for traffic distribution. | [optional] 
**udp_ipv4_hash** | **bool** | When enabled, both the IPv4 address and UDP port number are used for traffic distribution. | [optional] 
**udp_ipv6_hash** | **bool** | When enabled, both the IPv6 address and UDP port number are used for traffic distribution. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


