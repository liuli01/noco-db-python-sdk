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

from noco_db_python_sdk.pydantic.column import Column
from noco_db_python_sdk.pydantic.form import Form
from noco_db_python_sdk.pydantic.form_column import FormColumn
from noco_db_python_sdk.pydantic.gallery import Gallery
from noco_db_python_sdk.pydantic.gallery_column import GalleryColumn
from noco_db_python_sdk.pydantic.grid import Grid
from noco_db_python_sdk.pydantic.grid_column import GridColumn
from noco_db_python_sdk.pydantic.table import Table
from noco_db_python_sdk.pydantic.view import View

PublicViewMetaGetResponse = typing.Union[View,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
