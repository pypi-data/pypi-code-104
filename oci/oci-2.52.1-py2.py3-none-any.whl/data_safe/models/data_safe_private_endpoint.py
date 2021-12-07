# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSafePrivateEndpoint(object):
    """
    A Data Safe private endpoint that allows Data Safe to connect to databases in a customer's virtual cloud network (VCN).
    """

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpoint.
    #: This constant has a value of "NA"
    LIFECYCLE_STATE_NA = "NA"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSafePrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DataSafePrivateEndpoint.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DataSafePrivateEndpoint.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DataSafePrivateEndpoint.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this DataSafePrivateEndpoint.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DataSafePrivateEndpoint.
        :type subnet_id: str

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this DataSafePrivateEndpoint.
        :type private_endpoint_id: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this DataSafePrivateEndpoint.
        :type private_endpoint_ip: str

        :param endpoint_fqdn:
            The value to assign to the endpoint_fqdn property of this DataSafePrivateEndpoint.
        :type endpoint_fqdn: str

        :param description:
            The value to assign to the description property of this DataSafePrivateEndpoint.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this DataSafePrivateEndpoint.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataSafePrivateEndpoint.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this DataSafePrivateEndpoint.
        :type nsg_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DataSafePrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DataSafePrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DataSafePrivateEndpoint.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'private_endpoint_id': 'str',
            'private_endpoint_ip': 'str',
            'endpoint_fqdn': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'nsg_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'private_endpoint_id': 'privateEndpointId',
            'private_endpoint_ip': 'privateEndpointIp',
            'endpoint_fqdn': 'endpointFqdn',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'nsg_ids': 'nsgIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._vcn_id = None
        self._subnet_id = None
        self._private_endpoint_id = None
        self._private_endpoint_ip = None
        self._endpoint_fqdn = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._nsg_ids = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DataSafePrivateEndpoint.
        The OCID of the Data Safe private endpoint.


        :return: The id of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataSafePrivateEndpoint.
        The OCID of the Data Safe private endpoint.


        :param id: The id of this DataSafePrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DataSafePrivateEndpoint.
        The display name of the private endpoint.


        :return: The display_name of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataSafePrivateEndpoint.
        The display name of the private endpoint.


        :param display_name: The display_name of this DataSafePrivateEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DataSafePrivateEndpoint.
        The OCID of the compartment.


        :return: The compartment_id of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DataSafePrivateEndpoint.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this DataSafePrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DataSafePrivateEndpoint.
        The OCID of the VCN.


        :return: The vcn_id of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DataSafePrivateEndpoint.
        The OCID of the VCN.


        :param vcn_id: The vcn_id of this DataSafePrivateEndpoint.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DataSafePrivateEndpoint.
        The OCID of the subnet.


        :return: The subnet_id of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DataSafePrivateEndpoint.
        The OCID of the subnet.


        :param subnet_id: The subnet_id of this DataSafePrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_id(self):
        """
        **[Required]** Gets the private_endpoint_id of this DataSafePrivateEndpoint.
        The OCID of the underlying private endpoint.


        :return: The private_endpoint_id of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this DataSafePrivateEndpoint.
        The OCID of the underlying private endpoint.


        :param private_endpoint_id: The private_endpoint_id of this DataSafePrivateEndpoint.
        :type: str
        """
        self._private_endpoint_id = private_endpoint_id

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this DataSafePrivateEndpoint.
        The private IP address of the private endpoint.


        :return: The private_endpoint_ip of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this DataSafePrivateEndpoint.
        The private IP address of the private endpoint.


        :param private_endpoint_ip: The private_endpoint_ip of this DataSafePrivateEndpoint.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def endpoint_fqdn(self):
        """
        Gets the endpoint_fqdn of this DataSafePrivateEndpoint.
        The three-label fully qualified domain name (FQDN) of the private endpoint. The customer VCN's DNS records are updated with this FQDN.


        :return: The endpoint_fqdn of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._endpoint_fqdn

    @endpoint_fqdn.setter
    def endpoint_fqdn(self, endpoint_fqdn):
        """
        Sets the endpoint_fqdn of this DataSafePrivateEndpoint.
        The three-label fully qualified domain name (FQDN) of the private endpoint. The customer VCN's DNS records are updated with this FQDN.


        :param endpoint_fqdn: The endpoint_fqdn of this DataSafePrivateEndpoint.
        :type: str
        """
        self._endpoint_fqdn = endpoint_fqdn

    @property
    def description(self):
        """
        Gets the description of this DataSafePrivateEndpoint.
        The description of the private endpoint.


        :return: The description of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataSafePrivateEndpoint.
        The description of the private endpoint.


        :param description: The description of this DataSafePrivateEndpoint.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this DataSafePrivateEndpoint.
        The date and time the private endpoint was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DataSafePrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataSafePrivateEndpoint.
        The date and time the private endpoint was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DataSafePrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DataSafePrivateEndpoint.
        The current state of the private endpoint.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DataSafePrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataSafePrivateEndpoint.
        The current state of the private endpoint.


        :param lifecycle_state: The lifecycle_state of this DataSafePrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this DataSafePrivateEndpoint.
        The OCIDs of the network security groups that the private endpoint belongs to.


        :return: The nsg_ids of this DataSafePrivateEndpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this DataSafePrivateEndpoint.
        The OCIDs of the network security groups that the private endpoint belongs to.


        :param nsg_ids: The nsg_ids of this DataSafePrivateEndpoint.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DataSafePrivateEndpoint.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DataSafePrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DataSafePrivateEndpoint.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DataSafePrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DataSafePrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DataSafePrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DataSafePrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DataSafePrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DataSafePrivateEndpoint.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DataSafePrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DataSafePrivateEndpoint.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DataSafePrivateEndpoint.
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
