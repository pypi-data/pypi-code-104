# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupDestinationSummary(object):
    """
    Backup destination details, including the list of databases using the backup destination.
    """

    #: A constant which can be used with the type property of a BackupDestinationSummary.
    #: This constant has a value of "NFS"
    TYPE_NFS = "NFS"

    #: A constant which can be used with the type property of a BackupDestinationSummary.
    #: This constant has a value of "RECOVERY_APPLIANCE"
    TYPE_RECOVERY_APPLIANCE = "RECOVERY_APPLIANCE"

    #: A constant which can be used with the nfs_mount_type property of a BackupDestinationSummary.
    #: This constant has a value of "SELF_MOUNT"
    NFS_MOUNT_TYPE_SELF_MOUNT = "SELF_MOUNT"

    #: A constant which can be used with the nfs_mount_type property of a BackupDestinationSummary.
    #: This constant has a value of "AUTOMATED_MOUNT"
    NFS_MOUNT_TYPE_AUTOMATED_MOUNT = "AUTOMATED_MOUNT"

    #: A constant which can be used with the lifecycle_state property of a BackupDestinationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BackupDestinationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a BackupDestinationSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new BackupDestinationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BackupDestinationSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BackupDestinationSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BackupDestinationSummary.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this BackupDestinationSummary.
            Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param associated_databases:
            The value to assign to the associated_databases property of this BackupDestinationSummary.
        :type associated_databases: list[oci.database.models.AssociatedDatabaseDetails]

        :param connection_string:
            The value to assign to the connection_string property of this BackupDestinationSummary.
        :type connection_string: str

        :param vpc_users:
            The value to assign to the vpc_users property of this BackupDestinationSummary.
        :type vpc_users: list[str]

        :param local_mount_point_path:
            The value to assign to the local_mount_point_path property of this BackupDestinationSummary.
        :type local_mount_point_path: str

        :param nfs_mount_type:
            The value to assign to the nfs_mount_type property of this BackupDestinationSummary.
            Allowed values for this property are: "SELF_MOUNT", "AUTOMATED_MOUNT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type nfs_mount_type: str

        :param nfs_server:
            The value to assign to the nfs_server property of this BackupDestinationSummary.
        :type nfs_server: list[str]

        :param nfs_server_export:
            The value to assign to the nfs_server_export property of this BackupDestinationSummary.
        :type nfs_server_export: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BackupDestinationSummary.
            Allowed values for this property are: "ACTIVE", "FAILED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this BackupDestinationSummary.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this BackupDestinationSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BackupDestinationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BackupDestinationSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'associated_databases': 'list[AssociatedDatabaseDetails]',
            'connection_string': 'str',
            'vpc_users': 'list[str]',
            'local_mount_point_path': 'str',
            'nfs_mount_type': 'str',
            'nfs_server': 'list[str]',
            'nfs_server_export': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'associated_databases': 'associatedDatabases',
            'connection_string': 'connectionString',
            'vpc_users': 'vpcUsers',
            'local_mount_point_path': 'localMountPointPath',
            'nfs_mount_type': 'nfsMountType',
            'nfs_server': 'nfsServer',
            'nfs_server_export': 'nfsServerExport',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._associated_databases = None
        self._connection_string = None
        self._vpc_users = None
        self._local_mount_point_path = None
        self._nfs_mount_type = None
        self._nfs_server = None
        self._nfs_server_export = None
        self._lifecycle_state = None
        self._time_created = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this BackupDestinationSummary.
        The `OCID`__ of the backup destination.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this BackupDestinationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BackupDestinationSummary.
        The `OCID`__ of the backup destination.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this BackupDestinationSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this BackupDestinationSummary.
        The user-provided name of the backup destination.


        :return: The display_name of this BackupDestinationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BackupDestinationSummary.
        The user-provided name of the backup destination.


        :param display_name: The display_name of this BackupDestinationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this BackupDestinationSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this BackupDestinationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BackupDestinationSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this BackupDestinationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        Gets the type of this BackupDestinationSummary.
        Type of the backup destination.

        Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this BackupDestinationSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BackupDestinationSummary.
        Type of the backup destination.


        :param type: The type of this BackupDestinationSummary.
        :type: str
        """
        allowed_values = ["NFS", "RECOVERY_APPLIANCE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def associated_databases(self):
        """
        Gets the associated_databases of this BackupDestinationSummary.
        List of databases associated with the backup destination.


        :return: The associated_databases of this BackupDestinationSummary.
        :rtype: list[oci.database.models.AssociatedDatabaseDetails]
        """
        return self._associated_databases

    @associated_databases.setter
    def associated_databases(self, associated_databases):
        """
        Sets the associated_databases of this BackupDestinationSummary.
        List of databases associated with the backup destination.


        :param associated_databases: The associated_databases of this BackupDestinationSummary.
        :type: list[oci.database.models.AssociatedDatabaseDetails]
        """
        self._associated_databases = associated_databases

    @property
    def connection_string(self):
        """
        Gets the connection_string of this BackupDestinationSummary.
        For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.


        :return: The connection_string of this BackupDestinationSummary.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this BackupDestinationSummary.
        For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.


        :param connection_string: The connection_string of this BackupDestinationSummary.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def vpc_users(self):
        """
        Gets the vpc_users of this BackupDestinationSummary.
        For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.


        :return: The vpc_users of this BackupDestinationSummary.
        :rtype: list[str]
        """
        return self._vpc_users

    @vpc_users.setter
    def vpc_users(self, vpc_users):
        """
        Sets the vpc_users of this BackupDestinationSummary.
        For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.


        :param vpc_users: The vpc_users of this BackupDestinationSummary.
        :type: list[str]
        """
        self._vpc_users = vpc_users

    @property
    def local_mount_point_path(self):
        """
        Gets the local_mount_point_path of this BackupDestinationSummary.
        The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.


        :return: The local_mount_point_path of this BackupDestinationSummary.
        :rtype: str
        """
        return self._local_mount_point_path

    @local_mount_point_path.setter
    def local_mount_point_path(self, local_mount_point_path):
        """
        Sets the local_mount_point_path of this BackupDestinationSummary.
        The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.


        :param local_mount_point_path: The local_mount_point_path of this BackupDestinationSummary.
        :type: str
        """
        self._local_mount_point_path = local_mount_point_path

    @property
    def nfs_mount_type(self):
        """
        Gets the nfs_mount_type of this BackupDestinationSummary.
        NFS Mount type for backup destination.

        Allowed values for this property are: "SELF_MOUNT", "AUTOMATED_MOUNT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The nfs_mount_type of this BackupDestinationSummary.
        :rtype: str
        """
        return self._nfs_mount_type

    @nfs_mount_type.setter
    def nfs_mount_type(self, nfs_mount_type):
        """
        Sets the nfs_mount_type of this BackupDestinationSummary.
        NFS Mount type for backup destination.


        :param nfs_mount_type: The nfs_mount_type of this BackupDestinationSummary.
        :type: str
        """
        allowed_values = ["SELF_MOUNT", "AUTOMATED_MOUNT"]
        if not value_allowed_none_or_none_sentinel(nfs_mount_type, allowed_values):
            nfs_mount_type = 'UNKNOWN_ENUM_VALUE'
        self._nfs_mount_type = nfs_mount_type

    @property
    def nfs_server(self):
        """
        Gets the nfs_server of this BackupDestinationSummary.
        Host names or IP addresses for NFS Auto mount.


        :return: The nfs_server of this BackupDestinationSummary.
        :rtype: list[str]
        """
        return self._nfs_server

    @nfs_server.setter
    def nfs_server(self, nfs_server):
        """
        Sets the nfs_server of this BackupDestinationSummary.
        Host names or IP addresses for NFS Auto mount.


        :param nfs_server: The nfs_server of this BackupDestinationSummary.
        :type: list[str]
        """
        self._nfs_server = nfs_server

    @property
    def nfs_server_export(self):
        """
        Gets the nfs_server_export of this BackupDestinationSummary.
        Specifies the directory on which to mount the file system


        :return: The nfs_server_export of this BackupDestinationSummary.
        :rtype: str
        """
        return self._nfs_server_export

    @nfs_server_export.setter
    def nfs_server_export(self, nfs_server_export):
        """
        Sets the nfs_server_export of this BackupDestinationSummary.
        Specifies the directory on which to mount the file system


        :param nfs_server_export: The nfs_server_export of this BackupDestinationSummary.
        :type: str
        """
        self._nfs_server_export = nfs_server_export

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BackupDestinationSummary.
        The current lifecycle state of the backup destination.

        Allowed values for this property are: "ACTIVE", "FAILED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BackupDestinationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BackupDestinationSummary.
        The current lifecycle state of the backup destination.


        :param lifecycle_state: The lifecycle_state of this BackupDestinationSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "FAILED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this BackupDestinationSummary.
        The date and time the backup destination was created.


        :return: The time_created of this BackupDestinationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BackupDestinationSummary.
        The date and time the backup destination was created.


        :param time_created: The time_created of this BackupDestinationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this BackupDestinationSummary.
        A descriptive text associated with the lifecycleState.
        Typically contains additional displayable text


        :return: The lifecycle_details of this BackupDestinationSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this BackupDestinationSummary.
        A descriptive text associated with the lifecycleState.
        Typically contains additional displayable text


        :param lifecycle_details: The lifecycle_details of this BackupDestinationSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BackupDestinationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this BackupDestinationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BackupDestinationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this BackupDestinationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BackupDestinationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this BackupDestinationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BackupDestinationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this BackupDestinationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
