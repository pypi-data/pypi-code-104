# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseSoftwareImageDetails(object):
    """
    Parameters for creating a database software image in the specified compartment.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the image_shape_family property of a CreateDatabaseSoftwareImageDetails.
    #: This constant has a value of "VM_BM_SHAPE"
    IMAGE_SHAPE_FAMILY_VM_BM_SHAPE = "VM_BM_SHAPE"

    #: A constant which can be used with the image_shape_family property of a CreateDatabaseSoftwareImageDetails.
    #: This constant has a value of "EXADATA_SHAPE"
    IMAGE_SHAPE_FAMILY_EXADATA_SHAPE = "EXADATA_SHAPE"

    #: A constant which can be used with the image_shape_family property of a CreateDatabaseSoftwareImageDetails.
    #: This constant has a value of "EXACC_SHAPE"
    IMAGE_SHAPE_FAMILY_EXACC_SHAPE = "EXACC_SHAPE"

    #: A constant which can be used with the image_type property of a CreateDatabaseSoftwareImageDetails.
    #: This constant has a value of "GRID_IMAGE"
    IMAGE_TYPE_GRID_IMAGE = "GRID_IMAGE"

    #: A constant which can be used with the image_type property of a CreateDatabaseSoftwareImageDetails.
    #: This constant has a value of "DATABASE_IMAGE"
    IMAGE_TYPE_DATABASE_IMAGE = "DATABASE_IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseSoftwareImageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDatabaseSoftwareImageDetails.
        :type compartment_id: str

        :param database_version:
            The value to assign to the database_version property of this CreateDatabaseSoftwareImageDetails.
        :type database_version: str

        :param display_name:
            The value to assign to the display_name property of this CreateDatabaseSoftwareImageDetails.
        :type display_name: str

        :param image_shape_family:
            The value to assign to the image_shape_family property of this CreateDatabaseSoftwareImageDetails.
            Allowed values for this property are: "VM_BM_SHAPE", "EXADATA_SHAPE", "EXACC_SHAPE"
        :type image_shape_family: str

        :param image_type:
            The value to assign to the image_type property of this CreateDatabaseSoftwareImageDetails.
            Allowed values for this property are: "GRID_IMAGE", "DATABASE_IMAGE"
        :type image_type: str

        :param patch_set:
            The value to assign to the patch_set property of this CreateDatabaseSoftwareImageDetails.
        :type patch_set: str

        :param database_software_image_one_off_patches:
            The value to assign to the database_software_image_one_off_patches property of this CreateDatabaseSoftwareImageDetails.
        :type database_software_image_one_off_patches: list[str]

        :param ls_inventory:
            The value to assign to the ls_inventory property of this CreateDatabaseSoftwareImageDetails.
        :type ls_inventory: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDatabaseSoftwareImageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDatabaseSoftwareImageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param source_db_home_id:
            The value to assign to the source_db_home_id property of this CreateDatabaseSoftwareImageDetails.
        :type source_db_home_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'database_version': 'str',
            'display_name': 'str',
            'image_shape_family': 'str',
            'image_type': 'str',
            'patch_set': 'str',
            'database_software_image_one_off_patches': 'list[str]',
            'ls_inventory': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'source_db_home_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'database_version': 'databaseVersion',
            'display_name': 'displayName',
            'image_shape_family': 'imageShapeFamily',
            'image_type': 'imageType',
            'patch_set': 'patchSet',
            'database_software_image_one_off_patches': 'databaseSoftwareImageOneOffPatches',
            'ls_inventory': 'lsInventory',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'source_db_home_id': 'sourceDbHomeId'
        }

        self._compartment_id = None
        self._database_version = None
        self._display_name = None
        self._image_shape_family = None
        self._image_type = None
        self._patch_set = None
        self._database_software_image_one_off_patches = None
        self._ls_inventory = None
        self._freeform_tags = None
        self._defined_tags = None
        self._source_db_home_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDatabaseSoftwareImageDetails.
        The `OCID`__ of the compartment the database software image  belongs in.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDatabaseSoftwareImageDetails.
        The `OCID`__ of the compartment the database software image  belongs in.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDatabaseSoftwareImageDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_version(self):
        """
        Gets the database_version of this CreateDatabaseSoftwareImageDetails.
        The database version with which the database software image is to be built.


        :return: The database_version of this CreateDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this CreateDatabaseSoftwareImageDetails.
        The database version with which the database software image is to be built.


        :param database_version: The database_version of this CreateDatabaseSoftwareImageDetails.
        :type: str
        """
        self._database_version = database_version

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDatabaseSoftwareImageDetails.
        The user-friendly name for the database software image. The name does not have to be unique.


        :return: The display_name of this CreateDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDatabaseSoftwareImageDetails.
        The user-friendly name for the database software image. The name does not have to be unique.


        :param display_name: The display_name of this CreateDatabaseSoftwareImageDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def image_shape_family(self):
        """
        Gets the image_shape_family of this CreateDatabaseSoftwareImageDetails.
        To what shape the image is meant for.

        Allowed values for this property are: "VM_BM_SHAPE", "EXADATA_SHAPE", "EXACC_SHAPE"


        :return: The image_shape_family of this CreateDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._image_shape_family

    @image_shape_family.setter
    def image_shape_family(self, image_shape_family):
        """
        Sets the image_shape_family of this CreateDatabaseSoftwareImageDetails.
        To what shape the image is meant for.


        :param image_shape_family: The image_shape_family of this CreateDatabaseSoftwareImageDetails.
        :type: str
        """
        allowed_values = ["VM_BM_SHAPE", "EXADATA_SHAPE", "EXACC_SHAPE"]
        if not value_allowed_none_or_none_sentinel(image_shape_family, allowed_values):
            raise ValueError(
                "Invalid value for `image_shape_family`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._image_shape_family = image_shape_family

    @property
    def image_type(self):
        """
        Gets the image_type of this CreateDatabaseSoftwareImageDetails.
        The type of software image. Can be grid or database.

        Allowed values for this property are: "GRID_IMAGE", "DATABASE_IMAGE"


        :return: The image_type of this CreateDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """
        Sets the image_type of this CreateDatabaseSoftwareImageDetails.
        The type of software image. Can be grid or database.


        :param image_type: The image_type of this CreateDatabaseSoftwareImageDetails.
        :type: str
        """
        allowed_values = ["GRID_IMAGE", "DATABASE_IMAGE"]
        if not value_allowed_none_or_none_sentinel(image_type, allowed_values):
            raise ValueError(
                "Invalid value for `image_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._image_type = image_type

    @property
    def patch_set(self):
        """
        Gets the patch_set of this CreateDatabaseSoftwareImageDetails.
        The PSU or PBP or Release Updates. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :return: The patch_set of this CreateDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._patch_set

    @patch_set.setter
    def patch_set(self, patch_set):
        """
        Sets the patch_set of this CreateDatabaseSoftwareImageDetails.
        The PSU or PBP or Release Updates. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :param patch_set: The patch_set of this CreateDatabaseSoftwareImageDetails.
        :type: str
        """
        self._patch_set = patch_set

    @property
    def database_software_image_one_off_patches(self):
        """
        Gets the database_software_image_one_off_patches of this CreateDatabaseSoftwareImageDetails.
        List of one-off patches for Database Homes.


        :return: The database_software_image_one_off_patches of this CreateDatabaseSoftwareImageDetails.
        :rtype: list[str]
        """
        return self._database_software_image_one_off_patches

    @database_software_image_one_off_patches.setter
    def database_software_image_one_off_patches(self, database_software_image_one_off_patches):
        """
        Sets the database_software_image_one_off_patches of this CreateDatabaseSoftwareImageDetails.
        List of one-off patches for Database Homes.


        :param database_software_image_one_off_patches: The database_software_image_one_off_patches of this CreateDatabaseSoftwareImageDetails.
        :type: list[str]
        """
        self._database_software_image_one_off_patches = database_software_image_one_off_patches

    @property
    def ls_inventory(self):
        """
        Gets the ls_inventory of this CreateDatabaseSoftwareImageDetails.
        output from lsinventory which will get passed as a string


        :return: The ls_inventory of this CreateDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._ls_inventory

    @ls_inventory.setter
    def ls_inventory(self, ls_inventory):
        """
        Sets the ls_inventory of this CreateDatabaseSoftwareImageDetails.
        output from lsinventory which will get passed as a string


        :param ls_inventory: The ls_inventory of this CreateDatabaseSoftwareImageDetails.
        :type: str
        """
        self._ls_inventory = ls_inventory

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDatabaseSoftwareImageDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDatabaseSoftwareImageDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDatabaseSoftwareImageDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDatabaseSoftwareImageDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDatabaseSoftwareImageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDatabaseSoftwareImageDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDatabaseSoftwareImageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDatabaseSoftwareImageDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def source_db_home_id(self):
        """
        Gets the source_db_home_id of this CreateDatabaseSoftwareImageDetails.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_db_home_id of this CreateDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._source_db_home_id

    @source_db_home_id.setter
    def source_db_home_id(self, source_db_home_id):
        """
        Sets the source_db_home_id of this CreateDatabaseSoftwareImageDetails.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_db_home_id: The source_db_home_id of this CreateDatabaseSoftwareImageDetails.
        :type: str
        """
        self._source_db_home_id = source_db_home_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
