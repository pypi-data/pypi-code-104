# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .snapshot_export_details import SnapshotExportDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageSnapshotExportDetails(SnapshotExportDetails):
    """
    Specifies where to output the export in Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageSnapshotExportDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service.models.ObjectStorageSnapshotExportDetails.export_type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_type:
            The value to assign to the export_type property of this ObjectStorageSnapshotExportDetails.
            Allowed values for this property are: "OBJECT_STORAGE"
        :type export_type: str

        :param namespace:
            The value to assign to the namespace property of this ObjectStorageSnapshotExportDetails.
        :type namespace: str

        :param bucket:
            The value to assign to the bucket property of this ObjectStorageSnapshotExportDetails.
        :type bucket: str

        :param prefix:
            The value to assign to the prefix property of this ObjectStorageSnapshotExportDetails.
        :type prefix: str

        """
        self.swagger_types = {
            'export_type': 'str',
            'namespace': 'str',
            'bucket': 'str',
            'prefix': 'str'
        }

        self.attribute_map = {
            'export_type': 'exportType',
            'namespace': 'namespace',
            'bucket': 'bucket',
            'prefix': 'prefix'
        }

        self._export_type = None
        self._namespace = None
        self._bucket = None
        self._prefix = None
        self._export_type = 'OBJECT_STORAGE'

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this ObjectStorageSnapshotExportDetails.
        Bucket namespace name


        :return: The namespace of this ObjectStorageSnapshotExportDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ObjectStorageSnapshotExportDetails.
        Bucket namespace name


        :param namespace: The namespace of this ObjectStorageSnapshotExportDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket(self):
        """
        **[Required]** Gets the bucket of this ObjectStorageSnapshotExportDetails.
        Bucket name


        :return: The bucket of this ObjectStorageSnapshotExportDetails.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this ObjectStorageSnapshotExportDetails.
        Bucket name


        :param bucket: The bucket of this ObjectStorageSnapshotExportDetails.
        :type: str
        """
        self._bucket = bucket

    @property
    def prefix(self):
        """
        Gets the prefix of this ObjectStorageSnapshotExportDetails.
        Object path prefix to put snapshot file(s)


        :return: The prefix of this ObjectStorageSnapshotExportDetails.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this ObjectStorageSnapshotExportDetails.
        Object path prefix to put snapshot file(s)


        :param prefix: The prefix of this ObjectStorageSnapshotExportDetails.
        :type: str
        """
        self._prefix = prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
