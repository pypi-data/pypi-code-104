# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    Summary of a work request.
    """

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ENABLE_DATA_SAFE_CONFIGURATION"
    OPERATION_TYPE_ENABLE_DATA_SAFE_CONFIGURATION = "ENABLE_DATA_SAFE_CONFIGURATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_PRIVATE_ENDPOINT"
    OPERATION_TYPE_CREATE_PRIVATE_ENDPOINT = "CREATE_PRIVATE_ENDPOINT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_PRIVATE_ENDPOINT"
    OPERATION_TYPE_UPDATE_PRIVATE_ENDPOINT = "UPDATE_PRIVATE_ENDPOINT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_PRIVATE_ENDPOINT"
    OPERATION_TYPE_DELETE_PRIVATE_ENDPOINT = "DELETE_PRIVATE_ENDPOINT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT"
    OPERATION_TYPE_CHANGE_PRIVATE_ENDPOINT_COMPARTMENT = "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_ONPREM_CONNECTOR"
    OPERATION_TYPE_CREATE_ONPREM_CONNECTOR = "CREATE_ONPREM_CONNECTOR"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ONPREM_CONNECTOR"
    OPERATION_TYPE_UPDATE_ONPREM_CONNECTOR = "UPDATE_ONPREM_CONNECTOR"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_ONPREM_CONNECTOR"
    OPERATION_TYPE_DELETE_ONPREM_CONNECTOR = "DELETE_ONPREM_CONNECTOR"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ONPREM_CONNECTOR_WALLET"
    OPERATION_TYPE_UPDATE_ONPREM_CONNECTOR_WALLET = "UPDATE_ONPREM_CONNECTOR_WALLET"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_ONPREM_CONNECTOR_COMPARTMENT"
    OPERATION_TYPE_CHANGE_ONPREM_CONNECTOR_COMPARTMENT = "CHANGE_ONPREM_CONNECTOR_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_TARGET_DATABASE"
    OPERATION_TYPE_CREATE_TARGET_DATABASE = "CREATE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_TARGET_DATABASE"
    OPERATION_TYPE_UPDATE_TARGET_DATABASE = "UPDATE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ACTIVATE_TARGET_DATABASE"
    OPERATION_TYPE_ACTIVATE_TARGET_DATABASE = "ACTIVATE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DEACTIVATE_TARGET_DATABASE"
    OPERATION_TYPE_DEACTIVATE_TARGET_DATABASE = "DEACTIVATE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_TARGET_DATABASE"
    OPERATION_TYPE_DELETE_TARGET_DATABASE = "DELETE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_TARGET_DATABASE_COMPARTMENT"
    OPERATION_TYPE_CHANGE_TARGET_DATABASE_COMPARTMENT = "CHANGE_TARGET_DATABASE_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_USER_ASSESSMENT"
    OPERATION_TYPE_CREATE_USER_ASSESSMENT = "CREATE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ASSESS_USER_ASSESSMENT"
    OPERATION_TYPE_ASSESS_USER_ASSESSMENT = "ASSESS_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SNAPSHOT_USER_ASSESSMENT"
    OPERATION_TYPE_CREATE_SNAPSHOT_USER_ASSESSMENT = "CREATE_SNAPSHOT_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SCHEDULE_USER_ASSESSMENT"
    OPERATION_TYPE_CREATE_SCHEDULE_USER_ASSESSMENT = "CREATE_SCHEDULE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "COMPARE_WITH_BASELINE_USER_ASSESSMENT"
    OPERATION_TYPE_COMPARE_WITH_BASELINE_USER_ASSESSMENT = "COMPARE_WITH_BASELINE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_USER_ASSESSMENT"
    OPERATION_TYPE_DELETE_USER_ASSESSMENT = "DELETE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_USER_ASSESSMENT"
    OPERATION_TYPE_UPDATE_USER_ASSESSMENT = "UPDATE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_USER_ASSESSMENT_COMPARTMENT"
    OPERATION_TYPE_CHANGE_USER_ASSESSMENT_COMPARTMENT = "CHANGE_USER_ASSESSMENT_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "SET_USER_ASSESSMENT_BASELINE"
    OPERATION_TYPE_SET_USER_ASSESSMENT_BASELINE = "SET_USER_ASSESSMENT_BASELINE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UNSET_USER_ASSESSMENT_BASELINE"
    OPERATION_TYPE_UNSET_USER_ASSESSMENT_BASELINE = "UNSET_USER_ASSESSMENT_BASELINE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_USER_ASSESSMENT_REPORT"
    OPERATION_TYPE_GENERATE_USER_ASSESSMENT_REPORT = "GENERATE_USER_ASSESSMENT_REPORT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_CREATE_SECURITY_ASSESSMENT = "CREATE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SECURITY_ASSESSMENT_NOW"
    OPERATION_TYPE_CREATE_SECURITY_ASSESSMENT_NOW = "CREATE_SECURITY_ASSESSMENT_NOW"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ASSESS_SECURITY_ASSESSMENT"
    OPERATION_TYPE_ASSESS_SECURITY_ASSESSMENT = "ASSESS_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SNAPSHOT_SECURITY_ASSESSMENT"
    OPERATION_TYPE_CREATE_SNAPSHOT_SECURITY_ASSESSMENT = "CREATE_SNAPSHOT_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SCHEDULE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_CREATE_SCHEDULE_SECURITY_ASSESSMENT = "CREATE_SCHEDULE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT = "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_DELETE_SECURITY_ASSESSMENT = "DELETE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_UPDATE_SECURITY_ASSESSMENT = "UPDATE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT"
    OPERATION_TYPE_CHANGE_SECURITY_ASSESSMENT_COMPARTMENT = "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "SET_SECURITY_ASSESSMENT_BASELINE"
    OPERATION_TYPE_SET_SECURITY_ASSESSMENT_BASELINE = "SET_SECURITY_ASSESSMENT_BASELINE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UNSET_SECURITY_ASSESSMENT_BASELINE"
    OPERATION_TYPE_UNSET_SECURITY_ASSESSMENT_BASELINE = "UNSET_SECURITY_ASSESSMENT_BASELINE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_SECURITY_ASSESSMENT_REPORT"
    OPERATION_TYPE_GENERATE_SECURITY_ASSESSMENT_REPORT = "GENERATE_SECURITY_ASSESSMENT_REPORT"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequestSummary.
            Allowed values for this property are: "ENABLE_DATA_SAFE_CONFIGURATION", "CREATE_PRIVATE_ENDPOINT", "UPDATE_PRIVATE_ENDPOINT", "DELETE_PRIVATE_ENDPOINT", "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT", "CREATE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR", "DELETE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR_WALLET", "CHANGE_ONPREM_CONNECTOR_COMPARTMENT", "CREATE_TARGET_DATABASE", "UPDATE_TARGET_DATABASE", "ACTIVATE_TARGET_DATABASE", "DEACTIVATE_TARGET_DATABASE", "DELETE_TARGET_DATABASE", "CHANGE_TARGET_DATABASE_COMPARTMENT", "CREATE_USER_ASSESSMENT", "ASSESS_USER_ASSESSMENT", "CREATE_SNAPSHOT_USER_ASSESSMENT", "CREATE_SCHEDULE_USER_ASSESSMENT", "COMPARE_WITH_BASELINE_USER_ASSESSMENT", "DELETE_USER_ASSESSMENT", "UPDATE_USER_ASSESSMENT", "CHANGE_USER_ASSESSMENT_COMPARTMENT", "SET_USER_ASSESSMENT_BASELINE", "UNSET_USER_ASSESSMENT_BASELINE", "GENERATE_USER_ASSESSMENT_REPORT", "CREATE_SECURITY_ASSESSMENT", "CREATE_SECURITY_ASSESSMENT_NOW", "ASSESS_SECURITY_ASSESSMENT", "CREATE_SNAPSHOT_SECURITY_ASSESSMENT", "CREATE_SCHEDULE_SECURITY_ASSESSMENT", "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT", "DELETE_SECURITY_ASSESSMENT", "UPDATE_SECURITY_ASSESSMENT", "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT", "SET_SECURITY_ASSESSMENT_BASELINE", "UNSET_SECURITY_ASSESSMENT_BASELINE", "GENERATE_SECURITY_ASSESSMENT_REPORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this WorkRequestSummary.
        :type resources: list[oci.data_safe.models.WorkRequestResource]

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: float

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequestSummary.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._operation_type = None
        self._status = None
        self._id = None
        self._compartment_id = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequestSummary.
        The asynchronous operation tracked by this work request.

        Allowed values for this property are: "ENABLE_DATA_SAFE_CONFIGURATION", "CREATE_PRIVATE_ENDPOINT", "UPDATE_PRIVATE_ENDPOINT", "DELETE_PRIVATE_ENDPOINT", "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT", "CREATE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR", "DELETE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR_WALLET", "CHANGE_ONPREM_CONNECTOR_COMPARTMENT", "CREATE_TARGET_DATABASE", "UPDATE_TARGET_DATABASE", "ACTIVATE_TARGET_DATABASE", "DEACTIVATE_TARGET_DATABASE", "DELETE_TARGET_DATABASE", "CHANGE_TARGET_DATABASE_COMPARTMENT", "CREATE_USER_ASSESSMENT", "ASSESS_USER_ASSESSMENT", "CREATE_SNAPSHOT_USER_ASSESSMENT", "CREATE_SCHEDULE_USER_ASSESSMENT", "COMPARE_WITH_BASELINE_USER_ASSESSMENT", "DELETE_USER_ASSESSMENT", "UPDATE_USER_ASSESSMENT", "CHANGE_USER_ASSESSMENT_COMPARTMENT", "SET_USER_ASSESSMENT_BASELINE", "UNSET_USER_ASSESSMENT_BASELINE", "GENERATE_USER_ASSESSMENT_REPORT", "CREATE_SECURITY_ASSESSMENT", "CREATE_SECURITY_ASSESSMENT_NOW", "ASSESS_SECURITY_ASSESSMENT", "CREATE_SNAPSHOT_SECURITY_ASSESSMENT", "CREATE_SCHEDULE_SECURITY_ASSESSMENT", "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT", "DELETE_SECURITY_ASSESSMENT", "UPDATE_SECURITY_ASSESSMENT", "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT", "SET_SECURITY_ASSESSMENT_BASELINE", "UNSET_SECURITY_ASSESSMENT_BASELINE", "GENERATE_SECURITY_ASSESSMENT_REPORT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequestSummary.
        The asynchronous operation tracked by this work request.


        :param operation_type: The operation_type of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ENABLE_DATA_SAFE_CONFIGURATION", "CREATE_PRIVATE_ENDPOINT", "UPDATE_PRIVATE_ENDPOINT", "DELETE_PRIVATE_ENDPOINT", "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT", "CREATE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR", "DELETE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR_WALLET", "CHANGE_ONPREM_CONNECTOR_COMPARTMENT", "CREATE_TARGET_DATABASE", "UPDATE_TARGET_DATABASE", "ACTIVATE_TARGET_DATABASE", "DEACTIVATE_TARGET_DATABASE", "DELETE_TARGET_DATABASE", "CHANGE_TARGET_DATABASE_COMPARTMENT", "CREATE_USER_ASSESSMENT", "ASSESS_USER_ASSESSMENT", "CREATE_SNAPSHOT_USER_ASSESSMENT", "CREATE_SCHEDULE_USER_ASSESSMENT", "COMPARE_WITH_BASELINE_USER_ASSESSMENT", "DELETE_USER_ASSESSMENT", "UPDATE_USER_ASSESSMENT", "CHANGE_USER_ASSESSMENT_COMPARTMENT", "SET_USER_ASSESSMENT_BASELINE", "UNSET_USER_ASSESSMENT_BASELINE", "GENERATE_USER_ASSESSMENT_REPORT", "CREATE_SECURITY_ASSESSMENT", "CREATE_SECURITY_ASSESSMENT_NOW", "ASSESS_SECURITY_ASSESSMENT", "CREATE_SNAPSHOT_SECURITY_ASSESSMENT", "CREATE_SCHEDULE_SECURITY_ASSESSMENT", "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT", "DELETE_SECURITY_ASSESSMENT", "UPDATE_SECURITY_ASSESSMENT", "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT", "SET_SECURITY_ASSESSMENT_BASELINE", "UNSET_SECURITY_ASSESSMENT_BASELINE", "GENERATE_SECURITY_ASSESSMENT_REPORT"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        The current status of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        The current status of the work request.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The OCID of the work request.


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The OCID of the work request.


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request.


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request.


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequestSummary.
        The resources that are affected by the work request.


        :return: The resources of this WorkRequestSummary.
        :rtype: list[oci.data_safe.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequestSummary.
        The resources that are affected by the work request.


        :param resources: The resources of this WorkRequestSummary.
        :type: list[oci.data_safe.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequestSummary.
        Progress of the work request in percentage.


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        Progress of the work request in percentage.


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequestSummary.
        The date and time the work request was accepted, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_accepted of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequestSummary.
        The date and time the work request was accepted, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_accepted: The time_accepted of this WorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequestSummary.
        The date and time the work request transitioned from ACCEPTED to IN_PROGRESS, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequestSummary.
        The date and time the work request transitioned from ACCEPTED to IN_PROGRESS, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this WorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequestSummary.
        The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_finished of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequestSummary.
        The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_finished: The time_finished of this WorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
