from dataclasses import dataclass
import datetime
from typing import Dict, List

from grid.sdk import env
from grid.sdk._gql.queries import get_user_basic_info, get_user_teams


@dataclass(frozen=True)
class User:
    """Representation of generic information about the user in grid.

    Attributes
    ----------
    user_id
        The internal grid ID assigned to the user.
    username
        The normal 'name' which the user is associated with.
    first_name
        The real-life first name of the user.
    last_name
        The real-life last name of the user.
    """
    user_id: str
    username: str
    first_name: str
    last_name: str


def user_from_logged_in_account() -> "User":
    resp = get_user_basic_info()
    if not resp["isVerified"]:
        raise PermissionError(
            f"User account not yet verified. Verify your "
            f"account at {env.GRID_URL}/#/verification"
        )
    if not resp["completedSignup"]:
        raise PermissionError(
            f"You haven't yet completed registration. Please complete "
            f"registration at {env.GRID_URL}/#/registration"
        )
    if resp["isBlocked"]:
        raise PermissionError(
            f"Your account with username `{resp['username']}` has been "
            f"suspended. Please reach out to support at support@grid.ai"
        )

    return User(
        user_id=resp["userId"],
        username=resp["username"],
        first_name=resp["firstName"],
        last_name=resp["lastName"],
    )


@dataclass(frozen=True)
class SDKUser(User):
    email: str
    is_verified: bool
    is_blocked: bool
    completed_signup: bool


def sdkuser_from_logged_in_account() -> "SDKUser":
    resp = get_user_basic_info()
    if not resp["isVerified"]:
        raise PermissionError(
            f"User account not yet verified. Verify your "
            f"account at {env.GRID_URL}/#/verification"
        )
    if not resp["completedSignup"]:
        raise PermissionError(
            f"You haven't yet completed registration. Please complete "
            f"registration at {env.GRID_URL}/#/registration"
        )
    if resp["isBlocked"]:
        raise PermissionError(
            f"Your account with username `{resp['username']}` has been "
            f"suspended. Please reach out to support at support@grid.ai"
        )

    return SDKUser(
        user_id=resp["userId"],
        username=resp["username"],
        first_name=resp["firstName"],
        last_name=resp["lastName"],
        email=resp["email"],
        is_verified=resp["isVerified"],
        is_blocked=resp["isBlocked"],
        completed_signup=resp["completedSignup"],
    )


@dataclass(frozen=True)
class Team:
    team_id: str
    name: str
    created_at: datetime.datetime
    role: str
    members: Dict[str, User]


def get_teams() -> Dict[str, Team]:
    team_definitions = get_user_teams()
    teams = {}
    for team in team_definitions:
        members = {}
        for member in team['members']:
            user = User(
                user_id=member['userId'],
                username=member['username'],
                first_name=member['firstName'],
                last_name=member['lastName'],
            )
            members[user.user_id] = user

        team = Team(
            team_id=team['id'],
            name=team['name'],
            created_at=datetime.datetime.fromisoformat(team['createdAt']),
            role=team['role'],
            members=members,
        )
        teams[team.team_id] = team

    return teams
