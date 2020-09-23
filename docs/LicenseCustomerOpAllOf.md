# LicenseCustomerOpAllOf

Definition of the list of properties defined in 'license.CustomerOp', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_admin** | **bool** | The license administrative state. Set this property to &#39;true&#39; to activate the license entitlements. | [optional] 
**deregister_device** | **bool** | Trigger de-registration/disable. | [optional] 
**enable_trial** | **bool** | Enable trial for Intersight licensing. | [optional] 
**evaluation_period** | **int** | The default Trial or Grace period customer is entitled to. | [optional] 
**extra_evaluation** | **int** | The number of days the trial Trial or Grace period is extended. The trial or grace period can be extended once. | [optional] 
**renew_authorization** | **bool** | Trigger renew authorization. | [optional] 
**renew_id_certificate** | **bool** | Trigger renew registration. | [optional] 
**show_agent_tech_support** | **bool** | Trigger show tech support feature. | [optional] 
**account_license_data** | [**LicenseAccountLicenseDataRelationship**](LicenseAccountLicenseDataRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


