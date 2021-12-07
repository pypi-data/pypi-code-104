# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateSummary(object):
    """
    The details of the certificate. This object does not contain the certificate contents.
    """

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the config_type property of a CertificateSummary.
    #: This constant has a value of "ISSUED_BY_INTERNAL_CA"
    CONFIG_TYPE_ISSUED_BY_INTERNAL_CA = "ISSUED_BY_INTERNAL_CA"

    #: A constant which can be used with the config_type property of a CertificateSummary.
    #: This constant has a value of "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA"
    CONFIG_TYPE_MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA = "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA"

    #: A constant which can be used with the config_type property of a CertificateSummary.
    #: This constant has a value of "IMPORTED"
    CONFIG_TYPE_IMPORTED = "IMPORTED"

    #: A constant which can be used with the key_algorithm property of a CertificateSummary.
    #: This constant has a value of "RSA2048"
    KEY_ALGORITHM_RSA2048 = "RSA2048"

    #: A constant which can be used with the key_algorithm property of a CertificateSummary.
    #: This constant has a value of "RSA4096"
    KEY_ALGORITHM_RSA4096 = "RSA4096"

    #: A constant which can be used with the key_algorithm property of a CertificateSummary.
    #: This constant has a value of "ECDSA_P256"
    KEY_ALGORITHM_ECDSA_P256 = "ECDSA_P256"

    #: A constant which can be used with the key_algorithm property of a CertificateSummary.
    #: This constant has a value of "ECDSA_P384"
    KEY_ALGORITHM_ECDSA_P384 = "ECDSA_P384"

    #: A constant which can be used with the signature_algorithm property of a CertificateSummary.
    #: This constant has a value of "SHA256_WITH_RSA"
    SIGNATURE_ALGORITHM_SHA256_WITH_RSA = "SHA256_WITH_RSA"

    #: A constant which can be used with the signature_algorithm property of a CertificateSummary.
    #: This constant has a value of "SHA384_WITH_RSA"
    SIGNATURE_ALGORITHM_SHA384_WITH_RSA = "SHA384_WITH_RSA"

    #: A constant which can be used with the signature_algorithm property of a CertificateSummary.
    #: This constant has a value of "SHA512_WITH_RSA"
    SIGNATURE_ALGORITHM_SHA512_WITH_RSA = "SHA512_WITH_RSA"

    #: A constant which can be used with the signature_algorithm property of a CertificateSummary.
    #: This constant has a value of "SHA256_WITH_ECDSA"
    SIGNATURE_ALGORITHM_SHA256_WITH_ECDSA = "SHA256_WITH_ECDSA"

    #: A constant which can be used with the signature_algorithm property of a CertificateSummary.
    #: This constant has a value of "SHA384_WITH_ECDSA"
    SIGNATURE_ALGORITHM_SHA384_WITH_ECDSA = "SHA384_WITH_ECDSA"

    #: A constant which can be used with the signature_algorithm property of a CertificateSummary.
    #: This constant has a value of "SHA512_WITH_ECDSA"
    SIGNATURE_ALGORITHM_SHA512_WITH_ECDSA = "SHA512_WITH_ECDSA"

    #: A constant which can be used with the certificate_profile_type property of a CertificateSummary.
    #: This constant has a value of "TLS_SERVER_OR_CLIENT"
    CERTIFICATE_PROFILE_TYPE_TLS_SERVER_OR_CLIENT = "TLS_SERVER_OR_CLIENT"

    #: A constant which can be used with the certificate_profile_type property of a CertificateSummary.
    #: This constant has a value of "TLS_SERVER"
    CERTIFICATE_PROFILE_TYPE_TLS_SERVER = "TLS_SERVER"

    #: A constant which can be used with the certificate_profile_type property of a CertificateSummary.
    #: This constant has a value of "TLS_CLIENT"
    CERTIFICATE_PROFILE_TYPE_TLS_CLIENT = "TLS_CLIENT"

    #: A constant which can be used with the certificate_profile_type property of a CertificateSummary.
    #: This constant has a value of "TLS_CODE_SIGN"
    CERTIFICATE_PROFILE_TYPE_TLS_CODE_SIGN = "TLS_CODE_SIGN"

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CertificateSummary.
        :type id: str

        :param issuer_certificate_authority_id:
            The value to assign to the issuer_certificate_authority_id property of this CertificateSummary.
        :type issuer_certificate_authority_id: str

        :param name:
            The value to assign to the name property of this CertificateSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this CertificateSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this CertificateSummary.
        :type time_created: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this CertificateSummary.
        :type time_of_deletion: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CertificateSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CertificateSummary.
        :type compartment_id: str

        :param certificate_rules:
            The value to assign to the certificate_rules property of this CertificateSummary.
        :type certificate_rules: list[oci.certificates_management.models.CertificateRule]

        :param current_version_summary:
            The value to assign to the current_version_summary property of this CertificateSummary.
        :type current_version_summary: oci.certificates_management.models.CertificateVersionSummary

        :param subject:
            The value to assign to the subject property of this CertificateSummary.
        :type subject: oci.certificates_management.models.CertificateSubject

        :param config_type:
            The value to assign to the config_type property of this CertificateSummary.
            Allowed values for this property are: "ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_type: str

        :param key_algorithm:
            The value to assign to the key_algorithm property of this CertificateSummary.
            Allowed values for this property are: "RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type key_algorithm: str

        :param signature_algorithm:
            The value to assign to the signature_algorithm property of this CertificateSummary.
            Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type signature_algorithm: str

        :param certificate_profile_type:
            The value to assign to the certificate_profile_type property of this CertificateSummary.
            Allowed values for this property are: "TLS_SERVER_OR_CLIENT", "TLS_SERVER", "TLS_CLIENT", "TLS_CODE_SIGN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type certificate_profile_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CertificateSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CertificateSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'issuer_certificate_authority_id': 'str',
            'name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_of_deletion': 'datetime',
            'lifecycle_state': 'str',
            'compartment_id': 'str',
            'certificate_rules': 'list[CertificateRule]',
            'current_version_summary': 'CertificateVersionSummary',
            'subject': 'CertificateSubject',
            'config_type': 'str',
            'key_algorithm': 'str',
            'signature_algorithm': 'str',
            'certificate_profile_type': 'str',
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
            'lifecycle_state': 'lifecycleState',
            'compartment_id': 'compartmentId',
            'certificate_rules': 'certificateRules',
            'current_version_summary': 'currentVersionSummary',
            'subject': 'subject',
            'config_type': 'configType',
            'key_algorithm': 'keyAlgorithm',
            'signature_algorithm': 'signatureAlgorithm',
            'certificate_profile_type': 'certificateProfileType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._issuer_certificate_authority_id = None
        self._name = None
        self._description = None
        self._time_created = None
        self._time_of_deletion = None
        self._lifecycle_state = None
        self._compartment_id = None
        self._certificate_rules = None
        self._current_version_summary = None
        self._subject = None
        self._config_type = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self._certificate_profile_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CertificateSummary.
        The OCID of the certificate.


        :return: The id of this CertificateSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CertificateSummary.
        The OCID of the certificate.


        :param id: The id of this CertificateSummary.
        :type: str
        """
        self._id = id

    @property
    def issuer_certificate_authority_id(self):
        """
        Gets the issuer_certificate_authority_id of this CertificateSummary.
        The OCID of the certificate authority (CA) that issued the certificate.


        :return: The issuer_certificate_authority_id of this CertificateSummary.
        :rtype: str
        """
        return self._issuer_certificate_authority_id

    @issuer_certificate_authority_id.setter
    def issuer_certificate_authority_id(self, issuer_certificate_authority_id):
        """
        Sets the issuer_certificate_authority_id of this CertificateSummary.
        The OCID of the certificate authority (CA) that issued the certificate.


        :param issuer_certificate_authority_id: The issuer_certificate_authority_id of this CertificateSummary.
        :type: str
        """
        self._issuer_certificate_authority_id = issuer_certificate_authority_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CertificateSummary.
        A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :return: The name of this CertificateSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CertificateSummary.
        A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :param name: The name of this CertificateSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CertificateSummary.
        A brief description of the certificate.


        :return: The description of this CertificateSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CertificateSummary.
        A brief description of the certificate.


        :param description: The description of this CertificateSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CertificateSummary.
        A property indicating when the certificate was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CertificateSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CertificateSummary.
        A property indicating when the certificate was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CertificateSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this CertificateSummary.
        An optional property indicating when to delete the certificate version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this CertificateSummary.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this CertificateSummary.
        An optional property indicating when to delete the certificate version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this CertificateSummary.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CertificateSummary.
        The current lifecycle state of the certificate.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CertificateSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CertificateSummary.
        The current lifecycle state of the certificate.


        :param lifecycle_state: The lifecycle_state of this CertificateSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CertificateSummary.
        The OCID of the compartment that contains the certificate.


        :return: The compartment_id of this CertificateSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CertificateSummary.
        The OCID of the compartment that contains the certificate.


        :param compartment_id: The compartment_id of this CertificateSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def certificate_rules(self):
        """
        Gets the certificate_rules of this CertificateSummary.
        An optional list of rules that control how the certificate is used and managed.


        :return: The certificate_rules of this CertificateSummary.
        :rtype: list[oci.certificates_management.models.CertificateRule]
        """
        return self._certificate_rules

    @certificate_rules.setter
    def certificate_rules(self, certificate_rules):
        """
        Sets the certificate_rules of this CertificateSummary.
        An optional list of rules that control how the certificate is used and managed.


        :param certificate_rules: The certificate_rules of this CertificateSummary.
        :type: list[oci.certificates_management.models.CertificateRule]
        """
        self._certificate_rules = certificate_rules

    @property
    def current_version_summary(self):
        """
        Gets the current_version_summary of this CertificateSummary.

        :return: The current_version_summary of this CertificateSummary.
        :rtype: oci.certificates_management.models.CertificateVersionSummary
        """
        return self._current_version_summary

    @current_version_summary.setter
    def current_version_summary(self, current_version_summary):
        """
        Sets the current_version_summary of this CertificateSummary.

        :param current_version_summary: The current_version_summary of this CertificateSummary.
        :type: oci.certificates_management.models.CertificateVersionSummary
        """
        self._current_version_summary = current_version_summary

    @property
    def subject(self):
        """
        Gets the subject of this CertificateSummary.

        :return: The subject of this CertificateSummary.
        :rtype: oci.certificates_management.models.CertificateSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CertificateSummary.

        :param subject: The subject of this CertificateSummary.
        :type: oci.certificates_management.models.CertificateSubject
        """
        self._subject = subject

    @property
    def config_type(self):
        """
        **[Required]** Gets the config_type of this CertificateSummary.
        The origin of the certificate.

        Allowed values for this property are: "ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The config_type of this CertificateSummary.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this CertificateSummary.
        The origin of the certificate.


        :param config_type: The config_type of this CertificateSummary.
        :type: str
        """
        allowed_values = ["ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED"]
        if not value_allowed_none_or_none_sentinel(config_type, allowed_values):
            config_type = 'UNKNOWN_ENUM_VALUE'
        self._config_type = config_type

    @property
    def key_algorithm(self):
        """
        Gets the key_algorithm of this CertificateSummary.
        The algorithm used to create key pairs.

        Allowed values for this property are: "RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The key_algorithm of this CertificateSummary.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """
        Sets the key_algorithm of this CertificateSummary.
        The algorithm used to create key pairs.


        :param key_algorithm: The key_algorithm of this CertificateSummary.
        :type: str
        """
        allowed_values = ["RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"]
        if not value_allowed_none_or_none_sentinel(key_algorithm, allowed_values):
            key_algorithm = 'UNKNOWN_ENUM_VALUE'
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        """
        Gets the signature_algorithm of this CertificateSummary.
        The algorithm used to sign the public key certificate.

        Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The signature_algorithm of this CertificateSummary.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """
        Sets the signature_algorithm of this CertificateSummary.
        The algorithm used to sign the public key certificate.


        :param signature_algorithm: The signature_algorithm of this CertificateSummary.
        :type: str
        """
        allowed_values = ["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]
        if not value_allowed_none_or_none_sentinel(signature_algorithm, allowed_values):
            signature_algorithm = 'UNKNOWN_ENUM_VALUE'
        self._signature_algorithm = signature_algorithm

    @property
    def certificate_profile_type(self):
        """
        Gets the certificate_profile_type of this CertificateSummary.
        The name of the profile used to create the certificate, which depends on the type of certificate you need.

        Allowed values for this property are: "TLS_SERVER_OR_CLIENT", "TLS_SERVER", "TLS_CLIENT", "TLS_CODE_SIGN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The certificate_profile_type of this CertificateSummary.
        :rtype: str
        """
        return self._certificate_profile_type

    @certificate_profile_type.setter
    def certificate_profile_type(self, certificate_profile_type):
        """
        Sets the certificate_profile_type of this CertificateSummary.
        The name of the profile used to create the certificate, which depends on the type of certificate you need.


        :param certificate_profile_type: The certificate_profile_type of this CertificateSummary.
        :type: str
        """
        allowed_values = ["TLS_SERVER_OR_CLIENT", "TLS_SERVER", "TLS_CLIENT", "TLS_CODE_SIGN"]
        if not value_allowed_none_or_none_sentinel(certificate_profile_type, allowed_values):
            certificate_profile_type = 'UNKNOWN_ENUM_VALUE'
        self._certificate_profile_type = certificate_profile_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CertificateSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CertificateSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CertificateSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CertificateSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CertificateSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CertificateSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CertificateSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CertificateSummary.
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
