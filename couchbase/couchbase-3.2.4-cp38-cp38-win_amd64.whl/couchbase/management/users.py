from datetime import datetime

from couchbase.options import OptionBlock, OptionBlockTimeOut, timedelta, forward_args
from couchbase.management.generic import GenericManager
from couchbase.auth import AuthDomain
from typing import *
from couchbase.exceptions import HTTPException, ErrorMapper, InvalidArgumentException, FeatureNotFoundException
from copy import deepcopy


class GroupNotFoundException(HTTPException):
    """ The RBAC Group was not found"""


class UserNotFoundException(HTTPException):
    """ The RBAC User was not found"""


class UserErrorHandler(ErrorMapper):
    @staticmethod
    def mapping():
        # type (...)->Mapping[str, CBErrorType]
        return {HTTPException: {'Unknown group': GroupNotFoundException,
                                'Unknown user': UserNotFoundException,
                                'Not found': FeatureNotFoundException,
                                'Method Not Allowed': FeatureNotFoundException},
                }


@UserErrorHandler.wrap
class UserManager(GenericManager):
    def __init__(self,  # type: UserManager
                 admin):
        """User Manager
        Programmatic access to the user management REST API:
        https://docs.couchbase.com/server/current/rest-api/rbac.html

        Unless otherwise indicated, all objects SHOULD be immutable.
        :param parent_cluster: """
        super(UserManager, self).__init__(admin)

    def get_user(self,
                 username,  # type: str
                 *options,  # type: GetUserOptions
                 **kwargs   # type: Any
                 ):
        # type: (...) -> UserAndMetadata
        """
        Gets a user.

        :param str username: ID of the user.
        :param options: GetUserOptions
        :param Any kwargs: override corresponding values in the options.

        :returns: An instance of UserAndMetadata.

        :raises: UserNotFoundException
        :raises: InvalidArgumentsException
        Any exceptions raised by the underlying platform
        """

        # Implementation Notes
        # When parsing the "get" and "getAll" responses,
        # take care to distinguish between roles assigned directly to the user (role origin with type="user") and
        # roles inherited from groups (role origin with type="group" and name=<group name>).
        # If the server response does not include an "origins" field for a role,
        # then it was generated by a server version prior to 6.5 and the SDK MUST treat the role as if it had a
        # single origin of type="user".
        final_args = forward_args(kwargs, *options)
        domain = final_args.pop("domain_name", "local")
        timeout = final_args.pop("timeout", None)
        return UserAndMetadata.load_from_server(
            self._admin_bucket.user_get(username,
                                        domain,
                                        timeout).value)

    def get_all_users(self,
                      *options,  # type: GetAllUsersOptions
                      **kwargs  # type: Any
                      ):
        # type: (...) -> Iterable[UserAndMetadata]
        """
        Gets all users.

        :param options: GetAllUsersOptions
        :param Any kwargs: override corresponding values in the options.

        :return: An iterable collection of UserAndMetadata.
        """
        final_args = forward_args(kwargs, *options)
        domain = final_args.get("domain_name", "local")
        timeout = final_args.get("timeout", None)
        return list(map(lambda u: UserAndMetadata.load_from_server(u),
                        self._admin_bucket.users_get(domain, timeout).value))

    def upsert_user(self,
                    user,     # type: User
                    *options,  # type: UpsertUserOptions
                    **kwargs  # type: Any
                    ):
        """
        Creates or updates a user.

        :param User user: the new version of the user.
        :param options: UpsertUserOptions
        :param Any kwargs: override corresponding values in the options.

        :raises: InvalidArgumentsException
        """

        # Implementation Notes
        #
        # When building the PUT request to send to the REST endpoint, implementations MUST omit the "password" property
        # if it is not present in the given User domain object (so that the password is only changed if the calling code
        # provided a new password).

        final_args = forward_args(kwargs, *options)
        domain = final_args.pop("domain_name", "local")
        final_args.update({k: v for k, v in user.as_dict.items() if k in {
                          'password', 'roles', 'name', 'groups'}})
        self._admin_bucket.user_upsert(user.username, domain, **final_args)

    def drop_user(self,
                  username,  # type: str
                  *options,  # type: DropUserOptions
                  **kwargs   # type: Any
                  ):
        """
        Removes a user.

        :param str username: ID of the user.
        :param options: DropUserOptions
        :param Any kwargs: override corresponding values in the options.

        :raises: UserNotFoundException
        :raises: InvalidArgumentsException

        Any exceptions raised by the underlying platform
        """
        final_args = forward_args(kwargs, *options)
        domain = final_args.pop("domain_name", "local")
        timeout = final_args.get("timeout", None)
        self._admin_bucket.user_remove(username, domain, timeout)

    def get_roles(self,
                  *options,  # type: GetRolesOptions
                  **kwargs   # type: Any
                  ):
        # type: (...) -> Iterable[RoleAndDescription]
        """
        Returns the roles supported by the server.

        :param options: GetRolesOptions
        :param Any kwargs: override corresponding values in the options.

        :return: An iterable collection of RoleAndDescription.
        """

        final_args = forward_args(kwargs, *options)
        timeout = final_args.get("timeout", None)
        return list(map(lambda r: RoleAndDescription.load_from_server(r),
                        self._admin_bucket.get_roles(timeout).value))

    def get_group(self,
                  group_name,   # type: str
                  *options,     # type: GetGroupOptions
                  **kwargs      # type: Any
                  ):
        # type: (...) -> Group
        """
        Gets a group.

        :param str group_name: name of the group to get.
        :param options: GetRolesOptions
        :param Any kwargs: override corresponding values in the options.

        :return: An instance of Group.

        :raises: GroupNotFoundException
        :raises: InvalidArgumentsException
        Any exceptions raised by the underlying platform
        """

        final_args = forward_args(kwargs, *options)
        timeout = final_args.get("timeout", None)
        return Group.load_from_server(
            self._admin_bucket.group_get(group_name, timeout).value)

    def get_all_groups(self,
                       *options,    # type: GetAllGroupsOptions
                       **kwargs     # type: Any
                       ):
        # type: (...) -> Iterable[Group]
        """
        Get all groups.

        :param timedelta timeout: the time allowed for the operation to be terminated. This is controlled by the client.

        :returns: An iterable collection of Group.
        """

        final_args = forward_args(kwargs, *options)
        timeout = final_args.get("timeout", None)
        return list(map(lambda g: Group.load_from_server(g),
                        self._admin_bucket.groups_get(timeout).value))

    def upsert_group(self,
                     group,     # type: Group
                     *options,  # type: UpsertGroupOptions
                     **kwargs   # type: Any
                     ):
        """
        Creates or updates a group.

        :param Group group: the new version of the group.
        :param options: UpsertGroupOptions
        :param Any kwargs: override corresponding values in the options.

        :raises: InvalidArgumentsException
        Any exceptions raised by the underlying platform
        """
        # This endpoint accepts application/x-www-form-urlencoded and requires the data be sent as form data.
        # The name/id should not be included in the form data.
        # Roles should be a comma separated list of strings.
        # If, only if, the role contains a bucket name then the rolename should be suffixed
        # with[<bucket_name>] e.g. bucket_full_access[default],security_admin.

        final_args = forward_args(kwargs, *options)
        final_args.update({k: v for k, v in group.as_dict.items() if k in {
                          'roles', 'description', 'ldap_group_reference'}})
        self._admin_bucket.group_upsert(group.name, **final_args)

    def drop_group(self,
                   group_name,  # type: str
                   *options,    # type: DropGroupOptions
                   **kwargs     # type: Any
                   ):
        """
        Removes a group.

        :param str group_name: name of the group.
        :param options: DropGroupOptions
        :param Any kwargs: override corresponding values in the options.

        :raises: GroupNotFoundException
        :raises: InvalidArgumentsException
        """
        self._admin_bucket.http_request("/settings/rbac/groups/{}".format(group_name), method='DELETE',
                                        **forward_args(kwargs, *options))


