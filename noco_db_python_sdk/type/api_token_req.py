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


class RequiredApiTokenReq(TypedDict):
    pass

class OptionalApiTokenReq(TypedDict, total=False):
    # Description of the API token
    description: str

class ApiTokenReq(RequiredApiTokenReq, OptionalApiTokenReq):
    pass
