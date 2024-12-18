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

from noco_db_python_sdk.pydantic.id import Id
from noco_db_python_sdk.pydantic.model_bool import ModelBool

class Hook(BaseModel):
    # Hook Title
    title: typing.Optional[str] = Field(None, alias='title')

    # Hook Description
    description: typing.Optional[str] = Field(None, alias='description')

    # Hook Version
    version: typing.Optional[Literal["v1", "v2"]] = Field(None, alias='version')

    active: typing.Optional[ModelBool] = Field(None, alias='active')

    async_: typing.Optional[ModelBool] = Field(None, alias='async')

    # Environment for the hook
    env: typing.Optional[str] = Field(None, alias='env')

    # Event Type for the operation
    event: typing.Optional[Literal["after", "before"]] = Field(None, alias='event')

    # Foreign Key to Model
    fk_model_id: typing.Optional[str] = Field(None, alias='fk_model_id')

    id: typing.Optional[Id] = Field(None, alias='id')

    # Hook Notification including info such as type, payload, method, body, and etc
    notification: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='notification')

    # Hook Operation
    operation: typing.Optional[Literal["insert", "update", "delete", "bulkInsert", "bulkUpdate", "bulkDelete"]] = Field(None, alias='operation')

    # Retry Count
    retries: typing.Optional[typing.Union[int, float]] = Field(None, alias='retries')

    # Retry Interval
    retry_interval: typing.Optional[typing.Union[int, float]] = Field(None, alias='retry_interval')

    # Timeout
    timeout: typing.Optional[typing.Union[int, float]] = Field(None, alias='timeout')

    # Hook Type
    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
