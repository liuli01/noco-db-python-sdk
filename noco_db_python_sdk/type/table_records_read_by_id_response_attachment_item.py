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


class RequiredTableRecordsReadByIdResponseAttachmentItem(TypedDict):
    pass

class OptionalTableRecordsReadByIdResponseAttachmentItem(TypedDict, total=False):
    title: str

    url: str

    mimetype: str

    size: typing.Union[int, float]

    signedUrl: str

class TableRecordsReadByIdResponseAttachmentItem(RequiredTableRecordsReadByIdResponseAttachmentItem, OptionalTableRecordsReadByIdResponseAttachmentItem):
    pass