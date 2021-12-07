# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateVersion(object):
    """
    The details of the certificate version. This object does not contain the certificate contents.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_id:
            The value to assign to the certificate_id property of this CertificateVersion.
        :type certificate_id: str

        :param serial_number:
            The value to assign to the serial_number property of this CertificateVersion.
        :type serial_number: str

        :param time_created:
            The value to assign to the time_created property of this CertificateVersion.
        :type time_created: datetime

        :param version_number:
            The value to assign to the version_number property of this CertificateVersion.
        :type version_number: int

        :param issuer_ca_version_number:
            The value to assign to the issuer_ca_version_number property of this CertificateVersion.
        :type issuer_ca_version_number: int

        :param version_name:
            The value to assign to the version_name property of this CertificateVersion.
        :type version_name: str

        :param subject_alternative_names:
            The value to assign to the subject_alternative_names property of this CertificateVersion.
        :type subject_alternative_names: list[oci.certificates_management.models.CertificateSubjectAlternativeName]

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this CertificateVersion.
        :type time_of_deletion: datetime

        :param validity:
            The value to assign to the validity property of this CertificateVersion.
        :type validity: oci.certificates_management.models.Validity

        :param stages:
            The value to assign to the stages property of this CertificateVersion.
        :type stages: list[oci.certificates_management.models.VersionStage]

        :param revocation_status:
            The value to assign to the revocation_status property of this CertificateVersion.
        :type revocation_status: oci.certificates_management.models.RevocationStatus

        """
        self.swagger_types = {
            'certificate_id': 'str',
            'serial_number': 'str',
            'time_created': 'datetime',
            'version_number': 'int',
            'issuer_ca_version_number': 'int',
            'version_name': 'str',
            'subject_alternative_names': 'list[CertificateSubjectAlternativeName]',
            'time_of_deletion': 'datetime',
            'validity': 'Validity',
            'stages': 'list[VersionStage]',
            'revocation_status': 'RevocationStatus'
        }

        self.attribute_map = {
            'certificate_id': 'certificateId',
            'serial_number': 'serialNumber',
            'time_created': 'timeCreated',
            'version_number': 'versionNumber',
            'issuer_ca_version_number': 'issuerCaVersionNumber',
            'version_name': 'versionName',
            'subject_alternative_names': 'subjectAlternativeNames',
            'time_of_deletion': 'timeOfDeletion',
            'validity': 'validity',
            'stages': 'stages',
            'revocation_status': 'revocationStatus'
        }

        self._certificate_id = None
        self._serial_number = None
        self._time_created = None
        self._version_number = None
        self._issuer_ca_version_number = None
        self._version_name = None
        self._subject_alternative_names = None
        self._time_of_deletion = None
        self._validity = None
        self._stages = None
        self._revocation_status = None

    @property
    def certificate_id(self):
        """
        **[Required]** Gets the certificate_id of this CertificateVersion.
        The OCID of the certificate.


        :return: The certificate_id of this CertificateVersion.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this CertificateVersion.
        The OCID of the certificate.


        :param certificate_id: The certificate_id of this CertificateVersion.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def serial_number(self):
        """
        Gets the serial_number of this CertificateVersion.
        A unique certificate identifier used in certificate revocation tracking, formatted as octets.
        Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`


        :return: The serial_number of this CertificateVersion.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this CertificateVersion.
        A unique certificate identifier used in certificate revocation tracking, formatted as octets.
        Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`


        :param serial_number: The serial_number of this CertificateVersion.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CertificateVersion.
        A optional property indicating when the certificate version was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CertificateVersion.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CertificateVersion.
        A optional property indicating when the certificate version was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CertificateVersion.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version_number(self):
        """
        **[Required]** Gets the version_number of this CertificateVersion.
        The version number of the certificate.


        :return: The version_number of this CertificateVersion.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """
        Sets the version_number of this CertificateVersion.
        The version number of the certificate.


        :param version_number: The version_number of this CertificateVersion.
        :type: int
        """
        self._version_number = version_number

    @property
    def issuer_ca_version_number(self):
        """
        Gets the issuer_ca_version_number of this CertificateVersion.
        The version number of the issuing certificate authority (CA).


        :return: The issuer_ca_version_number of this CertificateVersion.
        :rtype: int
        """
        return self._issuer_ca_version_number

    @issuer_ca_version_number.setter
    def issuer_ca_version_number(self, issuer_ca_version_number):
        """
        Sets the issuer_ca_version_number of this CertificateVersion.
        The version number of the issuing certificate authority (CA).


        :param issuer_ca_version_number: The issuer_ca_version_number of this CertificateVersion.
        :type: int
        """
        self._issuer_ca_version_number = issuer_ca_version_number

    @property
    def version_name(self):
        """
        Gets the version_name of this CertificateVersion.
        The name of the certificate version. When the value is not null, a name is unique across versions of a given certificate.


        :return: The version_name of this CertificateVersion.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """
        Sets the version_name of this CertificateVersion.
        The name of the certificate version. When the value is not null, a name is unique across versions of a given certificate.


        :param version_name: The version_name of this CertificateVersion.
        :type: str
        """
        self._version_name = version_name

    @property
    def subject_alternative_names(self):
        """
        Gets the subject_alternative_names of this CertificateVersion.
        A list of subject alternative names.


        :return: The subject_alternative_names of this CertificateVersion.
        :rtype: list[oci.certificates_management.models.CertificateSubjectAlternativeName]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """
        Sets the subject_alternative_names of this CertificateVersion.
        A list of subject alternative names.


        :param subject_alternative_names: The subject_alternative_names of this CertificateVersion.
        :type: list[oci.certificates_management.models.CertificateSubjectAlternativeName]
        """
        self._subject_alternative_names = subject_alternative_names

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this CertificateVersion.
        An optional property indicating when to delete the certificate version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this CertificateVersion.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this CertificateVersion.
        An optional property indicating when to delete the certificate version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this CertificateVersion.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def validity(self):
        """
        Gets the validity of this CertificateVersion.

        :return: The validity of this CertificateVersion.
        :rtype: oci.certificates_management.models.Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this CertificateVersion.

        :param validity: The validity of this CertificateVersion.
        :type: oci.certificates_management.models.Validity
        """
        self._validity = validity

    @property
    def stages(self):
        """
        **[Required]** Gets the stages of this CertificateVersion.
        A list of stages of this entity.


        :return: The stages of this CertificateVersion.
        :rtype: list[oci.certificates_management.models.VersionStage]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this CertificateVersion.
        A list of stages of this entity.


        :param stages: The stages of this CertificateVersion.
        :type: list[oci.certificates_management.models.VersionStage]
        """
        self._stages = stages

    @property
    def revocation_status(self):
        """
        Gets the revocation_status of this CertificateVersion.

        :return: The revocation_status of this CertificateVersion.
        :rtype: oci.certificates_management.models.RevocationStatus
        """
        return self._revocation_status

    @revocation_status.setter
    def revocation_status(self, revocation_status):
        """
        Sets the revocation_status of this CertificateVersion.

        :param revocation_status: The revocation_status of this CertificateVersion.
        :type: oci.certificates_management.models.RevocationStatus
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
