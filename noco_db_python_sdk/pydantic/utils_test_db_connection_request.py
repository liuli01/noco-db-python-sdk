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

from noco_db_python_sdk.pydantic.utils_test_db_connection_request_connection import UtilsTestDbConnectionRequestConnection

class UtilsTestDbConnectionRequest(BaseModel):
    # DB Type
    client: typing.Optional[Literal["mssql", "mysql", "mysql2", "oracledb", "pg", "snowflake", "sqlite3"]] = Field(None, alias='client')

    connection: typing.Optional[UtilsTestDbConnectionRequestConnection] = Field(None, alias='connection')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
