# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_pipeline_stage_run_progress import BuildPipelineStageRunProgress
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WaitStageRunProgress(BuildPipelineStageRunProgress):
    """
    Specifies Wait stage specific run details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WaitStageRunProgress object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.WaitStageRunProgress.build_pipeline_stage_type` attribute
        of this class is ``WAIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stage_display_name:
            The value to assign to the stage_display_name property of this WaitStageRunProgress.
        :type stage_display_name: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this WaitStageRunProgress.
        :type build_pipeline_stage_type: str

        :param build_pipeline_stage_id:
            The value to assign to the build_pipeline_stage_id property of this WaitStageRunProgress.
        :type build_pipeline_stage_id: str

        :param time_started:
            The value to assign to the time_started property of this WaitStageRunProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WaitStageRunProgress.
        :type time_finished: datetime

        :param status:
            The value to assign to the status property of this WaitStageRunProgress.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"
        :type status: str

        :param build_pipeline_stage_predecessors:
            The value to assign to the build_pipeline_stage_predecessors property of this WaitStageRunProgress.
        :type build_pipeline_stage_predecessors: oci.devops.models.BuildPipelineStagePredecessorCollection

        """
        self.swagger_types = {
            'stage_display_name': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_stage_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'status': 'str',
            'build_pipeline_stage_predecessors': 'BuildPipelineStagePredecessorCollection'
        }

        self.attribute_map = {
            'stage_display_name': 'stageDisplayName',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_stage_id': 'buildPipelineStageId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'status': 'status',
            'build_pipeline_stage_predecessors': 'buildPipelineStagePredecessors'
        }

        self._stage_display_name = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_stage_id = None
        self._time_started = None
        self._time_finished = None
        self._status = None
        self._build_pipeline_stage_predecessors = None
        self._build_pipeline_stage_type = 'WAIT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
