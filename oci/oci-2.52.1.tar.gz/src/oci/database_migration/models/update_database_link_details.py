# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDatabaseLinkDetails(object):
    """
    Optional details for updating a network database link from OCI database to on-premise database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDatabaseLinkDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateDatabaseLinkDetails.
        :type name: str

        :param wallet_bucket:
            The value to assign to the wallet_bucket property of this UpdateDatabaseLinkDetails.
        :type wallet_bucket: oci.database_migration.models.UpdateObjectStoreBucket

        """
        self.swagger_types = {
            'name': 'str',
            'wallet_bucket': 'UpdateObjectStoreBucket'
        }

        self.attribute_map = {
            'name': 'name',
            'wallet_bucket': 'walletBucket'
        }

        self._name = None
        self._wallet_bucket = None

    @property
    def name(self):
        """
        Gets the name of this UpdateDatabaseLinkDetails.
        Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.


        :return: The name of this UpdateDatabaseLinkDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateDatabaseLinkDetails.
        Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.


        :param name: The name of this UpdateDatabaseLinkDetails.
        :type: str
        """
        self._name = name

    @property
    def wallet_bucket(self):
        """
        Gets the wallet_bucket of this UpdateDatabaseLinkDetails.

        :return: The wallet_bucket of this UpdateDatabaseLinkDetails.
        :rtype: oci.database_migration.models.UpdateObjectStoreBucket
        """
        return self._wallet_bucket

    @wallet_bucket.setter
    def wallet_bucket(self, wallet_bucket):
        """
        Sets the wallet_bucket of this UpdateDatabaseLinkDetails.

        :param wallet_bucket: The wallet_bucket of this UpdateDatabaseLinkDetails.
        :type: oci.database_migration.models.UpdateObjectStoreBucket
        """
        self._wallet_bucket = wallet_bucket

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
