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

from noco_db_python_sdk.pydantic.model_bool import ModelBool

class ProjectUserMetaReq(BaseModel):
    starred: typing.Optional[ModelBool] = Field(None, alias='starred')

    # The order among the bases
    order: typing.Optional[typing.Union[int, float]] = Field(None, alias='order')

    hidden: typing.Optional[ModelBool] = Field(None, alias='hidden')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
