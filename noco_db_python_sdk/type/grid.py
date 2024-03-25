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

from noco_db_python_sdk.type.grid_column import GridColumn
from noco_db_python_sdk.type.id import Id
from noco_db_python_sdk.type.meta import Meta

class RequiredGrid(TypedDict):
    pass

class OptionalGrid(TypedDict, total=False):
    id: Id

    base_id: Id

    source_id: Id

    fk_view_id: Id

    # Row Height
    row_height: typing.Union[int, float]

    meta: Meta

    # Grid View Columns
    columns: typing.List[GridColumn]

class Grid(RequiredGrid, OptionalGrid):
    pass
