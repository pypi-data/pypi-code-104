# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TriggerInfo(object):
    """
    Trigger details that need to be used for the BuildRun
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TriggerInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this TriggerInfo.
        :type display_name: str

        :param actions:
            The value to assign to the actions property of this TriggerInfo.
        :type actions: list[oci.devops.models.TriggerAction]

        """
        self.swagger_types = {
            'display_name': 'str',
            'actions': 'list[TriggerAction]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'actions': 'actions'
        }

        self._display_name = None
        self._actions = None

    @property
    def display_name(self):
        """
        Gets the display_name of this TriggerInfo.
        Name for Trigger.


        :return: The display_name of this TriggerInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TriggerInfo.
        Name for Trigger.


        :param display_name: The display_name of this TriggerInfo.
        :type: str
        """
        self._display_name = display_name

    @property
    def actions(self):
        """
        **[Required]** Gets the actions of this TriggerInfo.
        The list of actions that are to be performed for this Trigger


        :return: The actions of this TriggerInfo.
        :rtype: list[oci.devops.models.TriggerAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this TriggerInfo.
        The list of actions that are to be performed for this Trigger


        :param actions: The actions of this TriggerInfo.
        :type: list[oci.devops.models.TriggerAction]
        """
        self._actions = actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
