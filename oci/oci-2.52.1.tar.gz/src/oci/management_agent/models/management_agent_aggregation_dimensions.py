# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgentAggregationDimensions(object):
    """
    The Aggregation of Management Agent Dimensions
    """

    #: A constant which can be used with the availability_status property of a ManagementAgentAggregationDimensions.
    #: This constant has a value of "ACTIVE"
    AVAILABILITY_STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the availability_status property of a ManagementAgentAggregationDimensions.
    #: This constant has a value of "SILENT"
    AVAILABILITY_STATUS_SILENT = "SILENT"

    #: A constant which can be used with the availability_status property of a ManagementAgentAggregationDimensions.
    #: This constant has a value of "NOT_AVAILABLE"
    AVAILABILITY_STATUS_NOT_AVAILABLE = "NOT_AVAILABLE"

    #: A constant which can be used with the platform_type property of a ManagementAgentAggregationDimensions.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a ManagementAgentAggregationDimensions.
    #: This constant has a value of "WINDOWS"
    PLATFORM_TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the platform_type property of a ManagementAgentAggregationDimensions.
    #: This constant has a value of "SOLARIS"
    PLATFORM_TYPE_SOLARIS = "SOLARIS"

    #: A constant which can be used with the install_type property of a ManagementAgentAggregationDimensions.
    #: This constant has a value of "AGENT"
    INSTALL_TYPE_AGENT = "AGENT"

    #: A constant which can be used with the install_type property of a ManagementAgentAggregationDimensions.
    #: This constant has a value of "GATEWAY"
    INSTALL_TYPE_GATEWAY = "GATEWAY"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgentAggregationDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_status:
            The value to assign to the availability_status property of this ManagementAgentAggregationDimensions.
            Allowed values for this property are: "ACTIVE", "SILENT", "NOT_AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type availability_status: str

        :param platform_type:
            The value to assign to the platform_type property of this ManagementAgentAggregationDimensions.
            Allowed values for this property are: "LINUX", "WINDOWS", "SOLARIS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        :param version:
            The value to assign to the version property of this ManagementAgentAggregationDimensions.
        :type version: str

        :param has_plugins:
            The value to assign to the has_plugins property of this ManagementAgentAggregationDimensions.
        :type has_plugins: bool

        :param install_type:
            The value to assign to the install_type property of this ManagementAgentAggregationDimensions.
            Allowed values for this property are: "AGENT", "GATEWAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type install_type: str

        """
        self.swagger_types = {
            'availability_status': 'str',
            'platform_type': 'str',
            'version': 'str',
            'has_plugins': 'bool',
            'install_type': 'str'
        }

        self.attribute_map = {
            'availability_status': 'availabilityStatus',
            'platform_type': 'platformType',
            'version': 'version',
            'has_plugins': 'hasPlugins',
            'install_type': 'installType'
        }

        self._availability_status = None
        self._platform_type = None
        self._version = None
        self._has_plugins = None
        self._install_type = None

    @property
    def availability_status(self):
        """
        Gets the availability_status of this ManagementAgentAggregationDimensions.
        The availability status of managementAgent

        Allowed values for this property are: "ACTIVE", "SILENT", "NOT_AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The availability_status of this ManagementAgentAggregationDimensions.
        :rtype: str
        """
        return self._availability_status

    @availability_status.setter
    def availability_status(self, availability_status):
        """
        Sets the availability_status of this ManagementAgentAggregationDimensions.
        The availability status of managementAgent


        :param availability_status: The availability_status of this ManagementAgentAggregationDimensions.
        :type: str
        """
        allowed_values = ["ACTIVE", "SILENT", "NOT_AVAILABLE"]
        if not value_allowed_none_or_none_sentinel(availability_status, allowed_values):
            availability_status = 'UNKNOWN_ENUM_VALUE'
        self._availability_status = availability_status

    @property
    def platform_type(self):
        """
        Gets the platform_type of this ManagementAgentAggregationDimensions.
        Platform Type

        Allowed values for this property are: "LINUX", "WINDOWS", "SOLARIS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this ManagementAgentAggregationDimensions.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this ManagementAgentAggregationDimensions.
        Platform Type


        :param platform_type: The platform_type of this ManagementAgentAggregationDimensions.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "SOLARIS"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    @property
    def version(self):
        """
        Gets the version of this ManagementAgentAggregationDimensions.
        Agent image version


        :return: The version of this ManagementAgentAggregationDimensions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ManagementAgentAggregationDimensions.
        Agent image version


        :param version: The version of this ManagementAgentAggregationDimensions.
        :type: str
        """
        self._version = version

    @property
    def has_plugins(self):
        """
        Gets the has_plugins of this ManagementAgentAggregationDimensions.
        Whether or not a managementAgent has at least one plugin


        :return: The has_plugins of this ManagementAgentAggregationDimensions.
        :rtype: bool
        """
        return self._has_plugins

    @has_plugins.setter
    def has_plugins(self, has_plugins):
        """
        Sets the has_plugins of this ManagementAgentAggregationDimensions.
        Whether or not a managementAgent has at least one plugin


        :param has_plugins: The has_plugins of this ManagementAgentAggregationDimensions.
        :type: bool
        """
        self._has_plugins = has_plugins

    @property
    def install_type(self):
        """
        Gets the install_type of this ManagementAgentAggregationDimensions.
        The install type, either AGENT or GATEWAY

        Allowed values for this property are: "AGENT", "GATEWAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The install_type of this ManagementAgentAggregationDimensions.
        :rtype: str
        """
        return self._install_type

    @install_type.setter
    def install_type(self, install_type):
        """
        Sets the install_type of this ManagementAgentAggregationDimensions.
        The install type, either AGENT or GATEWAY


        :param install_type: The install_type of this ManagementAgentAggregationDimensions.
        :type: str
        """
        allowed_values = ["AGENT", "GATEWAY"]
        if not value_allowed_none_or_none_sentinel(install_type, allowed_values):
            install_type = 'UNKNOWN_ENUM_VALUE'
        self._install_type = install_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
