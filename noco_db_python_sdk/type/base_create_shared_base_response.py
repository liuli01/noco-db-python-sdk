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

from noco_db_python_sdk.type.string_or_null import StringOrNull

class RequiredBaseCreateSharedBaseResponse(TypedDict):
    pass

class OptionalBaseCreateSharedBaseResponse(TypedDict, total=False):
    uuid: StringOrNull

    roles: StringOrNull

class BaseCreateSharedBaseResponse(RequiredBaseCreateSharedBaseResponse, OptionalBaseCreateSharedBaseResponse):
    pass
