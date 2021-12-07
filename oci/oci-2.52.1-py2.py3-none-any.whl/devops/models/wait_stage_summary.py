# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_pipeline_stage_summary import BuildPipelineStageSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WaitStageSummary(BuildPipelineStageSummary):
    """
    Specifies the Wait stage. You can specify variable wait times or an absolute duration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WaitStageSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.WaitStageSummary.build_pipeline_stage_type` attribute
        of this class is ``WAIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WaitStageSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this WaitStageSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this WaitStageSummary.
        :type project_id: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this WaitStageSummary.
        :type build_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WaitStageSummary.
        :type compartment_id: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this WaitStageSummary.
        :type build_pipeline_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this WaitStageSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this WaitStageSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WaitStageSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this WaitStageSummary.
        :type lifecycle_details: str

        :param description:
            The value to assign to the description property of this WaitStageSummary.
        :type description: str

        :param build_pipeline_stage_predecessor_collection:
            The value to assign to the build_pipeline_stage_predecessor_collection property of this WaitStageSummary.
        :type build_pipeline_stage_predecessor_collection: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WaitStageSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WaitStageSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this WaitStageSummary.
        :type system_tags: dict(str, dict(str, object))

        :param wait_criteria:
            The value to assign to the wait_criteria property of this WaitStageSummary.
        :type wait_criteria: oci.devops.models.WaitCriteria

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'build_pipeline_id': 'str',
            'compartment_id': 'str',
            'build_pipeline_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'description': 'str',
            'build_pipeline_stage_predecessor_collection': 'BuildPipelineStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'wait_criteria': 'WaitCriteria'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'build_pipeline_id': 'buildPipelineId',
            'compartment_id': 'compartmentId',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'description': 'description',
            'build_pipeline_stage_predecessor_collection': 'buildPipelineStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'wait_criteria': 'waitCriteria'
        }

        self._id = None
        self._display_name = None
        self._project_id = None
        self._build_pipeline_id = None
        self._compartment_id = None
        self._build_pipeline_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._description = None
        self._build_pipeline_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._wait_criteria = None
        self._build_pipeline_stage_type = 'WAIT'

    @property
    def wait_criteria(self):
        """
        **[Required]** Gets the wait_criteria of this WaitStageSummary.

        :return: The wait_criteria of this WaitStageSummary.
        :rtype: oci.devops.models.WaitCriteria
        """
        return self._wait_criteria

    @wait_criteria.setter
    def wait_criteria(self, wait_criteria):
        """
        Sets the wait_criteria of this WaitStageSummary.

        :param wait_criteria: The wait_criteria of this WaitStageSummary.
        :type: oci.devops.models.WaitCriteria
        """
        self._wait_criteria = wait_criteria

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
