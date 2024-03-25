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

from noco_db_python_sdk.type.meta import Meta
from noco_db_python_sdk.type.model_bool import ModelBool

class RequiredViewUpdateReq(TypedDict):
    pass

class OptionalViewUpdateReq(TypedDict, total=False):
    # View Title
    title: str

    # View UUID. Used in Shared View.
    uuid: str

    # View Password. Used in Shared View.
    password: str

    # Lock type of View.
    lock_type: str

    meta: Meta

    # The order of the list of views.
    order: typing.Union[int, float]

    show_system_fields: ModelBool

class ViewUpdateReq(RequiredViewUpdateReq, OptionalViewUpdateReq):
    pass