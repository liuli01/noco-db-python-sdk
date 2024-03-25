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

from noco_db_python_sdk.pydantic.paginated import Paginated
from noco_db_python_sdk.pydantic.table_records_list_response_list import TableRecordsListResponseList

class TableRecordsListResponse(BaseModel):
    list_: TableRecordsListResponseList = Field(alias='list')

    page_info: Paginated = Field(alias='pageInfo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
