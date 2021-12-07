# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmClusterSummary(object):
    """
    Details of the Exadata Cloud@Customer VM cluster.
    """

    #: A constant which can be used with the lifecycle_state property of a VmClusterSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a VmClusterSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a VmClusterSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a VmClusterSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a VmClusterSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a VmClusterSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a VmClusterSummary.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the license_model property of a VmClusterSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a VmClusterSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new VmClusterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VmClusterSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VmClusterSummary.
        :type compartment_id: str

        :param last_patch_history_entry_id:
            The value to assign to the last_patch_history_entry_id property of this VmClusterSummary.
        :type last_patch_history_entry_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmClusterSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this VmClusterSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this VmClusterSummary.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VmClusterSummary.
        :type lifecycle_details: str

        :param time_zone:
            The value to assign to the time_zone property of this VmClusterSummary.
        :type time_zone: str

        :param is_local_backup_enabled:
            The value to assign to the is_local_backup_enabled property of this VmClusterSummary.
        :type is_local_backup_enabled: bool

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this VmClusterSummary.
        :type exadata_infrastructure_id: str

        :param is_sparse_diskgroup_enabled:
            The value to assign to the is_sparse_diskgroup_enabled property of this VmClusterSummary.
        :type is_sparse_diskgroup_enabled: bool

        :param vm_cluster_network_id:
            The value to assign to the vm_cluster_network_id property of this VmClusterSummary.
        :type vm_cluster_network_id: str

        :param cpus_enabled:
            The value to assign to the cpus_enabled property of this VmClusterSummary.
        :type cpus_enabled: int

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this VmClusterSummary.
        :type memory_size_in_gbs: int

        :param db_node_storage_size_in_gbs:
            The value to assign to the db_node_storage_size_in_gbs property of this VmClusterSummary.
        :type db_node_storage_size_in_gbs: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this VmClusterSummary.
        :type data_storage_size_in_tbs: float

        :param shape:
            The value to assign to the shape property of this VmClusterSummary.
        :type shape: str

        :param gi_version:
            The value to assign to the gi_version property of this VmClusterSummary.
        :type gi_version: str

        :param system_version:
            The value to assign to the system_version property of this VmClusterSummary.
        :type system_version: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this VmClusterSummary.
        :type ssh_public_keys: list[str]

        :param license_model:
            The value to assign to the license_model property of this VmClusterSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param db_servers:
            The value to assign to the db_servers property of this VmClusterSummary.
        :type db_servers: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VmClusterSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VmClusterSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'last_patch_history_entry_id': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'time_zone': 'str',
            'is_local_backup_enabled': 'bool',
            'exadata_infrastructure_id': 'str',
            'is_sparse_diskgroup_enabled': 'bool',
            'vm_cluster_network_id': 'str',
            'cpus_enabled': 'int',
            'memory_size_in_gbs': 'int',
            'db_node_storage_size_in_gbs': 'int',
            'data_storage_size_in_tbs': 'float',
            'shape': 'str',
            'gi_version': 'str',
            'system_version': 'str',
            'ssh_public_keys': 'list[str]',
            'license_model': 'str',
            'db_servers': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'last_patch_history_entry_id': 'lastPatchHistoryEntryId',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'time_zone': 'timeZone',
            'is_local_backup_enabled': 'isLocalBackupEnabled',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'is_sparse_diskgroup_enabled': 'isSparseDiskgroupEnabled',
            'vm_cluster_network_id': 'vmClusterNetworkId',
            'cpus_enabled': 'cpusEnabled',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'db_node_storage_size_in_gbs': 'dbNodeStorageSizeInGBs',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'shape': 'shape',
            'gi_version': 'giVersion',
            'system_version': 'systemVersion',
            'ssh_public_keys': 'sshPublicKeys',
            'license_model': 'licenseModel',
            'db_servers': 'dbServers',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._last_patch_history_entry_id = None
        self._lifecycle_state = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_details = None
        self._time_zone = None
        self._is_local_backup_enabled = None
        self._exadata_infrastructure_id = None
        self._is_sparse_diskgroup_enabled = None
        self._vm_cluster_network_id = None
        self._cpus_enabled = None
        self._memory_size_in_gbs = None
        self._db_node_storage_size_in_gbs = None
        self._data_storage_size_in_tbs = None
        self._shape = None
        self._gi_version = None
        self._system_version = None
        self._ssh_public_keys = None
        self._license_model = None
        self._db_servers = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this VmClusterSummary.
        The `OCID`__ of the VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this VmClusterSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VmClusterSummary.
        The `OCID`__ of the VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this VmClusterSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VmClusterSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this VmClusterSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VmClusterSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this VmClusterSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def last_patch_history_entry_id(self):
        """
        Gets the last_patch_history_entry_id of this VmClusterSummary.
        The `OCID`__ of the last patch history. This value is updated as soon as a patch operation starts.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_patch_history_entry_id of this VmClusterSummary.
        :rtype: str
        """
        return self._last_patch_history_entry_id

    @last_patch_history_entry_id.setter
    def last_patch_history_entry_id(self, last_patch_history_entry_id):
        """
        Sets the last_patch_history_entry_id of this VmClusterSummary.
        The `OCID`__ of the last patch history. This value is updated as soon as a patch operation starts.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_patch_history_entry_id: The last_patch_history_entry_id of this VmClusterSummary.
        :type: str
        """
        self._last_patch_history_entry_id = last_patch_history_entry_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this VmClusterSummary.
        The current state of the VM cluster.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VmClusterSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VmClusterSummary.
        The current state of the VM cluster.


        :param lifecycle_state: The lifecycle_state of this VmClusterSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        Gets the display_name of this VmClusterSummary.
        The user-friendly name for the Exadata Cloud@Customer VM cluster. The name does not need to be unique.


        :return: The display_name of this VmClusterSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VmClusterSummary.
        The user-friendly name for the Exadata Cloud@Customer VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this VmClusterSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this VmClusterSummary.
        The date and time that the VM cluster was created.


        :return: The time_created of this VmClusterSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VmClusterSummary.
        The date and time that the VM cluster was created.


        :param time_created: The time_created of this VmClusterSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this VmClusterSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this VmClusterSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this VmClusterSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this VmClusterSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_zone(self):
        """
        Gets the time_zone of this VmClusterSummary.
        The time zone of the Exadata infrastructure. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this VmClusterSummary.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this VmClusterSummary.
        The time zone of the Exadata infrastructure. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this VmClusterSummary.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def is_local_backup_enabled(self):
        """
        Gets the is_local_backup_enabled of this VmClusterSummary.
        If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not available in the VM cluster.


        :return: The is_local_backup_enabled of this VmClusterSummary.
        :rtype: bool
        """
        return self._is_local_backup_enabled

    @is_local_backup_enabled.setter
    def is_local_backup_enabled(self, is_local_backup_enabled):
        """
        Sets the is_local_backup_enabled of this VmClusterSummary.
        If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not available in the VM cluster.


        :param is_local_backup_enabled: The is_local_backup_enabled of this VmClusterSummary.
        :type: bool
        """
        self._is_local_backup_enabled = is_local_backup_enabled

    @property
    def exadata_infrastructure_id(self):
        """
        Gets the exadata_infrastructure_id of this VmClusterSummary.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this VmClusterSummary.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this VmClusterSummary.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this VmClusterSummary.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def is_sparse_diskgroup_enabled(self):
        """
        Gets the is_sparse_diskgroup_enabled of this VmClusterSummary.
        If true, sparse disk group is configured for the VM cluster. If false, sparse disk group is not created.


        :return: The is_sparse_diskgroup_enabled of this VmClusterSummary.
        :rtype: bool
        """
        return self._is_sparse_diskgroup_enabled

    @is_sparse_diskgroup_enabled.setter
    def is_sparse_diskgroup_enabled(self, is_sparse_diskgroup_enabled):
        """
        Sets the is_sparse_diskgroup_enabled of this VmClusterSummary.
        If true, sparse disk group is configured for the VM cluster. If false, sparse disk group is not created.


        :param is_sparse_diskgroup_enabled: The is_sparse_diskgroup_enabled of this VmClusterSummary.
        :type: bool
        """
        self._is_sparse_diskgroup_enabled = is_sparse_diskgroup_enabled

    @property
    def vm_cluster_network_id(self):
        """
        Gets the vm_cluster_network_id of this VmClusterSummary.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_network_id of this VmClusterSummary.
        :rtype: str
        """
        return self._vm_cluster_network_id

    @vm_cluster_network_id.setter
    def vm_cluster_network_id(self, vm_cluster_network_id):
        """
        Sets the vm_cluster_network_id of this VmClusterSummary.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_network_id: The vm_cluster_network_id of this VmClusterSummary.
        :type: str
        """
        self._vm_cluster_network_id = vm_cluster_network_id

    @property
    def cpus_enabled(self):
        """
        Gets the cpus_enabled of this VmClusterSummary.
        The number of enabled CPU cores.


        :return: The cpus_enabled of this VmClusterSummary.
        :rtype: int
        """
        return self._cpus_enabled

    @cpus_enabled.setter
    def cpus_enabled(self, cpus_enabled):
        """
        Sets the cpus_enabled of this VmClusterSummary.
        The number of enabled CPU cores.


        :param cpus_enabled: The cpus_enabled of this VmClusterSummary.
        :type: int
        """
        self._cpus_enabled = cpus_enabled

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this VmClusterSummary.
        The memory allocated in GBs.


        :return: The memory_size_in_gbs of this VmClusterSummary.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this VmClusterSummary.
        The memory allocated in GBs.


        :param memory_size_in_gbs: The memory_size_in_gbs of this VmClusterSummary.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def db_node_storage_size_in_gbs(self):
        """
        Gets the db_node_storage_size_in_gbs of this VmClusterSummary.
        The local node storage allocated in GBs.


        :return: The db_node_storage_size_in_gbs of this VmClusterSummary.
        :rtype: int
        """
        return self._db_node_storage_size_in_gbs

    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, db_node_storage_size_in_gbs):
        """
        Sets the db_node_storage_size_in_gbs of this VmClusterSummary.
        The local node storage allocated in GBs.


        :param db_node_storage_size_in_gbs: The db_node_storage_size_in_gbs of this VmClusterSummary.
        :type: int
        """
        self._db_node_storage_size_in_gbs = db_node_storage_size_in_gbs

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this VmClusterSummary.
        Size, in terabytes, of the DATA disk group.


        :return: The data_storage_size_in_tbs of this VmClusterSummary.
        :rtype: float
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this VmClusterSummary.
        Size, in terabytes, of the DATA disk group.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this VmClusterSummary.
        :type: float
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def shape(self):
        """
        Gets the shape of this VmClusterSummary.
        The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.


        :return: The shape of this VmClusterSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this VmClusterSummary.
        The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.


        :param shape: The shape of this VmClusterSummary.
        :type: str
        """
        self._shape = shape

    @property
    def gi_version(self):
        """
        Gets the gi_version of this VmClusterSummary.
        The Oracle Grid Infrastructure software version for the VM cluster.


        :return: The gi_version of this VmClusterSummary.
        :rtype: str
        """
        return self._gi_version

    @gi_version.setter
    def gi_version(self, gi_version):
        """
        Sets the gi_version of this VmClusterSummary.
        The Oracle Grid Infrastructure software version for the VM cluster.


        :param gi_version: The gi_version of this VmClusterSummary.
        :type: str
        """
        self._gi_version = gi_version

    @property
    def system_version(self):
        """
        Gets the system_version of this VmClusterSummary.
        Operating system version of the image.


        :return: The system_version of this VmClusterSummary.
        :rtype: str
        """
        return self._system_version

    @system_version.setter
    def system_version(self, system_version):
        """
        Sets the system_version of this VmClusterSummary.
        Operating system version of the image.


        :param system_version: The system_version of this VmClusterSummary.
        :type: str
        """
        self._system_version = system_version

    @property
    def ssh_public_keys(self):
        """
        Gets the ssh_public_keys of this VmClusterSummary.
        The public key portion of one or more key pairs used for SSH access to the VM cluster.


        :return: The ssh_public_keys of this VmClusterSummary.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this VmClusterSummary.
        The public key portion of one or more key pairs used for SSH access to the VM cluster.


        :param ssh_public_keys: The ssh_public_keys of this VmClusterSummary.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def license_model(self):
        """
        Gets the license_model of this VmClusterSummary.
        The Oracle license model that applies to the VM cluster. The default is LICENSE_INCLUDED.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this VmClusterSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this VmClusterSummary.
        The Oracle license model that applies to the VM cluster. The default is LICENSE_INCLUDED.


        :param license_model: The license_model of this VmClusterSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def db_servers(self):
        """
        Gets the db_servers of this VmClusterSummary.
        The list of Db server.


        :return: The db_servers of this VmClusterSummary.
        :rtype: list[str]
        """
        return self._db_servers

    @db_servers.setter
    def db_servers(self, db_servers):
        """
        Sets the db_servers of this VmClusterSummary.
        The list of Db server.


        :param db_servers: The db_servers of this VmClusterSummary.
        :type: list[str]
        """
        self._db_servers = db_servers

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VmClusterSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VmClusterSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VmClusterSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VmClusterSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VmClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VmClusterSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VmClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VmClusterSummary.
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
