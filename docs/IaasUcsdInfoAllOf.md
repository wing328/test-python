# IaasUcsdInfoAllOf

Definition of the list of properties defined in 'iaas.UcsdInfo', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Moid of the UCS Director device connector&#39;s asset.DeviceRegistration. | [optional] [readonly] 
**guid** | **str** | Unique ID of UCS Director getting registerd with Intersight. | [optional] [readonly] 
**host_name** | **str** | The UCS Director hostname for management. | [optional] [readonly] 
**ip** | **str** | The UCS Director IP address for management. | [optional] [readonly] 
**last_backup** | **datetime** | Last successful backup created for this UCS Director appliance if backup is configured. | [optional] [readonly] 
**node_type** | **str** | NodeType specifies if UCS Director is deployed in Stand-alone or Multi Node. | [optional] [readonly] 
**product_name** | **str** | The UCS Director product name. | [optional] [readonly] 
**product_vendor** | **str** | The UCS Director product vendor. | [optional] [readonly] 
**product_version** | **str** | The UCS Director product/platform version. | [optional] [readonly] 
**status** | **str** | The UCS Director status. Possible values are Active, Inactive, Unknown. | [optional] [readonly] 
**connector_pack** | [**[IaasConnectorPackRelationship], none_type**](IaasConnectorPackRelationship.md) | An array of relationships to iaasConnectorPack resources. | [optional] [readonly] 
**device_status** | [**[IaasDeviceStatusRelationship], none_type**](IaasDeviceStatusRelationship.md) | An array of relationships to iaasDeviceStatus resources. | [optional] [readonly] 
**license_info** | [**IaasLicenseInfoRelationship**](IaasLicenseInfoRelationship.md) |  | [optional] 
**most_run_tasks** | [**[IaasMostRunTasksRelationship], none_type**](IaasMostRunTasksRelationship.md) | An array of relationships to iaasMostRunTasks resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**ucsd_managed_infra** | [**IaasUcsdManagedInfraRelationship**](IaasUcsdManagedInfraRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


