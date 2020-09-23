# ManagementControllerAllOf

Definition of the list of properties defined in 'management.Controller', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Model of the endpoint that houses the management controller. | [optional] [readonly] 
**adapter_unit** | [**AdapterUnitRelationship**](AdapterUnitRelationship.md) |  | [optional] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**equipment_io_card_base** | [**EquipmentIoCardBaseRelationship**](EquipmentIoCardBaseRelationship.md) |  | [optional] 
**equipment_shared_io_module** | [**EquipmentSharedIoModuleRelationship**](EquipmentSharedIoModuleRelationship.md) |  | [optional] 
**equipment_system_io_controller** | [**EquipmentSystemIoControllerRelationship**](EquipmentSystemIoControllerRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**management_interfaces** | [**[ManagementInterfaceRelationship], none_type**](ManagementInterfaceRelationship.md) | An array of relationships to managementInterface resources. | [optional] [readonly] 
**network_element** | [**NetworkElementRelationship**](NetworkElementRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**running_firmware** | [**[FirmwareRunningFirmwareRelationship], none_type**](FirmwareRunningFirmwareRelationship.md) | An array of relationships to firmwareRunningFirmware resources. | [optional] [readonly] 
**storage_sas_expander** | [**StorageSasExpanderRelationship**](StorageSasExpanderRelationship.md) |  | [optional] 
**top_system** | [**TopSystemRelationship**](TopSystemRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


