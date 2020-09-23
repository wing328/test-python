# AssetDeviceContractInformation

Contains information about the Cisco device identified by a unique identifier like serial number. It also contains information about warranty, contract status, validity of the device. In future this object could be expanded to store Case, RMA, device topology details. We observe new asset.DeviceRegisteration and use it as a trigger for creating an instance of this object. Currently the data is restricted to Cisco Standalone IMC servers and Fabric Interconnects. Support for more product lines will be added in future.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**contract** | [**AssetContractInformation**](AssetContractInformation.md) |  | [optional] 
**contract_status** | **str** | Calculated contract status that is derived based on the service line status and contract end date. It is different from serviceLineStatus property. serviceLineStatus gives us ACTIVE, OVERDUE, EXPIRED. These are transformed into Active, Expiring Soon and Not Covered. | [optional] [readonly]  if omitted the server will use the default value of "Not Covered"
**covered_product_line_end_date** | **str** | End date of the covered product line. The coverage end date is fetched from Cisco SN2INFO API. | [optional] [readonly] 
**device_id** | **str** | Unique identifier of the Cisco device. This information is used to query Cisco APIx SN2INFO and CCWR databases. | [optional] [readonly] 
**device_type** | **str** | Type used to classify the device in Cisco Intersight. Currently supported values are Server and FabricInterconnect. This will be expanded to support more types in future. | [optional] [readonly]  if omitted the server will use the default value of "None"
**end_customer** | [**AssetCustomerInformation**](AssetCustomerInformation.md) |  | [optional] 
**end_user_global_ultimate** | [**AssetGlobalUltimate**](AssetGlobalUltimate.md) |  | [optional] 
**is_valid** | **bool** | Validates if the device is a genuine Cisco device. Validated is done using the Cisco SN2INFO APIs. | [optional] [readonly] 
**item_type** | **str** | Item type of this specific Cisco device. example \&quot;Chassis\&quot;. | [optional] [readonly] 
**maintenance_purchase_order_number** | **str** | Maintenance purchase order number for the Cisco device. | [optional] [readonly] 
**maintenance_sales_order_number** | **str** | Maintenance sales order number for the Cisco device. | [optional] [readonly] 
**platform_type** | **str** | The platform type of the Cisco device. | [optional] [readonly]  if omitted the server will use the default value of ""
**product** | [**AssetProductInformation**](AssetProductInformation.md) |  | [optional] 
**purchase_order_number** | **str** | Purchase order number for the Cisco device. It is a unique number assigned for every purchase. | [optional] [readonly] 
**reseller_global_ultimate** | [**AssetGlobalUltimate**](AssetGlobalUltimate.md) |  | [optional] 
**sales_order_number** | **str** | Sales order number for the Cisco device. It is a unique number assigned for every sale. | [optional] [readonly] 
**service_description** | **str** | The type of service contract that covers the Cisco device. | [optional] [readonly] 
**service_end_date** | **datetime** | End date for the Cisco service contract that covers this Cisco device. | [optional] [readonly] 
**service_level** | **str** | The type of service contract that covers the Cisco device. | [optional] [readonly] 
**service_sku** | **str** | The SKU of the service contract that covers the Cisco device. | [optional] [readonly] 
**service_start_date** | **datetime** | Start date for the Cisco service contract that covers this Cisco device. | [optional] [readonly] 
**state_contract** | **str** | Internal property used for triggering and tracking actions for contract information. | [optional]  if omitted the server will use the default value of "Update"
**warranty_end_date** | **str** | End date for the warranty that covers the Cisco device. | [optional] [readonly] 
**warranty_type** | **str** | Type of warranty that covers the Cisco device. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
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


