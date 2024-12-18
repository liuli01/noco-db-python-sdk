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


class Attachment(BaseModel):
    # The title of the attachment. Used in UI.
    title: typing.Optional[str] = Field(None, alias='title')

    # Data for uploading
    data: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='data')

    # The mimetype of the attachment
    mimetype: typing.Optional[str] = Field(None, alias='mimetype')

    # File Path
    path: typing.Optional[str] = Field(None, alias='path')

    # Attachment Size
    size: typing.Optional[typing.Union[int, float]] = Field(None, alias='size')

    # Attachment URL
    url: typing.Optional[str] = Field(None, alias='url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
