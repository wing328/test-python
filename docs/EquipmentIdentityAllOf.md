# EquipmentIdentityAllOf

Definition of the list of properties defined in 'equipment.Identity', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_action** | **str** | Updated by UI/API to trigger specific chassis action type. | [optional]  if omitted the server will use the default value of "None"
**admin_action_state** | **str** | The state of Maintenance Action performed. This will have three states. Applying - Action is in progress. Applied - Action is completed and applied. Failed - Action has failed. | [optional]  if omitted the server will use the default value of "None"
**identifier** | **int** | Numeric Identifier assigned by the management system to the equipment. | [optional] 
**lifecycle** | **str** | The equipment&#39;s lifecycle status. | [optional]  if omitted the server will use the default value of "None"
**model** | **str** | The vendor provided model name for the equipment. | [optional] 
**serial** | **str** | The serial number of the equipment. | [optional] 
**vendor** | **str** | The manufacturer of the equipment. | [optional] 
**device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


