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

from noco_db_python_sdk.pydantic.meta import Meta

class MapUpdateReq(BaseModel):
    # Foreign Key to GeoData Column
    fk_geo_data_col_id: typing.Optional[str] = Field(None, alias='fk_geo_data_col_id')

    meta: typing.Optional[Meta] = Field(None, alias='meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )