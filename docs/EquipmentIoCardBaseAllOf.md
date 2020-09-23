# EquipmentIoCardBaseAllOf

Definition of the list of properties defined in 'equipment.IoCardBase', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** | Connectivity Status of FEX/IOM to Switch - A or B or AB. | [optional] 
**description** | **str** | This field is to provide description for the iocard module model. | [optional] [readonly] 
**module_id** | **int** | Module Identifier for the IO module. | [optional] [readonly] 
**oper_state** | **str** | Operational state of IO card or fabric extender. | [optional] [readonly] 
**part_number** | **str** | Part Number identifier for the IO module. | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for the IO module. | [optional] [readonly] 
**presence** | **str** | This field identifies the Presence state of the IO card module. | [optional] [readonly] 
**product_name** | **str** | This field identifies the Product Name for the iocard module model. | [optional] [readonly] 
**sku** | **str** | This field identifies the Stock Keeping Unit for the IO card module. | [optional] [readonly] 
**version** | **str** | This field identifies the version of the IO card module. | [optional] [readonly] 
**vid** | **str** | This field identifies the Vendor ID for the IO card module. | [optional] [readonly] 
**host_ports** | [**[EtherHostPortRelationship], none_type**](EtherHostPortRelationship.md) | An array of relationships to etherHostPort resources. | [optional] 
**mgmt_controller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**network_ports** | [**[EtherNetworkPortRelationship], none_type**](EtherNetworkPortRelationship.md) | An array of relationships to etherNetworkPort resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


