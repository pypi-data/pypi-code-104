# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .trigger_create_result import TriggerCreateResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GitlabTriggerCreateResult(TriggerCreateResult):
    """
    Trigger create response specific to GitLab.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GitlabTriggerCreateResult object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.GitlabTriggerCreateResult.trigger_source` attribute
        of this class is ``GITLAB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GitlabTriggerCreateResult.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this GitlabTriggerCreateResult.
        :type display_name: str

        :param description:
            The value to assign to the description property of this GitlabTriggerCreateResult.
        :type description: str

        :param project_id:
            The value to assign to the project_id property of this GitlabTriggerCreateResult.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GitlabTriggerCreateResult.
        :type compartment_id: str

        :param trigger_source:
            The value to assign to the trigger_source property of this GitlabTriggerCreateResult.
        :type trigger_source: str

        :param time_created:
            The value to assign to the time_created property of this GitlabTriggerCreateResult.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this GitlabTriggerCreateResult.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GitlabTriggerCreateResult.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this GitlabTriggerCreateResult.
        :type lifecycle_details: str

        :param actions:
            The value to assign to the actions property of this GitlabTriggerCreateResult.
        :type actions: list[oci.devops.models.TriggerAction]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GitlabTriggerCreateResult.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GitlabTriggerCreateResult.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this GitlabTriggerCreateResult.
        :type system_tags: dict(str, dict(str, object))

        :param secret:
            The value to assign to the secret property of this GitlabTriggerCreateResult.
        :type secret: str

        :param trigger_url:
            The value to assign to the trigger_url property of this GitlabTriggerCreateResult.
        :type trigger_url: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'trigger_source': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'actions': 'list[TriggerAction]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'secret': 'str',
            'trigger_url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'trigger_source': 'triggerSource',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'actions': 'actions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'secret': 'secret',
            'trigger_url': 'triggerUrl'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._project_id = None
        self._compartment_id = None
        self._trigger_source = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._actions = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._secret = None
        self._trigger_url = None
        self._trigger_source = 'GITLAB'

    @property
    def secret(self):
        """
        **[Required]** Gets the secret of this GitlabTriggerCreateResult.
        The secret used to validate the incoming trigger call. This is visible only after the resource is created.


        :return: The secret of this GitlabTriggerCreateResult.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this GitlabTriggerCreateResult.
        The secret used to validate the incoming trigger call. This is visible only after the resource is created.


        :param secret: The secret of this GitlabTriggerCreateResult.
        :type: str
        """
        self._secret = secret

    @property
    def trigger_url(self):
        """
        **[Required]** Gets the trigger_url of this GitlabTriggerCreateResult.
        The endpoint that listens to trigger events.


        :return: The trigger_url of this GitlabTriggerCreateResult.
        :rtype: str
        """
        return self._trigger_url

    @trigger_url.setter
    def trigger_url(self, trigger_url):
        """
        Sets the trigger_url of this GitlabTriggerCreateResult.
        The endpoint that listens to trigger events.


        :param trigger_url: The trigger_url of this GitlabTriggerCreateResult.
        :type: str
        """
        self._trigger_url = trigger_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
