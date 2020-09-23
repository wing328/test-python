# VnicPlacementSettingsAllOf

Definition of the list of properties defined in 'vnic.PlacementSettings', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | PCIe Slot where the VIC adapter is installed. Supported values are (1-15) and MLOM. | [optional] 
**pci_link** | **int** | The PCI Link used as transport for the virtual interface. All VIC adapters have a single PCI link except VIC 1385 which has two. | [optional] 
**switch_id** | **str** | The fabric port to which the vnics will be associated. | [optional]  if omitted the server will use the default value of "None"
**uplink** | **int** | Adapter port on which the virtual interface will be created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


