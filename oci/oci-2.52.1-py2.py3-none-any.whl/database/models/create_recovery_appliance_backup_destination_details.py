# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_backup_destination_details import CreateBackupDestinationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRecoveryApplianceBackupDestinationDetails(CreateBackupDestinationDetails):
    """
    Used for creating Recovery Appliance backup destinations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRecoveryApplianceBackupDestinationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateRecoveryApplianceBackupDestinationDetails.type` attribute
        of this class is ``RECOVERY_APPLIANCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateRecoveryApplianceBackupDestinationDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRecoveryApplianceBackupDestinationDetails.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this CreateRecoveryApplianceBackupDestinationDetails.
            Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE"
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRecoveryApplianceBackupDestinationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRecoveryApplianceBackupDestinationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param connection_string:
            The value to assign to the connection_string property of this CreateRecoveryApplianceBackupDestinationDetails.
        :type connection_string: str

        :param vpc_users:
            The value to assign to the vpc_users property of this CreateRecoveryApplianceBackupDestinationDetails.
        :type vpc_users: list[str]

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'connection_string': 'str',
            'vpc_users': 'list[str]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'connection_string': 'connectionString',
            'vpc_users': 'vpcUsers'
        }

        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._connection_string = None
        self._vpc_users = None
        self._type = 'RECOVERY_APPLIANCE'

    @property
    def connection_string(self):
        """
        **[Required]** Gets the connection_string of this CreateRecoveryApplianceBackupDestinationDetails.
        The connection string for connecting to the Recovery Appliance.


        :return: The connection_string of this CreateRecoveryApplianceBackupDestinationDetails.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this CreateRecoveryApplianceBackupDestinationDetails.
        The connection string for connecting to the Recovery Appliance.


        :param connection_string: The connection_string of this CreateRecoveryApplianceBackupDestinationDetails.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def vpc_users(self):
        """
        **[Required]** Gets the vpc_users of this CreateRecoveryApplianceBackupDestinationDetails.
        The Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.


        :return: The vpc_users of this CreateRecoveryApplianceBackupDestinationDetails.
        :rtype: list[str]
        """
        return self._vpc_users

    @vpc_users.setter
    def vpc_users(self, vpc_users):
        """
        Sets the vpc_users of this CreateRecoveryApplianceBackupDestinationDetails.
        The Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.


        :param vpc_users: The vpc_users of this CreateRecoveryApplianceBackupDestinationDetails.
        :type: list[str]
        """
        self._vpc_users = vpc_users

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
