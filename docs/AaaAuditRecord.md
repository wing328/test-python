# AaaAuditRecord

AuditRecord presents the configuration changes made by the user per transaction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**email** | **str** | The email of the associated user that made the change.  In case the user is later deleted, we still have some reference to the information. | [optional] 
**inst_id** | **str** | The instance id of AuditRecordLocal, which is used to identify if the comming AuditRecordLocal was already processed before. | [optional] 
**source_ip** | **str** | The source IP of the client. | [optional] 
**timestamp** | **datetime** | The creation time of AuditRecordLocal, which is the time when the affected MO was created/modified/deleted. | [optional] [readonly] 
**user_id_or_email** | **str** | The userId or the email of the associated user that made the change. In case that user is later deleted, we still have some reference to the information. | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**sessions** | [**IamSessionRelationship**](IamSessionRelationship.md) |  | [optional] 
**user** | [**IamUserRelationship**](IamUserRelationship.md) |  | [optional] 
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
**event** | **str** | The operation that was performed on this Managed Object. The event is a compound string that includes the CRUD operation such as Create, Modify, Delete, and a string representing the Managed Object type. | [optional] 
**mo_display_names** | **bool, date, datetime, dict, float, int, list, str, none_type** | The user-friendly names of the changed MO. | [optional] 
**mo_type** | **str** | The object type of the REST resource that was created, modified or deleted. | [optional] 
**object_moid** | **str** | The Moid of the REST resource that was created, modified or deleted. | [optional] 
**request** | **bool, date, datetime, dict, float, int, list, str, none_type** | The body of the REST request that was received from a client to create or modify a REST resource, represented as a JSON document. | [optional] 
**trace_id** | **str** | The trace id of the request that was used to create, modify or delete a REST resource. A trace id is a unique identifier for one particular REST request. It may be used for troubleshooting purpose by the Intersight technical support team. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

