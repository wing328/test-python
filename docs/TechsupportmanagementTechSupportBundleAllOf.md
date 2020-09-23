# TechsupportmanagementTechSupportBundleAllOf

Definition of the list of properties defined in 'techsupportmanagement.TechSupportBundle', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_identifier** | **str** | The device identifier used to uniquely identify an individual device. | [optional] [readonly] 
**device_type** | **str** | The device type obtained from the inventory. | [optional] [readonly] 
**pid** | **str** | Product identification of the device. | [optional] 
**platform_param** | [**ConnectorPlatformParamBase**](ConnectorPlatformParamBase.md) |  | [optional] 
**platform_type** | **str** | The platform type of the device. | [optional]  if omitted the server will use the default value of ""
**serial** | **str** | Serial number of the device. | [optional] 
**device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**target_resource** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**tech_support_status** | [**TechsupportmanagementTechSupportStatusRelationship**](TechsupportmanagementTechSupportStatusRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


