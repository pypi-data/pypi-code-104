# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitorStatusCountMap(object):
    """
    Details of the monitor count per state.
    Example: `{ \"total\" : 5, \"enabled\" : 3 , \"disabled\" : 2, \"invalid\" : 0 }`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitorStatusCountMap object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total:
            The value to assign to the total property of this MonitorStatusCountMap.
        :type total: int

        :param enabled:
            The value to assign to the enabled property of this MonitorStatusCountMap.
        :type enabled: int

        :param disabled:
            The value to assign to the disabled property of this MonitorStatusCountMap.
        :type disabled: int

        :param invalid:
            The value to assign to the invalid property of this MonitorStatusCountMap.
        :type invalid: int

        """
        self.swagger_types = {
            'total': 'int',
            'enabled': 'int',
            'disabled': 'int',
            'invalid': 'int'
        }

        self.attribute_map = {
            'total': 'total',
            'enabled': 'enabled',
            'disabled': 'disabled',
            'invalid': 'invalid'
        }

        self._total = None
        self._enabled = None
        self._disabled = None
        self._invalid = None

    @property
    def total(self):
        """
        **[Required]** Gets the total of this MonitorStatusCountMap.
        Total number of monitors using the script.


        :return: The total of this MonitorStatusCountMap.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this MonitorStatusCountMap.
        Total number of monitors using the script.


        :param total: The total of this MonitorStatusCountMap.
        :type: int
        """
        self._total = total

    @property
    def enabled(self):
        """
        **[Required]** Gets the enabled of this MonitorStatusCountMap.
        Number of enabled monitors using the script.


        :return: The enabled of this MonitorStatusCountMap.
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this MonitorStatusCountMap.
        Number of enabled monitors using the script.


        :param enabled: The enabled of this MonitorStatusCountMap.
        :type: int
        """
        self._enabled = enabled

    @property
    def disabled(self):
        """
        **[Required]** Gets the disabled of this MonitorStatusCountMap.
        Number of disabled monitors using the script.


        :return: The disabled of this MonitorStatusCountMap.
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """
        Sets the disabled of this MonitorStatusCountMap.
        Number of disabled monitors using the script.


        :param disabled: The disabled of this MonitorStatusCountMap.
        :type: int
        """
        self._disabled = disabled

    @property
    def invalid(self):
        """
        **[Required]** Gets the invalid of this MonitorStatusCountMap.
        Number of invalid monitors using the script.


        :return: The invalid of this MonitorStatusCountMap.
        :rtype: int
        """
        return self._invalid

    @invalid.setter
    def invalid(self, invalid):
        """
        Sets the invalid of this MonitorStatusCountMap.
        Number of invalid monitors using the script.


        :param invalid: The invalid of this MonitorStatusCountMap.
        :type: int
        """
        self._invalid = invalid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
