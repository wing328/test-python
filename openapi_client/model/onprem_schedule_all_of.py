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


class OnpremScheduleAllOf(ModelNormal):
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
        ('time_zone',): {
            'PACIFIC/NIUE': "Pacific/Niue",
            'PACIFIC/PAGO_PAGO': "Pacific/Pago_Pago",
            'PACIFIC/HONOLULU': "Pacific/Honolulu",
            'PACIFIC/RAROTONGA': "Pacific/Rarotonga",
            'PACIFIC/TAHITI': "Pacific/Tahiti",
            'PACIFIC/MARQUESAS': "Pacific/Marquesas",
            'AMERICA/ANCHORAGE': "America/Anchorage",
            'PACIFIC/GAMBIER': "Pacific/Gambier",
            'AMERICA/LOS_ANGELES': "America/Los_Angeles",
            'AMERICA/TIJUANA': "America/Tijuana",
            'AMERICA/VANCOUVER': "America/Vancouver",
            'AMERICA/WHITEHORSE': "America/Whitehorse",
            'PACIFIC/PITCAIRN': "Pacific/Pitcairn",
            'AMERICA/DAWSON_CREEK': "America/Dawson_Creek",
            'AMERICA/DENVER': "America/Denver",
            'AMERICA/EDMONTON': "America/Edmonton",
            'AMERICA/HERMOSILLO': "America/Hermosillo",
            'AMERICA/MAZATLAN': "America/Mazatlan",
            'AMERICA/PHOENIX': "America/Phoenix",
            'AMERICA/YELLOWKNIFE': "America/Yellowknife",
            'AMERICA/BELIZE': "America/Belize",
            'AMERICA/CHICAGO': "America/Chicago",
            'AMERICA/COSTA_RICA': "America/Costa_Rica",
            'AMERICA/EL_SALVADOR': "America/El_Salvador",
            'AMERICA/GUATEMALA': "America/Guatemala",
            'AMERICA/MANAGUA': "America/Managua",
            'AMERICA/MEXICO_CITY': "America/Mexico_City",
            'AMERICA/REGINA': "America/Regina",
            'AMERICA/TEGUCIGALPA': "America/Tegucigalpa",
            'AMERICA/WINNIPEG': "America/Winnipeg",
            'PACIFIC/GALAPAGOS': "Pacific/Galapagos",
            'AMERICA/BOGOTA': "America/Bogota",
            'AMERICA/CANCUN': "America/Cancun",
            'AMERICA/CAYMAN': "America/Cayman",
            'AMERICA/GUAYAQUIL': "America/Guayaquil",
            'AMERICA/HAVANA': "America/Havana",
            'AMERICA/IQALUIT': "America/Iqaluit",
            'AMERICA/JAMAICA': "America/Jamaica",
            'AMERICA/LIMA': "America/Lima",
            'AMERICA/NASSAU': "America/Nassau",
            'AMERICA/NEW_YORK': "America/New_York",
            'AMERICA/PANAMA': "America/Panama",
            'AMERICA/PORT-AU-PRINCE': "America/Port-au-Prince",
            'AMERICA/RIO_BRANCO': "America/Rio_Branco",
            'AMERICA/TORONTO': "America/Toronto",
            'PACIFIC/EASTER': "Pacific/Easter",
            'AMERICA/CARACAS': "America/Caracas",
            'AMERICA/ASUNCION': "America/Asuncion",
            'AMERICA/BARBADOS': "America/Barbados",
            'AMERICA/BOA_VISTA': "America/Boa_Vista",
            'AMERICA/CAMPO_GRANDE': "America/Campo_Grande",
            'AMERICA/CUIABA': "America/Cuiaba",
            'AMERICA/CURACAO': "America/Curacao",
            'AMERICA/GRAND_TURK': "America/Grand_Turk",
            'AMERICA/GUYANA': "America/Guyana",
            'AMERICA/HALIFAX': "America/Halifax",
            'AMERICA/LA_PAZ': "America/La_Paz",
            'AMERICA/MANAUS': "America/Manaus",
            'AMERICA/MARTINIQUE': "America/Martinique",
            'AMERICA/PORT_OF_SPAIN': "America/Port_of_Spain",
            'AMERICA/PORTO_VELHO': "America/Porto_Velho",
            'AMERICA/PUERTO_RICO': "America/Puerto_Rico",
            'AMERICA/SANTO_DOMINGO': "America/Santo_Domingo",
            'AMERICA/THULE': "America/Thule",
            'ATLANTIC/BERMUDA': "Atlantic/Bermuda",
            'AMERICA/ST_JOHNS': "America/St_Johns",
            'AMERICA/ARAGUAINA': "America/Araguaina",
            'AMERICA/ARGENTINA/BUENOS_AIRES': "America/Argentina/Buenos_Aires",
            'AMERICA/BAHIA': "America/Bahia",
            'AMERICA/BELEM': "America/Belem",
            'AMERICA/CAYENNE': "America/Cayenne",
            'AMERICA/FORTALEZA': "America/Fortaleza",
            'AMERICA/GODTHAB': "America/Godthab",
            'AMERICA/MACEIO': "America/Maceio",
            'AMERICA/MIQUELON': "America/Miquelon",
            'AMERICA/MONTEVIDEO': "America/Montevideo",
            'AMERICA/PARAMARIBO': "America/Paramaribo",
            'AMERICA/RECIFE': "America/Recife",
            'AMERICA/SANTIAGO': "America/Santiago",
            'AMERICA/SAO_PAULO': "America/Sao_Paulo",
            'ANTARCTICA/PALMER': "Antarctica/Palmer",
            'ANTARCTICA/ROTHERA': "Antarctica/Rothera",
            'ATLANTIC/STANLEY': "Atlantic/Stanley",
            'AMERICA/NORONHA': "America/Noronha",
            'ATLANTIC/SOUTH_GEORGIA': "Atlantic/South_Georgia",
            'AMERICA/SCORESBYSUND': "America/Scoresbysund",
            'ATLANTIC/AZORES': "Atlantic/Azores",
            'ATLANTIC/CAPE_VERDE': "Atlantic/Cape_Verde",
            'AFRICA/ABIDJAN': "Africa/Abidjan",
            'AFRICA/ACCRA': "Africa/Accra",
            'AFRICA/BISSAU': "Africa/Bissau",
            'AFRICA/CASABLANCA': "Africa/Casablanca",
            'AFRICA/EL_AAIUN': "Africa/El_Aaiun",
            'AFRICA/MONROVIA': "Africa/Monrovia",
            'AMERICA/DANMARKSHAVN': "America/Danmarkshavn",
            'ATLANTIC/CANARY': "Atlantic/Canary",
            'ATLANTIC/FAROE': "Atlantic/Faroe",
            'ATLANTIC/REYKJAVIK': "Atlantic/Reykjavik",
            'ETC/GMT': "Etc/GMT",
            'EUROPE/DUBLIN': "Europe/Dublin",
            'EUROPE/LISBON': "Europe/Lisbon",
            'EUROPE/LONDON': "Europe/London",
            'AFRICA/ALGIERS': "Africa/Algiers",
            'AFRICA/CEUTA': "Africa/Ceuta",
            'AFRICA/LAGOS': "Africa/Lagos",
            'AFRICA/NDJAMENA': "Africa/Ndjamena",
            'AFRICA/TUNIS': "Africa/Tunis",
            'AFRICA/WINDHOEK': "Africa/Windhoek",
            'EUROPE/AMSTERDAM': "Europe/Amsterdam",
            'EUROPE/ANDORRA': "Europe/Andorra",
            'EUROPE/BELGRADE': "Europe/Belgrade",
            'EUROPE/BERLIN': "Europe/Berlin",
            'EUROPE/BRUSSELS': "Europe/Brussels",
            'EUROPE/BUDAPEST': "Europe/Budapest",
            'EUROPE/COPENHAGEN': "Europe/Copenhagen",
            'EUROPE/GIBRALTAR': "Europe/Gibraltar",
            'EUROPE/LUXEMBOURG': "Europe/Luxembourg",
            'EUROPE/MADRID': "Europe/Madrid",
            'EUROPE/MALTA': "Europe/Malta",
            'EUROPE/MONACO': "Europe/Monaco",
            'EUROPE/OSLO': "Europe/Oslo",
            'EUROPE/PARIS': "Europe/Paris",
            'EUROPE/PRAGUE': "Europe/Prague",
            'EUROPE/ROME': "Europe/Rome",
            'EUROPE/STOCKHOLM': "Europe/Stockholm",
            'EUROPE/TIRANE': "Europe/Tirane",
            'EUROPE/VIENNA': "Europe/Vienna",
            'EUROPE/WARSAW': "Europe/Warsaw",
            'EUROPE/ZURICH': "Europe/Zurich",
            'AFRICA/CAIRO': "Africa/Cairo",
            'AFRICA/JOHANNESBURG': "Africa/Johannesburg",
            'AFRICA/MAPUTO': "Africa/Maputo",
            'AFRICA/TRIPOLI': "Africa/Tripoli",
            'ASIA/AMMAN': "Asia/Amman",
            'ASIA/BEIRUT': "Asia/Beirut",
            'ASIA/DAMASCUS': "Asia/Damascus",
            'ASIA/GAZA': "Asia/Gaza",
            'ASIA/JERUSALEM': "Asia/Jerusalem",
            'ASIA/NICOSIA': "Asia/Nicosia",
            'EUROPE/ATHENS': "Europe/Athens",
            'EUROPE/BUCHAREST': "Europe/Bucharest",
            'EUROPE/CHISINAU': "Europe/Chisinau",
            'EUROPE/HELSINKI': "Europe/Helsinki",
            'EUROPE/ISTANBUL': "Europe/Istanbul",
            'EUROPE/KALININGRAD': "Europe/Kaliningrad",
            'EUROPE/KIEV': "Europe/Kiev",
            'EUROPE/RIGA': "Europe/Riga",
            'EUROPE/SOFIA': "Europe/Sofia",
            'EUROPE/TALLINN': "Europe/Tallinn",
            'EUROPE/VILNIUS': "Europe/Vilnius",
            'AFRICA/KHARTOUM': "Africa/Khartoum",
            'AFRICA/NAIROBI': "Africa/Nairobi",
            'ANTARCTICA/SYOWA': "Antarctica/Syowa",
            'ASIA/BAGHDAD': "Asia/Baghdad",
            'ASIA/QATAR': "Asia/Qatar",
            'ASIA/RIYADH': "Asia/Riyadh",
            'EUROPE/MINSK': "Europe/Minsk",
            'EUROPE/MOSCOW': "Europe/Moscow",
            'ASIA/TEHRAN': "Asia/Tehran",
            'ASIA/BAKU': "Asia/Baku",
            'ASIA/DUBAI': "Asia/Dubai",
            'ASIA/TBILISI': "Asia/Tbilisi",
            'ASIA/YEREVAN': "Asia/Yerevan",
            'EUROPE/SAMARA': "Europe/Samara",
            'INDIAN/MAHE': "Indian/Mahe",
            'INDIAN/MAURITIUS': "Indian/Mauritius",
            'INDIAN/REUNION': "Indian/Reunion",
            'ASIA/KABUL': "Asia/Kabul",
            'ANTARCTICA/MAWSON': "Antarctica/Mawson",
            'ASIA/AQTAU': "Asia/Aqtau",
            'ASIA/AQTOBE': "Asia/Aqtobe",
            'ASIA/ASHGABAT': "Asia/Ashgabat",
            'ASIA/DUSHANBE': "Asia/Dushanbe",
            'ASIA/KARACHI': "Asia/Karachi",
            'ASIA/TASHKENT': "Asia/Tashkent",
            'ASIA/YEKATERINBURG': "Asia/Yekaterinburg",
            'INDIAN/KERGUELEN': "Indian/Kerguelen",
            'INDIAN/MALDIVES': "Indian/Maldives",
            'ASIA/CALCUTTA': "Asia/Calcutta",
            'ASIA/KOLKATA': "Asia/Kolkata",
            'ASIA/COLOMBO': "Asia/Colombo",
            'ASIA/KATMANDU': "Asia/Katmandu",
            'ANTARCTICA/VOSTOK': "Antarctica/Vostok",
            'ASIA/ALMATY': "Asia/Almaty",
            'ASIA/BISHKEK': "Asia/Bishkek",
            'ASIA/DHAKA': "Asia/Dhaka",
            'ASIA/OMSK': "Asia/Omsk",
            'ASIA/THIMPHU': "Asia/Thimphu",
            'INDIAN/CHAGOS': "Indian/Chagos",
            'ASIA/RANGOON': "Asia/Rangoon",
            'INDIAN/COCOS': "Indian/Cocos",
            'ANTARCTICA/DAVIS': "Antarctica/Davis",
            'ASIA/BANGKOK': "Asia/Bangkok",
            'ASIA/HOVD': "Asia/Hovd",
            'ASIA/JAKARTA': "Asia/Jakarta",
            'ASIA/KRASNOYARSK': "Asia/Krasnoyarsk",
            'ASIA/SAIGON': "Asia/Saigon",
            'INDIAN/CHRISTMAS': "Indian/Christmas",
            'ANTARCTICA/CASEY': "Antarctica/Casey",
            'ASIA/BRUNEI': "Asia/Brunei",
            'ASIA/CHOIBALSAN': "Asia/Choibalsan",
            'ASIA/HONG_KONG': "Asia/Hong_Kong",
            'ASIA/IRKUTSK': "Asia/Irkutsk",
            'ASIA/KUALA_LUMPUR': "Asia/Kuala_Lumpur",
            'ASIA/MACAU': "Asia/Macau",
            'ASIA/MAKASSAR': "Asia/Makassar",
            'ASIA/MANILA': "Asia/Manila",
            'ASIA/SHANGHAI': "Asia/Shanghai",
            'ASIA/SINGAPORE': "Asia/Singapore",
            'ASIA/TAIPEI': "Asia/Taipei",
            'ASIA/ULAANBAATAR': "Asia/Ulaanbaatar",
            'AUSTRALIA/PERTH': "Australia/Perth",
            'ASIA/PYONGYANG': "Asia/Pyongyang",
            'ASIA/DILI': "Asia/Dili",
            'ASIA/JAYAPURA': "Asia/Jayapura",
            'ASIA/SEOUL': "Asia/Seoul",
            'ASIA/TOKYO': "Asia/Tokyo",
            'ASIA/YAKUTSK': "Asia/Yakutsk",
            'PACIFIC/PALAU': "Pacific/Palau",
            'AUSTRALIA/ADELAIDE': "Australia/Adelaide",
            'AUSTRALIA/DARWIN': "Australia/Darwin",
            'ANTARCTICA/DUMONTDURVILLE': "Antarctica/DumontDUrville",
            'ASIA/MAGADAN': "Asia/Magadan",
            'ASIA/VLADIVOSTOK': "Asia/Vladivostok",
            'AUSTRALIA/BRISBANE': "Australia/Brisbane",
            'AUSTRALIA/HOBART': "Australia/Hobart",
            'AUSTRALIA/SYDNEY': "Australia/Sydney",
            'PACIFIC/CHUUK': "Pacific/Chuuk",
            'PACIFIC/GUAM': "Pacific/Guam",
            'PACIFIC/PORT_MORESBY': "Pacific/Port_Moresby",
            'PACIFIC/EFATE': "Pacific/Efate",
            'PACIFIC/GUADALCANAL': "Pacific/Guadalcanal",
            'PACIFIC/KOSRAE': "Pacific/Kosrae",
            'PACIFIC/NORFOLK': "Pacific/Norfolk",
            'PACIFIC/NOUMEA': "Pacific/Noumea",
            'PACIFIC/POHNPEI': "Pacific/Pohnpei",
            'ASIA/KAMCHATKA': "Asia/Kamchatka",
            'PACIFIC/AUCKLAND': "Pacific/Auckland",
            'PACIFIC/FIJI': "Pacific/Fiji",
            'PACIFIC/FUNAFUTI': "Pacific/Funafuti",
            'PACIFIC/KWAJALEIN': "Pacific/Kwajalein",
            'PACIFIC/MAJURO': "Pacific/Majuro",
            'PACIFIC/NAURU': "Pacific/Nauru",
            'PACIFIC/TARAWA': "Pacific/Tarawa",
            'PACIFIC/WAKE': "Pacific/Wake",
            'PACIFIC/WALLIS': "Pacific/Wallis",
            'PACIFIC/APIA': "Pacific/Apia",
            'PACIFIC/ENDERBURY': "Pacific/Enderbury",
            'PACIFIC/FAKAOFO': "Pacific/Fakaofo",
            'PACIFIC/TONGATAPU': "Pacific/Tongatapu",
            'PACIFIC/KIRITIMATI': "Pacific/Kiritimati",
        },
    }

    validations = {
        ('day_of_month',): {
            'inclusive_maximum': 31,
            'inclusive_minimum': 0,
        },
        ('day_of_week',): {
            'inclusive_maximum': 7,
            'inclusive_minimum': 0,
        },
        ('month_of_year',): {
            'inclusive_maximum': 12,
            'inclusive_minimum': 0,
        },
        ('time_of_day',): {
            'inclusive_maximum': 86399,
            'inclusive_minimum': 0,
        },
        ('week_of_month',): {
            'inclusive_maximum': 5,
            'inclusive_minimum': 0,
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
        return {
            'day_of_month': (int,),  # noqa: E501
            'day_of_week': (int,),  # noqa: E501
            'month_of_year': (int,),  # noqa: E501
            'repeat_interval': (int,),  # noqa: E501
            'time_of_day': (int,),  # noqa: E501
            'time_zone': (str,),  # noqa: E501
            'week_of_month': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'day_of_month': 'DayOfMonth',  # noqa: E501
        'day_of_week': 'DayOfWeek',  # noqa: E501
        'month_of_year': 'MonthOfYear',  # noqa: E501
        'repeat_interval': 'RepeatInterval',  # noqa: E501
        'time_of_day': 'TimeOfDay',  # noqa: E501
        'time_zone': 'TimeZone',  # noqa: E501
        'week_of_month': 'WeekOfMonth',  # noqa: E501
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
        """OnpremScheduleAllOf - a model defined in OpenAPI

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
            day_of_month (int): Schedule a task on a specific day of the month. Valid values are 1 through 31. If monthOfYear is specified, then dayOfMonth value must be valid for that month. DayOfMonth may not be set when dayOfWeek is specfied.. [optional]  # noqa: E501
            day_of_week (int): Schedule a task on a specific day of the week. Valid values are 1 through 7, with 1 being Sunday. DayOfWeek may not be specfied when dayOfMonth is specified.. [optional]  # noqa: E501
            month_of_year (int): Schedule a task on a specific month of the year. Valid values are 1 through 12, with 1 being January.. [optional]  # noqa: E501
            repeat_interval (int): Schedule a task to run periodically at an interval. Default unit of the RepeatInterval is in minutes. If the RepeateInterval value is set, then all other properties are ignored by the scheduler. RepeateInterval constraints are enforced by the services that use the schedule. Each service has pre-configured service specific properties for enforcing minimum and maximum values of the RepeatInterval.. [optional]  # noqa: E501
            time_of_day (int): Time of the day in seconds. TimeOfDay is required for all schedule configurations, except when the RepeateInterval field is specified.. [optional]  # noqa: E501
            time_zone (str): Timezone to use for the schedule calculation. If a timezone value is not speficied, then the schedule calculation will be based on UTC.. [optional] if omitted the server will use the default value of "Pacific/Niue"  # noqa: E501
            week_of_month (int): Schedule a task on a specific week of the month. Valid values are 1 through 5. Value of 5 means last week of the month. WeekOfMonth may not be set when dayOfMonth is specified.. [optional]  # noqa: E501
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