class SetHelper(object):

    @classmethod
    def to_set(cls, value, valid_type, display_name):

        if not value:
            return value
        elif isinstance(value, set):
            cls.validate_all_set_types(value, valid_type, display_name)
            return value
        elif isinstance(value, list):
            cls.validate_all_set_types(value, valid_type, display_name)
            return set(value)
        elif isinstance(value, tuple):
            cls.validate_all_set_types(value, valid_type, display_name)
            return set(value)
        elif isinstance(value, valid_type):
            return set([value])
        else:
            raise InvalidArgumentException(
                '{} must be of type {}.'.format(display_name,
                                                valid_type.__name__))

    @classmethod
    def validate_all_set_types(cls, value, valid_type, display_name):

        if all(map(lambda r: isinstance(r, type), value)):
            raise InvalidArgumentException(
                '{} must contain only objects of type {}.'.format(display_name,
                                                                  valid_type.__name__))


class Role(object):

    def __init__(self,
                 name=None,         # type: str
                 bucket=None,       # type: str
                 scope=None,        # type: str
                 collection=None,   # type: str
                 ):

        if not name:
            raise InvalidArgumentException('A role must have a name')

        self._name = name
        self._bucket = bucket
        self._scope = scope
        self._collection = collection

    @property
    def name(self):
        # type: (...) -> str
        return self._name

    @property
    def bucket(self):
        # type: (...) -> str
        return self._bucket

    @property
    def scope(self):
        # type: (...) -> str
        return self._scope

    @property
    def collection(self):
        # type: (...) -> str
        return self._collection

    def to_server_str(self):
        if self.bucket and self.scope and self.collection:
            return '{0}[{1}:{2}:{3}]'.format(self.name,
                                             self.bucket,
                                             self.scope,
                                             self.collection)
        elif self.bucket and self.scope:
            return '{0}[{1}:{2}]'.format(self.name,
                                         self.bucket,
                                         self.scope)
        elif self.bucket:
            return '{0}[{1}]'.format(self.name,
                                     self.bucket)
        else:
            return self.name

    def as_dict(self):
        return {
            'name': self._name,
            'bucket': self._bucket,
            'scope': self._scope,
            'collection': self._collection
        }

    def __eq__(self, other):
        return (isinstance(other, type(self))
                and (self._name, self._bucket, self._scope, self._collection)
                == (other._name, other._bucket, other._scope, other._collection))

    def __hash__(self):
        return hash((self._name, self._bucket, self._scope, self._collection))

    @classmethod
    def load_from_server(cls, json_data):
        return cls(
            name=json_data.get('role', None),
            bucket=json_data.get('bucket_name', None),
            scope=json_data.get('scope_name', None),
            collection=json_data.get('collection_name', None)
        )


