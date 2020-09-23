# coding: utf-8

"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations. The Intersight OpenAPI document defines the complete set of properties that are returned in the HTTP response. From that perspective, a client can expect that no additional properties are returned, unless these properties are explicitly defined in the OpenAPI document. However, when a client uses an older version of the Intersight OpenAPI document, the server may send additional properties because the software is more recent than the client. In that case, the client may receive properties that it does not know about. Some generated SDKs perform a strict validation of the HTTP response body against the OpenAPI document. This document was created on 2020-06-30T07:31:54Z.  # noqa: E501

    The version of the OpenAPI document: 1.0.9-1950
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.asset_device_registration_relationship import AssetDeviceRegistrationRelationship
    from openapi_client.model.compute_blade_relationship import ComputeBladeRelationship
    from openapi_client.model.compute_board_relationship import ComputeBoardRelationship
    from openapi_client.model.compute_rack_unit_relationship import ComputeRackUnitRelationship
    from openapi_client.model.firmware_running_firmware_relationship import FirmwareRunningFirmwareRelationship
    from openapi_client.model.inventory_device_info_relationship import InventoryDeviceInfoRelationship
    from openapi_client.model.storage_disk_group_relationship import StorageDiskGroupRelationship
    from openapi_client.model.storage_physical_disk_extension_relationship import StoragePhysicalDiskExtensionRelationship
    from openapi_client.model.storage_physical_disk_relationship import StoragePhysicalDiskRelationship
    from openapi_client.model.storage_virtual_drive_extension_relationship import StorageVirtualDriveExtensionRelationship
    from openapi_client.model.storage_virtual_drive_relationship import StorageVirtualDriveRelationship
    globals()['AssetDeviceRegistrationRelationship'] = AssetDeviceRegistrationRelationship
    globals()['ComputeBladeRelationship'] = ComputeBladeRelationship
    globals()['ComputeBoardRelationship'] = ComputeBoardRelationship
    globals()['ComputeRackUnitRelationship'] = ComputeRackUnitRelationship
    globals()['FirmwareRunningFirmwareRelationship'] = FirmwareRunningFirmwareRelationship
    globals()['InventoryDeviceInfoRelationship'] = InventoryDeviceInfoRelationship
    globals()['StorageDiskGroupRelationship'] = StorageDiskGroupRelationship
    globals()['StoragePhysicalDiskExtensionRelationship'] = StoragePhysicalDiskExtensionRelationship
    globals()['StoragePhysicalDiskRelationship'] = StoragePhysicalDiskRelationship
    globals()['StorageVirtualDriveExtensionRelationship'] = StorageVirtualDriveExtensionRelationship
    globals()['StorageVirtualDriveRelationship'] = StorageVirtualDriveRelationship


