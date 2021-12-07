# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeploymentBackupSummary(object):
    """
    The summary of the Backup.
    """

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a DeploymentBackupSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the backup_type property of a DeploymentBackupSummary.
    #: This constant has a value of "INCREMENTAL"
    BACKUP_TYPE_INCREMENTAL = "INCREMENTAL"

    #: A constant which can be used with the backup_type property of a DeploymentBackupSummary.
    #: This constant has a value of "FULL"
    BACKUP_TYPE_FULL = "FULL"

    def __init__(self, **kwargs):
        """
        Initializes a new DeploymentBackupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DeploymentBackupSummary.
        :type id: str

        :param deployment_id:
            The value to assign to the deployment_id property of this DeploymentBackupSummary.
        :type deployment_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeploymentBackupSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DeploymentBackupSummary.
        :type display_name: str

        :param is_automatic:
            The value to assign to the is_automatic property of this DeploymentBackupSummary.
        :type is_automatic: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeploymentBackupSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeploymentBackupSummary.
        :type lifecycle_details: str

        :param time_of_backup:
            The value to assign to the time_of_backup property of this DeploymentBackupSummary.
        :type time_of_backup: datetime

        :param time_backup_finished:
            The value to assign to the time_backup_finished property of this DeploymentBackupSummary.
        :type time_backup_finished: datetime

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this DeploymentBackupSummary.
        :type size_in_bytes: float

        :param backup_type:
            The value to assign to the backup_type property of this DeploymentBackupSummary.
            Allowed values for this property are: "INCREMENTAL", "FULL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type backup_type: str

        :param ogg_version:
            The value to assign to the ogg_version property of this DeploymentBackupSummary.
        :type ogg_version: str

        :param namespace_name:
            The value to assign to the namespace_name property of this DeploymentBackupSummary.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this DeploymentBackupSummary.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this DeploymentBackupSummary.
        :type object_name: str

        :param time_created:
            The value to assign to the time_created property of this DeploymentBackupSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeploymentBackupSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeploymentBackupSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeploymentBackupSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeploymentBackupSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'deployment_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'is_automatic': 'bool',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_of_backup': 'datetime',
            'time_backup_finished': 'datetime',
            'size_in_bytes': 'float',
            'backup_type': 'str',
            'ogg_version': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'deployment_id': 'deploymentId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'is_automatic': 'isAutomatic',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_of_backup': 'timeOfBackup',
            'time_backup_finished': 'timeBackupFinished',
            'size_in_bytes': 'sizeInBytes',
            'backup_type': 'backupType',
            'ogg_version': 'oggVersion',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._deployment_id = None
        self._compartment_id = None
        self._display_name = None
        self._is_automatic = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_of_backup = None
        self._time_backup_finished = None
        self._size_in_bytes = None
        self._backup_type = None
        self._ogg_version = None
        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DeploymentBackupSummary.
        The `OCID`__ of the backup being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeploymentBackupSummary.
        The `OCID`__ of the backup being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DeploymentBackupSummary.
        :type: str
        """
        self._id = id

    @property
    def deployment_id(self):
        """
        **[Required]** Gets the deployment_id of this DeploymentBackupSummary.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this DeploymentBackupSummary.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this DeploymentBackupSummary.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DeploymentBackupSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DeploymentBackupSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DeploymentBackupSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DeploymentBackupSummary.
        An object's Display Name.


        :return: The display_name of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeploymentBackupSummary.
        An object's Display Name.


        :param display_name: The display_name of this DeploymentBackupSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_automatic(self):
        """
        Gets the is_automatic of this DeploymentBackupSummary.
        True if this object is automatically created


        :return: The is_automatic of this DeploymentBackupSummary.
        :rtype: bool
        """
        return self._is_automatic

    @is_automatic.setter
    def is_automatic(self, is_automatic):
        """
        Sets the is_automatic of this DeploymentBackupSummary.
        True if this object is automatically created


        :param is_automatic: The is_automatic of this DeploymentBackupSummary.
        :type: bool
        """
        self._is_automatic = is_automatic

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DeploymentBackupSummary.
        Possible lifecycle states.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DeploymentBackupSummary.
        Possible lifecycle states.


        :param lifecycle_state: The lifecycle_state of this DeploymentBackupSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DeploymentBackupSummary.
        Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DeploymentBackupSummary.
        Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this DeploymentBackupSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_of_backup(self):
        """
        Gets the time_of_backup of this DeploymentBackupSummary.
        The time of the resource backup. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_backup of this DeploymentBackupSummary.
        :rtype: datetime
        """
        return self._time_of_backup

    @time_of_backup.setter
    def time_of_backup(self, time_of_backup):
        """
        Sets the time_of_backup of this DeploymentBackupSummary.
        The time of the resource backup. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_backup: The time_of_backup of this DeploymentBackupSummary.
        :type: datetime
        """
        self._time_of_backup = time_of_backup

    @property
    def time_backup_finished(self):
        """
        Gets the time_backup_finished of this DeploymentBackupSummary.
        The time of the resource backup finish. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_backup_finished of this DeploymentBackupSummary.
        :rtype: datetime
        """
        return self._time_backup_finished

    @time_backup_finished.setter
    def time_backup_finished(self, time_backup_finished):
        """
        Sets the time_backup_finished of this DeploymentBackupSummary.
        The time of the resource backup finish. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_backup_finished: The time_backup_finished of this DeploymentBackupSummary.
        :type: datetime
        """
        self._time_backup_finished = time_backup_finished

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this DeploymentBackupSummary.
        The size of the backup stored in object storage (in bytes)


        :return: The size_in_bytes of this DeploymentBackupSummary.
        :rtype: float
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this DeploymentBackupSummary.
        The size of the backup stored in object storage (in bytes)


        :param size_in_bytes: The size_in_bytes of this DeploymentBackupSummary.
        :type: float
        """
        self._size_in_bytes = size_in_bytes

    @property
    def backup_type(self):
        """
        Gets the backup_type of this DeploymentBackupSummary.
        Possible Deployment backup types.

        Allowed values for this property are: "INCREMENTAL", "FULL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The backup_type of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this DeploymentBackupSummary.
        Possible Deployment backup types.


        :param backup_type: The backup_type of this DeploymentBackupSummary.
        :type: str
        """
        allowed_values = ["INCREMENTAL", "FULL"]
        if not value_allowed_none_or_none_sentinel(backup_type, allowed_values):
            backup_type = 'UNKNOWN_ENUM_VALUE'
        self._backup_type = backup_type

    @property
    def ogg_version(self):
        """
        **[Required]** Gets the ogg_version of this DeploymentBackupSummary.
        Version of OGG


        :return: The ogg_version of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._ogg_version

    @ogg_version.setter
    def ogg_version(self, ogg_version):
        """
        Sets the ogg_version of this DeploymentBackupSummary.
        Version of OGG


        :param ogg_version: The ogg_version of this DeploymentBackupSummary.
        :type: str
        """
        self._ogg_version = ogg_version

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this DeploymentBackupSummary.
        Name of namespace that serves as a container for all of your buckets


        :return: The namespace_name of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this DeploymentBackupSummary.
        Name of namespace that serves as a container for all of your buckets


        :param namespace_name: The namespace_name of this DeploymentBackupSummary.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this DeploymentBackupSummary.
        Name of the bucket where the object is to be uploaded in the object storage


        :return: The bucket_name of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this DeploymentBackupSummary.
        Name of the bucket where the object is to be uploaded in the object storage


        :param bucket_name: The bucket_name of this DeploymentBackupSummary.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        Gets the object_name of this DeploymentBackupSummary.
        Name of the object to be uploaded to object storage


        :return: The object_name of this DeploymentBackupSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this DeploymentBackupSummary.
        Name of the object to be uploaded to object storage


        :param object_name: The object_name of this DeploymentBackupSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def time_created(self):
        """
        Gets the time_created of this DeploymentBackupSummary.
        The time the resource was created. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DeploymentBackupSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DeploymentBackupSummary.
        The time the resource was created. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DeploymentBackupSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DeploymentBackupSummary.
        The time the resource was last updated. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DeploymentBackupSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DeploymentBackupSummary.
        The time the resource was last updated. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DeploymentBackupSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DeploymentBackupSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DeploymentBackupSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DeploymentBackupSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DeploymentBackupSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DeploymentBackupSummary.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DeploymentBackupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DeploymentBackupSummary.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DeploymentBackupSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DeploymentBackupSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DeploymentBackupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DeploymentBackupSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DeploymentBackupSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
