"""Perspective Functions.

The following functions offer various ways to interact with a
Perspective session from a Python script.
"""

from __future__ import print_function

__all__ = [
    "alterLogging",
    "closeDock",
    "closePage",
    "closePopup",
    "closeSession",
    "download",
    "getSessionInfo",
    "isAuthorized",
    "login",
    "logout",
    "navigate",
    "openDock",
    "openPopup",
    "print",
    "refresh",
    "sendMessage",
    "setTheme",
    "toggleDock",
    "togglePopup",
    "vibrateDevice",
]

import __builtin__ as builtins

from typing import Any, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common.script.adapters import PyJsonObjectAdapter

String = Union[str, unicode]


def alterLogging(
    remoteLoggingEnabled=False,  # type: Optional[bool]
    level="info",  # type: Optional[String]
    remoteLoggingLevel="warn",  # type: Optional[String]
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
):
    # type: (...) -> None
    """Changes Perspective Session logging attributes and levels.

    All parameters are optional, with the caveat that at least one of
    them needs to be used.

    Args:
        remoteLoggingEnabled: Will enable remote logging if True. Remote
            logging will send log events from the Session to the Gateway
            under the perspective.client logger if the meet the
            remoteLevel logging level requirement. Optional.
        level: The desired Session logging level. Possible values are:
            all, trace, debug, info, warn, error, fatal, off. The
            default is info. Optional.
        remoteLoggingLevel: The desired remote logging level. Possible
            values are: all, trace, debug, info, warn, error, fatal,
            off. The default is warn. Optional.
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(remoteLoggingEnabled, level, remoteLoggingLevel, sessionId, pageId)


def closeDock(id, sessionId="current_session", pageId="current_page"):
    # type: (String, Optional[String], Optional[String]) -> None
    """Closes a docked view.

    Args:
        id: The unique, preconfigured dock ID for the docked View. Is
            specified when a View is assigned as docked for a particular
            Page (in Page Configuration).
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(id, sessionId, pageId)


def closePage(
    message=None,  # type: Optional[String]
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
):
    # type: (...) -> None
    """Closes the page with the given page id or the current page if no
    page id is provided.

    If a message is provided, it is displayed on the page when the page
    closes. Otherwise, the default message (set in the Project
    Properties) is displayed.

    Args:
        message: The message to display when the page closes. If
            omitted, the default message (set in the Project Properties)
            is shown. Optional.
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the page to be closed. If omitted, the
            current pageId is used. Optional.
    """
    builtins.print(message, sessionId, pageId)


def closePopup(id, sessionId="current_session", pageId="current_page"):
    # type: (String, Optional[String], Optional[String]) -> None
    """Closes a popup View.

    Args:
        id: The unique identifier for the the popup, given to the popup
            when first opened. If given an empty string, then the most
            recently focused popup will be closed.
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(id, sessionId, pageId)


def closeSession(message=None, sessionId="current_session"):
    # type: (Optional[String], Optional[String]) -> None
    """Closes the Perspective Session with the given Session ID or the
    current Session if no ID is provided.

    If a message is provided, it is displayed on the page when the
    Session closes. Otherwise the default message (set in the Project
    Properties) is displayed.

    Args:
        message: The message to display when the Session closes. If
            omitted, the default message (set in the Project Properties)
            is shown. Optional.
        sessionId: Identifier of the Session to be closed. If omitted,
            the current sessionId is used. Optional.
    """
    builtins.print(message, sessionId)


def download(
    filename,  # type: String
    data,  # type: Any
    contentType=None,  # type: Optional[String]
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
):
    # type: (...) -> None
    """Downloads data from the gateway to a device running a Session.

    Args:
        filename: Suggested name for the downloaded file.
        data: The data to be downloaded. May be a String, a byte[], or
            an InputStream. Strings will be written with in "utf-8"
            encoding.
        contentType: Value for the "Content-Type" header. Example:
            "text/plain; charset=utf-8". Optional.
        sessionId: Identifier of the Session to target. If omitted the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(filename, data, contentType, sessionId, pageId)


