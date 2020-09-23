# ConnectorpackUpgradeImpactAllOf

Definition of the list of properties defined in 'connectorpack.UpgradeImpact', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_pack** | [**[ConnectorpackConnectorPackUpdate]**](ConnectorpackConnectorPackUpdate.md) |  | [optional] 
**is_eligible_for_upgrade** | **bool** | States whether the UCS Director is eligible for an upgrade. Set to true if connector packs are available for upgrade, else set to false. | [optional] [readonly] 
**is_update_downloaded** | **bool** | States whether all the requisite updates have been downloaded to the target UCS Director. Set to true if all connector packs required to upgrade UCS Director to the next iteration have been downloaded, else set to false. | [optional] [readonly] 
**ucsd_info** | [**IaasUcsdInfoRelationship**](IaasUcsdInfoRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


