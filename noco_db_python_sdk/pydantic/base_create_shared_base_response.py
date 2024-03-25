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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from noco_db_python_sdk.pydantic.string_or_null import StringOrNull

class BaseCreateSharedBaseResponse(BaseModel):
    uuid: typing.Optional[StringOrNull] = Field(None, alias='uuid')

    roles: typing.Optional[StringOrNull] = Field(None, alias='roles')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )