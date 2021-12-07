# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_details import DatabaseDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstalledDatabaseDetails(DatabaseDetails):
    """
    The details of the database running on-premises or on a compute instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstalledDatabaseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.InstalledDatabaseDetails.database_type` attribute
        of this class is ``INSTALLED_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_type:
            The value to assign to the database_type property of this InstalledDatabaseDetails.
            Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE"
        :type database_type: str

        :param infrastructure_type:
            The value to assign to the infrastructure_type property of this InstalledDatabaseDetails.
            Allowed values for this property are: "ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"
        :type infrastructure_type: str

        :param instance_id:
            The value to assign to the instance_id property of this InstalledDatabaseDetails.
        :type instance_id: str

        :param ip_addresses:
            The value to assign to the ip_addresses property of this InstalledDatabaseDetails.
        :type ip_addresses: list[str]

        :param listener_port:
            The value to assign to the listener_port property of this InstalledDatabaseDetails.
        :type listener_port: int

        :param service_name:
            The value to assign to the service_name property of this InstalledDatabaseDetails.
        :type service_name: str

        """
        self.swagger_types = {
            'database_type': 'str',
            'infrastructure_type': 'str',
            'instance_id': 'str',
            'ip_addresses': 'list[str]',
            'listener_port': 'int',
            'service_name': 'str'
        }

        self.attribute_map = {
            'database_type': 'databaseType',
            'infrastructure_type': 'infrastructureType',
            'instance_id': 'instanceId',
            'ip_addresses': 'ipAddresses',
            'listener_port': 'listenerPort',
            'service_name': 'serviceName'
        }

        self._database_type = None
        self._infrastructure_type = None
        self._instance_id = None
        self._ip_addresses = None
        self._listener_port = None
        self._service_name = None
        self._database_type = 'INSTALLED_DATABASE'

    @property
    def instance_id(self):
        """
        Gets the instance_id of this InstalledDatabaseDetails.
        The OCID of the compute instance on which the database is running.


        :return: The instance_id of this InstalledDatabaseDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this InstalledDatabaseDetails.
        The OCID of the compute instance on which the database is running.


        :param instance_id: The instance_id of this InstalledDatabaseDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this InstalledDatabaseDetails.
        The list of database host IP Addresses. Fully qualified domain names can be used if connectionType is 'ONPREM_CONNECTOR'.


        :return: The ip_addresses of this InstalledDatabaseDetails.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this InstalledDatabaseDetails.
        The list of database host IP Addresses. Fully qualified domain names can be used if connectionType is 'ONPREM_CONNECTOR'.


        :param ip_addresses: The ip_addresses of this InstalledDatabaseDetails.
        :type: list[str]
        """
        self._ip_addresses = ip_addresses

    @property
    def listener_port(self):
        """
        Gets the listener_port of this InstalledDatabaseDetails.
        The port number of the database listener.


        :return: The listener_port of this InstalledDatabaseDetails.
        :rtype: int
        """
        return self._listener_port

    @listener_port.setter
    def listener_port(self, listener_port):
        """
        Sets the listener_port of this InstalledDatabaseDetails.
        The port number of the database listener.


        :param listener_port: The listener_port of this InstalledDatabaseDetails.
        :type: int
        """
        self._listener_port = listener_port

    @property
    def service_name(self):
        """
        Gets the service_name of this InstalledDatabaseDetails.
        The service name of the database registered as target database.


        :return: The service_name of this InstalledDatabaseDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this InstalledDatabaseDetails.
        The service name of the database registered as target database.


        :param service_name: The service_name of this InstalledDatabaseDetails.
        :type: str
        """
        self._service_name = service_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
