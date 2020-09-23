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
    from openapi_client.model.niatelemetry_diskinfo import NiatelemetryDiskinfo
    from openapi_client.model.niatelemetry_nia_license_state_relationship import NiatelemetryNiaLicenseStateRelationship
    globals()['AssetDeviceRegistrationRelationship'] = AssetDeviceRegistrationRelationship
    globals()['NiatelemetryDiskinfo'] = NiatelemetryDiskinfo
    globals()['NiatelemetryNiaLicenseStateRelationship'] = NiatelemetryNiaLicenseStateRelationship


class NiatelemetryNiaInventoryAllOf(ModelNormal):
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
            'cpu': (float,),  # noqa: E501
            'crash_reset_logs': (str,),  # noqa: E501
            'device_name': (str,),  # noqa: E501
            'device_type': (str,),  # noqa: E501
            'disk': (NiatelemetryDiskinfo,),  # noqa: E501
            'log_in_time': (str,),  # noqa: E501
            'log_out_time': (str,),  # noqa: E501
            'memory': (int,),  # noqa: E501
            'record_type': (str,),  # noqa: E501
            'record_version': (str,),  # noqa: E501
            'serial': (str,),  # noqa: E501
            'software_download': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'license_state': (NiatelemetryNiaLicenseStateRelationship,),  # noqa: E501
            'registered_device': (AssetDeviceRegistrationRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'cpu': 'Cpu',  # noqa: E501
        'crash_reset_logs': 'CrashResetLogs',  # noqa: E501
        'device_name': 'DeviceName',  # noqa: E501
        'device_type': 'DeviceType',  # noqa: E501
        'disk': 'Disk',  # noqa: E501
        'log_in_time': 'LogInTime',  # noqa: E501
        'log_out_time': 'LogOutTime',  # noqa: E501
        'memory': 'Memory',  # noqa: E501
        'record_type': 'RecordType',  # noqa: E501
        'record_version': 'RecordVersion',  # noqa: E501
        'serial': 'Serial',  # noqa: E501
        'software_download': 'SoftwareDownload',  # noqa: E501
        'version': 'Version',  # noqa: E501
        'license_state': 'LicenseState',  # noqa: E501
        'registered_device': 'RegisteredDevice',  # noqa: E501
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
        """NiatelemetryNiaInventoryAllOf - a model defined in OpenAPI

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
            cpu (float): CPU usage of device being inventoried. This determines the percentage of CPU resources used.. [optional]  # noqa: E501
            crash_reset_logs (str): Last crash reset reason of device being inventoried. This determines the last reason for a device&#39;s restart due to crash of the system.. [optional]  # noqa: E501
            device_name (str): Name of device being inventoried. The name the user assigns to the device is inventoried here.. [optional]  # noqa: E501
            device_type (str): Type of device being inventoried. This determines whether the device is a controller, leaf or spine.. [optional]  # noqa: E501
            disk (NiatelemetryDiskinfo): [optional]  # noqa: E501
            log_in_time (str): Last log in time device being inventoried. This determines the last login time on the device.. [optional]  # noqa: E501
            log_out_time (str): Last log out time of device being inventoried. This determines the last logout time on the device.. [optional]  # noqa: E501
            memory (int): Memory usage of device being inventoried. This determines the percentage of memory resources used.. [optional]  # noqa: E501
            record_type (str): Type of record DCNM / APIC / SE. This determines the type of platform where inventory was collected.. [optional]  # noqa: E501
            record_version (str): Version of record being pushed. This determines what was the API version for data available from the device.. [optional]  # noqa: E501
            serial (str): Serial number of device being invetoried. The serial number is unique per device and will be used as the key.. [optional]  # noqa: E501
            software_download (str): Last software downloaded of device being inventoried. This determines if software download API was used.. [optional]  # noqa: E501
            version (str): Software version of device being inventoried. The various software version values for each device are available on cisco.com.. [optional]  # noqa: E501
            license_state (NiatelemetryNiaLicenseStateRelationship): [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
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