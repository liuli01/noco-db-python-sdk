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
from noco_db_python_sdk.type.string_or_null import StringOrNull

class RequiredGalleryUpdateReq(TypedDict):
    pass

class OptionalGalleryUpdateReq(TypedDict, total=False):
    fk_cover_image_col_id: StringOrNull

    meta: Meta

class GalleryUpdateReq(RequiredGalleryUpdateReq, OptionalGalleryUpdateReq):
    pass