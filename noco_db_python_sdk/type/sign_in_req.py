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


class RequiredSignInReq(TypedDict):
    # Email address of the user
    email: str

    # Password of the user
    password: str

class OptionalSignInReq(TypedDict, total=False):
    pass

class SignInReq(RequiredSignInReq, OptionalSignInReq):
    pass
