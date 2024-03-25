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


class RequiredTableEventBody(TypedDict):
    # The title of the table associated with the event
    title: str

    # The ID of the base that the table belongs to
    base_id: str

    # The ID of the source that the table belongs to
    source_id: str

    # The ID of the table associated with the event
    id: str

class OptionalTableEventBody(TypedDict, total=False):
    pass

class TableEventBody(RequiredTableEventBody, OptionalTableEventBody):
    pass
