# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OriginGroup(object):
    """
    OriginGroup model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OriginGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param origins:
            The value to assign to the origins property of this OriginGroup.
        :type origins: list[oci.waas.models.OriginGroupOrigins]

        """
        self.swagger_types = {
            'origins': 'list[OriginGroupOrigins]'
        }

        self.attribute_map = {
            'origins': 'origins'
        }

        self._origins = None

    @property
    def origins(self):
        """
        Gets the origins of this OriginGroup.
        The list of objects containing origin references and additional properties.


        :return: The origins of this OriginGroup.
        :rtype: list[oci.waas.models.OriginGroupOrigins]
        """
        return self._origins

    @origins.setter
    def origins(self, origins):
        """
        Sets the origins of this OriginGroup.
        The list of objects containing origin references and additional properties.


        :param origins: The origins of this OriginGroup.
        :type: list[oci.waas.models.OriginGroupOrigins]
        """
        self._origins = origins

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
