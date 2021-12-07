# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildRunProgress(object):
    """
    The run progress details of a build run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BuildRunProgress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_started:
            The value to assign to the time_started property of this BuildRunProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this BuildRunProgress.
        :type time_finished: datetime

        :param build_pipeline_stage_run_progress:
            The value to assign to the build_pipeline_stage_run_progress property of this BuildRunProgress.
        :type build_pipeline_stage_run_progress: dict(str, BuildPipelineStageRunProgress)

        """
        self.swagger_types = {
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'build_pipeline_stage_run_progress': 'dict(str, BuildPipelineStageRunProgress)'
        }

        self.attribute_map = {
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'build_pipeline_stage_run_progress': 'buildPipelineStageRunProgress'
        }

        self._time_started = None
        self._time_finished = None
        self._build_pipeline_stage_run_progress = None

    @property
    def time_started(self):
        """
        Gets the time_started of this BuildRunProgress.
        The time the build run started. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_started of this BuildRunProgress.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this BuildRunProgress.
        The time the build run started. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_started: The time_started of this BuildRunProgress.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this BuildRunProgress.
        The time the build run finished. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_finished of this BuildRunProgress.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this BuildRunProgress.
        The time the build run finished. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_finished: The time_finished of this BuildRunProgress.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def build_pipeline_stage_run_progress(self):
        """
        Gets the build_pipeline_stage_run_progress of this BuildRunProgress.
        Map of stage OCIDs to build pipeline stage run progress model.


        :return: The build_pipeline_stage_run_progress of this BuildRunProgress.
        :rtype: dict(str, BuildPipelineStageRunProgress)
        """
        return self._build_pipeline_stage_run_progress

    @build_pipeline_stage_run_progress.setter
    def build_pipeline_stage_run_progress(self, build_pipeline_stage_run_progress):
        """
        Sets the build_pipeline_stage_run_progress of this BuildRunProgress.
        Map of stage OCIDs to build pipeline stage run progress model.


        :param build_pipeline_stage_run_progress: The build_pipeline_stage_run_progress of this BuildRunProgress.
        :type: dict(str, BuildPipelineStageRunProgress)
        """
        self._build_pipeline_stage_run_progress = build_pipeline_stage_run_progress

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
