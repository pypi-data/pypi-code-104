# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsEndpointServiceSummary(object):
    """
    Summary of the DatabaseToolsEndpointService.
    """

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsEndpointServiceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsEndpointServiceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsEndpointServiceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsEndpointServiceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsEndpointServiceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsEndpointServiceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsEndpointServiceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DatabaseToolsEndpointServiceSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DatabaseToolsEndpointServiceSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this DatabaseToolsEndpointServiceSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseToolsEndpointServiceSummary.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseToolsEndpointServiceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseToolsEndpointServiceSummary.
        :type freeform_tags: dict(str, str)

        :param system_tags:
            The value to assign to the system_tags property of this DatabaseToolsEndpointServiceSummary.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this DatabaseToolsEndpointServiceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatabaseToolsEndpointServiceSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseToolsEndpointServiceSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseToolsEndpointServiceSummary.
        :type lifecycle_details: str

        :param description:
            The value to assign to the description property of this DatabaseToolsEndpointServiceSummary.
        :type description: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'description': 'description'
        }

        self._id = None
        self._display_name = None
        self._name = None
        self._compartment_id = None
        self._defined_tags = None
        self._freeform_tags = None
        self._system_tags = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._description = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DatabaseToolsEndpointServiceSummary.
        The `OCID`__ of the DatabaseToolsEndpointService.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DatabaseToolsEndpointServiceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseToolsEndpointServiceSummary.
        The `OCID`__ of the DatabaseToolsEndpointService.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DatabaseToolsEndpointServiceSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DatabaseToolsEndpointServiceSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this DatabaseToolsEndpointServiceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DatabaseToolsEndpointServiceSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this DatabaseToolsEndpointServiceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        Gets the name of this DatabaseToolsEndpointServiceSummary.
        A unique, non-changeable resource name.


        :return: The name of this DatabaseToolsEndpointServiceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatabaseToolsEndpointServiceSummary.
        A unique, non-changeable resource name.


        :param name: The name of this DatabaseToolsEndpointServiceSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DatabaseToolsEndpointServiceSummary.
        The `OCID`__ of the containing Compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DatabaseToolsEndpointServiceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseToolsEndpointServiceSummary.
        The `OCID`__ of the containing Compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DatabaseToolsEndpointServiceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DatabaseToolsEndpointServiceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DatabaseToolsEndpointServiceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatabaseToolsEndpointServiceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DatabaseToolsEndpointServiceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DatabaseToolsEndpointServiceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DatabaseToolsEndpointServiceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatabaseToolsEndpointServiceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DatabaseToolsEndpointServiceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DatabaseToolsEndpointServiceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DatabaseToolsEndpointServiceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DatabaseToolsEndpointServiceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DatabaseToolsEndpointServiceSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def time_created(self):
        """
        Gets the time_created of this DatabaseToolsEndpointServiceSummary.
        The time the DatabaseToolsEndpointService was created. An RFC3339 formatted datetime string


        :return: The time_created of this DatabaseToolsEndpointServiceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DatabaseToolsEndpointServiceSummary.
        The time the DatabaseToolsEndpointService was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this DatabaseToolsEndpointServiceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DatabaseToolsEndpointServiceSummary.
        The time the DatabaseToolsEndpointService was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this DatabaseToolsEndpointServiceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DatabaseToolsEndpointServiceSummary.
        The time the DatabaseToolsEndpointService was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this DatabaseToolsEndpointServiceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DatabaseToolsEndpointServiceSummary.
        The current state of the DatabaseToolsEndpointService.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DatabaseToolsEndpointServiceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatabaseToolsEndpointServiceSummary.
        The current state of the DatabaseToolsEndpointService.


        :param lifecycle_state: The lifecycle_state of this DatabaseToolsEndpointServiceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatabaseToolsEndpointServiceSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DatabaseToolsEndpointServiceSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatabaseToolsEndpointServiceSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DatabaseToolsEndpointServiceSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def description(self):
        """
        Gets the description of this DatabaseToolsEndpointServiceSummary.
        A description of the DatabaseToolsEndpointService.


        :return: The description of this DatabaseToolsEndpointServiceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DatabaseToolsEndpointServiceSummary.
        A description of the DatabaseToolsEndpointService.


        :param description: The description of this DatabaseToolsEndpointServiceSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
