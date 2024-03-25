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

class RequiredProjectUserMetaReq(TypedDict):
    pass

class OptionalProjectUserMetaReq(TypedDict, total=False):
    starred: ModelBool

    # The order among the bases
    order: typing.Union[int, float]

    hidden: ModelBool

class ProjectUserMetaReq(RequiredProjectUserMetaReq, OptionalProjectUserMetaReq):
    pass