class StorageControllerAllOf(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'controller_flags': (str,),  # noqa: E501
            'controller_id': (str,),  # noqa: E501
            'controller_status': (str,),  # noqa: E501
            'foreign_config_present': (bool,),  # noqa: E501
            'hw_revision': (str,),  # noqa: E501
            'interface_type': (str,),  # noqa: E501
            'max_volumes_supported': (int,),  # noqa: E501
            'oob_interface_supported': (str,),  # noqa: E501
            'oper_state': (str,),  # noqa: E501
            'operability': (str,),  # noqa: E501
            'pci_addr': (str,),  # noqa: E501
            'pci_slot': (str,),  # noqa: E501
            'presence': (str,),  # noqa: E501
            'raid_support': (str,),  # noqa: E501
            'rebuild_rate': (str,),  # noqa: E501
            'self_encrypt_enabled': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'compute_blade': (ComputeBladeRelationship,),  # noqa: E501
            'compute_board': (ComputeBoardRelationship,),  # noqa: E501
            'compute_rack_unit': (ComputeRackUnitRelationship,),  # noqa: E501
            'disk_group': ([StorageDiskGroupRelationship], none_type,),  # noqa: E501
            'inventory_device_info': (InventoryDeviceInfoRelationship,),  # noqa: E501
            'physical_disk_extensions': ([StoragePhysicalDiskExtensionRelationship], none_type,),  # noqa: E501
            'physical_disks': ([StoragePhysicalDiskRelationship], none_type,),  # noqa: E501
            'registered_device': (AssetDeviceRegistrationRelationship,),  # noqa: E501
            'running_firmware': ([FirmwareRunningFirmwareRelationship], none_type,),  # noqa: E501
            'virtual_drive_extensions': ([StorageVirtualDriveExtensionRelationship], none_type,),  # noqa: E501
            'virtual_drives': ([StorageVirtualDriveRelationship], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'controller_flags': 'ControllerFlags',  # noqa: E501
        'controller_id': 'ControllerId',  # noqa: E501
        'controller_status': 'ControllerStatus',  # noqa: E501
        'foreign_config_present': 'ForeignConfigPresent',  # noqa: E501
        'hw_revision': 'HwRevision',  # noqa: E501
        'interface_type': 'InterfaceType',  # noqa: E501
        'max_volumes_supported': 'MaxVolumesSupported',  # noqa: E501
        'oob_interface_supported': 'OobInterfaceSupported',  # noqa: E501
        'oper_state': 'OperState',  # noqa: E501
        'operability': 'Operability',  # noqa: E501
        'pci_addr': 'PciAddr',  # noqa: E501
        'pci_slot': 'PciSlot',  # noqa: E501
        'presence': 'Presence',  # noqa: E501
        'raid_support': 'RaidSupport',  # noqa: E501
        'rebuild_rate': 'RebuildRate',  # noqa: E501
        'self_encrypt_enabled': 'SelfEncryptEnabled',  # noqa: E501
        'type': 'Type',  # noqa: E501
        'compute_blade': 'ComputeBlade',  # noqa: E501
        'compute_board': 'ComputeBoard',  # noqa: E501
        'compute_rack_unit': 'ComputeRackUnit',  # noqa: E501
        'disk_group': 'DiskGroup',  # noqa: E501
        'inventory_device_info': 'InventoryDeviceInfo',  # noqa: E501
        'physical_disk_extensions': 'PhysicalDiskExtensions',  # noqa: E501
        'physical_disks': 'PhysicalDisks',  # noqa: E501
        'registered_device': 'RegisteredDevice',  # noqa: E501
        'running_firmware': 'RunningFirmware',  # noqa: E501
        'virtual_drive_extensions': 'VirtualDriveExtensions',  # noqa: E501
        'virtual_drives': 'VirtualDrives',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """StorageControllerAllOf - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            controller_flags (str): The flags for the storage controller.. [optional]  # noqa: E501
            controller_id (str): The Id of the storage controller.. [optional]  # noqa: E501
            controller_status (str): The current status of controller.. [optional]  # noqa: E501
            foreign_config_present (bool): Storage controller has detected disks in foreign config.. [optional]  # noqa: E501
            hw_revision (str): The hardware revision of controller.. [optional]  # noqa: E501
            interface_type (str): Interface types are Sas, Sata, PCH.. [optional]  # noqa: E501
            max_volumes_supported (int): Maximum virtual drives that can be created on this Storage Controller.. [optional]  # noqa: E501
            oob_interface_supported (str): The CIMC support for out-of-band configuration of controller.. [optional]  # noqa: E501
            oper_state (str): The current operational state of controller.. [optional]  # noqa: E501
            operability (str): Operability state of the storage controller.. [optional]  # noqa: E501
            pci_addr (str): The current pci address of controller.. [optional]  # noqa: E501
            pci_slot (str): The pci slot name for the controller.. [optional]  # noqa: E501
            presence (str): Physical Presence State for the Storage Controller.. [optional]  # noqa: E501
            raid_support (str): The RAID levels supported by controller.. [optional]  # noqa: E501
            rebuild_rate (str): Logical volume or RAID rebuild rate of Storage Controller.. [optional]  # noqa: E501
            self_encrypt_enabled (str): Storage controller disk self encryption state.. [optional]  # noqa: E501
            type (str): Controller types are Raid, FlexFlash.. [optional]  # noqa: E501
            compute_blade (ComputeBladeRelationship): [optional]  # noqa: E501
            compute_board (ComputeBoardRelationship): [optional]  # noqa: E501
            compute_rack_unit (ComputeRackUnitRelationship): [optional]  # noqa: E501
            disk_group ([StorageDiskGroupRelationship], none_type): An array of relationships to storageDiskGroup resources.. [optional]  # noqa: E501
            inventory_device_info (InventoryDeviceInfoRelationship): [optional]  # noqa: E501
            physical_disk_extensions ([StoragePhysicalDiskExtensionRelationship], none_type): An array of relationships to storagePhysicalDiskExtension resources.. [optional]  # noqa: E501
            physical_disks ([StoragePhysicalDiskRelationship], none_type): An array of relationships to storagePhysicalDisk resources.. [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
            running_firmware ([FirmwareRunningFirmwareRelationship], none_type): An array of relationships to firmwareRunningFirmware resources.. [optional]  # noqa: E501
            virtual_drive_extensions ([StorageVirtualDriveExtensionRelationship], none_type): An array of relationships to storageVirtualDriveExtension resources.. [optional]  # noqa: E501
            virtual_drives ([StorageVirtualDriveRelationship], none_type): An array of relationships to storageVirtualDrive resources.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
