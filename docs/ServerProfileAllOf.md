# ServerProfileAllOf

Definition of the list of properties defined in 'server.Profile', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_changes** | [**PolicyConfigChange**](PolicyConfigChange.md) |  | [optional] 
**is_pmc_deployed_secure_passphrase_set** | **bool** | Indicates whether the value of the &#39;pmcDeployedSecurePassphrase&#39; property has been set. | [optional] [readonly] 
**pmc_deployed_secure_passphrase** | **str** | Secure passphrase that is already deployed on all the Persistent Memory Modules on the server. This deployed passphrase is required during deploy of server profile if secure passphrase is changed or security is disabled in the attached persistent memory policy. | [optional] 
**target_platform** | **str** | The platform for which the server profile is applicable. It can either be a server that is operating in standalone mode or which is attached to a Fabric Interconnect managed by Intersight. | [optional]  if omitted the server will use the default value of "Standalone"
**assigned_server** | [**ComputePhysicalRelationship**](ComputePhysicalRelationship.md) |  | [optional] 
**associated_server** | [**ComputePhysicalRelationship**](ComputePhysicalRelationship.md) |  | [optional] 
**config_change_details** | [**[ServerConfigChangeDetailRelationship], none_type**](ServerConfigChangeDetailRelationship.md) | An array of relationships to serverConfigChangeDetail resources. | [optional] [readonly] 
**config_result** | [**ServerConfigResultRelationship**](ServerConfigResultRelationship.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**running_workflows** | [**[WorkflowWorkflowInfoRelationship], none_type**](WorkflowWorkflowInfoRelationship.md) | An array of relationships to workflowWorkflowInfo resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


