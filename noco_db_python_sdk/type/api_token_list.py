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

from noco_db_python_sdk.type.api_token import ApiToken
from noco_db_python_sdk.type.paginated import Paginated

RequiredApiTokenList = TypedDict("RequiredApiTokenList", {
    # List of api token objects
    "list": typing.List[ApiToken],

    "pageInfo": Paginated,
    })

OptionalApiTokenList = TypedDict("OptionalApiTokenList", {
    }, total=False)

class ApiTokenList(RequiredApiTokenList, OptionalApiTokenList):
    pass
