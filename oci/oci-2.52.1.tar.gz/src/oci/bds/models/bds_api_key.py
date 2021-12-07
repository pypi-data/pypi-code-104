# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BdsApiKey(object):
    """
    The API key information.
    """

    #: A constant which can be used with the lifecycle_state property of a BdsApiKey.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a BdsApiKey.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BdsApiKey.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a BdsApiKey.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a BdsApiKey.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new BdsApiKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BdsApiKey.
        :type id: str

        :param user_id:
            The value to assign to the user_id property of this BdsApiKey.
        :type user_id: str

        :param key_alias:
            The value to assign to the key_alias property of this BdsApiKey.
        :type key_alias: str

        :param default_region:
            The value to assign to the default_region property of this BdsApiKey.
        :type default_region: str

        :param tenant_id:
            The value to assign to the tenant_id property of this BdsApiKey.
        :type tenant_id: str

        :param fingerprint:
            The value to assign to the fingerprint property of this BdsApiKey.
        :type fingerprint: str

        :param pemfilepath:
            The value to assign to the pemfilepath property of this BdsApiKey.
        :type pemfilepath: str

        :param time_created:
            The value to assign to the time_created property of this BdsApiKey.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BdsApiKey.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'key_alias': 'str',
            'default_region': 'str',
            'tenant_id': 'str',
            'fingerprint': 'str',
            'pemfilepath': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'key_alias': 'keyAlias',
            'default_region': 'defaultRegion',
            'tenant_id': 'tenantId',
            'fingerprint': 'fingerprint',
            'pemfilepath': 'pemfilepath',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._user_id = None
        self._key_alias = None
        self._default_region = None
        self._tenant_id = None
        self._fingerprint = None
        self._pemfilepath = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BdsApiKey.
        Identifier of the user's API key.


        :return: The id of this BdsApiKey.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BdsApiKey.
        Identifier of the user's API key.


        :param id: The id of this BdsApiKey.
        :type: str
        """
        self._id = id

    @property
    def user_id(self):
        """
        **[Required]** Gets the user_id of this BdsApiKey.
        The user OCID for which this API key was created.


        :return: The user_id of this BdsApiKey.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this BdsApiKey.
        The user OCID for which this API key was created.


        :param user_id: The user_id of this BdsApiKey.
        :type: str
        """
        self._user_id = user_id

    @property
    def key_alias(self):
        """
        **[Required]** Gets the key_alias of this BdsApiKey.
        User friendly identifier used to uniquely differentiate between different API keys.
        Only ASCII alphanumeric characters with no spaces allowed.


        :return: The key_alias of this BdsApiKey.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        """
        Sets the key_alias of this BdsApiKey.
        User friendly identifier used to uniquely differentiate between different API keys.
        Only ASCII alphanumeric characters with no spaces allowed.


        :param key_alias: The key_alias of this BdsApiKey.
        :type: str
        """
        self._key_alias = key_alias

    @property
    def default_region(self):
        """
        **[Required]** Gets the default_region of this BdsApiKey.
        The name of the region to establish the Object Storage endpoint. Example us-phoenix-1 .


        :return: The default_region of this BdsApiKey.
        :rtype: str
        """
        return self._default_region

    @default_region.setter
    def default_region(self, default_region):
        """
        Sets the default_region of this BdsApiKey.
        The name of the region to establish the Object Storage endpoint. Example us-phoenix-1 .


        :param default_region: The default_region of this BdsApiKey.
        :type: str
        """
        self._default_region = default_region

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this BdsApiKey.
        The OCID of your tenancy.


        :return: The tenant_id of this BdsApiKey.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this BdsApiKey.
        The OCID of your tenancy.


        :param tenant_id: The tenant_id of this BdsApiKey.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def fingerprint(self):
        """
        **[Required]** Gets the fingerprint of this BdsApiKey.
        The fingerprint that corresponds to the public API key requested.


        :return: The fingerprint of this BdsApiKey.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this BdsApiKey.
        The fingerprint that corresponds to the public API key requested.


        :param fingerprint: The fingerprint of this BdsApiKey.
        :type: str
        """
        self._fingerprint = fingerprint

    @property
    def pemfilepath(self):
        """
        **[Required]** Gets the pemfilepath of this BdsApiKey.
        The full path and file name of the private key used for authentication. This location will be automatically selected
        on the BDS local file system.


        :return: The pemfilepath of this BdsApiKey.
        :rtype: str
        """
        return self._pemfilepath

    @pemfilepath.setter
    def pemfilepath(self, pemfilepath):
        """
        Sets the pemfilepath of this BdsApiKey.
        The full path and file name of the private key used for authentication. This location will be automatically selected
        on the BDS local file system.


        :param pemfilepath: The pemfilepath of this BdsApiKey.
        :type: str
        """
        self._pemfilepath = pemfilepath

    @property
    def time_created(self):
        """
        Gets the time_created of this BdsApiKey.
        The time the API key was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_created of this BdsApiKey.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BdsApiKey.
        The time the API key was created, shown as an RFC 3339 formatted datetime string.


        :param time_created: The time_created of this BdsApiKey.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BdsApiKey.
        The state of the key.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BdsApiKey.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BdsApiKey.
        The state of the key.


        :param lifecycle_state: The lifecycle_state of this BdsApiKey.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
