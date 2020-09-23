# GraphicsCardAllOf

Definition of the list of properties defined in 'graphics.Card', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **int** | The id of the graphics card. | [optional] [readonly] 
**device_id** | **int** | The device id of the graphics card. | [optional] [readonly] 
**expander_slot** | **str** | The expander slot information of the card. | [optional] [readonly] 
**firmware_version** | **str** | The firmware version of the graphics card. | [optional] [readonly] 
**mode** | **str** | The current mode of the graphics card. | [optional] [readonly] 
**num_gpus** | **str** | The number of controllers under each card. | [optional] 
**oper_state** | **str** | The current operational state of the graphics card. | [optional] [readonly] 
**pci_address** | **str** | The PCI address of the graphics card. | [optional] [readonly] 
**pci_address_list** | **str** | This list contains the PCI address of all controllers for corresponding card. | [optional] [readonly] 
**pci_slot** | **str** | The PCI slot name of the graphics card. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**graphics_controllers** | [**[GraphicsControllerRelationship], none_type**](GraphicsControllerRelationship.md) | An array of relationships to graphicsController resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**running_firmware** | [**[FirmwareRunningFirmwareRelationship], none_type**](FirmwareRunningFirmwareRelationship.md) | An array of relationships to firmwareRunningFirmware resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


