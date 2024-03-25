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

from noco_db_python_sdk.type.model_bool import ModelBool

class RequiredViewColumnUpdateReq(TypedDict):
    pass

class OptionalViewColumnUpdateReq(TypedDict, total=False):
    show: ModelBool

    # The order of the list of views.
    order: typing.Union[int, float]

class ViewColumnUpdateReq(RequiredViewColumnUpdateReq, OptionalViewColumnUpdateReq):
    pass