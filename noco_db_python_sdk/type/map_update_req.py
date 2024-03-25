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

class RequiredMapUpdateReq(TypedDict):
    pass

class OptionalMapUpdateReq(TypedDict, total=False):
    # Foreign Key to GeoData Column
    fk_geo_data_col_id: str

    meta: Meta

class MapUpdateReq(RequiredMapUpdateReq, OptionalMapUpdateReq):
    pass