def getSessionInfo(
    usernameFilter=None,  # type: Optional[String]
    projectFilter=None,  # type: Optional[String]
):
    # type: (...) -> List[PyJsonObjectAdapter]
    """Returns information about one or more Perspective Sessions.

    The information returned by this function is a combination of
    information available on the perspective Sessions status page on the
    Gateway, and some Session props (id and userAgent).

    Args:
        usernameFilter: A filter based on logged in user. Optional.
        projectFilter: A filter based on the project name. Optional.

    Returns:
        A list of objects (PyJsonObjectAdapter).
    """
    builtins.print(usernameFilter, projectFilter)
    return [PyJsonObjectAdapter(None)]


def isAuthorized(isAllOf, securityLevels):
    # type: (bool, List[String]) -> bool
    """Checks if the user in the current Session is authorized against a
    target collection of security levels.

    Args:
        isAllOf: True if the current user must have all of the given
            security levels to be authorized. False if the current user
            must have at least one of the given security levels to be
            authorized.
        securityLevels: An array of string paths to a security level
            node in the form of "Path/To/Node". Each level in the tree
            is delimited by a forward slash character. The public node
            is never a part of the path.

    Returns:
        True if the user in the current Session is authorized, False
        otherwise.
    """
    builtins.print(isAllOf, securityLevels)
    return True


def login(sessionId="current_session", pageId="current_page", forceAuth=False):
    # type: (Optional[String], Optional[String], Optional[bool]) -> None
    """Triggers a login event that will allow the user to login with the
    project's configured Identity Provider (IdP).

    For this function to work, an Identity Provider must be set in
    Perspective project properties. This is particularly useful when you
    want it to be possible to start a Session without authentication and
    sign in to access certain restricted features.

    Args:
        sessionId: Identifier of the Session to target. If omitted the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        forceAuth: Determines if Ignition should ask the Identity
            Provider to re-authenticate the user, even if the user is
            already signed into the Identity Provider. If set to True,
            then the Identity Provider will ask the user to re-enter
            their credentials. If set to False, then the Gateway will
            request that the Identity Provider use the last provided
            credentials for the Session, potentially allowing
            re-authentication without requiring the user to re-type
            their credentials. Note that support for this argument is
            determined by the Identity Provider; the IdP may choose to
            ignore this request. If this parameter is omitted, then the
            function will use the re-authentication setting defined
            under Project Properties. Optional.
    """
    builtins.print(sessionId, pageId, forceAuth)


def logout(sessionId="current_session", pageId="current_page"):
    # type: (Optional[String], Optional[String]) -> None
    """Triggers a logout event, which will log the user out.

    For this function to work, an Identity Provider must be set in the
    Perspective project properties.

    Args:
        sessionId: Identifier of the Session to target. If omitted the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(sessionId, pageId)


def navigate(
    page,  # type: String
    url=None,  # type: Optional[String]
    view=None,  # type: Optional[String]
    params=None,  # type: Optional[Dict[String, String]]
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
):
    # type: (...) -> None
    """Navigate the Session to a specified view or mounted page.

    The function can be used in three different ways, depending on which
    parameter is specified:
        page: navigates to a perspective-page
        url: navigates to a Web address, so the function can be used to
            navigate the user to a Web portal, search engine, or other
            Website. This parameter is specified via keyword argument
        view: navigates to a view. Note that using this parameter does
            not modify the Web browser's address bar, so the browser's
            history will not contain a listing for the new view. This
            parameter is specified via keyword argument

    Args:
        page: The URL of a Perspective page to navigate to.
        url: The URL of a Web address to navigate to. If the page or
            view parameters are specified, then this parameter is
            ignored. Optional.
        view: If specified, will navigate to a specific view. Navigating
            to a view via this parameter does not change the address in
            the Web browser. Thus the Web browser's back button will not
            be able to return the user to the previous view. If the page
            parameter is specified, then this parameter is ignored.
            Optional.
        params: Used only in conjunction with the view parameter,
            Dictionary of values to pass to any parameters on the view.
            Optional.
        sessionId: Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different Session, then the pageId parameter
            must be included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(page, url, view, params, sessionId, pageId)


