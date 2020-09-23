# HyperflexLogicalAvailabilityZone

A configuration for the Logical Availability Zone. Logical Availability Zones (LAZ) allow for increased fault tolerance by dividing clusters into logical partitions where a given block of data is only written to a zone once. This allows replications of data to be distributed evenly across zones. LAZ configurations are compatible with HyperFlex clusters meeting all of the following criteria: 1. The HyperFlex cluster must be attached to a UCS Fabric Interconnect. 2. The HyperFlex cluster must be running HyperFlex Data Platform 3.0 or higher. 3. The HyperFlex cluster must have 8 or more converged nodes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**auto_config** | **bool** | Enable or disable Logical Availability Zones (LAZ). If enabled, HyperFlex Data Platform automatically selects and groups nodes into different availability zones. For HyperFlex Data Platform versions prior to 3.0 release, this setting does not apply. For HyperFlex Data Platform versions 3.0 or higher, this setting is only applicable to Fabric Interconnect attached HyperFlex systems with 8 or more converged nodes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


