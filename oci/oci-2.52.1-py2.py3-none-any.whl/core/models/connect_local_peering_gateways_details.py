# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectLocalPeeringGatewaysDetails(object):
    """
    Information about the other local peering gateway (LPG).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectLocalPeeringGatewaysDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param peer_id:
            The value to assign to the peer_id property of this ConnectLocalPeeringGatewaysDetails.
        :type peer_id: str

        """
        self.swagger_types = {
            'peer_id': 'str'
        }

        self.attribute_map = {
            'peer_id': 'peerId'
        }

        self._peer_id = None

    @property
    def peer_id(self):
        """
        **[Required]** Gets the peer_id of this ConnectLocalPeeringGatewaysDetails.
        The `OCID`__ of the LPG you want to peer with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The peer_id of this ConnectLocalPeeringGatewaysDetails.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this ConnectLocalPeeringGatewaysDetails.
        The `OCID`__ of the LPG you want to peer with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param peer_id: The peer_id of this ConnectLocalPeeringGatewaysDetails.
        :type: str
        """
        self._peer_id = peer_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
