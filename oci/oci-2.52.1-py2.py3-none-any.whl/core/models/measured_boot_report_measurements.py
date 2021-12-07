# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MeasuredBootReportMeasurements(object):
    """
    A list of Trusted Platform Module (TPM) Platform Configuration Register (PCR) entries.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MeasuredBootReportMeasurements object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this MeasuredBootReportMeasurements.
        :type policy: list[oci.core.models.MeasuredBootEntry]

        :param actual:
            The value to assign to the actual property of this MeasuredBootReportMeasurements.
        :type actual: list[oci.core.models.MeasuredBootEntry]

        """
        self.swagger_types = {
            'policy': 'list[MeasuredBootEntry]',
            'actual': 'list[MeasuredBootEntry]'
        }

        self.attribute_map = {
            'policy': 'policy',
            'actual': 'actual'
        }

        self._policy = None
        self._actual = None

    @property
    def policy(self):
        """
        Gets the policy of this MeasuredBootReportMeasurements.
        The list of expected PCR entries to use during verification.


        :return: The policy of this MeasuredBootReportMeasurements.
        :rtype: list[oci.core.models.MeasuredBootEntry]
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this MeasuredBootReportMeasurements.
        The list of expected PCR entries to use during verification.


        :param policy: The policy of this MeasuredBootReportMeasurements.
        :type: list[oci.core.models.MeasuredBootEntry]
        """
        self._policy = policy

    @property
    def actual(self):
        """
        Gets the actual of this MeasuredBootReportMeasurements.
        The list of actual PCR entries measured during boot.


        :return: The actual of this MeasuredBootReportMeasurements.
        :rtype: list[oci.core.models.MeasuredBootEntry]
        """
        return self._actual

    @actual.setter
    def actual(self, actual):
        """
        Sets the actual of this MeasuredBootReportMeasurements.
        The list of actual PCR entries measured during boot.


        :param actual: The actual of this MeasuredBootReportMeasurements.
        :type: list[oci.core.models.MeasuredBootEntry]
        """
        self._actual = actual

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
