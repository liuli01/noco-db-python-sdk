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

from noco_db_python_sdk.type.id import Id

class RequiredSortReq(TypedDict):
    pass

class OptionalSortReq(TypedDict, total=False):
    fk_column_id: Id

    # Sort direction
    direction: str

class SortReq(RequiredSortReq, OptionalSortReq):
    pass