class RoleAndDescription(object):

    def __init__(self,
                 role=None,          # type: Role
                 display_name=None,  # type: str
                 description=None,   # type: str
                 ce=None,            # type: bool
                 ):

        self._role = role
        self._display_name = display_name
        self._description = description
        self._ce = ce

    @property
    def role(self):
        # type: (...) -> Role
        return self._role

    @property
    def display_name(self):
        # type: (...) -> str
        return self._display_name

    @property
    def description(self):
        # type: (...) -> str
        return self._description

    @property
    def ce(self):
        # type: (...) -> bool
        return self._ce

    @classmethod
    def load_from_server(cls, json_data):
        return cls(
            role=Role.load_from_server(json_data),
            display_name=json_data.get('name', None),
            description=json_data.get('desc', None),
            ce=json_data.get('ce', None)
        )


class RoleAndOrigins(object):

    def __init__(self,
                 role=None,  # type: Role
                 origins=[]  # type: List[Origin]
                 ):

        self._role = role
        self._origins = origins

    @property
    def role(self):
        # type: (...) -> Role
        return self._role

    @property
    def origins(self):
        # type: (...) -> list[Origin]
        return self._origins

    @classmethod
    def load_from_server(cls, json_data):

        # RBAC prior to v6.5 does not have origins
        origin_data = json_data.get('origins', None)

        return cls(
            role=Role.load_from_server(json_data),
            origins=list(map(lambda o: Origin(**o), origin_data))
            if origin_data else []
        )


