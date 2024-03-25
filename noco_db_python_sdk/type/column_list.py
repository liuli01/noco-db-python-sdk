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

from noco_db_python_sdk.type.column import Column
from noco_db_python_sdk.type.paginated import Paginated

RequiredColumnList = TypedDict("RequiredColumnList", {
    # List of column objects
    "list": typing.List[Column],

    "pageInfo": Paginated,
    })

OptionalColumnList = TypedDict("OptionalColumnList", {
    }, total=False)

class ColumnList(RequiredColumnList, OptionalColumnList):
    pass