def openDock(
    id,  # type: String
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
    params=None,  # type: Optional[Dict[String, String]]
):
    # type: (...) -> None
    """Opens a docked View.

    Requires the preconfigured dock ID for the view.

    Args:
        id: The unique, preconfigured 'Dock ID' for the docked View. Is
            specified when a View is assigned as docked for a particular
            Page (in Page Configuration).
        sessionId: Identifier of the Session to target. If omitted the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        params: Parameters that can be passed into the docked view. Must
            match the docked views View Parameters. Optional.
    """
    builtins.print(id, sessionId, pageId, params)


def openPopup(
    id,  # type: String
    view,  # type: String
    params=None,  # type: Optional[Dict[String, Any]]
    title="",  # type: Optional[String]
    position=None,  # type: Optional[Dict[String, int]]
    showCloseIcon=True,  # type: Optional[bool]
    draggable=True,  # type: Optional[bool]
    resizable=False,  # type: Optional[bool]
    modal=False,  # type: Optional[bool]
    overlayDismiss=False,  # type: Optional[bool]
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
):
    # type: (...) -> None
    """Open a popup view over the given page.

    Args:
        id: A unique popup string. Will be used to close the popup from
            other popup or script actions.
        view: The path to the View to use in the popup.
        params: Dictionary of key-value pairs to us as input parameters
            to the View. Optional.
        title: Text to display in the title bar. If no value or an empty
            string are given, the title bar will not be displayed.
            Defaults to an empty string. Optional.
        position: Dictionary of key-value pairs to use for position.
            Possible position keys are: left, top, right, bottom, width,
            height. Defaults to the center of the window. Optional.
        showCloseIcon: Will show the close icon if True. Defaults to
            True. Optional.
        draggable: Will allow the popup to be dragged if True. Defaults
            to True. Optional.
        resizable: Will allow the popup to be resized if True. Defaults
            to False. Optional.
        modal: Will make the popup modal if True. A modal popup is the
            only view the user can interact with. Defaults to False.
            Optional.
        overlayDismiss: Will allow the user to dismiss and close a modal
            popup by clicking outside of it if True. Defaults to False.
            Optional.
        sessionId: Identifier of the Session to target. If omitted the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(
        id,
        view,
        params,
        title,
        position,
        showCloseIcon,
        draggable,
        resizable,
        modal,
        overlayDismiss,
        sessionId,
        pageId,
    )


def print(
    message,  # type: String
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
    destination="client",  # type: Optional[String]
):
    # type: (...) -> None
    """Sends print statements to the scripting console when in the
    Designer.

    When in a Session, sends print statements to the output console.
    This function makes scripting diagnostics easier.

    Args:
        message: The print statement that will be displayed on the
            console.
        sessionId: Identifier of the Session to target. If omitted the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        destination: Where the message should be printed. If specified,
            must be "client", "gateway", or "all". Default is "client".
            Optional.
    """
    builtins.print(message, sessionId, pageId, destination)


def refresh(sessionId="current_session", pageId="current_page"):
    # type: (Optional[String], Optional[String]) -> None
    """Triggers a refresh of the page.

    Note:
        This method should not be confused with the refreshBinding
        component method, which automatically fires a binding on a
        Perspective component property.

    Args:
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(sessionId, pageId)


