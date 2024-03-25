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

from noco_db_python_sdk.type.paginated import Paginated
from noco_db_python_sdk.type.view import View

RequiredViewList = TypedDict("RequiredViewList", {
    # List of view objects
    "list": typing.List[View],

    "pageInfo": Paginated,
    })

OptionalViewList = TypedDict("OptionalViewList", {
    }, total=False)

class ViewList(RequiredViewList, OptionalViewList):
    pass