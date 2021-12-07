# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection_option import ConnectionOption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OnPremiseConnector(ConnectionOption):
    """
    The details required to establish a connection to the database using an on-premises connector.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OnPremiseConnector object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.OnPremiseConnector.connection_type` attribute
        of this class is ``ONPREM_CONNECTOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this OnPremiseConnector.
            Allowed values for this property are: "PRIVATE_ENDPOINT", "ONPREM_CONNECTOR"
        :type connection_type: str

        :param on_prem_connector_id:
            The value to assign to the on_prem_connector_id property of this OnPremiseConnector.
        :type on_prem_connector_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'on_prem_connector_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'on_prem_connector_id': 'onPremConnectorId'
        }

        self._connection_type = None
        self._on_prem_connector_id = None
        self._connection_type = 'ONPREM_CONNECTOR'

    @property
    def on_prem_connector_id(self):
        """
        Gets the on_prem_connector_id of this OnPremiseConnector.
        The OCID of the on-premises connector.


        :return: The on_prem_connector_id of this OnPremiseConnector.
        :rtype: str
        """
        return self._on_prem_connector_id

    @on_prem_connector_id.setter
    def on_prem_connector_id(self, on_prem_connector_id):
        """
        Sets the on_prem_connector_id of this OnPremiseConnector.
        The OCID of the on-premises connector.


        :param on_prem_connector_id: The on_prem_connector_id of this OnPremiseConnector.
        :type: str
        """
        self._on_prem_connector_id = on_prem_connector_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
