# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,invalid-name,abstract-method,method-hidden
"""
RESTful API Rules
-----------------------
"""
import logging

from flask_login import current_user
from flask_restx_patched._http import HTTPStatus
from permission import Rule as BaseRule
from wbia.web.extensions.api import abort

log = logging.getLogger(__name__)  # pylint: disable=invalid-name


class DenyAbortMixin(object):
    """
    A helper permissions mixin raising an HTTP Error (specified in
    ``DENY_ABORT_CODE``) on deny.

    NOTE: Apply this mixin before Rule class so it can override NotImplemented
    deny method.
    """

    DENY_ABORT_HTTP_CODE = HTTPStatus.FORBIDDEN
    DENY_ABORT_MESSAGE = None

    def deny(self):
        """
        Abort HTTP request by raising HTTP error exception with a specified
        HTTP code.
        """
        return abort(code=self.DENY_ABORT_HTTP_CODE, message=self.DENY_ABORT_MESSAGE)


class Rule(BaseRule):
    """
    Experimental base Rule class that helps to automatically handle inherited
    rules.
    """

    def base(self):
        # XXX: it handles only the first appropriate Rule base class
        # TODO: PR this case to permission project
        for base_class in self.__class__.__bases__:
            if issubclass(base_class, Rule):
                if base_class in {Rule, BaseRule}:
                    continue
                return base_class()
        return None


class AllowAllRule(Rule):
    """
    Helper rule that always grants access.
    """

    def check(self):
        return True


class ActiveUserRoleRule(DenyAbortMixin, Rule):
    """
    Ensure that the current_user is activated.
    """

    def check(self):
        # Do not override DENY_ABORT_HTTP_CODE because inherited classes will
        # better use HTTP 403/Forbidden code on denial.
        self.DENY_ABORT_HTTP_CODE = HTTPStatus.UNAUTHORIZED
        # NOTE: `is_active` implies `is_authenticated`.
        return current_user.is_active


class PasswordRequiredRule(DenyAbortMixin, Rule):
    """
    Ensure that the current user has provided a correct password.
    """

    def __init__(self, password, **kwargs):
        super(PasswordRequiredRule, self).__init__(**kwargs)
        self._password = password

    def check(self):
        return current_user.password == self._password


class AdminRoleRule(ActiveUserRoleRule):
    """
    Ensure that the current_user has an Admin role.
    """

    def check(self):
        return current_user.is_admin


class InternalRoleRule(ActiveUserRoleRule):
    """
    Ensure that the current_user has an Internal role.
    """

    def check(self):
        return current_user.is_internal


class PartialPermissionDeniedRule(Rule):
    """
    Helper rule that must fail on every check since it should never be checked.
    """

    def check(self):
        raise RuntimeError('Partial permissions are not intended to be checked')
