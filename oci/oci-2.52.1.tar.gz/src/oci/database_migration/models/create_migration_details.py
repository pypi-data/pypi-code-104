# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMigrationDetails(object):
    """
    Create Migration resource parameters.
    """

    #: A constant which can be used with the type property of a CreateMigrationDetails.
    #: This constant has a value of "ONLINE"
    TYPE_ONLINE = "ONLINE"

    #: A constant which can be used with the type property of a CreateMigrationDetails.
    #: This constant has a value of "OFFLINE"
    TYPE_OFFLINE = "OFFLINE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMigrationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateMigrationDetails.
            Allowed values for this property are: "ONLINE", "OFFLINE"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this CreateMigrationDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMigrationDetails.
        :type compartment_id: str

        :param agent_id:
            The value to assign to the agent_id property of this CreateMigrationDetails.
        :type agent_id: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this CreateMigrationDetails.
        :type source_database_connection_id: str

        :param source_container_database_connection_id:
            The value to assign to the source_container_database_connection_id property of this CreateMigrationDetails.
        :type source_container_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this CreateMigrationDetails.
        :type target_database_connection_id: str

        :param data_transfer_medium_details:
            The value to assign to the data_transfer_medium_details property of this CreateMigrationDetails.
        :type data_transfer_medium_details: oci.database_migration.models.CreateDataTransferMediumDetails

        :param dump_transfer_details:
            The value to assign to the dump_transfer_details property of this CreateMigrationDetails.
        :type dump_transfer_details: oci.database_migration.models.CreateDumpTransferDetails

        :param datapump_settings:
            The value to assign to the datapump_settings property of this CreateMigrationDetails.
        :type datapump_settings: oci.database_migration.models.CreateDataPumpSettings

        :param advisor_settings:
            The value to assign to the advisor_settings property of this CreateMigrationDetails.
        :type advisor_settings: oci.database_migration.models.CreateAdvisorSettings

        :param exclude_objects:
            The value to assign to the exclude_objects property of this CreateMigrationDetails.
        :type exclude_objects: list[oci.database_migration.models.DatabaseObject]

        :param include_objects:
            The value to assign to the include_objects property of this CreateMigrationDetails.
        :type include_objects: list[oci.database_migration.models.DatabaseObject]

        :param golden_gate_details:
            The value to assign to the golden_gate_details property of this CreateMigrationDetails.
        :type golden_gate_details: oci.database_migration.models.CreateGoldenGateDetails

        :param vault_details:
            The value to assign to the vault_details property of this CreateMigrationDetails.
        :type vault_details: oci.database_migration.models.CreateVaultDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMigrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMigrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'agent_id': 'str',
            'source_database_connection_id': 'str',
            'source_container_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'data_transfer_medium_details': 'CreateDataTransferMediumDetails',
            'dump_transfer_details': 'CreateDumpTransferDetails',
            'datapump_settings': 'CreateDataPumpSettings',
            'advisor_settings': 'CreateAdvisorSettings',
            'exclude_objects': 'list[DatabaseObject]',
            'include_objects': 'list[DatabaseObject]',
            'golden_gate_details': 'CreateGoldenGateDetails',
            'vault_details': 'CreateVaultDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'agent_id': 'agentId',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'source_container_database_connection_id': 'sourceContainerDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'data_transfer_medium_details': 'dataTransferMediumDetails',
            'dump_transfer_details': 'dumpTransferDetails',
            'datapump_settings': 'datapumpSettings',
            'advisor_settings': 'advisorSettings',
            'exclude_objects': 'excludeObjects',
            'include_objects': 'includeObjects',
            'golden_gate_details': 'goldenGateDetails',
            'vault_details': 'vaultDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._type = None
        self._display_name = None
        self._compartment_id = None
        self._agent_id = None
        self._source_database_connection_id = None
        self._source_container_database_connection_id = None
        self._target_database_connection_id = None
        self._data_transfer_medium_details = None
        self._dump_transfer_details = None
        self._datapump_settings = None
        self._advisor_settings = None
        self._exclude_objects = None
        self._include_objects = None
        self._golden_gate_details = None
        self._vault_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateMigrationDetails.
        Migration type.

        Allowed values for this property are: "ONLINE", "OFFLINE"


        :return: The type of this CreateMigrationDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateMigrationDetails.
        Migration type.


        :param type: The type of this CreateMigrationDetails.
        :type: str
        """
        allowed_values = ["ONLINE", "OFFLINE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMigrationDetails.
        Migration Display Name


        :return: The display_name of this CreateMigrationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMigrationDetails.
        Migration Display Name


        :param display_name: The display_name of this CreateMigrationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMigrationDetails.
        OCID of the compartment


        :return: The compartment_id of this CreateMigrationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMigrationDetails.
        OCID of the compartment


        :param compartment_id: The compartment_id of this CreateMigrationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def agent_id(self):
        """
        Gets the agent_id of this CreateMigrationDetails.
        The OCID of the registered ODMS Agent. Only valid for Offline Logical Migrations.


        :return: The agent_id of this CreateMigrationDetails.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this CreateMigrationDetails.
        The OCID of the registered ODMS Agent. Only valid for Offline Logical Migrations.


        :param agent_id: The agent_id of this CreateMigrationDetails.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def source_database_connection_id(self):
        """
        **[Required]** Gets the source_database_connection_id of this CreateMigrationDetails.
        The OCID of the Source Database Connection.


        :return: The source_database_connection_id of this CreateMigrationDetails.
        :rtype: str
        """
        return self._source_database_connection_id

    @source_database_connection_id.setter
    def source_database_connection_id(self, source_database_connection_id):
        """
        Sets the source_database_connection_id of this CreateMigrationDetails.
        The OCID of the Source Database Connection.


        :param source_database_connection_id: The source_database_connection_id of this CreateMigrationDetails.
        :type: str
        """
        self._source_database_connection_id = source_database_connection_id

    @property
    def source_container_database_connection_id(self):
        """
        Gets the source_container_database_connection_id of this CreateMigrationDetails.
        The OCID of the Source Container Database Connection. Only used for Online migrations.
        Only Connections of type Non-Autonomous can be used as source container databases.


        :return: The source_container_database_connection_id of this CreateMigrationDetails.
        :rtype: str
        """
        return self._source_container_database_connection_id

    @source_container_database_connection_id.setter
    def source_container_database_connection_id(self, source_container_database_connection_id):
        """
        Sets the source_container_database_connection_id of this CreateMigrationDetails.
        The OCID of the Source Container Database Connection. Only used for Online migrations.
        Only Connections of type Non-Autonomous can be used as source container databases.


        :param source_container_database_connection_id: The source_container_database_connection_id of this CreateMigrationDetails.
        :type: str
        """
        self._source_container_database_connection_id = source_container_database_connection_id

    @property
    def target_database_connection_id(self):
        """
        **[Required]** Gets the target_database_connection_id of this CreateMigrationDetails.
        The OCID of the Target Database Connection.


        :return: The target_database_connection_id of this CreateMigrationDetails.
        :rtype: str
        """
        return self._target_database_connection_id

    @target_database_connection_id.setter
    def target_database_connection_id(self, target_database_connection_id):
        """
        Sets the target_database_connection_id of this CreateMigrationDetails.
        The OCID of the Target Database Connection.


        :param target_database_connection_id: The target_database_connection_id of this CreateMigrationDetails.
        :type: str
        """
        self._target_database_connection_id = target_database_connection_id

    @property
    def data_transfer_medium_details(self):
        """
        Gets the data_transfer_medium_details of this CreateMigrationDetails.

        :return: The data_transfer_medium_details of this CreateMigrationDetails.
        :rtype: oci.database_migration.models.CreateDataTransferMediumDetails
        """
        return self._data_transfer_medium_details

    @data_transfer_medium_details.setter
    def data_transfer_medium_details(self, data_transfer_medium_details):
        """
        Sets the data_transfer_medium_details of this CreateMigrationDetails.

        :param data_transfer_medium_details: The data_transfer_medium_details of this CreateMigrationDetails.
        :type: oci.database_migration.models.CreateDataTransferMediumDetails
        """
        self._data_transfer_medium_details = data_transfer_medium_details

    @property
    def dump_transfer_details(self):
        """
        Gets the dump_transfer_details of this CreateMigrationDetails.

        :return: The dump_transfer_details of this CreateMigrationDetails.
        :rtype: oci.database_migration.models.CreateDumpTransferDetails
        """
        return self._dump_transfer_details

    @dump_transfer_details.setter
    def dump_transfer_details(self, dump_transfer_details):
        """
        Sets the dump_transfer_details of this CreateMigrationDetails.

        :param dump_transfer_details: The dump_transfer_details of this CreateMigrationDetails.
        :type: oci.database_migration.models.CreateDumpTransferDetails
        """
        self._dump_transfer_details = dump_transfer_details

    @property
    def datapump_settings(self):
        """
        Gets the datapump_settings of this CreateMigrationDetails.

        :return: The datapump_settings of this CreateMigrationDetails.
        :rtype: oci.database_migration.models.CreateDataPumpSettings
        """
        return self._datapump_settings

    @datapump_settings.setter
    def datapump_settings(self, datapump_settings):
        """
        Sets the datapump_settings of this CreateMigrationDetails.

        :param datapump_settings: The datapump_settings of this CreateMigrationDetails.
        :type: oci.database_migration.models.CreateDataPumpSettings
        """
        self._datapump_settings = datapump_settings

    @property
    def advisor_settings(self):
        """
        Gets the advisor_settings of this CreateMigrationDetails.

        :return: The advisor_settings of this CreateMigrationDetails.
        :rtype: oci.database_migration.models.CreateAdvisorSettings
        """
        return self._advisor_settings

    @advisor_settings.setter
    def advisor_settings(self, advisor_settings):
        """
        Sets the advisor_settings of this CreateMigrationDetails.

        :param advisor_settings: The advisor_settings of this CreateMigrationDetails.
        :type: oci.database_migration.models.CreateAdvisorSettings
        """
        self._advisor_settings = advisor_settings

    @property
    def exclude_objects(self):
        """
        Gets the exclude_objects of this CreateMigrationDetails.
        Database objects to exclude from migration, cannot be specified alongside 'includeObjects'


        :return: The exclude_objects of this CreateMigrationDetails.
        :rtype: list[oci.database_migration.models.DatabaseObject]
        """
        return self._exclude_objects

    @exclude_objects.setter
    def exclude_objects(self, exclude_objects):
        """
        Sets the exclude_objects of this CreateMigrationDetails.
        Database objects to exclude from migration, cannot be specified alongside 'includeObjects'


        :param exclude_objects: The exclude_objects of this CreateMigrationDetails.
        :type: list[oci.database_migration.models.DatabaseObject]
        """
        self._exclude_objects = exclude_objects

    @property
    def include_objects(self):
        """
        Gets the include_objects of this CreateMigrationDetails.
        Database objects to include from migration, cannot be specified alongside 'excludeObjects'


        :return: The include_objects of this CreateMigrationDetails.
        :rtype: list[oci.database_migration.models.DatabaseObject]
        """
        return self._include_objects

    @include_objects.setter
    def include_objects(self, include_objects):
        """
        Sets the include_objects of this CreateMigrationDetails.
        Database objects to include from migration, cannot be specified alongside 'excludeObjects'


        :param include_objects: The include_objects of this CreateMigrationDetails.
        :type: list[oci.database_migration.models.DatabaseObject]
        """
        self._include_objects = include_objects

    @property
    def golden_gate_details(self):
        """
        Gets the golden_gate_details of this CreateMigrationDetails.

        :return: The golden_gate_details of this CreateMigrationDetails.
        :rtype: oci.database_migration.models.CreateGoldenGateDetails
        """
        return self._golden_gate_details

    @golden_gate_details.setter
    def golden_gate_details(self, golden_gate_details):
        """
        Sets the golden_gate_details of this CreateMigrationDetails.

        :param golden_gate_details: The golden_gate_details of this CreateMigrationDetails.
        :type: oci.database_migration.models.CreateGoldenGateDetails
        """
        self._golden_gate_details = golden_gate_details

    @property
    def vault_details(self):
        """
        Gets the vault_details of this CreateMigrationDetails.

        :return: The vault_details of this CreateMigrationDetails.
        :rtype: oci.database_migration.models.CreateVaultDetails
        """
        return self._vault_details

    @vault_details.setter
    def vault_details(self, vault_details):
        """
        Sets the vault_details of this CreateMigrationDetails.

        :param vault_details: The vault_details of this CreateMigrationDetails.
        :type: oci.database_migration.models.CreateVaultDetails
        """
        self._vault_details = vault_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMigrationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMigrationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMigrationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMigrationDetails.
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
