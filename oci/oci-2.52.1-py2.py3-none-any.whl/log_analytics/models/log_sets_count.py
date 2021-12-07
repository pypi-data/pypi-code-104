# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogSetsCount(object):
    """
    total number of log sets
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogSetsCount object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param count:
            The value to assign to the count property of this LogSetsCount.
        :type count: int

        """
        self.swagger_types = {
            'count': 'int'
        }

        self.attribute_map = {
            'count': 'count'
        }

        self._count = None

    @property
    def count(self):
        """
        **[Required]** Gets the count of this LogSetsCount.
        This is the total number of log sets the tenancy has configured.


        :return: The count of this LogSetsCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this LogSetsCount.
        This is the total number of log sets the tenancy has configured.


        :param count: The count of this LogSetsCount.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
