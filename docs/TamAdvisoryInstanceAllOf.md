# TamAdvisoryInstanceAllOf

Definition of the list of properties defined in 'tam.AdvisoryInstance', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_object_moid** | **str** | Moid of the Intersight MO affected by the alert. Deprecated now and will be removed in subsequent releases. | [optional] 
**affected_object_type** | **str** | Object type of the Intersight MO affected by the alert. Deprecated now and will be removed in subsequent releases. | [optional] 
**last_state_change_time** | **datetime** | Timestamp when a state change was observed on this advisory instnace. | [optional] [readonly] 
**last_verified_time** | **datetime** | Timestamp when this advisory was last evaluated. | [optional] [readonly] 
**state** | **str** | Current state of the advisory instance (Active/Cleared/Unknown etc.). | [optional]  if omitted the server will use the default value of "unknown"
**advisory** | [**TamBaseAdvisoryRelationship**](TamBaseAdvisoryRelationship.md) |  | [optional] 
**affected_object** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


