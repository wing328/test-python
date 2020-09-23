# EquipmentIdentitySummaryAllOf

Definition of the list of properties defined in 'equipment.IdentitySummary', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter_serial** | **str** | Serial Identifier of an adapter participating in SWM. | [optional] [readonly] 
**admin_action** | **str** | Updated by UI/API to trigger specific chassis action type. | [optional] [readonly]  if omitted the server will use the default value of "None"
**admin_action_state** | **str** | The state of Maintenance Action performed. This will have three states. Applying - Action is in progress. Applied - Action is completed and applied. Failed - Action has failed. | [optional] [readonly]  if omitted the server will use the default value of "None"
**chassis_id** | **int** | Chassis Identifier of a blade server. | [optional] [readonly] 
**device_mo_id** | **str** | FI Device registration Mo ID. | [optional] [readonly] 
**identifier** | **int** | Numeric Identifier assigned by the management system to the equipment. | [optional] [readonly] 
**io_card_identity_list** | [**[EquipmentIoCardIdentity]**](EquipmentIoCardIdentity.md) |  | [optional] 
**lifecycle** | **str** | The equipment&#39;s lifecycle status. | [optional] [readonly]  if omitted the server will use the default value of "None"
**model** | **str** | The vendor provided model name for the equipment. | [optional] [readonly] 
**pending_discovery** | **str** | Indicates pending discovery flag. | [optional] [readonly] 
**serial** | **str** | The serial number of the equipment. | [optional] [readonly] 
**slot_id** | **int** | Chassis slot number of a blade server. | [optional] [readonly] 
**source_object_type** | **str** | The source object type of this view MO. | [optional] [readonly] 
**switch_id** | **int** | Switch ID to which Fabric Extender is connected, ID can be either 1 or 2, equalent to A or B. | [optional] [readonly] 
**vendor** | **str** | The manufacturer of the equipment. | [optional] [readonly] 
**device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


