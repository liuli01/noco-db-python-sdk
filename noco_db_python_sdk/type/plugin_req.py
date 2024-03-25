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

class RequiredPluginReq(TypedDict):
    pass

class OptionalPluginReq(TypedDict, total=False):
    active: ModelBool

    # Plugin Input
    input: typing.Union[str, none_type]

class PluginReq(RequiredPluginReq, OptionalPluginReq):
    pass
