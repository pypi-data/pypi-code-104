# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceDefinition(object):
    """
    Model for details associated with service
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ServiceDefinition.
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this ServiceDefinition.
        :type display_name: str

        :param short_display_name:
            The value to assign to the short_display_name property of this ServiceDefinition.
        :type short_display_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'short_display_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'short_display_name': 'shortDisplayName'
        }

        self._type = None
        self._display_name = None
        self._short_display_name = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ServiceDefinition.
        The service definition type.


        :return: The type of this ServiceDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ServiceDefinition.
        The service definition type.


        :param type: The type of this ServiceDefinition.
        :type: str
        """
        self._type = type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ServiceDefinition.
        Display name of the service.


        :return: The display_name of this ServiceDefinition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ServiceDefinition.
        Display name of the service.


        :param display_name: The display_name of this ServiceDefinition.
        :type: str
        """
        self._display_name = display_name

    @property
    def short_display_name(self):
        """
        **[Required]** Gets the short_display_name of this ServiceDefinition.
        Short display name of the service.


        :return: The short_display_name of this ServiceDefinition.
        :rtype: str
        """
        return self._short_display_name

    @short_display_name.setter
    def short_display_name(self, short_display_name):
        """
        Sets the short_display_name of this ServiceDefinition.
        Short display name of the service.


        :param short_display_name: The short_display_name of this ServiceDefinition.
        :type: str
        """
        self._short_display_name = short_display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
