# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .topology_entity_relationship import TopologyEntityRelationship
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopologyContainsEntityRelationship(TopologyEntityRelationship):
    """
    Defines the `contains` relationship between virtual network topology entities. A `Contains` relationship
    is defined when an entity fully owns, contains or manages another entity.
    For example, a subnet is contained and managed in the scope of a VCN, therefore a VCN has a
    `contains` relationship to a subnet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TopologyContainsEntityRelationship object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.TopologyContainsEntityRelationship.type` attribute
        of this class is ``CONTAINS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id1:
            The value to assign to the id1 property of this TopologyContainsEntityRelationship.
        :type id1: str

        :param id2:
            The value to assign to the id2 property of this TopologyContainsEntityRelationship.
        :type id2: str

        :param type:
            The value to assign to the type property of this TopologyContainsEntityRelationship.
            Allowed values for this property are: "CONTAINS", "ASSOCIATED_WITH", "ROUTES_TO"
        :type type: str

        """
        self.swagger_types = {
            'id1': 'str',
            'id2': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'id1': 'id1',
            'id2': 'id2',
            'type': 'type'
        }

        self._id1 = None
        self._id2 = None
        self._type = None
        self._type = 'CONTAINS'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
