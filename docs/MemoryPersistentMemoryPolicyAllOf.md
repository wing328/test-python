# MemoryPersistentMemoryPolicyAllOf

Definition of the list of properties defined in 'memory.PersistentMemoryPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | [**[MemoryPersistentMemoryGoal]**](MemoryPersistentMemoryGoal.md) |  | [optional] 
**local_security** | [**MemoryPersistentMemoryLocalSecurity**](MemoryPersistentMemoryLocalSecurity.md) |  | [optional] 
**logical_namespaces** | [**[MemoryPersistentMemoryLogicalNamespace]**](MemoryPersistentMemoryLogicalNamespace.md) |  | [optional] 
**management_mode** | **str** | Management Mode of the policy. This can be either Configured from Intersight or Configured from Operating System. | [optional]  if omitted the server will use the default value of "configured-from-intersight"
**retain_namespaces** | **bool** | Persistent Memory Namespaces to be retained or not. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


