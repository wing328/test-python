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
    from openapi_client.model.macpool_lease_relationship import MacpoolLeaseRelationship
    from openapi_client.model.macpool_pool_relationship import MacpoolPoolRelationship
    from openapi_client.model.policy_abstract_config_profile_relationship import PolicyAbstractConfigProfileRelationship
    from openapi_client.model.vnic_cdn import VnicCdn
    from openapi_client.model.vnic_eth_adapter_policy_relationship import VnicEthAdapterPolicyRelationship
    from openapi_client.model.vnic_eth_if_relationship import VnicEthIfRelationship
    from openapi_client.model.vnic_eth_network_policy_relationship import VnicEthNetworkPolicyRelationship
    from openapi_client.model.vnic_eth_qos_policy_relationship import VnicEthQosPolicyRelationship
    from openapi_client.model.vnic_lan_connectivity_policy_relationship import VnicLanConnectivityPolicyRelationship
    from openapi_client.model.vnic_placement_settings import VnicPlacementSettings
    from openapi_client.model.vnic_usnic_settings import VnicUsnicSettings
    from openapi_client.model.vnic_vmq_settings import VnicVmqSettings
    globals()['MacpoolLeaseRelationship'] = MacpoolLeaseRelationship
    globals()['MacpoolPoolRelationship'] = MacpoolPoolRelationship
    globals()['PolicyAbstractConfigProfileRelationship'] = PolicyAbstractConfigProfileRelationship
    globals()['VnicCdn'] = VnicCdn
    globals()['VnicEthAdapterPolicyRelationship'] = VnicEthAdapterPolicyRelationship
    globals()['VnicEthIfRelationship'] = VnicEthIfRelationship
    globals()['VnicEthNetworkPolicyRelationship'] = VnicEthNetworkPolicyRelationship
    globals()['VnicEthQosPolicyRelationship'] = VnicEthQosPolicyRelationship
    globals()['VnicLanConnectivityPolicyRelationship'] = VnicLanConnectivityPolicyRelationship
    globals()['VnicPlacementSettings'] = VnicPlacementSettings
    globals()['VnicUsnicSettings'] = VnicUsnicSettings
    globals()['VnicVmqSettings'] = VnicVmqSettings


class VnicEthIfAllOf(ModelNormal):
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
        ('name',): {
            'max_length': 31,
            'regex': {
                'pattern': r'^[a-zA-Z0-9-._:]*$',  # noqa: E501
            },
        },
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
            'cdn': (VnicCdn,),  # noqa: E501
            'failover_enabled': (bool,),  # noqa: E501
            'mac_address': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'order': (int,),  # noqa: E501
            'placement': (VnicPlacementSettings,),  # noqa: E501
            'standby_vif_id': (int,),  # noqa: E501
            'usnic_settings': (VnicUsnicSettings,),  # noqa: E501
            'vif_id': (int,),  # noqa: E501
            'vmq_settings': (VnicVmqSettings,),  # noqa: E501
            'eth_adapter_policy': (VnicEthAdapterPolicyRelationship,),  # noqa: E501
            'eth_network_policy': (VnicEthNetworkPolicyRelationship,),  # noqa: E501
            'eth_qos_policy': (VnicEthQosPolicyRelationship,),  # noqa: E501
            'lan_connectivity_policy': (VnicLanConnectivityPolicyRelationship,),  # noqa: E501
            'lcp_vnic': (VnicEthIfRelationship,),  # noqa: E501
            'mac_lease': (MacpoolLeaseRelationship,),  # noqa: E501
            'mac_pool': (MacpoolPoolRelationship,),  # noqa: E501
            'profile': (PolicyAbstractConfigProfileRelationship,),  # noqa: E501
            'sp_vnics': ([VnicEthIfRelationship], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'cdn': 'Cdn',  # noqa: E501
        'failover_enabled': 'FailoverEnabled',  # noqa: E501
        'mac_address': 'MacAddress',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'order': 'Order',  # noqa: E501
        'placement': 'Placement',  # noqa: E501
        'standby_vif_id': 'StandbyVifId',  # noqa: E501
        'usnic_settings': 'UsnicSettings',  # noqa: E501
        'vif_id': 'VifId',  # noqa: E501
        'vmq_settings': 'VmqSettings',  # noqa: E501
        'eth_adapter_policy': 'EthAdapterPolicy',  # noqa: E501
        'eth_network_policy': 'EthNetworkPolicy',  # noqa: E501
        'eth_qos_policy': 'EthQosPolicy',  # noqa: E501
        'lan_connectivity_policy': 'LanConnectivityPolicy',  # noqa: E501
        'lcp_vnic': 'LcpVnic',  # noqa: E501
        'mac_lease': 'MacLease',  # noqa: E501
        'mac_pool': 'MacPool',  # noqa: E501
        'profile': 'Profile',  # noqa: E501
        'sp_vnics': 'SpVnics',  # noqa: E501
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
        """VnicEthIfAllOf - a model defined in OpenAPI

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
            cdn (VnicCdn): [optional]  # noqa: E501
            failover_enabled (bool): Setting this to true esnures that the traffic failsover from one uplink to another auotmatically in case of an uplink failure. It is applicable for Cisco VIC adapters only which are connected to Fabric Interconnect cluster. The uplink if specified determines the primary uplink in case of a failover.. [optional]  # noqa: E501
            mac_address (str): The MAC address that is assigned to the vnic based on the MAC pool that has been assigned to the LAN Connectivity Policy.. [optional]  # noqa: E501
            name (str): Name of the virtual ethernet interface.. [optional]  # noqa: E501
            order (int): The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two.. [optional]  # noqa: E501
            placement (VnicPlacementSettings): [optional]  # noqa: E501
            standby_vif_id (int): The Standby VIF Id is applicable for failover enabled vNICS. It should be the same as the channel number of the standby vethernet created on switch in order to set up the standby data path.. [optional]  # noqa: E501
            usnic_settings (VnicUsnicSettings): [optional]  # noqa: E501
            vif_id (int): The Vif Id should be same as the channel number of the vethernet created on switch in order to set up the data path. The property is applicable only for FI attached servers where a vethernet is created on the switch for every vNIC.. [optional]  # noqa: E501
            vmq_settings (VnicVmqSettings): [optional]  # noqa: E501
            eth_adapter_policy (VnicEthAdapterPolicyRelationship): [optional]  # noqa: E501
            eth_network_policy (VnicEthNetworkPolicyRelationship): [optional]  # noqa: E501
            eth_qos_policy (VnicEthQosPolicyRelationship): [optional]  # noqa: E501
            lan_connectivity_policy (VnicLanConnectivityPolicyRelationship): [optional]  # noqa: E501
            lcp_vnic (VnicEthIfRelationship): [optional]  # noqa: E501
            mac_lease (MacpoolLeaseRelationship): [optional]  # noqa: E501
            mac_pool (MacpoolPoolRelationship): [optional]  # noqa: E501
            profile (PolicyAbstractConfigProfileRelationship): [optional]  # noqa: E501
            sp_vnics ([VnicEthIfRelationship], none_type): An array of relationships to vnicEthIf resources.. [optional]  # noqa: E501
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
