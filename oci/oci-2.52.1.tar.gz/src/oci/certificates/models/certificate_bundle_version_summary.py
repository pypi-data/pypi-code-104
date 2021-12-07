# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateBundleVersionSummary(object):
    """
    The properties of the certificate bundle. Certificate bundle version summary objects do not include the actual contents of the certificate.
    """

    #: A constant which can be used with the stages property of a CertificateBundleVersionSummary.
    #: This constant has a value of "CURRENT"
    STAGES_CURRENT = "CURRENT"

    #: A constant which can be used with the stages property of a CertificateBundleVersionSummary.
    #: This constant has a value of "PENDING"
    STAGES_PENDING = "PENDING"

    #: A constant which can be used with the stages property of a CertificateBundleVersionSummary.
    #: This constant has a value of "LATEST"
    STAGES_LATEST = "LATEST"

    #: A constant which can be used with the stages property of a CertificateBundleVersionSummary.
    #: This constant has a value of "PREVIOUS"
    STAGES_PREVIOUS = "PREVIOUS"

    #: A constant which can be used with the stages property of a CertificateBundleVersionSummary.
    #: This constant has a value of "DEPRECATED"
    STAGES_DEPRECATED = "DEPRECATED"

    #: A constant which can be used with the stages property of a CertificateBundleVersionSummary.
    #: This constant has a value of "FAILED"
    STAGES_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateBundleVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_id:
            The value to assign to the certificate_id property of this CertificateBundleVersionSummary.
        :type certificate_id: str

        :param serial_number:
            The value to assign to the serial_number property of this CertificateBundleVersionSummary.
        :type serial_number: str

        :param version_name:
            The value to assign to the version_name property of this CertificateBundleVersionSummary.
        :type version_name: str

        :param certificate_name:
            The value to assign to the certificate_name property of this CertificateBundleVersionSummary.
        :type certificate_name: str

        :param version_number:
            The value to assign to the version_number property of this CertificateBundleVersionSummary.
        :type version_number: int

        :param time_created:
            The value to assign to the time_created property of this CertificateBundleVersionSummary.
        :type time_created: datetime

        :param validity:
            The value to assign to the validity property of this CertificateBundleVersionSummary.
        :type validity: oci.certificates.models.Validity

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this CertificateBundleVersionSummary.
        :type time_of_deletion: datetime

        :param stages:
            The value to assign to the stages property of this CertificateBundleVersionSummary.
            Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type stages: list[str]

        :param revocation_status:
            The value to assign to the revocation_status property of this CertificateBundleVersionSummary.
        :type revocation_status: oci.certificates.models.RevocationStatus

        """
        self.swagger_types = {
            'certificate_id': 'str',
            'serial_number': 'str',
            'version_name': 'str',
            'certificate_name': 'str',
            'version_number': 'int',
            'time_created': 'datetime',
            'validity': 'Validity',
            'time_of_deletion': 'datetime',
            'stages': 'list[str]',
            'revocation_status': 'RevocationStatus'
        }

        self.attribute_map = {
            'certificate_id': 'certificateId',
            'serial_number': 'serialNumber',
            'version_name': 'versionName',
            'certificate_name': 'certificateName',
            'version_number': 'versionNumber',
            'time_created': 'timeCreated',
            'validity': 'validity',
            'time_of_deletion': 'timeOfDeletion',
            'stages': 'stages',
            'revocation_status': 'revocationStatus'
        }

        self._certificate_id = None
        self._serial_number = None
        self._version_name = None
        self._certificate_name = None
        self._version_number = None
        self._time_created = None
        self._validity = None
        self._time_of_deletion = None
        self._stages = None
        self._revocation_status = None

    @property
    def certificate_id(self):
        """
        **[Required]** Gets the certificate_id of this CertificateBundleVersionSummary.
        The OCID of the certificate.


        :return: The certificate_id of this CertificateBundleVersionSummary.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this CertificateBundleVersionSummary.
        The OCID of the certificate.


        :param certificate_id: The certificate_id of this CertificateBundleVersionSummary.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def serial_number(self):
        """
        Gets the serial_number of this CertificateBundleVersionSummary.
        A unique certificate identifier used in certificate revocation tracking, formatted as octets.
        Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`


        :return: The serial_number of this CertificateBundleVersionSummary.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this CertificateBundleVersionSummary.
        A unique certificate identifier used in certificate revocation tracking, formatted as octets.
        Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`


        :param serial_number: The serial_number of this CertificateBundleVersionSummary.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def version_name(self):
        """
        Gets the version_name of this CertificateBundleVersionSummary.
        The name of the certificate version.


        :return: The version_name of this CertificateBundleVersionSummary.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """
        Sets the version_name of this CertificateBundleVersionSummary.
        The name of the certificate version.


        :param version_name: The version_name of this CertificateBundleVersionSummary.
        :type: str
        """
        self._version_name = version_name

    @property
    def certificate_name(self):
        """
        **[Required]** Gets the certificate_name of this CertificateBundleVersionSummary.
        The name of the certificate.


        :return: The certificate_name of this CertificateBundleVersionSummary.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """
        Sets the certificate_name of this CertificateBundleVersionSummary.
        The name of the certificate.


        :param certificate_name: The certificate_name of this CertificateBundleVersionSummary.
        :type: str
        """
        self._certificate_name = certificate_name

    @property
    def version_number(self):
        """
        **[Required]** Gets the version_number of this CertificateBundleVersionSummary.
        The version number of the certificate.


        :return: The version_number of this CertificateBundleVersionSummary.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """
        Sets the version_number of this CertificateBundleVersionSummary.
        The version number of the certificate.


        :param version_number: The version_number of this CertificateBundleVersionSummary.
        :type: int
        """
        self._version_number = version_number

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CertificateBundleVersionSummary.
        An optional property indicating when the certificate version was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CertificateBundleVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CertificateBundleVersionSummary.
        An optional property indicating when the certificate version was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CertificateBundleVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def validity(self):
        """
        Gets the validity of this CertificateBundleVersionSummary.

        :return: The validity of this CertificateBundleVersionSummary.
        :rtype: oci.certificates.models.Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this CertificateBundleVersionSummary.

        :param validity: The validity of this CertificateBundleVersionSummary.
        :type: oci.certificates.models.Validity
        """
        self._validity = validity

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this CertificateBundleVersionSummary.
        An optional property indicating when to delete the certificate version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this CertificateBundleVersionSummary.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this CertificateBundleVersionSummary.
        An optional property indicating when to delete the certificate version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this CertificateBundleVersionSummary.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def stages(self):
        """
        **[Required]** Gets the stages of this CertificateBundleVersionSummary.
        A list of rotation states for this certificate bundle version.

        Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The stages of this CertificateBundleVersionSummary.
        :rtype: list[str]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this CertificateBundleVersionSummary.
        A list of rotation states for this certificate bundle version.


        :param stages: The stages of this CertificateBundleVersionSummary.
        :type: list[str]
        """
        allowed_values = ["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", "FAILED"]
        if stages:
            stages[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in stages]
        self._stages = stages

    @property
    def revocation_status(self):
        """
        Gets the revocation_status of this CertificateBundleVersionSummary.

        :return: The revocation_status of this CertificateBundleVersionSummary.
        :rtype: oci.certificates.models.RevocationStatus
        """
        return self._revocation_status

    @revocation_status.setter
    def revocation_status(self, revocation_status):
        """
        Sets the revocation_status of this CertificateBundleVersionSummary.

        :param revocation_status: The revocation_status of this CertificateBundleVersionSummary.
        :type: oci.certificates.models.RevocationStatus
        """
        self._revocation_status = revocation_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
