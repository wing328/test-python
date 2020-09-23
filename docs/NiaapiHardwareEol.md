# NiaapiHardwareEol

This contains the end of life notice of hardware.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**affected_pids** | **str** | String contains the PID of hardwares affected by this notice, seperated by comma. | [optional] 
**announcement_date** | **datetime** | When this notice is announced. | [optional] 
**announcement_date_epoch** | **int** | Epoch time of Announcement Date. | [optional] 
**bulletin_no** | **str** | The bulletinno of this hardware end of life notice. | [optional] 
**description** | **str** | The description of this hardware end of life notice. | [optional] 
**endof_new_service_attachment_date** | **datetime** | Date time of end of new services attachment  . | [optional] 
**endof_new_service_attachment_date_epoch** | **int** | Epoch time of New service attachment Date . | [optional] 
**endof_routine_failure_analysis_date** | **datetime** | Date time of end of routinefailure analysis. | [optional] 
**endof_routine_failure_analysis_date_epoch** | **int** | Epoch time of End of Routine Failure Analysis Date. | [optional] 
**endof_sale_date** | **datetime** | When this hardware will end sale. | [optional] 
**endof_sale_date_epoch** | **int** | Epoch time of End of Sale Date. | [optional] 
**endof_security_support** | **datetime** | Date time of end of security support . | [optional] 
**endof_security_support_epoch** | **int** | Epoch time of End of Security Support Date . | [optional] 
**endof_service_contract_renewal_date** | **datetime** | Date time of end of service contract renew . | [optional] 
**endof_service_contract_renewal_date_epoch** | **int** | Epoch time of End of Renewal service contract. | [optional] 
**endof_sw_maintenance_date** | **datetime** | The date of end of maintainance. | [optional] 
**endof_sw_maintenance_date_epoch** | **int** | Epoch time of End of maintenance Date. | [optional] 
**hardware_eol_url** | **str** | Hardware end of sale URL link to the notice webpage. | [optional] 
**headline** | **str** | The title of this hardware end of life notice. | [optional] 
**last_dateof_support** | **datetime** | Date time of end of support . | [optional] 
**last_dateof_support_epoch** | **int** | Epoch time of last date of support . | [optional] 
**last_ship_date** | **datetime** | Date time of Lastship Date. | [optional] 
**last_ship_date_epoch** | **int** | Epoch time of last ship Date. | [optional] 
**migration_url** | **str** | The URL of this migration notice. | [optional] 
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


