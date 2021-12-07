# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Model(object):
    """
    Description of Model.
    """

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new Model object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Model.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Model.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Model.
        :type compartment_id: str

        :param model_training_details:
            The value to assign to the model_training_details property of this Model.
        :type model_training_details: oci.ai_anomaly_detection.models.ModelTrainingDetails

        :param model_training_results:
            The value to assign to the model_training_results property of this Model.
        :type model_training_results: oci.ai_anomaly_detection.models.ModelTrainingResults

        :param project_id:
            The value to assign to the project_id property of this Model.
        :type project_id: str

        :param description:
            The value to assign to the description property of this Model.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Model.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Model.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Model.
            Allowed values for this property are: "DELETING", "DELETED", "FAILED", "CREATING", "ACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Model.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Model.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Model.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Model.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'model_training_details': 'ModelTrainingDetails',
            'model_training_results': 'ModelTrainingResults',
            'project_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'model_training_details': 'modelTrainingDetails',
            'model_training_results': 'modelTrainingResults',
            'project_id': 'projectId',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._model_training_details = None
        self._model_training_results = None
        self._project_id = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Model.
        The OCID of the model that is immutable on creation.


        :return: The id of this Model.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Model.
        The OCID of the model that is immutable on creation.


        :param id: The id of this Model.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Model.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.


        :return: The display_name of this Model.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Model.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this Model.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Model.
        The OCID for the model's compartment.


        :return: The compartment_id of this Model.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Model.
        The OCID for the model's compartment.


        :param compartment_id: The compartment_id of this Model.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def model_training_details(self):
        """
        **[Required]** Gets the model_training_details of this Model.

        :return: The model_training_details of this Model.
        :rtype: oci.ai_anomaly_detection.models.ModelTrainingDetails
        """
        return self._model_training_details

    @model_training_details.setter
    def model_training_details(self, model_training_details):
        """
        Sets the model_training_details of this Model.

        :param model_training_details: The model_training_details of this Model.
        :type: oci.ai_anomaly_detection.models.ModelTrainingDetails
        """
        self._model_training_details = model_training_details

    @property
    def model_training_results(self):
        """
        **[Required]** Gets the model_training_results of this Model.

        :return: The model_training_results of this Model.
        :rtype: oci.ai_anomaly_detection.models.ModelTrainingResults
        """
        return self._model_training_results

    @model_training_results.setter
    def model_training_results(self, model_training_results):
        """
        Sets the model_training_results of this Model.

        :param model_training_results: The model_training_results of this Model.
        :type: oci.ai_anomaly_detection.models.ModelTrainingResults
        """
        self._model_training_results = model_training_results

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this Model.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this Model.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Model.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this Model.
        :type: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """
        Gets the description of this Model.
        A short description of the Model.


        :return: The description of this Model.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Model.
        A short description of the Model.


        :param description: The description of this Model.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Model.
        The time the the Model was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Model.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Model.
        The time the the Model was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Model.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Model.
        The time the Model was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this Model.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Model.
        The time the Model was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Model.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Model.
        The state of the model.

        Allowed values for this property are: "DELETING", "DELETED", "FAILED", "CREATING", "ACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Model.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Model.
        The state of the model.


        :param lifecycle_state: The lifecycle_state of this Model.
        :type: str
        """
        allowed_values = ["DELETING", "DELETED", "FAILED", "CREATING", "ACTIVE", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Model.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this Model.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Model.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this Model.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Model.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Model.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Model.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Model.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Model.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Model.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Model.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Model.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Model.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Model.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Model.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Model.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
