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
    from openapi_client.model.display_names import DisplayNames
    from openapi_client.model.mo_base_mo_relationship import MoBaseMoRelationship
    from openapi_client.model.mo_mo_ref import MoMoRef
    from openapi_client.model.mo_tag import MoTag
    from openapi_client.model.mo_version_context import MoVersionContext
    from openapi_client.model.workflow_catalog_relationship import WorkflowCatalogRelationship
    from openapi_client.model.workflow_internal_properties import WorkflowInternalProperties
    from openapi_client.model.workflow_properties import WorkflowProperties
    from openapi_client.model.workflow_task_definition import WorkflowTaskDefinition
    globals()['DisplayNames'] = DisplayNames
    globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
    globals()['MoMoRef'] = MoMoRef
    globals()['MoTag'] = MoTag
    globals()['MoVersionContext'] = MoVersionContext
    globals()['WorkflowCatalogRelationship'] = WorkflowCatalogRelationship
    globals()['WorkflowInternalProperties'] = WorkflowInternalProperties
    globals()['WorkflowProperties'] = WorkflowProperties
    globals()['WorkflowTaskDefinition'] = WorkflowTaskDefinition


class WorkflowTaskDefinitionRelationship(ModelComposed):
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
        ('license_entitlement',): {
            'BASE': "Base",
            'ESSENTIAL': "Essential",
            'STANDARD': "Standard",
            'ADVANTAGE': "Advantage",
            'PREMIER': "Premier",
        },
    }

    validations = {
        ('label',): {
            'regex': {
                'pattern': r'^[a-zA-Z0-9]+[\sa-zA-Z0-9_\'.:-]{1,92}$',  # noqa: E501
            },
        },
        ('name',): {
            'regex': {
                'pattern': r'^[a-zA-Z0-9_.:-]{1,64}$',  # noqa: E501
            },
        },
        ('version',): {
            'inclusive_minimum': 1,
        },
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
            'default_version': (bool,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'internal_properties': (WorkflowInternalProperties,),  # noqa: E501
            'label': (str,),  # noqa: E501
            'license_entitlement': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'properties': (WorkflowProperties,),  # noqa: E501
            'secure_prop_access': (bool,),  # noqa: E501
            'version': (int,),  # noqa: E501
            'catalog': (WorkflowCatalogRelationship,),  # noqa: E501
            'implemented_tasks': ([WorkflowTaskDefinitionRelationship], none_type,),  # noqa: E501
            'interface_task': (WorkflowTaskDefinitionRelationship,),  # noqa: E501
            'selector': (str,),  # noqa: E501
            'link': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'mo.MoRef': MoMoRef,
            'workflow.TaskDefinition': WorkflowTaskDefinition,
        }
        if not val:
            return None
        return {'class_id': val}

    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
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
        'default_version': 'DefaultVersion',  # noqa: E501
        'description': 'Description',  # noqa: E501
        'internal_properties': 'InternalProperties',  # noqa: E501
        'label': 'Label',  # noqa: E501
        'license_entitlement': 'LicenseEntitlement',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'properties': 'Properties',  # noqa: E501
        'secure_prop_access': 'SecurePropAccess',  # noqa: E501
        'version': 'Version',  # noqa: E501
        'catalog': 'Catalog',  # noqa: E501
        'implemented_tasks': 'ImplementedTasks',  # noqa: E501
        'interface_task': 'InterfaceTask',  # noqa: E501
        'selector': 'Selector',  # noqa: E501
        'link': 'link',  # noqa: E501
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
    def __init__(self, class_id, *args, **kwargs):  # noqa: E501
        """WorkflowTaskDefinitionRelationship - a model defined in OpenAPI

        Args:
            class_id (str): The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value.

        Keyword Args:
            object_type (str): The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.. defaults to nulltype.Null  # noqa: E501
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
            default_version (bool): When true this will be the task version that is used when a specific task definition version is not specified. The very first task definition created with a name will be set as the default version, after that user can explicitly set any version of the task definition as the default version.. [optional]  # noqa: E501
            description (str): The task definition description to describe what this task will do when executed.. [optional]  # noqa: E501
            internal_properties (WorkflowInternalProperties): [optional]  # noqa: E501
            label (str): A user friendly short name to identify the task definition.. [optional]  # noqa: E501
            license_entitlement (str): License entitlement required to run this task. It is determined by license requirement of features.. [optional] if omitted the server will use the default value of "Base"  # noqa: E501
            name (str): The name of the task definition. The name should follow this convention &lt;Verb or Action&gt;&lt;Category&gt;&lt;Vendor&gt;&lt;Product&gt;&lt;Noun or object&gt; Verb or Action is a required portion of the name and this must be part of the pre-approved verb list. Category is an optional field and this will refer to the broad category of the task referring to the type of resource or endpoint. If there is no specific category then use \&quot;Generic\&quot; if required. Vendor is an optional field and this will refer to the specific vendor this task applies to. If the task is generic and not tied to a vendor, then do not specify anything. Product is an optional field, this will contain the vendor product and model when desired. Noun or object is a required field and  this will contain the noun or object on which the action is being performed. Examples SendEmail  - This is a task in Generic category for sending email. NewStorageVolume - This is a vendor agnostic task under Storage device category for creating a new volume.. [optional]  # noqa: E501
            properties (WorkflowProperties): [optional]  # noqa: E501
            secure_prop_access (bool): If set to true, the task requires access to secure properties and uses an encyption token associated with a workflow moid to encrypt or decrypt the secure properties.. [optional]  # noqa: E501
            version (int): The version of the task definition so we can support multiple versions of a task definition.. [optional]  # noqa: E501
            catalog (WorkflowCatalogRelationship): [optional]  # noqa: E501
            implemented_tasks ([WorkflowTaskDefinitionRelationship], none_type): An array of relationships to workflowTaskDefinition resources.. [optional]  # noqa: E501
            interface_task (WorkflowTaskDefinitionRelationship): [optional]  # noqa: E501
            selector (str): An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of &#39;moid&#39; by clients. 1. If &#39;moid&#39; is set this field is ignored. 1. If &#39;selector&#39; is set and &#39;moid&#39; is empty/absent from the request, Intersight determines the Moid of the resource matching the filter expression and populates it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq &#39;3AA8B7T11&#39;.. [optional]  # noqa: E501
            link (str): A URL to an instance of the &#39;mo.MoRef&#39; class.. [optional]  # noqa: E501
        """

        object_type = kwargs.get('object_type', nulltype.Null)
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
          ],
          'oneOf': [
              MoMoRef,
              WorkflowTaskDefinition,
              none_type,
          ],
        }
