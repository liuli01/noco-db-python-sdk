# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredProjectInviteEventBody(TypedDict):
    # The title of the base being invited to
    title: str

    # The ID of the base being invited to
    id: str

    # The type of the base being invited to
    type: str

    # The email address of the user who invited the recipient
    invited_by: str

class OptionalProjectInviteEventBody(TypedDict, total=False):
    pass

class ProjectInviteEventBody(RequiredProjectInviteEventBody, OptionalProjectInviteEventBody):
    pass
