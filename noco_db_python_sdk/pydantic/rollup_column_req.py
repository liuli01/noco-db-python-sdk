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

from noco_db_python_sdk.pydantic.id import Id

class RollupColumnReq(BaseModel):
    # Rollup Column Title
    title: typing.Optional[str] = Field(None, alias='title')

    fk_relation_column_id: typing.Optional[Id] = Field(None, alias='fk_relation_column_id')

    fk_rollup_column_id: typing.Optional[Id] = Field(None, alias='fk_rollup_column_id')

    # Rollup Function
    rollup_function: typing.Optional[Literal["avg", "avgDistinct", "count", "countDistinct", "max", "min", "sum", "sumDistinct"]] = Field(None, alias='rollup_function')

    # UI DataType
    uidt: typing.Optional[Literal["Rollup"]] = Field(None, alias='uidt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
