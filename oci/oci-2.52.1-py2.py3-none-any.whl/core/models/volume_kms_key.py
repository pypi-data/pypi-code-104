# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeKmsKey(object):
    """
    The Key Management master encryption key associated with this volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeKmsKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this VolumeKmsKey.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'kms_key_id': 'str'
        }

        self.attribute_map = {
            'kms_key_id': 'kmsKeyId'
        }

        self._kms_key_id = None

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this VolumeKmsKey.
        The OCID of the Key Management key assigned to this volume. If the volume is not using Key Management, then the `kmsKeyId` will be a null string.


        :return: The kms_key_id of this VolumeKmsKey.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this VolumeKmsKey.
        The OCID of the Key Management key assigned to this volume. If the volume is not using Key Management, then the `kmsKeyId` will be a null string.


        :param kms_key_id: The kms_key_id of this VolumeKmsKey.
        :type: str
        """
        self._kms_key_id = kms_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