class Origin(object):
    """Indicates why the user has a specific role.
    If the type is "user" it means the role is assigned directly to the user. If the type is "group" it means the role is inherited from the group identified by the "name" field."""

    def __init__(self,
                 type=None,  # type: str
                 name=None   # type: str
                 ):

        self._type = type
        self._name = name

    @property
    def type(self):
        # type: (...) -> str
        return self._type

    @property
    def name(self):
        # type: (...) -> str
        return self._name


class User(object):

    def __init__(self,
                 username=None,      # type: str
                 display_name=None,  # type: str
                 groups=None,        # type: Set[str]
                 roles=None,         # type: Set[Role]
                 password=None       # type: str
                 ):

        if not username:
            raise InvalidArgumentException('A user must have a username')

        self._username = username
        self._display_name = display_name
        self._groups = SetHelper.to_set(groups, str, 'Groups')
        self._roles = SetHelper.to_set(roles, Role, 'Roles')
        self._password = password

    @property
    def username(self):
        # type: (...) -> str
        return self._username

    @property
    def display_name(self):
        # type: (...) -> str
        return self._display_name

    @display_name.setter
    def display_name(self,
                     value  # type: str
                     ):
        self._display_name = value

    @property
    def groups(self):
        # type: (...) -> Set[str]
        """names of the groups"""
        return self._groups

    @groups.setter
    def groups(self,
               value  # type: Set[str]
               ):
        self._groups = SetHelper.to_set(value, str, 'Groups')

    @property
    def roles(self):
        # type: (...) -> Set[Role]
        """only roles assigned directly to the user (not inherited from groups)"""
        return self._roles

    @roles.setter
    def roles(self,
              value  # type: Set[Role]
              ):
        self._roles = SetHelper.to_set(value, Role, 'Roles')

    def password(self, value):
        self._password = value

    password = property(None, password)

    @property
    def as_dict(self):
        output = {
            'username': self.username,
            'name': self.display_name,
            'password': self._password
        }

        if self.roles:
            output['roles'] = list(self.roles)

        if self.groups:
            output['groups'] = list(self.groups)

        return output

    def __eq__(self, other):
        return (isinstance(other, type(self))
                and (self._username, self._display_name, self._groups, self._roles)
                == (other._username, other._display_name, other._groups, other._roles))

    def __hash__(self):
        return hash((self._username, self._display_name,
                    self._groups, self._roles))

    @classmethod
    def load_from_server(cls, json_data, roles=None):

        user_roles = roles
        if not user_roles:
            set(map(lambda r: Role.load_from_server(r),
                    json_data.get('roles')))

        # RBAC prior to v6.5 does not have groups
        group_data = json_data.get('groups', None)

        return cls(
            username=json_data.get('id'),
            display_name=json_data.get('name'),
            roles=user_roles,
            groups=set(group_data) if group_data else None
        )


class UserAndMetadata(object):
    """Models the "get user" / "get all users" response.
    Associates the mutable properties of a user with derived properties such as the effective roles inherited from groups."""

    def __init__(self,
                 domain=None,            # type: AuthDomain
                 user=None,              # type: User
                 effective_roles=[],     # type: List[RoleAndOrigins]
                 password_changed=None,  # type: datetime
                 external_groups=None,   # type: Set[str]
                 **kwargs                # type: Any
                 ):

        self._domain = domain
        self._user = user
        self._effective_roles = effective_roles
        self._password_changed = password_changed
        self._external_groups = external_groups
        self._raw_data = kwargs.get('raw_data', None)

    @property
    def domain(self):
        # type: (...) -> AuthDomain
        """ AuthDomain is an enumeration with values "local" and "external".
        It MAY alternatively be represented as String."""
        return self._domain

    @property
    def user(self):
        # type: (...) -> User
        """- returns a new mutable User object each time this method is called.
        Modifying the fields of the returned User MUST have no effect on the UserAndMetadata object it came from."""
        return deepcopy(self._user)

    @property
    def effective_roles(self):
        # type: (...) -> List[RoleAndOrigins]
        """all roles, regardless of origin."""
        return self._effective_roles

    @property
    def password_changed(self):
        # type: (...) -> Optional[datetime]
        return self._password_changed

    @property
    def external_groups(self):
        # type: (...) -> Set[str]
        return self._external_groups

    @property
    def raw_data(self):
        # type: (...) -> Dict
        return self._raw_data

    @classmethod
    def load_from_server(cls, json_data):

        effective_roles = list(map(lambda r: RoleAndOrigins.load_from_server(r),
                                   json_data.get('roles')))

        user_roles = set(r.role for r in effective_roles if any(map(lambda o: o.type == 'user', r.origins))
                         or len(r.origins) == 0)

        # RBAC prior to v6.5 does not have groups
        ext_group_data = json_data.get('external_groups', None)

        # password_change_date is optional
        pw_data = json_data.get('password_change_date', None)

        return cls(
            domain=AuthDomain.from_str(json_data.get('domain')),
            effective_roles=effective_roles,
            user=User.load_from_server(json_data, roles=user_roles),
            password_changed=datetime.strptime(pw_data,
                                               '%Y-%m-%dT%H:%M:%S.%fZ') if pw_data else None,
            external_groups=set(ext_group_data) if ext_group_data else None,
            raw_data=json_data
        )


