# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .filter import Filter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GithubFilter(Filter):
    """
    The filter for GitHub events.
    """

    #: A constant which can be used with the events property of a GithubFilter.
    #: This constant has a value of "PUSH"
    EVENTS_PUSH = "PUSH"

    #: A constant which can be used with the events property of a GithubFilter.
    #: This constant has a value of "PULL_REQUEST_CREATED"
    EVENTS_PULL_REQUEST_CREATED = "PULL_REQUEST_CREATED"

    #: A constant which can be used with the events property of a GithubFilter.
    #: This constant has a value of "PULL_REQUEST_UPDATED"
    EVENTS_PULL_REQUEST_UPDATED = "PULL_REQUEST_UPDATED"

    #: A constant which can be used with the events property of a GithubFilter.
    #: This constant has a value of "PULL_REQUEST_REOPENED"
    EVENTS_PULL_REQUEST_REOPENED = "PULL_REQUEST_REOPENED"

    #: A constant which can be used with the events property of a GithubFilter.
    #: This constant has a value of "PULL_REQUEST_MERGED"
    EVENTS_PULL_REQUEST_MERGED = "PULL_REQUEST_MERGED"

    def __init__(self, **kwargs):
        """
        Initializes a new GithubFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.GithubFilter.trigger_source` attribute
        of this class is ``GITHUB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param trigger_source:
            The value to assign to the trigger_source property of this GithubFilter.
        :type trigger_source: str

        :param events:
            The value to assign to the events property of this GithubFilter.
            Allowed values for items in this list are: "PUSH", "PULL_REQUEST_CREATED", "PULL_REQUEST_UPDATED", "PULL_REQUEST_REOPENED", "PULL_REQUEST_MERGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type events: list[str]

        :param include:
            The value to assign to the include property of this GithubFilter.
        :type include: oci.devops.models.GithubFilterAttributes

        """
        self.swagger_types = {
            'trigger_source': 'str',
            'events': 'list[str]',
            'include': 'GithubFilterAttributes'
        }

        self.attribute_map = {
            'trigger_source': 'triggerSource',
            'events': 'events',
            'include': 'include'
        }

        self._trigger_source = None
        self._events = None
        self._include = None
        self._trigger_source = 'GITHUB'

    @property
    def events(self):
        """
        Gets the events of this GithubFilter.
        The events, for example, PUSH, PULL_REQUEST_MERGE.

        Allowed values for items in this list are: "PUSH", "PULL_REQUEST_CREATED", "PULL_REQUEST_UPDATED", "PULL_REQUEST_REOPENED", "PULL_REQUEST_MERGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The events of this GithubFilter.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this GithubFilter.
        The events, for example, PUSH, PULL_REQUEST_MERGE.


        :param events: The events of this GithubFilter.
        :type: list[str]
        """
        allowed_values = ["PUSH", "PULL_REQUEST_CREATED", "PULL_REQUEST_UPDATED", "PULL_REQUEST_REOPENED", "PULL_REQUEST_MERGED"]
        if events:
            events[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in events]
        self._events = events

    @property
    def include(self):
        """
        Gets the include of this GithubFilter.

        :return: The include of this GithubFilter.
        :rtype: oci.devops.models.GithubFilterAttributes
        """
        return self._include

    @include.setter
    def include(self, include):
        """
        Sets the include of this GithubFilter.

        :param include: The include of this GithubFilter.
        :type: oci.devops.models.GithubFilterAttributes
        """
        self._include = include

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
