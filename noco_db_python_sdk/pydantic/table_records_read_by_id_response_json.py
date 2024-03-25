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

from noco_db_python_sdk.pydantic.table_records_read_by_id_response_json_address import TableRecordsReadByIdResponseJsonAddress
from noco_db_python_sdk.pydantic.table_records_read_by_id_response_json_hobbies import TableRecordsReadByIdResponseJsonHobbies
from noco_db_python_sdk.pydantic.table_records_read_by_id_response_json_scores import TableRecordsReadByIdResponseJsonScores

class TableRecordsReadByIdResponseJson(BaseModel):
    name: typing.Optional[str] = Field(None, alias='name')

    age: typing.Optional[typing.Union[int, float]] = Field(None, alias='age')

    email: typing.Optional[str] = Field(None, alias='email')

    is_subscribed: typing.Optional[bool] = Field(None, alias='isSubscribed')

    address: typing.Optional[TableRecordsReadByIdResponseJsonAddress] = Field(None, alias='address')

    hobbies: typing.Optional[TableRecordsReadByIdResponseJsonHobbies] = Field(None, alias='hobbies')

    scores: typing.Optional[TableRecordsReadByIdResponseJsonScores] = Field(None, alias='scores')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )