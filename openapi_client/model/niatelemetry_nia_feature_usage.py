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
    from openapi_client.model.display_names import DisplayNames
    from openapi_client.model.mo_base_mo import MoBaseMo
    from openapi_client.model.mo_base_mo_relationship import MoBaseMoRelationship
    from openapi_client.model.mo_tag import MoTag
    from openapi_client.model.mo_version_context import MoVersionContext
    from openapi_client.model.niatelemetry_nia_feature_usage_all_of import NiatelemetryNiaFeatureUsageAllOf
    globals()['AssetDeviceRegistrationRelationship'] = AssetDeviceRegistrationRelationship
    globals()['DisplayNames'] = DisplayNames
    globals()['MoBaseMo'] = MoBaseMo
    globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
    globals()['MoTag'] = MoTag
    globals()['MoVersionContext'] = MoVersionContext
    globals()['NiatelemetryNiaFeatureUsageAllOf'] = NiatelemetryNiaFeatureUsageAllOf


class NiatelemetryNiaFeatureUsage(ModelComposed):
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

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

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
            'class_id': (str,),  # noqa: E501
            'object_type': (str,),  # noqa: E501
            'apic_count': (int,),  # noqa: E501
            'app_center_count': (int,),  # noqa: E501
            'ave': (str,),  # noqa: E501
            'bd_count': (int,),  # noqa: E501
            'consistency_checker_app': (str,),  # noqa: E501
            'contract_count': (int,),  # noqa: E501
            'dns_count': (int,),  # noqa: E501
            'eigrp_count': (int,),  # noqa: E501
            'epg_count': (int,),  # noqa: E501
            'hsrp_count': (int,),  # noqa: E501
            'ibgp_count': (int,),  # noqa: E501
            'igmp_access_list_count': (int,),  # noqa: E501
            'igmp_snoop': (str,),  # noqa: E501
            'ip_epg_count': (int,),  # noqa: E501
            'isis_count': (int,),  # noqa: E501
            'l2_multicast': (str,),  # noqa: E501
            'leaf_count': (int,),  # noqa: E501
            'maintenance_mode_count': (int,),  # noqa: E501
            'management_over_v6_count': (int,),  # noqa: E501
            'nir': (str,),  # noqa: E501
            'opflex_kubernetes_count': (int,),  # noqa: E501
            'ospf_count': (int,),  # noqa: E501
            'poe_count': (int,),  # noqa: E501
            'qin_vni_tunnel_count': (int,),  # noqa: E501
            'remote_leaf_count': (int,),  # noqa: E501
            'scvmm_count': (int,),  # noqa: E501
            'shared_l3_out_count': (int,),  # noqa: E501
            'smart_call_home': (str,),  # noqa: E501
            'snmp': (str,),  # noqa: E501
            'spine_count': (int,),  # noqa: E501
            'ssh_over_v6_count': (int,),  # noqa: E501
            'syslog_over_v6_count': (int,),  # noqa: E501
            'tenant_count': (int,),  # noqa: E501
            'tier_two_leaf_count': (int,),  # noqa: E501
            'twamp': (str,),  # noqa: E501
            'useg': (str,),  # noqa: E501
            'vpod_count': (int,),  # noqa: E501
            'registered_device': (AssetDeviceRegistrationRelationship,),  # noqa: E501
            'account_moid': (str,),  # noqa: E501
            'create_time': (datetime,),  # noqa: E501
            'domain_group_moid': (str,),  # noqa: E501
            'mod_time': (datetime,),  # noqa: E501
            'moid': (str,),  # noqa: E501
            'owners': ([str],),  # noqa: E501
            'shared_scope': (str,),  # noqa: E501
            'tags': ([MoTag],),  # noqa: E501
            'version_context': (MoVersionContext,),  # noqa: E501
            'ancestors': ([MoBaseMoRelationship], none_type,),  # noqa: E501
            'parent': (MoBaseMoRelationship,),  # noqa: E501
            'permission_resources': ([MoBaseMoRelationship], none_type,),  # noqa: E501
            'display_names': (DisplayNames,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        val = {
        }
        if not val:
            return None
        return {'class_id': val}

    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'apic_count': 'ApicCount',  # noqa: E501
        'app_center_count': 'AppCenterCount',  # noqa: E501
        'ave': 'Ave',  # noqa: E501
        'bd_count': 'BdCount',  # noqa: E501
        'consistency_checker_app': 'ConsistencyCheckerApp',  # noqa: E501
        'contract_count': 'ContractCount',  # noqa: E501
        'dns_count': 'DnsCount',  # noqa: E501
        'eigrp_count': 'EigrpCount',  # noqa: E501
        'epg_count': 'EpgCount',  # noqa: E501
        'hsrp_count': 'HsrpCount',  # noqa: E501
        'ibgp_count': 'IbgpCount',  # noqa: E501
        'igmp_access_list_count': 'IgmpAccessListCount',  # noqa: E501
        'igmp_snoop': 'IgmpSnoop',  # noqa: E501
        'ip_epg_count': 'IpEpgCount',  # noqa: E501
        'isis_count': 'IsisCount',  # noqa: E501
        'l2_multicast': 'L2Multicast',  # noqa: E501
        'leaf_count': 'LeafCount',  # noqa: E501
        'maintenance_mode_count': 'MaintenanceModeCount',  # noqa: E501
        'management_over_v6_count': 'ManagementOverV6Count',  # noqa: E501
        'nir': 'Nir',  # noqa: E501
        'opflex_kubernetes_count': 'OpflexKubernetesCount',  # noqa: E501
        'ospf_count': 'OspfCount',  # noqa: E501
        'poe_count': 'PoeCount',  # noqa: E501
        'qin_vni_tunnel_count': 'QinVniTunnelCount',  # noqa: E501
        'remote_leaf_count': 'RemoteLeafCount',  # noqa: E501
        'scvmm_count': 'ScvmmCount',  # noqa: E501
        'shared_l3_out_count': 'SharedL3OutCount',  # noqa: E501
        'smart_call_home': 'SmartCallHome',  # noqa: E501
        'snmp': 'Snmp',  # noqa: E501
        'spine_count': 'SpineCount',  # noqa: E501
        'ssh_over_v6_count': 'SshOverV6Count',  # noqa: E501
        'syslog_over_v6_count': 'SyslogOverV6Count',  # noqa: E501
        'tenant_count': 'TenantCount',  # noqa: E501
        'tier_two_leaf_count': 'TierTwoLeafCount',  # noqa: E501
        'twamp': 'Twamp',  # noqa: E501
        'useg': 'Useg',  # noqa: E501
        'vpod_count': 'VpodCount',  # noqa: E501
        'registered_device': 'RegisteredDevice',  # noqa: E501
        'account_moid': 'AccountMoid',  # noqa: E501
        'create_time': 'CreateTime',  # noqa: E501
        'domain_group_moid': 'DomainGroupMoid',  # noqa: E501
        'mod_time': 'ModTime',  # noqa: E501
        'moid': 'Moid',  # noqa: E501
        'owners': 'Owners',  # noqa: E501
        'shared_scope': 'SharedScope',  # noqa: E501
        'tags': 'Tags',  # noqa: E501
        'version_context': 'VersionContext',  # noqa: E501
        'ancestors': 'Ancestors',  # noqa: E501
        'parent': 'Parent',  # noqa: E501
        'permission_resources': 'PermissionResources',  # noqa: E501
        'display_names': 'DisplayNames',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, class_id, object_type, *args, **kwargs):  # noqa: E501
        """NiatelemetryNiaFeatureUsage - a model defined in OpenAPI

        Args:
            class_id (str): The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value.
            object_type (str): The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

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
            apic_count (int): Number of APIC controllers. This determines the value of controllers for the fabric.. [optional]  # noqa: E501
            app_center_count (int): ACI APPs feature usage. This determines the total number of apps installed on the fabric.. [optional]  # noqa: E501
            ave (str): AVE feature usage. This determines if ACI virtual edge feature is enabled or disabled.. [optional]  # noqa: E501
            bd_count (int): Number of BDs. This determines the total number of Broadcast Domains across the fabric.. [optional]  # noqa: E501
            consistency_checker_app (str): Consistency checker application usage. This determines if the fabric has Consistency checker application installed.. [optional]  # noqa: E501
            contract_count (int): Number of contracts. This determines the total number of Contracts configured across the fabric.. [optional]  # noqa: E501
            dns_count (int): DNS feature usage. This determines the total number of DNS configurations across the fabric.. [optional]  # noqa: E501
            eigrp_count (int): Eigrp feature usage. This determines the total number of EIGRP sessions across the fabric.. [optional]  # noqa: E501
            epg_count (int): Number of EPGs. This determines the total number of End Point Groups across the fabric.. [optional]  # noqa: E501
            hsrp_count (int): Hsrp feature usage. This determines the total number of HSRP sessions across the fabric.. [optional]  # noqa: E501
            ibgp_count (int): Ibgp feature usage. This determines the total number of BGP sessions across the fabric.. [optional]  # noqa: E501
            igmp_access_list_count (int): IGMP Access List feature usage. This determines the total number of IGMP access lists configured across the fabric.. [optional]  # noqa: E501
            igmp_snoop (str): IGMP Snooping feature usage. This determines if this feature is enabled or disabled.. [optional]  # noqa: E501
            ip_epg_count (int): Number of IP based EPGs. This determines the total number of IP End Point Groups across the fabric.. [optional]  # noqa: E501
            isis_count (int): Isis feature usage. TThis determines the total number of ISIS sessions across the fabric.. [optional]  # noqa: E501
            l2_multicast (str): L2Multicast feature usage. This determines if this Layer 2 Multicast feature is being enabled / disabled on the fabric.. [optional]  # noqa: E501
            leaf_count (int): Number of Leafs. This determines the total number of Leaf switches in the fabric.. [optional]  # noqa: E501
            maintenance_mode_count (int): Maintenance Mode feature usage. This determines the number of switches that are currently in maintenance mode.. [optional]  # noqa: E501
            management_over_v6_count (int): Management over IPv6 feature usage. This determines the total number of IPv6 configurtaions in the fabric.. [optional]  # noqa: E501
            nir (str): NIR application usage. This determines if the fabric has NIR application installed.. [optional]  # noqa: E501
            opflex_kubernetes_count (int): Opflex for Kubernetes feature usage. This determines the total number of VMM sessions of type kubernetes.. [optional]  # noqa: E501
            ospf_count (int): Ospf feature usage. This determines the total number of OSPF sessions across the fabric.. [optional]  # noqa: E501
            poe_count (int): POE feature usage. This determines the total number of POE configurations across the fabric.. [optional]  # noqa: E501
            qin_vni_tunnel_count (int): QinVniTunnel feature usage. This determines if the qinVniTunnel feature is being used on the fabric and the scale of it.. [optional]  # noqa: E501
            remote_leaf_count (int): Number of remote Leafs. This determines if this feature is being enabled or disabled.. [optional]  # noqa: E501
            scvmm_count (int): SCVMM feature usage. This determines the total number of SCVMM configurations in the fabric.. [optional]  # noqa: E501
            shared_l3_out_count (int): SharedL3Out feature usage. This determines the total number of Shared L3 out configured across the fabric.. [optional]  # noqa: E501
            smart_call_home (str): Smart callhome feature usage. This determines if this feature is being enabled or disabled.. [optional]  # noqa: E501
            snmp (str): SNMP feature usage. This determines if this feature is enabled or disabled.. [optional]  # noqa: E501
            spine_count (int): Number of Spines. This determines the total number of spine switches in the fabric.. [optional]  # noqa: E501
            ssh_over_v6_count (int): Ssh over IPv6 feature usage. This determines the total number of IPv6 configurtaions in the fabric.. [optional]  # noqa: E501
            syslog_over_v6_count (int): Syslog over IPv6 feature usage. This determines the total number of IPv6 configurtaions in the fabric.. [optional]  # noqa: E501
            tenant_count (int): Number of tenants. This determines the total number of tenants configured across the fabric.. [optional]  # noqa: E501
            tier_two_leaf_count (int): Number of tier 2 Leafs. This determines the total number of tier 2 Leaf switches in the fabric.. [optional]  # noqa: E501
            twamp (str): TWAMP feature usage. This determines if this feature is enabled or disabled.. [optional]  # noqa: E501
            useg (str): VMM uSegmentation feature usage. This determines if microsegmentation feature is enabled or disabled.. [optional]  # noqa: E501
            vpod_count (int): Virtual pod feature usage. This determines the total number of virtual POD configurations in the fabrics.. [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
            account_moid (str): The Account ID for this managed object.. [optional]  # noqa: E501
            create_time (datetime): The time when this managed object was created.. [optional]  # noqa: E501
            domain_group_moid (str): The DomainGroup ID for this managed object.. [optional]  # noqa: E501
            mod_time (datetime): The time when this managed object was last modified.. [optional]  # noqa: E501
            moid (str): The unique identifier of this Managed Object instance.. [optional]  # noqa: E501
            owners ([str]): [optional]  # noqa: E501
            shared_scope (str): Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a &#39;shared&#39; ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.. [optional]  # noqa: E501
            tags ([MoTag]): [optional]  # noqa: E501
            version_context (MoVersionContext): [optional]  # noqa: E501
            ancestors ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            parent (MoBaseMoRelationship): [optional]  # noqa: E501
            permission_resources ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            display_names (DisplayNames): [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'class_id': class_id,
            'object_type': object_type,
        }
        # remove args whose value is Null because they are unset
        required_arg_names = list(required_args.keys())
        for required_arg_name in required_arg_names:
            if required_args[required_arg_name] is nulltype.Null:
                del required_args[required_arg_name]
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              MoBaseMo,
              NiatelemetryNiaFeatureUsageAllOf,
          ],
          'oneOf': [
          ],
        }
