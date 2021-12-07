# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CollaborativeCapabilityWeightOverride(object):
    """
    Collaborative capability key and overriding weight.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CollaborativeCapabilityWeightOverride object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CollaborativeCapabilityWeightOverride.
        :type key: str

        :param weight:
            The value to assign to the weight property of this CollaborativeCapabilityWeightOverride.
        :type weight: int

        """
        self.swagger_types = {
            'key': 'str',
            'weight': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'weight': 'weight'
        }

        self._key = None
        self._weight = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this CollaborativeCapabilityWeightOverride.
        Unique key of collaborative capability for which weight will be overridden.


        :return: The key of this CollaborativeCapabilityWeightOverride.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CollaborativeCapabilityWeightOverride.
        Unique key of collaborative capability for which weight will be overridden.


        :param key: The key of this CollaborativeCapabilityWeightOverride.
        :type: str
        """
        self._key = key

    @property
    def weight(self):
        """
        **[Required]** Gets the weight of this CollaborativeCapabilityWeightOverride.
        The value of weight to set.


        :return: The weight of this CollaborativeCapabilityWeightOverride.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this CollaborativeCapabilityWeightOverride.
        The value of weight to set.


        :param weight: The weight of this CollaborativeCapabilityWeightOverride.
        :type: int
        """
        self._weight = weight

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
