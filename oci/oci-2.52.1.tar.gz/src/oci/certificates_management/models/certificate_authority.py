# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateAuthority(object):
    """
    The metadata details of the certificate authority (CA). This object does not contain the CA contents.
    """

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a CertificateAuthority.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the config_type property of a CertificateAuthority.
    #: This constant has a value of "ROOT_CA_GENERATED_INTERNALLY"
    CONFIG_TYPE_ROOT_CA_GENERATED_INTERNALLY = "ROOT_CA_GENERATED_INTERNALLY"

    #: A constant which can be used with the config_type property of a CertificateAuthority.
    #: This constant has a value of "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"
    CONFIG_TYPE_SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA = "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"

    #: A constant which can be used with the signing_algorithm property of a CertificateAuthority.
    #: This constant has a value of "SHA256_WITH_RSA"
    SIGNING_ALGORITHM_SHA256_WITH_RSA = "SHA256_WITH_RSA"

    #: A constant which can be used with the signing_algorithm property of a CertificateAuthority.
    #: This constant has a value of "SHA384_WITH_RSA"
    SIGNING_ALGORITHM_SHA384_WITH_RSA = "SHA384_WITH_RSA"

    #: A constant which can be used with the signing_algorithm property of a CertificateAuthority.
    #: This constant has a value of "SHA512_WITH_RSA"
    SIGNING_ALGORITHM_SHA512_WITH_RSA = "SHA512_WITH_RSA"

    #: A constant which can be used with the signing_algorithm property of a CertificateAuthority.
    #: This constant has a value of "SHA256_WITH_ECDSA"
    SIGNING_ALGORITHM_SHA256_WITH_ECDSA = "SHA256_WITH_ECDSA"

    #: A constant which can be used with the signing_algorithm property of a CertificateAuthority.
    #: This constant has a value of "SHA384_WITH_ECDSA"
    SIGNING_ALGORITHM_SHA384_WITH_ECDSA = "SHA384_WITH_ECDSA"

    #: A constant which can be used with the signing_algorithm property of a CertificateAuthority.
    #: This constant has a value of "SHA512_WITH_ECDSA"
    SIGNING_ALGORITHM_SHA512_WITH_ECDSA = "SHA512_WITH_ECDSA"

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateAuthority object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CertificateAuthority.
        :type id: str

        :param issuer_certificate_authority_id:
            The value to assign to the issuer_certificate_authority_id property of this CertificateAuthority.
        :type issuer_certificate_authority_id: str

        :param name:
            The value to assign to the name property of this CertificateAuthority.
        :type name: str

        :param description:
            The value to assign to the description property of this CertificateAuthority.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this CertificateAuthority.
        :type time_created: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this CertificateAuthority.
        :type time_of_deletion: datetime

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CertificateAuthority.
        :type kms_key_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CertificateAuthority.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CertificateAuthority.
        :type lifecycle_details: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CertificateAuthority.
        :type compartment_id: str

        :param certificate_authority_rules:
            The value to assign to the certificate_authority_rules property of this CertificateAuthority.
        :type certificate_authority_rules: list[oci.certificates_management.models.CertificateAuthorityRule]

        :param current_version:
            The value to assign to the current_version property of this CertificateAuthority.
        :type current_version: oci.certificates_management.models.CertificateAuthorityVersionSummary

        :param certificate_revocation_list_details:
            The value to assign to the certificate_revocation_list_details property of this CertificateAuthority.
        :type certificate_revocation_list_details: oci.certificates_management.models.CertificateRevocationListDetails

        :param config_type:
            The value to assign to the config_type property of this CertificateAuthority.
            Allowed values for this property are: "ROOT_CA_GENERATED_INTERNALLY", "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_type: str

        :param subject:
            The value to assign to the subject property of this CertificateAuthority.
        :type subject: oci.certificates_management.models.CertificateSubject

        :param signing_algorithm:
            The value to assign to the signing_algorithm property of this CertificateAuthority.
            Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type signing_algorithm: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CertificateAuthority.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CertificateAuthority.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'issuer_certificate_authority_id': 'str',
            'name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_of_deletion': 'datetime',
            'kms_key_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'compartment_id': 'str',
            'certificate_authority_rules': 'list[CertificateAuthorityRule]',
            'current_version': 'CertificateAuthorityVersionSummary',
            'certificate_revocation_list_details': 'CertificateRevocationListDetails',
            'config_type': 'str',
            'subject': 'CertificateSubject',
            'signing_algorithm': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'issuer_certificate_authority_id': 'issuerCertificateAuthorityId',
            'name': 'name',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_of_deletion': 'timeOfDeletion',
            'kms_key_id': 'kmsKeyId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'compartment_id': 'compartmentId',
            'certificate_authority_rules': 'certificateAuthorityRules',
            'current_version': 'currentVersion',
            'certificate_revocation_list_details': 'certificateRevocationListDetails',
            'config_type': 'configType',
            'subject': 'subject',
            'signing_algorithm': 'signingAlgorithm',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._issuer_certificate_authority_id = None
        self._name = None
        self._description = None
        self._time_created = None
        self._time_of_deletion = None
        self._kms_key_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._compartment_id = None
        self._certificate_authority_rules = None
        self._current_version = None
        self._certificate_revocation_list_details = None
        self._config_type = None
        self._subject = None
        self._signing_algorithm = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CertificateAuthority.
        The OCID of the CA.


        :return: The id of this CertificateAuthority.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CertificateAuthority.
        The OCID of the CA.


        :param id: The id of this CertificateAuthority.
        :type: str
        """
        self._id = id

    @property
    def issuer_certificate_authority_id(self):
        """
        Gets the issuer_certificate_authority_id of this CertificateAuthority.
        The OCID of the parent CA that issued this CA. If this is the root CA, then this value is null.


        :return: The issuer_certificate_authority_id of this CertificateAuthority.
        :rtype: str
        """
        return self._issuer_certificate_authority_id

    @issuer_certificate_authority_id.setter
    def issuer_certificate_authority_id(self, issuer_certificate_authority_id):
        """
        Sets the issuer_certificate_authority_id of this CertificateAuthority.
        The OCID of the parent CA that issued this CA. If this is the root CA, then this value is null.


        :param issuer_certificate_authority_id: The issuer_certificate_authority_id of this CertificateAuthority.
        :type: str
        """
        self._issuer_certificate_authority_id = issuer_certificate_authority_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CertificateAuthority.
        A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :return: The name of this CertificateAuthority.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CertificateAuthority.
        A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :param name: The name of this CertificateAuthority.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CertificateAuthority.
        A brief description of the CA.


        :return: The description of this CertificateAuthority.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CertificateAuthority.
        A brief description of the CA.


        :param description: The description of this CertificateAuthority.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CertificateAuthority.
        A property indicating when the CA was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CertificateAuthority.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CertificateAuthority.
        A property indicating when the CA was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CertificateAuthority.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this CertificateAuthority.
        An optional property indicating when to delete the CA version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this CertificateAuthority.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this CertificateAuthority.
        An optional property indicating when to delete the CA version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this CertificateAuthority.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CertificateAuthority.
        The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.


        :return: The kms_key_id of this CertificateAuthority.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CertificateAuthority.
        The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.


        :param kms_key_id: The kms_key_id of this CertificateAuthority.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CertificateAuthority.
        The current lifecycle state of the certificate authority.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CertificateAuthority.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CertificateAuthority.
        The current lifecycle state of the certificate authority.


        :param lifecycle_state: The lifecycle_state of this CertificateAuthority.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CertificateAuthority.
        Additional information about the current CA lifecycle state.


        :return: The lifecycle_details of this CertificateAuthority.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CertificateAuthority.
        Additional information about the current CA lifecycle state.


        :param lifecycle_details: The lifecycle_details of this CertificateAuthority.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CertificateAuthority.
        The OCID of the compartment under which the CA is created.


        :return: The compartment_id of this CertificateAuthority.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CertificateAuthority.
        The OCID of the compartment under which the CA is created.


        :param compartment_id: The compartment_id of this CertificateAuthority.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def certificate_authority_rules(self):
        """
        Gets the certificate_authority_rules of this CertificateAuthority.
        An optional list of rules that control how the CA is used and managed.


        :return: The certificate_authority_rules of this CertificateAuthority.
        :rtype: list[oci.certificates_management.models.CertificateAuthorityRule]
        """
        return self._certificate_authority_rules

    @certificate_authority_rules.setter
    def certificate_authority_rules(self, certificate_authority_rules):
        """
        Sets the certificate_authority_rules of this CertificateAuthority.
        An optional list of rules that control how the CA is used and managed.


        :param certificate_authority_rules: The certificate_authority_rules of this CertificateAuthority.
        :type: list[oci.certificates_management.models.CertificateAuthorityRule]
        """
        self._certificate_authority_rules = certificate_authority_rules

    @property
    def current_version(self):
        """
        Gets the current_version of this CertificateAuthority.

        :return: The current_version of this CertificateAuthority.
        :rtype: oci.certificates_management.models.CertificateAuthorityVersionSummary
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """
        Sets the current_version of this CertificateAuthority.

        :param current_version: The current_version of this CertificateAuthority.
        :type: oci.certificates_management.models.CertificateAuthorityVersionSummary
        """
        self._current_version = current_version

    @property
    def certificate_revocation_list_details(self):
        """
        Gets the certificate_revocation_list_details of this CertificateAuthority.

        :return: The certificate_revocation_list_details of this CertificateAuthority.
        :rtype: oci.certificates_management.models.CertificateRevocationListDetails
        """
        return self._certificate_revocation_list_details

    @certificate_revocation_list_details.setter
    def certificate_revocation_list_details(self, certificate_revocation_list_details):
        """
        Sets the certificate_revocation_list_details of this CertificateAuthority.

        :param certificate_revocation_list_details: The certificate_revocation_list_details of this CertificateAuthority.
        :type: oci.certificates_management.models.CertificateRevocationListDetails
        """
        self._certificate_revocation_list_details = certificate_revocation_list_details

    @property
    def config_type(self):
        """
        **[Required]** Gets the config_type of this CertificateAuthority.
        The origin of the CA.

        Allowed values for this property are: "ROOT_CA_GENERATED_INTERNALLY", "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The config_type of this CertificateAuthority.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this CertificateAuthority.
        The origin of the CA.


        :param config_type: The config_type of this CertificateAuthority.
        :type: str
        """
        allowed_values = ["ROOT_CA_GENERATED_INTERNALLY", "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"]
        if not value_allowed_none_or_none_sentinel(config_type, allowed_values):
            config_type = 'UNKNOWN_ENUM_VALUE'
        self._config_type = config_type

    @property
    def subject(self):
        """
        Gets the subject of this CertificateAuthority.

        :return: The subject of this CertificateAuthority.
        :rtype: oci.certificates_management.models.CertificateSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CertificateAuthority.

        :param subject: The subject of this CertificateAuthority.
        :type: oci.certificates_management.models.CertificateSubject
        """
        self._subject = subject

    @property
    def signing_algorithm(self):
        """
        Gets the signing_algorithm of this CertificateAuthority.
        The algorithm used to sign public key certificates that the CA issues.

        Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The signing_algorithm of this CertificateAuthority.
        :rtype: str
        """
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        """
        Sets the signing_algorithm of this CertificateAuthority.
        The algorithm used to sign public key certificates that the CA issues.


        :param signing_algorithm: The signing_algorithm of this CertificateAuthority.
        :type: str
        """
        allowed_values = ["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]
        if not value_allowed_none_or_none_sentinel(signing_algorithm, allowed_values):
            signing_algorithm = 'UNKNOWN_ENUM_VALUE'
        self._signing_algorithm = signing_algorithm

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CertificateAuthority.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CertificateAuthority.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CertificateAuthority.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CertificateAuthority.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CertificateAuthority.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CertificateAuthority.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CertificateAuthority.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CertificateAuthority.
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
