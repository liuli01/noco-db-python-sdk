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

from noco_db_python_sdk.type.auth_list_base_users_response_users import AuthListBaseUsersResponseUsers

class RequiredAuthListBaseUsersResponse(TypedDict):
    pass

class OptionalAuthListBaseUsersResponse(TypedDict, total=False):
    users: AuthListBaseUsersResponseUsers

class AuthListBaseUsersResponse(RequiredAuthListBaseUsersResponse, OptionalAuthListBaseUsersResponse):
    pass
