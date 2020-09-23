# ApplianceSetupInfo

SetupInfo will have only one managed object. SetupInfo managed object is to keep track of the Intersight Appliance's setup information and guide the UI through the initial configuration of the Intersight Appliance. The SetupInfo managed object is created during the Intersight Appliance setup. The Intersight UI uses this object to store the initial configuration states that the user has completed. If the user closes the Intersight UI without finishing all the initial configuration, then the Intersight UI will use this managed object to display the next configuration that the user needs to complete when the user uses the Intersight Appliance next time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**build_type** | **str** | Build type of the Intersight Appliance setup (e.g. release or debug). | [optional] [readonly] 
**capabilities** | [**[ApplianceKeyValuePair]**](ApplianceKeyValuePair.md) |  | [optional] 
**cloud_url** | **str** | URL of the Intersight to which this Intersight Appliance is connected to. | [optional] [readonly] 
**deployment_mode** | **str** | Indicates where Intersight Appliance is installed in air-gapped or connected mode. In connected mode, Intersight Appliance is claimed by Intesight SaaS. In air-gapped mode, Intersight Appliance does not connect to any Cisco services. | [optional] [readonly]  if omitted the server will use the default value of "Connected"
**end_time** | **datetime** | End date of the Intersight Appliance&#39;s initial setup. | [optional] [readonly] 
**setup_states** | **[str]** |  | [optional] 
**start_time** | **datetime** | Start date of the Intersight Appliance&#39;s initial setup. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**account_moid** | **str** | The Account ID for this managed object. | [optional] [readonly] 
**create_time** | **datetime** | The time when this managed object was created. | [optional] [readonly] 
**domain_group_moid** | **str** | The DomainGroup ID for this managed object. | [optional] [readonly] 
**mod_time** | **datetime** | The time when this managed object was last modified. | [optional] [readonly] 
**moid** | **str** | The unique identifier of this Managed Object instance. | [optional] 
**owners** | **[str]** |  | [optional] 
**shared_scope** | **str** | Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a &#39;shared&#39; ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs. | [optional] [readonly] 
**tags** | [**[MoTag]**](MoTag.md) |  | [optional] 
**version_context** | [**MoVersionContext**](MoVersionContext.md) |  | [optional] 
**ancestors** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**parent** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**permission_resources** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**display_names** | [**DisplayNames**](DisplayNames.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


