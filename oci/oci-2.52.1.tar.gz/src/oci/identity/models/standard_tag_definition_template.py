# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StandardTagDefinitionTemplate(object):
    """
    The template of the tag definition. This object includes necessary details to create the provided standard tag definition.
    """

    #: A constant which can be used with the type property of a StandardTagDefinitionTemplate.
    #: This constant has a value of "ENUM"
    TYPE_ENUM = "ENUM"

    #: A constant which can be used with the type property of a StandardTagDefinitionTemplate.
    #: This constant has a value of "STRING"
    TYPE_STRING = "STRING"

    #: A constant which can be used with the enum_mutability property of a StandardTagDefinitionTemplate.
    #: This constant has a value of "IMMUTABLE"
    ENUM_MUTABILITY_IMMUTABLE = "IMMUTABLE"

    #: A constant which can be used with the enum_mutability property of a StandardTagDefinitionTemplate.
    #: This constant has a value of "MUTABLE"
    ENUM_MUTABILITY_MUTABLE = "MUTABLE"

    #: A constant which can be used with the enum_mutability property of a StandardTagDefinitionTemplate.
    #: This constant has a value of "APPENDABLE"
    ENUM_MUTABILITY_APPENDABLE = "APPENDABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new StandardTagDefinitionTemplate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this StandardTagDefinitionTemplate.
        :type description: str

        :param tag_definition_name:
            The value to assign to the tag_definition_name property of this StandardTagDefinitionTemplate.
        :type tag_definition_name: str

        :param type:
            The value to assign to the type property of this StandardTagDefinitionTemplate.
            Allowed values for this property are: "ENUM", "STRING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param possible_values:
            The value to assign to the possible_values property of this StandardTagDefinitionTemplate.
        :type possible_values: list[str]

        :param is_cost_tracking:
            The value to assign to the is_cost_tracking property of this StandardTagDefinitionTemplate.
        :type is_cost_tracking: bool

        :param enum_mutability:
            The value to assign to the enum_mutability property of this StandardTagDefinitionTemplate.
            Allowed values for this property are: "IMMUTABLE", "MUTABLE", "APPENDABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type enum_mutability: str

        """
        self.swagger_types = {
            'description': 'str',
            'tag_definition_name': 'str',
            'type': 'str',
            'possible_values': 'list[str]',
            'is_cost_tracking': 'bool',
            'enum_mutability': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'tag_definition_name': 'tagDefinitionName',
            'type': 'type',
            'possible_values': 'possibleValues',
            'is_cost_tracking': 'isCostTracking',
            'enum_mutability': 'enumMutability'
        }

        self._description = None
        self._tag_definition_name = None
        self._type = None
        self._possible_values = None
        self._is_cost_tracking = None
        self._enum_mutability = None

    @property
    def description(self):
        """
        **[Required]** Gets the description of this StandardTagDefinitionTemplate.
        The default description of the tag namespace that users can use to create the tag definition


        :return: The description of this StandardTagDefinitionTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StandardTagDefinitionTemplate.
        The default description of the tag namespace that users can use to create the tag definition


        :param description: The description of this StandardTagDefinitionTemplate.
        :type: str
        """
        self._description = description

    @property
    def tag_definition_name(self):
        """
        **[Required]** Gets the tag_definition_name of this StandardTagDefinitionTemplate.
        The name of this standard tag definition


        :return: The tag_definition_name of this StandardTagDefinitionTemplate.
        :rtype: str
        """
        return self._tag_definition_name

    @tag_definition_name.setter
    def tag_definition_name(self, tag_definition_name):
        """
        Sets the tag_definition_name of this StandardTagDefinitionTemplate.
        The name of this standard tag definition


        :param tag_definition_name: The tag_definition_name of this StandardTagDefinitionTemplate.
        :type: str
        """
        self._tag_definition_name = tag_definition_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this StandardTagDefinitionTemplate.
        The type of tag definition. Enum or string.

        Allowed values for this property are: "ENUM", "STRING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this StandardTagDefinitionTemplate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StandardTagDefinitionTemplate.
        The type of tag definition. Enum or string.


        :param type: The type of this StandardTagDefinitionTemplate.
        :type: str
        """
        allowed_values = ["ENUM", "STRING"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def possible_values(self):
        """
        Gets the possible_values of this StandardTagDefinitionTemplate.
        List of possible values. An optional parameter that will be present if the type of definition is enum.


        :return: The possible_values of this StandardTagDefinitionTemplate.
        :rtype: list[str]
        """
        return self._possible_values

    @possible_values.setter
    def possible_values(self, possible_values):
        """
        Sets the possible_values of this StandardTagDefinitionTemplate.
        List of possible values. An optional parameter that will be present if the type of definition is enum.


        :param possible_values: The possible_values of this StandardTagDefinitionTemplate.
        :type: list[str]
        """
        self._possible_values = possible_values

    @property
    def is_cost_tracking(self):
        """
        **[Required]** Gets the is_cost_tracking of this StandardTagDefinitionTemplate.
        Is the tag a cost tracking tag. Default will be false as cost tracking tags have been deprecated


        :return: The is_cost_tracking of this StandardTagDefinitionTemplate.
        :rtype: bool
        """
        return self._is_cost_tracking

    @is_cost_tracking.setter
    def is_cost_tracking(self, is_cost_tracking):
        """
        Sets the is_cost_tracking of this StandardTagDefinitionTemplate.
        Is the tag a cost tracking tag. Default will be false as cost tracking tags have been deprecated


        :param is_cost_tracking: The is_cost_tracking of this StandardTagDefinitionTemplate.
        :type: bool
        """
        self._is_cost_tracking = is_cost_tracking

    @property
    def enum_mutability(self):
        """
        Gets the enum_mutability of this StandardTagDefinitionTemplate.
        The mutability of the possible values list for enum tags. This will default to IMMUTABLE for string value tags

        Allowed values for this property are: "IMMUTABLE", "MUTABLE", "APPENDABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The enum_mutability of this StandardTagDefinitionTemplate.
        :rtype: str
        """
        return self._enum_mutability

    @enum_mutability.setter
    def enum_mutability(self, enum_mutability):
        """
        Sets the enum_mutability of this StandardTagDefinitionTemplate.
        The mutability of the possible values list for enum tags. This will default to IMMUTABLE for string value tags


        :param enum_mutability: The enum_mutability of this StandardTagDefinitionTemplate.
        :type: str
        """
        allowed_values = ["IMMUTABLE", "MUTABLE", "APPENDABLE"]
        if not value_allowed_none_or_none_sentinel(enum_mutability, allowed_values):
            enum_mutability = 'UNKNOWN_ENUM_VALUE'
        self._enum_mutability = enum_mutability

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
