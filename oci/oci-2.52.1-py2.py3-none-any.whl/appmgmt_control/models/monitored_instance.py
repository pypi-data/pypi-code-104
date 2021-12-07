# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredInstance(object):
    """
    Description of Monitored Instance.
    """

    #: A constant which can be used with the monitoring_state property of a MonitoredInstance.
    #: This constant has a value of "ENABLED"
    MONITORING_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the monitoring_state property of a MonitoredInstance.
    #: This constant has a value of "DISABLED"
    MONITORING_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoredInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoredInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_id:
            The value to assign to the instance_id property of this MonitoredInstance.
        :type instance_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoredInstance.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MonitoredInstance.
        :type display_name: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MonitoredInstance.
        :type management_agent_id: str

        :param time_created:
            The value to assign to the time_created property of this MonitoredInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MonitoredInstance.
        :type time_updated: datetime

        :param monitoring_state:
            The value to assign to the monitoring_state property of this MonitoredInstance.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type monitoring_state: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MonitoredInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MonitoredInstance.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'instance_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'management_agent_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'monitoring_state': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'instance_id': 'instanceId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'management_agent_id': 'managementAgentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'monitoring_state': 'monitoringState',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._instance_id = None
        self._compartment_id = None
        self._display_name = None
        self._management_agent_id = None
        self._time_created = None
        self._time_updated = None
        self._monitoring_state = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this MonitoredInstance.
        The `OCID`__ of monitored instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The instance_id of this MonitoredInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this MonitoredInstance.
        The `OCID`__ of monitored instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param instance_id: The instance_id of this MonitoredInstance.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoredInstance.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoredInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoredInstance.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoredInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this MonitoredInstance.
        A user-friendly name of the monitored instance. It is binded to `Compute Instance`__.
        DisplayName is fetched from `Core Service API`__.

        __ https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm
        __ https://docs.cloud.oracle.com/api/#/en/iaas/20160918/Instance/


        :return: The display_name of this MonitoredInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MonitoredInstance.
        A user-friendly name of the monitored instance. It is binded to `Compute Instance`__.
        DisplayName is fetched from `Core Service API`__.

        __ https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm
        __ https://docs.cloud.oracle.com/api/#/en/iaas/20160918/Instance/


        :param display_name: The display_name of this MonitoredInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this MonitoredInstance.
        Management Agent Identifier `OCID`__.
        Used to invoke manage operations on Management Agent Cloud Service.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MonitoredInstance.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MonitoredInstance.
        Management Agent Identifier `OCID`__.
        Used to invoke manage operations on Management Agent Cloud Service.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MonitoredInstance.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def time_created(self):
        """
        Gets the time_created of this MonitoredInstance.
        The time the MonitoredInstance was created. An RFC3339 formatted datetime string


        :return: The time_created of this MonitoredInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MonitoredInstance.
        The time the MonitoredInstance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this MonitoredInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MonitoredInstance.
        The time the MonitoredInstance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this MonitoredInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MonitoredInstance.
        The time the MonitoredInstance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this MonitoredInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def monitoring_state(self):
        """
        Gets the monitoring_state of this MonitoredInstance.
        Monitoring status. Can be either enabled or disabled.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The monitoring_state of this MonitoredInstance.
        :rtype: str
        """
        return self._monitoring_state

    @monitoring_state.setter
    def monitoring_state(self, monitoring_state):
        """
        Sets the monitoring_state of this MonitoredInstance.
        Monitoring status. Can be either enabled or disabled.


        :param monitoring_state: The monitoring_state of this MonitoredInstance.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(monitoring_state, allowed_values):
            monitoring_state = 'UNKNOWN_ENUM_VALUE'
        self._monitoring_state = monitoring_state

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MonitoredInstance.
        The current state of the monitored instance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MonitoredInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MonitoredInstance.
        The current state of the monitored instance.


        :param lifecycle_state: The lifecycle_state of this MonitoredInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MonitoredInstance.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this MonitoredInstance.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MonitoredInstance.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this MonitoredInstance.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
