# PciSwitchAllOf

Definition of the list of properties defined in 'pci.Switch', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | The device id of the switch. | [optional] [readonly] 
**health** | **str** | The composite health of the switch. | [optional] [readonly] 
**num_of_adaptors** | **str** | The number of GPUs and PCI adapters connected the switch. | [optional] [readonly] 
**pci_address** | **str** | The PCI address of the switch. | [optional] [readonly] 
**pci_slot** | **str** | The PCI slot name of the switch. | [optional] [readonly] 
**product_name** | **str** | The model information for the switch. | [optional] [readonly] 
**product_revision** | **str** | The product revision of the switch. | [optional] [readonly] 
**sub_device_id** | **str** | The sub device id of the switch. | [optional] [readonly] 
**sub_vendor_id** | **str** | The sub vendor id of the switch. | [optional] [readonly] 
**temperature** | **str** | The current temperature of the switch. | [optional] [readonly] 
**type** | **str** | The type information of the switch. | [optional] 
**vendor_id** | **str** | The vendor id of the switch. | [optional] [readonly] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**links** | [**[PciLinkRelationship], none_type**](PciLinkRelationship.md) | An array of relationships to pciLink resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**running_firmware** | [**[FirmwareRunningFirmwareRelationship], none_type**](FirmwareRunningFirmwareRelationship.md) | An array of relationships to firmwareRunningFirmware resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