class Group(object):
    def __init__(self,
                 name=None,                 # type: str
                 description=None,          # type: str
                 roles=None,                # type: Set[Role]
                 ldap_group_reference=None,  # type: str
                 **kwargs                   # type: Any
                 ):

        if not name:
            raise InvalidArgumentException('A group must have a name')

        self._name = name
        self._description = description
        self._roles = SetHelper.to_set(roles, Role, 'Roles')
        self._ldap_group_reference = ldap_group_reference
        self._raw_data = kwargs.get('raw_data', None)

    @property
    def name(self):
        # type: (...) -> str
        return self._name

    @property
    def description(self):
        # type: (...) -> str
        return self._description

    @description.setter
    def description(self,
                    value  # type: str
                    ):
        self._description = value

    @property
    def roles(self):
        # type: (...) -> Set[Role]
        return self._roles

    @roles.setter
    def roles(self,
              value  # type: Set[Role]
              ):
        self._roles = SetHelper.to_set(value, Role, 'Roles')

    @property
    def ldap_group_reference(self):
        # type: (...) -> str
        return self._ldap_group_reference

    @ldap_group_reference.setter
    def ldap_group_reference(self,
                             value  # type: str
                             ):
        self._ldap_group_reference = value

    @property
    def raw_data(self):
        # type: (...) -> Dict
        return self._raw_data

    @property
    def as_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'roles': self.roles,
            'ldap_group_reference': self.ldap_group_reference
        }

    def __eq__(self, other):
        return (isinstance(other, type(self))
                and (self._name, self._description, self._roles, self._ldap_group_reference)
                == (other._name, other._description, other._roles, other._ldap_group_reference))

    @classmethod
    def load_from_server(cls, json_data):
        return cls(
            json_data.get('id'),
            description=json_data.get('description'),
            roles=set(map(lambda r: Role.load_from_server(
                r), json_data.get('roles'))),
            ldap_group_referenc=json_data.get('ldap_group_ref')
        )


class UserOptions(OptionBlock):

    def __init__(self,
                 domain_name="local",     # type: str
                 timeout=None,            # type: timedelta
                 **kwargs                 # type: Any
                 ):
        """
        An OptionBlock with an auth domain and timeout

        :param str domain_name: name of the user domain (local | external). Defaults to local.
        :param timedelta timeout: the time allowed for the operation to be terminated. This is controlled by the client.
        :param kwargs: parameters to pass in to the OptionBlock
        """
        super(UserOptions, self).__init__(domain_name=domain_name,
                                          timeout=timeout,
                                          **kwargs)


class GetUserOptions(UserOptions):
    pass


class GetAllUsersOptions(UserOptions):
    pass


class UpsertUserOptions(UserOptions):
    pass


class DropUserOptions(UserOptions):
    pass


class GetRolesOptions(OptionBlockTimeOut):
    pass


class DropGroupOptions(OptionBlockTimeOut):
    pass


class GetGroupOptions(OptionBlockTimeOut):
    pass


class GetAllGroupsOptions(OptionBlockTimeOut):
    pass


class UpsertGroupOptions(OptionBlockTimeOut):
    pass
