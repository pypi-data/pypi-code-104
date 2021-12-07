"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.12.07
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from agilicus_api.exceptions import ApiAttributeError



class ApplicationSummaryStatus(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('published',): {
            'NO': "no",
            'PUBLIC': "public",
        },
    }

    validations = {
        ('application_id',): {
            'max_length': 40,
            'min_length': 1,
        },
        ('application_name',): {
            'max_length': 40,
            'min_length': 1,
        },
        ('assigned_org_id',): {
            'max_length': 40,
            'min_length': 1,
        },
        ('icon_url',): {
            'max_length': 1024,
        },
        ('description',): {
            'max_length': 100,
        },
        ('category',): {
            'max_length': 100,
        },
        ('default_role_name',): {
            'max_length': 100,
            'min_length': 1,
        },
        ('default_role_id',): {
            'max_length': 40,
            'min_length': 1,
        },
    }

    @property
    def application_id(self):
       return self.get("application_id")

    @application_id.setter
    def application_id(self, new_value):
       self.application_id = new_value

    @property
    def application_name(self):
       return self.get("application_name")

    @application_name.setter
    def application_name(self, new_value):
       self.application_name = new_value

    @property
    def assigned_org_id(self):
       return self.get("assigned_org_id")

    @assigned_org_id.setter
    def assigned_org_id(self, new_value):
       self.assigned_org_id = new_value

    @property
    def published(self):
       return self.get("published")

    @published.setter
    def published(self, new_value):
       self.published = new_value

    @property
    def description(self):
       return self.get("description")

    @description.setter
    def description(self, new_value):
       self.description = new_value

    @property
    def category(self):
       return self.get("category")

    @category.setter
    def category(self, new_value):
       self.category = new_value

    @property
    def icon_url(self):
       return self.get("icon_url")

    @icon_url.setter
    def icon_url(self, new_value):
       self.icon_url = new_value

    @property
    def default_role_name(self):
       return self.get("default_role_name")

    @default_role_name.setter
    def default_role_name(self, new_value):
       self.default_role_name = new_value

    @property
    def default_role_id(self):
       return self.get("default_role_id")

    @default_role_id.setter
    def default_role_id(self, new_value):
       self.default_role_id = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'application_id': (str,),  # noqa: E501
            'application_name': (str,),  # noqa: E501
            'assigned_org_id': (str,),  # noqa: E501
            'published': (str,),  # noqa: E501
            'icon_url': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'category': (str,),  # noqa: E501
            'default_role_name': (str, none_type,),  # noqa: E501
            'default_role_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'application_id': 'application_id',  # noqa: E501
        'application_name': 'application_name',  # noqa: E501
        'assigned_org_id': 'assigned_org_id',  # noqa: E501
        'published': 'published',  # noqa: E501
        'icon_url': 'icon_url',  # noqa: E501
        'description': 'description',  # noqa: E501
        'category': 'category',  # noqa: E501
        'default_role_name': 'default_role_name',  # noqa: E501
        'default_role_id': 'default_role_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, application_id, application_name, assigned_org_id, published, *args, **kwargs):  # noqa: E501
        """ApplicationSummaryStatus - a model defined in OpenAPI

        Args:
            application_id (str): The ID of the application to which this organiastion is assigned.
            application_name (str): The name of the application
            assigned_org_id (str): The id of the organisation assigned to the application
            published (str): Whether or not this Application is published, and if so, how. An application that has been published somewhere will have high level details about it visible, such as its name and description. The enum values mean the following:   - no: This application is not published. It will only be visibile to users with       permission to access the application, or to administrators.   - public: This application is published to the public catalogue. Any user who       can request access to the organisation will see high level details about this       application. 

        Keyword Args:
            icon_url (str): A url pointing to an icon representing this application. . defaults to "https://storage.googleapis.com/agilicus/logo.svg"  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str): A brief description of the application.. [optional]  # noqa: E501
            category (str): A category used to group similar applications together.. [optional]  # noqa: E501
            default_role_name (str, none_type): The name of the default role of the application. This will be granted to users by default when an admin grants access to this application in response to a request for access. . [optional]  # noqa: E501
            default_role_id (str, none_type): The unique id the default role of the application. This will be granted to users by default when an admin grants access to this application in response to a request for access. . [optional]  # noqa: E501
        """

        icon_url = kwargs.get('icon_url', "https://storage.googleapis.com/agilicus/logo.svg")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.application_id = application_id
        self.application_name = application_name
        self.assigned_org_id = assigned_org_id
        self.published = published
        self.icon_url = icon_url
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    def __python_set(val):
        return set(val)
 
    required_properties = __python_set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, application_id, application_name, assigned_org_id, published, *args, **kwargs):  # noqa: E501
        """ApplicationSummaryStatus - a model defined in OpenAPI

        Args:
            application_id (str): The ID of the application to which this organiastion is assigned.
            application_name (str): The name of the application
            assigned_org_id (str): The id of the organisation assigned to the application
            published (str): Whether or not this Application is published, and if so, how. An application that has been published somewhere will have high level details about it visible, such as its name and description. The enum values mean the following:   - no: This application is not published. It will only be visibile to users with       permission to access the application, or to administrators.   - public: This application is published to the public catalogue. Any user who       can request access to the organisation will see high level details about this       application. 

        Keyword Args:
            icon_url (str): A url pointing to an icon representing this application. . defaults to "https://storage.googleapis.com/agilicus/logo.svg"  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str): A brief description of the application.. [optional]  # noqa: E501
            category (str): A category used to group similar applications together.. [optional]  # noqa: E501
            default_role_name (str, none_type): The name of the default role of the application. This will be granted to users by default when an admin grants access to this application in response to a request for access. . [optional]  # noqa: E501
            default_role_id (str, none_type): The unique id the default role of the application. This will be granted to users by default when an admin grants access to this application in response to a request for access. . [optional]  # noqa: E501
        """

        icon_url = kwargs.get('icon_url', "https://storage.googleapis.com/agilicus/logo.svg")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.application_id = application_id
        self.application_name = application_name
        self.assigned_org_id = assigned_org_id
        self.published = published
        self.icon_url = icon_url
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

