# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancerTrafficShiftRolloutPolicy(object):
    """
    Description of rollout policy for load balancer traffic shift stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancerTrafficShiftRolloutPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param batch_count:
            The value to assign to the batch_count property of this LoadBalancerTrafficShiftRolloutPolicy.
        :type batch_count: int

        :param batch_delay_in_seconds:
            The value to assign to the batch_delay_in_seconds property of this LoadBalancerTrafficShiftRolloutPolicy.
        :type batch_delay_in_seconds: int

        :param ramp_limit_percent:
            The value to assign to the ramp_limit_percent property of this LoadBalancerTrafficShiftRolloutPolicy.
        :type ramp_limit_percent: float

        """
        self.swagger_types = {
            'batch_count': 'int',
            'batch_delay_in_seconds': 'int',
            'ramp_limit_percent': 'float'
        }

        self.attribute_map = {
            'batch_count': 'batchCount',
            'batch_delay_in_seconds': 'batchDelayInSeconds',
            'ramp_limit_percent': 'rampLimitPercent'
        }

        self._batch_count = None
        self._batch_delay_in_seconds = None
        self._ramp_limit_percent = None

    @property
    def batch_count(self):
        """
        **[Required]** Gets the batch_count of this LoadBalancerTrafficShiftRolloutPolicy.
        Specifies number of batches for this stage.


        :return: The batch_count of this LoadBalancerTrafficShiftRolloutPolicy.
        :rtype: int
        """
        return self._batch_count

    @batch_count.setter
    def batch_count(self, batch_count):
        """
        Sets the batch_count of this LoadBalancerTrafficShiftRolloutPolicy.
        Specifies number of batches for this stage.


        :param batch_count: The batch_count of this LoadBalancerTrafficShiftRolloutPolicy.
        :type: int
        """
        self._batch_count = batch_count

    @property
    def batch_delay_in_seconds(self):
        """
        Gets the batch_delay_in_seconds of this LoadBalancerTrafficShiftRolloutPolicy.
        Specifies delay in seconds between batches. The default delay is 1 minute.


        :return: The batch_delay_in_seconds of this LoadBalancerTrafficShiftRolloutPolicy.
        :rtype: int
        """
        return self._batch_delay_in_seconds

    @batch_delay_in_seconds.setter
    def batch_delay_in_seconds(self, batch_delay_in_seconds):
        """
        Sets the batch_delay_in_seconds of this LoadBalancerTrafficShiftRolloutPolicy.
        Specifies delay in seconds between batches. The default delay is 1 minute.


        :param batch_delay_in_seconds: The batch_delay_in_seconds of this LoadBalancerTrafficShiftRolloutPolicy.
        :type: int
        """
        self._batch_delay_in_seconds = batch_delay_in_seconds

    @property
    def ramp_limit_percent(self):
        """
        Gets the ramp_limit_percent of this LoadBalancerTrafficShiftRolloutPolicy.
        Indicates the criteria to stop.


        :return: The ramp_limit_percent of this LoadBalancerTrafficShiftRolloutPolicy.
        :rtype: float
        """
        return self._ramp_limit_percent

    @ramp_limit_percent.setter
    def ramp_limit_percent(self, ramp_limit_percent):
        """
        Sets the ramp_limit_percent of this LoadBalancerTrafficShiftRolloutPolicy.
        Indicates the criteria to stop.


        :param ramp_limit_percent: The ramp_limit_percent of this LoadBalancerTrafficShiftRolloutPolicy.
        :type: float
        """
        self._ramp_limit_percent = ramp_limit_percent

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