def sendMessage(
    messageType,  # type: String
    payload,  # type: Dict[String, String]
    scope="page",  # type: Optional[String]
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
):
    # type: (...) -> None
    """Send a message to a message handler within the same Session.

    Args:
        messageType: The message type that will be invoked. Message
            handlers configured within the project are listening for
            messages of a specific messageType.
        payload: A python dictionary representing any parameters that
            will be passed to the message handler.
        scope: The scope that the message should be delivered to. Valid
            values are "Session", "page", or "view". If omitted, "page"
            will be used. Optional.
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used. Optional.
    """
    builtins.print(messageType, payload, scope, sessionId, pageId)


def setTheme(name, sessionId="current_session", pageId="current_page"):
    # type: (String, Optional[String], Optional[String]) -> None
    """Changes the theme in a page to the specified theme.

    Note that this function only changes the theme for a single page,
    not the entire session. To change the theme for a session, write
    directly to the session.theme property instead.

    Args:
        name: The theme name to switch to. Possible values are "dark" or
            "light".
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(name, sessionId, pageId)


def toggleDock(
    id,  # type: String
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
    params=None,  # type: Optional[Dict[String, String]]
):
    # type: (...) -> None
    """Toggles a docked View.

    Args:
        id: The unique, preconfigured 'Dock ID' for the docked View. Is
            specified when a View is assigned as docked for a particular
            Page (in Page Configuration).
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        params: Parameters that can be passed into the docked view. Must
            match the docked views View Parameters. Optional.
    """
    builtins.print(id, sessionId, pageId, params)


def togglePopup(
    id,  # type: String
    view,  # type: String
    params,  # type: Optional[Dict[String, Any]]
    title="",  # type: Optional[String]
    position=None,  # type: Optional[Dict[String, int]]
    showCloseIcon=True,  # type: Optional[bool]
    draggable=True,  # type: Optional[bool]
    resizable=False,  # type: Optional[bool]
    modal=False,  # type: Optional[bool]
    overlayDismiss=False,  # type: Optional[bool]
    sessionId="current_session",  # type: Optional[String]
    pageId="current_page",  # type: Optional[String]
):
    # type: (...) -> None
    """Toggles a popup view.

    Will open up the popup if it has not been opened yet. Otherwise, it
    will close the currently opened popup.

    Args:
        id: A unique popup string. Will be used to close the popup from
            other popup or script actions.
        view: The path to the View to use in the popup.
        params: Dictionary of key-value pairs to us as input parameters
            to the View. Optional.
        title: Text to display in the title bar. If no value or an empty
            string are given, the title bar will not be displayed.
            Defaults to an empty string. Optional.
        position: Dictionary of key-value pairs to use for position.
            Possible position keys are: left, top, right, bottom, width,
            height. Defaults to the center of the window. Optional.
        showCloseIcon: Will show the close icon if True. Defaults to
            True. Optional.
        draggable: Will allow the popup to be dragged if True. Defaults
            to True. Optional.
        resizable: Will allow the popup to be resized if True. Defaults
            to False. Optional.
        modal: Will make the popup modal if True. A modal popup is the
            only view the user can interact with. Defaults to False.
            Optional.
        overlayDismiss: Will allow the user to dismiss and close a modal
            popup by clicking outside of it if True. Defaults to False.
            Optional.
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. When targeting a
            different Session, then the pageId parameter must be
            included in the call. Optional.
        pageId: Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(
        id,
        view,
        params,
        title,
        position,
        showCloseIcon,
        draggable,
        resizable,
        modal,
        overlayDismiss,
        sessionId,
        pageId,
    )


def vibrateDevice(duration, sessionId="current_session"):
    # type: (int, Optional[String]) -> None
    """When called from the Perspective App, will cause the
    device to vibrate for the specified number of milliseconds.

    Note:
        iOS vibration duration is fixed. This function will cause an iOS
        device to vibrate for its default duration, 0.4 seconds
        (400 milliseconds).

    Args:
        duration: The duration in milliseconds to vibrate the device.
        sessionId: Identifier of the Session to target. If omitted, the
            current Session will be used automatically. Optional.
    """
    builtins.print(duration, sessionId)
