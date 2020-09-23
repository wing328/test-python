# EquipmentChassisAllOf

Definition of the list of properties defined in 'equipment.Chassis', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **int** | The assigned identifier for a chassis. | [optional] [readonly] 
**connection_path** | **str** | This field identifies the connectivity path for the chassis enclosure. | [optional] [readonly] 
**connection_status** | **str** | This field identifies the connectivity status for the chassis enclosure. | [optional] [readonly] 
**description** | **str** | This field is to provide description for chassis model. | [optional] [readonly] 
**fault_summary** | **int** | This field summarizes the faults on the chassis enclosure. | [optional] 
**management_mode** | **str** | The management mode of the blade server chassis. | [optional] [readonly]  if omitted the server will use the default value of "IntersightStandalone"
**name** | **str** | This field identifies the name for the chassis enclosure. | [optional] [readonly] 
**oper_state** | **str** | This field identifies the Chassis Operational State. | [optional] [readonly] 
**part_number** | **str** | Part Number identifier for the chassis enclosure. | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for the chassis enclosure. | [optional] [readonly] 
**platform_type** | **str** | The platform type that the chassis is a part of. | [optional] 
**product_name** | **str** | This field identifies the Product Name for the chassis enclosure. | [optional] [readonly] 
**sku** | **str** | This field identifies the Stock Keeping Unit for the chassis enclosure. | [optional] [readonly] 
**vid** | **str** | This field identifies the Vendor ID for the chassis enclosure. | [optional] [readonly] 
**blades** | [**[ComputeBladeRelationship], none_type**](ComputeBladeRelationship.md) | An array of relationships to computeBlade resources. | [optional] [readonly] 
**fanmodules** | [**[EquipmentFanModuleRelationship], none_type**](EquipmentFanModuleRelationship.md) | An array of relationships to equipmentFanModule resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**ioms** | [**[EquipmentIoCardRelationship], none_type**](EquipmentIoCardRelationship.md) | An array of relationships to equipmentIoCard resources. | [optional] [readonly] 
**locator_led** | [**EquipmentLocatorLedRelationship**](EquipmentLocatorLedRelationship.md) |  | [optional] 
**psu_control** | [**EquipmentPsuControlRelationship**](EquipmentPsuControlRelationship.md) |  | [optional] 
**psus** | [**[EquipmentPsuRelationship], none_type**](EquipmentPsuRelationship.md) | An array of relationships to equipmentPsu resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**sasexpanders** | [**[StorageSasExpanderRelationship], none_type**](StorageSasExpanderRelationship.md) | An array of relationships to storageSasExpander resources. | [optional] [readonly] 
**siocs** | [**[EquipmentSystemIoControllerRelationship], none_type**](EquipmentSystemIoControllerRelationship.md) | An array of relationships to equipmentSystemIoController resources. | [optional] [readonly] 
**storage_enclosures** | [**[StorageEnclosureRelationship], none_type**](StorageEnclosureRelationship.md) | An array of relationships to storageEnclosure resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


