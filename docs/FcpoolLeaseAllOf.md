# FcpoolLeaseAllOf

Definition of the list of properties defined in 'fcpool.Lease', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_purpose** | **str** | Purpose of this WWN pool. | [optional] [readonly] 
**wwn_id** | **str** | WWN ID allocated for pool based allocation. | [optional] 
**assigned_to_entity** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**pool** | [**FcpoolPoolRelationship**](FcpoolPoolRelationship.md) |  | [optional] 
**pool_member** | [**FcpoolPoolMemberRelationship**](FcpoolPoolMemberRelationship.md) |  | [optional] 
**universe** | [**FcpoolUniverseRelationship**](FcpoolUniverseRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


