# ApplianceSetupInfoAllOf

Definition of the list of properties defined in 'appliance.SetupInfo', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_type** | **str** | Build type of the Intersight Appliance setup (e.g. release or debug). | [optional] [readonly] 
**capabilities** | [**[ApplianceKeyValuePair]**](ApplianceKeyValuePair.md) |  | [optional] 
**cloud_url** | **str** | URL of the Intersight to which this Intersight Appliance is connected to. | [optional] [readonly] 
**deployment_mode** | **str** | Indicates where Intersight Appliance is installed in air-gapped or connected mode. In connected mode, Intersight Appliance is claimed by Intesight SaaS. In air-gapped mode, Intersight Appliance does not connect to any Cisco services. | [optional] [readonly]  if omitted the server will use the default value of "Connected"
**end_time** | **datetime** | End date of the Intersight Appliance&#39;s initial setup. | [optional] [readonly] 
**setup_states** | **[str]** |  | [optional] 
**start_time** | **datetime** | Start date of the Intersight Appliance&#39;s initial setup. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


