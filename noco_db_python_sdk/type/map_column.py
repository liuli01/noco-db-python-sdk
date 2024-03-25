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


class RequiredMapColumn(TypedDict):
    pass

class OptionalMapColumn(TypedDict, total=False):
    # The ID of the source that this map column belongs to
    source_id: str

    # Foreign Key to Column
    fk_column_id: str

    # Foreign Key to View
    fk_view_id: str

    # Unique ID of Map Column
    id: str

    # the order in the list of map columns
    order: typing.Union[int, float]

    # The ID of the base that this map column belongs to
    base_id: str

    # Whether to show this column or not
    show: typing.Union[int, float]

class MapColumn(RequiredMapColumn, OptionalMapColumn):
    pass
